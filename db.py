#db
import mysql.connector
#change localhost database for same database hosted in 000webhost

def dbConect():
    conn=mysql.connector.connect( host='sql.freedb.tech', user= 'freedb_pizzi686', passwd='Nnu9UPx9Xf7j$Nq', db='freedb_adm-pedidos' )
    return conn

#guardar en las respectivas tablas el pedido y sus detalles pasando un objeto pedido como parametro 
def registrarPedidoInDB(pedido):
    #save pedido 
    conection=dbConect()
    con=conection.cursor()
    con.execute(f"insert into pedidos (idProveedor,hora,fecha, costoTotal) values ('{pedido.proveedor}','{pedido.hora}','{pedido.fecha}','{pedido.total}')")
    conection.commit()
    con.execute(f"select idPedido from pedidos where fecha='{pedido.fecha}' and hora='{pedido.hora}'")
    idPedido=con.fetchone()[0]
    conection.close()

    for detalle in pedido.númeroDePedido:
        conection=dbConect()
        con=conection.cursor()
        #get idArticle 
        con.execute(f"select idArticulo FROM Articulo WHERE Nombre='{detalle.artículo.nombre}' ;")
        id=con.fetchone()[0]
        #save in db los detalles 
        con.execute(f"INSERT INTO detallePedido (idArticulo, idPedido, cantidad, subtotal,precioUnitario) VALUES({int(id)},{idPedido},{int(detalle.cantidad)},{int(detalle.subtotal)},{int(detalle.precioUnitario)})" )    
        conection.commit()
        conection.close()
def getProveedores():
    conection=dbConect()
    con=conection.cursor()
    con.execute("select * from proveedores")
    user=con.fetchall()
    conection.close()
    return user
def getArticles():
    conection=dbConect()
    con=conection.cursor()
    con.execute("select * from Articulo")
    articulo=con.fetchall()
    conection.close()
    return articulo
def getPedidos():
    conection=dbConect()
    con=conection.cursor()
    con.execute("select * from pedidos")
    pedidos=con.fetchall()
    conection.close()
    return pedidos
def getdetallePedido(): 
    conection=dbConect()
    con=conection.cursor()
    con.execute("select * from detallePedido")
    detallePedido=con.fetchall()
    conection.close()
    return detallePedido


#pedidos segun proveedor
def getPedidos_Proveedor(idProveedor):
    conection=dbConect()
    con=conection.cursor()
    con.execute(f"select * from pedidos where idProveedor='{idProveedor}'")
    pedidos=con.fetchall()
    conection.close()
    return pedidos
#detalles segun Pedido
def getDetalles_Pedido(idPedido):
    conection=dbConect()
    con=conection.cursor()
    con.execute(f"select * from detallePedido where idPedido='{idPedido}'")
    detalles=con.fetchall()
    conection.close()
    return detalles
def getArticle_id(idArticle):
    conection=dbConect()
    con=conection.cursor()
    con.execute(f"select * from Articulo where idArticulo='{idArticle}'")
    article=con.fetchone()
    conection.close()
    return article

def registrarProveedor(Rs,CUIT,condIva,domicilio,localidad,telefono,fax):
    conection=dbConect()
    con=conection.cursor()
    con.execute(f"INSERT INTO proveedores(razonSocial, CUIT, CondIVA, domicilio, localidad, telefono, fax) VALUES ('{Rs}','{CUIT}','{condIva}','{domicilio}','{localidad}','{telefono}','{fax}') ")
    conection.commit()
    conection.close()
    
def getIdArticleByName(name):
        conection=dbConect()
        con=conection.cursor()
        con.execute(f"select idArticulo FROM Articulo WHERE Nombre='{name}' ;")
        articleID=con.fetchone()[0]
        return articleID
print(getIdArticleByName("Yerba Mate") )   
    

    