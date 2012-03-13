#!/usr/bin/python
# -*- coding: utf-8 -*-

class ServicioMapaTematico(object):
    def __init__(self):
        self.variables = {}
        self.conceptos = {}
        self.colorPorConcepto = {}
    
    def agregaVariableFiltro(self, variable, valor):
        self.variables[variable] = valor
        return self

    def obtenConcepto(self, nombreConcepto):
        concepto = None
        if nombreConcepto not in self.conceptos:
            self.conceptos[nombreConcepto] = {}

        elementoProxy = ServicioMapaTematicoConcepto(self)
        elementoProxy.nombreConcepto = nombreConcepto
        elementoProxy.concepto = self.conceptos[nombreConcepto]
        return elementoProxy

class Proxy:
    def __init__(self, subject):
        self.__subject = subject
        
    def __getattr__( self, name ):
        return getattr( self.__subject, name )


class ServicioMapaTematicoConcepto(Proxy):
    def agregaVariableConValorEnConcepto(self, variable, valor):
        self.concepto[variable] = valor
        return self
    
    def estableceColorEnConcepto(self, nombreColor):
        self.colorPorConcepto[self.nombreConcepto] = nombreColor
        return self

