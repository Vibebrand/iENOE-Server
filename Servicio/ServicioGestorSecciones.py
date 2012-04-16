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
        salida["tipo_valor"] = lambda: self.propiedades["tipo_valor"]()
        salida["tipo_concepto"] = lambda: self.propiedades["tipo_concepto"]()
        salida["valores"] = []

        conceptoProxy = ServicioGestorSeccionesConcepto(self)
        conceptoProxy.concepto = salida

        self.propiedades["conceptos"].append(salida)

        return conceptoProxy

    def conTipoValor(self, tipo):
        self.propiedades["tipo_valor"] = lambda: tipo
        return self

    def conTipoConcepto(self, tipo):
        self.propiedades["tipo_concepto"] = lambda: tipo
        return self

    def obtenDefinicion(self):
        salida = dict(self.propiedades)

        def obtenValorSeccion(concepto):
            conceptoProxy = ServicioGestorSeccionesConcepto(self)
            conceptoProxy.concepto = concepto
            return conceptoProxy.obtenDefinicionConcepto()

        salida["conceptos"] = [obtenValorSeccion(concepto) for concepto in salida["conceptos"]]
        salida.pop("tipo_valor")
        salida.pop("tipo_concepto")
        return salida


class ServicioGestorSeccionesConcepto(Proxy):
    def conNombreConcepto(self, nombre):
        self.concepto["nombre"] = nombre
        return self
    
    def conValor(self):
        valor = {}
        valor["tipo_valor"] = lambda: self.concepto["tipo_valor"]()

        self.concepto["valores"].append(valor)

        valorProxy = ServicioGestorSeccionesValor(self)
        valorProxy.valor = valor
        
        return valorProxy

    def conTipoValor(self, tipo):
        self.concepto["tipo_valor"] = lambda: tipo
        return self

    def conTipoConcepto(self, tipo):
        self.concepto["tipo_concepto"] = lambda: tipo
        return self

    def obtenDefinicionConcepto(self):
        salida = dict(self.concepto)

        def obtenValorConcepto(valor):
            valorProxy = ServicioGestorSeccionesValor(self)
            valorProxy.valor = valor
            return valorProxy.obtenDefinicionValor()
        
        
        salida["valores"] = [obtenValorConcepto(valor) for valor in self.concepto["valores"]]
        salida["tipo_concepto"] = salida["tipo_concepto"]()
        salida.pop("tipo_valor")
        return salida


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

    def obtenDefinicionValor(self):
        salida = dict(self.valor)
        salida["valor"] = salida["valor"]()
        salida["tipo_valor"] = salida["tipo_valor"]()
        return salida