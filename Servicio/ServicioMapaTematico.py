#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

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

class ServicioMapaTematicoConcepto(Proxy):
    def agregaVariableConValorEnConcepto(self, variable, valor):
        self.concepto[variable] = valor
        return self
    
    def estableceColorEnConcepto(self, nombreColor):
        self.colorPorConcepto[self.nombreConcepto] = nombreColor
        return self

