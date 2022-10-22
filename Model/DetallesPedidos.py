#!/usr/bin/python
#-*- coding: utf-8 -*-
#from Artículos import Artículo
class DetallePedido:
    
    def __init__(self,art,cant, pu,idpedido=None):
        self.artículo = art
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
        #SubTotal=0
        SubTotal=(int(self.artículo.precioUnitario)*int(self.cantidad))
        self.subtotal=SubTotal

    def conocerArtículo(self, ):
        pass


#casos de prueba
'''
artículo1=Artículo("Azucar", 150)
artículo2=Artículo("Yerba Mate", 350)


detalle=DetallePedido([artículo1,artículo2],[3,1],[artículo1.precioUnitario,artículo2.precioUnitario])
print(detalle.mostrar())
print (detalle.calcularSubtotal())
'''