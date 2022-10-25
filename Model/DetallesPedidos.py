#!/usr/bin/python
#-*- coding: utf-8 -*-
#from Artículos import Artículo
class DetallePedido:
    
    def __init__(self,art,cant, pu,idpedido=None):
        self.artículo = art #one object 
        self.cantidad = cant
        self.subtotal = None
        self.precioUnitario = pu
        self.idpedido=idpedido
    def crear(self, ):
        pass

    def mostrar(self, ):

        return f"\n'Articulo': '{self.artículo.nombre}', 'cantidad': {self.cantidad} , 'subtotal': {self.subtotal} , 'Precio Unitario': {self.precioUnitario}"
    
    def setidpedido(value):
        self.idpedido = value
    
    def calcularSubtotal(self, ):
        SubTotal=0
        SubTotal=(int(self.artículo.precioUnitario)*int(self.cantidad))
        self.subtotal=SubTotal

    def conocerArtículo(self, ):
        pass


#casos de prueba
'''
from Artículos import Artículo

artículo1=Artículo(1,"Azucar", 150)
artículo2=Artículo(2,"Yerba Mate", 350)


detalle1=DetallePedido(artículo1,1,artículo1.precioUnitario)
detalle1.calcularSubtotal()
print (detalle1.mostrar())
'''
