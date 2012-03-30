#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

'''
{
	variables: {
		"Indicador" : "Bienestar"
	},
	conjuntos: [
		{
			nombre: "XXX"
			variables: {
				"Trimestre" : "1"
			},
			secciones: [

			]
		},
		{

		}
	]
} '''

###--ServicioGestorConjuntosXML--###

class ServicioGestorConjuntosXML(Proxy):
	def obtenRepresentacion(self):
		pass


def obtenRepresentacion(self, formato = u"XML", info = {}):
    servicioMapaTematicoRenderizador = None

    if type(info) is dict:
        info = Struct(**info)

    # TODO Inyectar proveedor
    if formato == u"XML":
        servicioGestorConjuntosRenderizador = ServicioGestorConjuntosXML(self)

    if servicioGestorConjuntosRenderizador is not None:
        servicioGestorConjuntosRenderizador.info = info
        return servicioGestorConjuntosRenderizador.obtenRepresentacion() 


setattr(ServicioGestorConjuntos, "obtenRepresentacion", obtenRepresentacion)