#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

class ServicioGestorSecciones(object):
    def __init__(self):
        self.propiedades = {}
        self.propiedades["conceptos"] = []
        self.propiedades["nombre"] = None
        self.propiedades["tipo_valor"] = lambda: None
        self.propiedades["tipo_concepto"] = lambda: None
        
    def conNombreSeccion(self, nombre):
        self.propiedades["nombre"] = nombre
        return self

    def conConcepto(self):
        salida = {}
        self.propiedades["conceptos"].append(salida)

        conceptoProxy = ServicioGestorSeccionesConcepto(self)
        conceptoProxy.concepto = salida
        conceptoProxy.concepto["tipo_valor"] = lambda: self.propiedades["tipo_valor"]()
        conceptoProxy.concepto["tipo_concepto"] = lambda: self.propiedades["tipo_concepto"]()

        return conceptoProxy

    def conTipoValor(self, tipo):
        self.propiedades["tipo_valor"] = lambda: tipo
        return self

    def conTipoConcepto(self, tipo):
        self.propiedades["tipo_concepto"] = lambda: tipo
        return self


class ServicioGestorSeccionesConcepto(Proxy):
    def conNombreConcepto(self, nombre):
        self.concepto["nombre"] = nombre
        self.concepto["valores"] = []
        return self
    
    def conValor(self):
        valor = {}
        self.concepto["valores"].append(valor)
        valorProxy = ServicioGestorSeccionesValor(self)
        valorProxy.valor = valor
        valorProxy.valor["tipo_valor"] = lambda: self.concepto["tipo_valor"]()
        valorProxy.valor["tipo_concepto"] = lambda: self.concepto["tipo_concepto"]()
        return valorProxy

    def conTipoValor(self, tipo):
        self.concepto["tipo_valor"] = lambda: tipo
        return self

    def conTipoConcepto(self, tipo):
        self.concepto["tipo_concepto"] = lambda: tipo
        return self


class ServicioGestorSeccionesValor(Proxy):
    def conNombreValor(self, nombre):
        self.valor["nombre"] = nombre
        return self

    def conValorAplicado(self, valor):
        self.valor["valor"] = lambda: valor
        return self

    def conTipoValor(self, tipo):
        self.valor["tipo_valor"] = lambda: tipo
        return self