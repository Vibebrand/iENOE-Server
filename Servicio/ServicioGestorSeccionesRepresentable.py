#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

class ServicioGestorSeccionesXML(Proxy):
	def obtenRepresentacion(self):
		pass


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