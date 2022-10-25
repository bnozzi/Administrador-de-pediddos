#!/usr/bin/python
#-*- coding: utf-8 -*-

#from DetallePedido import DetallePedido
#from Artículo import Artículo
from datetime import datetime


class Pedido:
    def __init__(self,idPedido=None, detalle=None,idProveedor=None, fecha=datetime.now().date(), hora=str(datetime.now().hour) + ":"+ str(datetime.now().minute) + ":"+ str(datetime.now().second)):
        self.idPedido=idPedido
        self.fecha = fecha
        self.hora = hora
        self.númeroDePedido = detalle # detalle pedido lista de detalles 
        self.total=None
        self.proveedor = idProveedor
        #self.artículos = None 

            

    def crear(self, ):
        pass

    def mostrar(self, ):
        detalles=""
        for detalle in self.númeroDePedido:
            detalles+="\n" +detalle.mostrar()
        return f"Fecha: '{self.fecha}' , hora: '{self.hora}' , Detalle: '{detalles}' total: {self.total}"
    

    def conocerArtículo(self, ):
        pass

    def calcularTotal(self, ):
        self.total=0
        for detalle in self.númeroDePedido:
            self.total+=int(detalle.subtotal)
    def getnumeroDePedido(self,):
        return (self.númeroDePedido)

    def setidpedido(self,id):
        self.idPedido=id

    def conocerDetallePedido(self, ):
        pass
# print (datetime.now().date())
#CP
'''
from Artículos import Artículo
from DetallesPedidos import DetallePedido
artículo1=Artículo(1,"Azucar", 150)
artículo2=Artículo(2,"Yerba Mate", 350)

detalle1=DetallePedido(artículo1,1,artículo1.precioUnitario)
detalle2=DetallePedido(artículo2,1,artículo2.precioUnitario)
detalle1.calcularSubtotal()
detalle2.calcularSubtotal()
Pedido1=Pedido(detalle=[detalle1,detalle2])

Pedido1.calcularTotal()
print(Pedido1.mostrar())
'''