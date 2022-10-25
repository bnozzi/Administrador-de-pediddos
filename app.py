from Model import *
from Model.Artículos import Artículo
from Model.DetallesPedidos import DetallePedido
from Model.Pedidos import Pedido
from db import *
import json
from flask import Flask, render_template,redirect, url_for, flash,jsonify, request
app= Flask(__name__)
app.secret_key="dev"
app.config["DEBUG"] = True

@app.route("/")
def index():
    proveedores=getProveedores()       
    articles=getArticles()
    return render_template("index.html", proveedores=proveedores, articles=articles) 


@app.route("/registrarNuevoPedido/<idproveedor>",methods=["GET","POST"])
def registrarNuevoPedido(idproveedor):
    list=[]
    detalles=[]
    def dictToList(dict):
        for key in dict:
            list.append(dict[key])
                
    if request.method == "POST":
        form=json.dumps(request.form)
        dictform=json.loads(form)
    dictToList(dictform)
    for value in range(0,len(list),4):
            print(list[value])
            detalles.append(DetallesPedidos.DetallePedido(Artículos.Artículo(getIdArticleByName(list[value]),list[value],list[value+3]),list[value+1],list[value+3]))
    for detalle in detalles:
        detalle.calcularSubtotal()
        print (detalle.mostrar())

    pedido=Pedido(detalle=detalles,idProveedor=idproveedor)
    pedido.calcularTotal()
    
    registrarPedidoInDB(pedido)
    return  redirect(url_for("index",msg=flash("Pedido registrado con exito :D")))   

    
#obtener los los detalles de los pedidos y devolverlo como json 
@app.route("/pedidos/<idProveedor>",methods=["GET","POST"])
def getPedidosByProveedor(idProveedor):
    pedidos=getPedidos_Proveedor(idProveedor)
    detalles=[]
    #detalles de un pedido segun proveedor 
    for pedido in pedidos:
        detalles.append(getDetalles_Pedido(pedido[0]))
            
    
    objDetalle=[]
    #detalles
    # [[(17, 1, 16, 3, 1140, 380)],
    #  [(18, 3, 17, 5, 500, 100)],
    #  [(19, 1, 18, 10, 3800, 380), (20, 3, 18, 10, 1000, 100)]]
    def detalleToListObjects(tupleLists,listObjects):
        for detalle in tupleLists:
            for articulos in detalle:
                print(articulos)
                artDB=getArticle_id(articulos[1])
                artObj=Artículo(artDB[4],artDB[0],artDB[3])
                listObjects.append(DetallePedido(artObj,articulos[3],articulos[5],idpedido=articulos[2]) )
        return listObjects
    (detalleToListObjects(detalles,objDetalle))
    
    for detalle in objDetalle:
        detalle.calcularSubtotal()
        

    objPedidos=[]
    def filtrar(idpedido,objetosDetalle):
        lista=[]
        for detalle in objetosDetalle:
            if detalle.idpedido==idpedido:
                lista.append(detalle)
        return lista
    #ver si toma los detalles segun el pedido segun el proveedor 
    for pedido in pedidos:
        objPedidos.append(Pedido(pedido[0],filtrar(pedido[0],objDetalle),idProveedor,pedido[2],pedido[3]))
    respuesta=[]
    respuestaDict={}
    for obj in objPedidos :
        obj.calcularTotal()
        respuesta.append(obj.mostrar())
        respuestaDict[obj.idPedido]=    (obj.mostrar())

    print(respuestaDict)
    return  json.dumps(respuestaDict, indent=4, sort_keys=True, default=str)
    
    
@app.route("/nuevoProveedor", methods=["POST"])
def nuevoProveedor():

        if request.method == "POST":
            form=json.dumps(request.form)
            dictform=json.loads(form)

            registrarProveedor(dictform["Razon social"], dictform["CUIL"], dictform["COND IVA"], dictform["provincia"], dictform["Localidad"], dictform["numero"], dictform["fax"])
            return  redirect(url_for("index",msg=flash("proveedor registrado con exito")))






