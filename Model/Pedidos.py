#!/usr/bin/python
#-*- coding: utf-8 -*-

#from DetallePedido import DetallePedido
#from Artículo import Artículo
from datetime import datetime


class Pedido:
    def __init__(self, detalle,idProveedor):
        self.idPedido=None
        self.fecha = datetime.now().date()
        self.hora = str(datetime.now().hour) + ":"+ str(datetime.now().minute) + ":"+ str(datetime.now().second)
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
        return f"\nFecha: {self.fecha} , hora: {self.hora} \nDetalle: {detalles} , total: {self.total}"
    def setidPedido(value):
        self.idPedido=value      
    def conocerArtículo(self, ):
        pass

    def calcularTotal(self, ):
        self.total=0
        for detalle in self.númeroDePedido:
            self.total+=detalle.subtotal
        

    def conocerDetallePedido(self, ):
        pass
# print (datetime.now().date())
#CP
'''
artículo1=Artículo("Azucar", 150)
artículo2=Artículo("Yerba Mate", 350)


detalle=DetallePedido([artículo1,artículo2],[1,1],[150,350],[artículo1.precioUnitario,artículo2.precioUnitario])
Pedido1=Pedido(detalle)

print(Pedido1.mostrar())
'''
