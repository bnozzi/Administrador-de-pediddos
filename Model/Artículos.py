#!/usr/bin/python
#-*- coding: utf-8 -*-

class Artículo:
    def __init__(self,id,nombre,precioUnitario):
        self.id=id
        self.nombre = nombre
        #self.stock = None
        # self.descripción = None
        #self.unidadDeMedida = None
        self.precioUnitario = precioUnitario

    def crear(self, ):
        pass
    
    def mostrar(self, ):
        return f"nombre: {self.nombre} ,  Precio Unitario: {self.precioUnitario}"
        

    def actualizaciónDePrecios(self,nuevoPrecio ):
        self.precioUnitario=nuevoPrecio

