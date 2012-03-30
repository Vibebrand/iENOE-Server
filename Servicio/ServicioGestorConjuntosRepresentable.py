#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy


###--ServicioGestorConjuntosXML--###

class ServicioGestorConjuntosXML(Proxy):
    def obtenRepresentacion(self):
        salida = u'''$$definicionXML
            <conjunto nombre="$$nombreConjunto" $$definicionXSD>
                $$contenidoConjunto
            </conjunto>
        '''

        # Variables unicas no heredables en XML
        definicionXML = getattr(self.info, u"definicionXML", u'''<?xml version="1.0" encoding="ISO-8859-1"?>''')
        definicionXSD = getattr(self.info, u"definicionXSD", u'''xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.inegi.org.mx/imapa/info" xsi:schemaLocation="http://www.inegi.org.mx/imapa/info info-imapa.xsd "''')
        
        self.info.definicionXML = ""
        self.info.definicionXSD = ""
        nombreConjunto = self.nombre
        
        contenidoConjunto = ""
        contenidoConjunto += self.__obtenRepresentacionVariables()
        contenidoConjunto += self.__obtenerRepresentacionConjuntos()
        contenidoConjunto += self.__obtenerRepresentacionSecciones()

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenRepresentacionVariables(self):
        salida = u'''
            <variables>
                $$contenidoVariables
            </variables>
        '''

        contenidoVariables = u""

        for nombreVariable in self.variables:
            representacionVariable = u'''<concepto nombre="$$nombreVariable">$$valorVariable</concepto>'''
            valorVariable = self.variables[nombreVariable]
            contenidoVariables += self.__actualizaSegunVariables(representacionVariable, locals())

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenerRepresentacionConjuntos(self):
        salida = u"$$contenidoConceptos"

        contenidoConceptos = ""
        for conjuntoInterno in self.conjuntos:
            contenidoConceptos += conjuntoInterno.obtenRepresentacion(formato = self.formato, info=self.info)

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenerRepresentacionSecciones(self):
        salida = u"$$contenidoSecciones"

        contenidoSecciones = u""
        for seccionInterna in self.secciones:
            if hasattr(seccionInterna, u"obtenRepresentacion"):
                contenidoSecciones += seccionInterna.obtenRepresentacion(formato = self.formato, info=self.info)
        
        return self.__actualizaSegunVariables(salida, locals())

    def __actualizaSegunVariables(self, informacion, locales):
        u'''
            Substitucion de elementos con variables definidas en los metodos que le invocan
            @see http://stackoverflow.com/questions/1041639/get-a-dict-of-all-variables-currently-in-scope-and-their-values
        '''
        informacionAnterior = u""

        while informacion != informacionAnterior:
            informacionAnterior = informacion
            for llave in locales:
                informacion  = informacion.replace(u"$$" + llave, unicode(locales[llave]))

        return informacion

from Servicio.ServicioGestorConjuntos import ServicioGestorConjuntos
from Herramienta.Proxy import Struct

def obtenRepresentacion(self, formato = u"XML", info = {}):
    servicioMapaTematicoRenderizador = None

    if type(info) is dict:
        info = Struct(**info)

    # TODO Inyectar proveedor
    if formato == u"XML":
        servicioGestorConjuntosRenderizador = ServicioGestorConjuntosXML(self)

    if servicioGestorConjuntosRenderizador is not None:
        servicioGestorConjuntosRenderizador.info = info
        servicioGestorConjuntosRenderizador.formato = formato
        return servicioGestorConjuntosRenderizador.obtenRepresentacion() 


setattr(ServicioGestorConjuntos, u"obtenRepresentacion", obtenRepresentacion)