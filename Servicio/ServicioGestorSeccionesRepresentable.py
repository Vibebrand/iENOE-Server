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

        

        contenidoSeccion = ""

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