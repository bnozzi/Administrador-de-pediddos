from Model import *
from Model.Artículos import Artículo
from Model.DetallesPedidos import DetallePedido
from Model.Pedidos import Pedido
from db import *
import json
from flask import Flask, render_template,redirect, url_for, flash,jsonify
app= Flask(__name__)
app.secret_key="dev"
app.config["DEBUG"] = True

@app.route("/")
def index():
    proveedores=getProveedores()       
    articles=getArticles()
    return render_template("index.html", proveedores=proveedores, articles=articles) 



@app.route("/registrarPedido/<datosForm><idproveedor>",methods=("GET","POST"))
def registrarPedido(datosForm,idproveedor):
    #info=json.loads(datosForm)
    
    info=json.loads(datosForm)
    print (info)

    detalles=[]
    for article in info:
        #GET idArticle from db 
        conection=dbConect()
        con=conection.cursor()
        con.execute(f"select idArticulo FROM Articulo WHERE Nombre='{article}' ;")
        #Instancio el objeto detalle de Pedido segun los articulos que haya en el diccionario y los guardo en una lista  
        detalles.append(DetallesPedidos.DetallePedido(Artículos.Artículo(con.fetchone()[0],article,info[article]["Precio Unitario"]),info[article]["cantidad"],info[article]["Precio Unitario"]))   
        conection.close()
    #calculo el subtotal de cada articulo
    for detalle in detalles:
        detalle.calcularSubtotal()
        print("here", detalle.mostrar())


    #!!!
    
    pedido=Pedido(detalle=detalles,idProveedor=idproveedor)
    print(pedido.númeroDePedido)
    pedido.calcularTotal()
    
    registrarPedidoInDB(pedido)
    return  redirect(url_for("index",msg=flash("Pedido registrado con exito :D")))
    
    #recibir el formulario y guardar en bd
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
    
    






