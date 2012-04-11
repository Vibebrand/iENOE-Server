#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

class ServicioGestorSeccionesXML(Proxy):
    def obtenRepresentacion(self):
        salida = u'''
            <seccion nombre="$$nombreConjunto">
                $$contenidoSeccion
            </seccion>
        '''
        nombreConjunto = self.propiedades["nombre"] if "nombre" in self.propiedades else ""
        contenidoSeccion = self.__obtenRepresentacionContenidoSeccion()

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenRepresentacionContenidoSeccion(self):
        salida = ""
        for concepto in self.propiedades["conceptos"]:
            salida += self.__obtenRepresentacionConcepto(concepto)
        return salida

    def __obtenRepresentacionConcepto(self, concepto):
        salida = u'''
            <concepto nombre="$$nombreConcepto" $$atributos>
                $$contenidoConcepto
            </concepto>
        '''

        nombreConcepto = concepto["nombre"] if "nombre" in concepto else ""
        atributos = ""

        tipoConcepto = concepto["tipo_concepto"]()
        atributos += "" if tipoConcepto is None else  "tipo-concepto='" + tipoConcepto + "' "
        
        contenidoConcepto = ""

        if len(concepto["valores"]) > 0:
            if len(concepto["valores"]) == 1 and "nombre" not in concepto["valores"][0]:
                contenidoConcepto = concepto["valores"][0]["valor"]()
            else:
                for valor in concepto["valores"]:
                    contenidoConcepto += self.__obtenRepresentacionValor(valor)

        return self.__actualizaSegunVariables(salida, locals())


    def __obtenRepresentacionValor(self, valor):
        salida = u'''
            <valor nombre="$$nombreValor" $$atributos>$$valorValor</valor>
        '''
        nombreValor = valor["nombre"] if "nombre" in valor else ""
        valorValor = valor["valor"]() if "valor" in valor else ""
        atributos = ""

        tipoValor = self.propiedades["tipo_valor"]()
        atributos += "" if tipoValor is None else  "tipo-valor='" + tipoValor + "' " 

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


from Servicio.ServicioGestorSecciones import ServicioGestorSecciones
from Herramienta.Proxy import Struct

def obtenRepresentacion(self, formato = u"XML", info = {}):
    renderizador = None

    if type(info) is dict:
        info = Struct(**info)

    # TODO Inyectar proveedor
    if formato == u"XML":
        renderizador = ServicioGestorSeccionesXML(self)

    if renderizador is not None:
        renderizador.info = info
        renderizador.formato = formato
        return renderizador.obtenRepresentacion() 


setattr(ServicioGestorSecciones, u"obtenRepresentacion", obtenRepresentacion)