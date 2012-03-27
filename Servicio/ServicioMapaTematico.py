#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy
from Herramienta.Proxy import Struct

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

    def obtenRepresentacion(self, formato = "XML", info = {}):
        servicioMapaTematicoRenderizador = None

        if type(info) is dict:
            info = Struct(**info)

        # TODO Inyectar proveedor
        if formato == "XML":
            servicioMapaTematicoRenderizador = ServicioMapaTematicoRenderizadorXML(self)

        if servicioMapaTematicoRenderizador is not None:
            servicioMapaTematicoRenderizador.info = info
            return servicioMapaTematicoRenderizador.obtenRepresentacion()


class ServicioMapaTematicoConcepto(Proxy):
    def agregaVariableConValorEnConcepto(self, variable, valor):
        self.concepto[variable] = valor
        return self
    
    def estableceColorEnConcepto(self, nombreColor):
        self.colorPorConcepto[self.nombreConcepto] = nombreColor
        return self


class ServicioMapaTematicoRenderizadorXML(Proxy):
    def obtenRepresentacion(self):
        salida = '''
            <seccion nombre="$$nombreSeccion">
                $$contenidoSeccion
            </seccion>
        '''

        nombreSeccion = getattr(self.info, "nombreSeccion", "Indicadores Color Mexico")
        contenidoSeccion = ""

        for nombreConcepto in self.conceptos:
            concepto = self.conceptos[nombreConcepto]
            colorPorConcepto = None if nombreConcepto not in self.colorPorConcepto else self.colorPorConcepto[nombreConcepto]

            contenidoSeccion += self.__obtenRepresentacionConcepto(nombreConcepto, concepto, colorPorConcepto)

        return self.__actualizaSegunVariables(salida, **locals())

    def __obtenRepresentacionConcepto(self, nombreConcepto, concepto, colorPorConcepto = None):
        salida = '''
            <concepto nombre="$$nombreConcepto">
                $$contenidoConcepto
            </concepto>
        '''

        contenidoConcepto = ""

        if colorPorConcepto is not None:
            contenidoConcepto += self.__obtenRepresentacionValor("Color", colorPorConcepto, "color")

        for llave in concepto:
            valor = concepto[llave]
            contenidoConcepto += self.__obtenRepresentacionValor(llave, valor, "")

        return self.__actualizaSegunVariables(salida, **locals())

    def __obtenRepresentacionValor(self, nombre, valor, tipoValor = ""):
        salida = '''
            <valor nombre="$$llave" $$atributos>$$valor</valor>
        '''

        atributos = ""
        atributos = atributos if len(tipoValor) == 0 else atributos + ' tipo-valor="$$tipoValor" '
        # TODO Revisar ejecucion de __actualizaSegunVariables al ser evaluada en el return
        return self.__actualizaSegunVariables(salida, **locals())

    def __actualizaSegunVariables(self, informacion, locales):
        for llave in locales:
            informacion = informacion.replace("$$" + llave, str(locales[llave]))
        return informacion
