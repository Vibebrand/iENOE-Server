#!/usr/bin/python
# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy

class ServicioGestorConjuntos(object):
	def __init__(self):
		self.definicionGestoresPorNombre = {}
		self.gestorConjuntoPadre = None
		self.nombre = None
		self.variables = {}
		self.conjuntos = []
		self.secciones = []

	def conNombre(self, nombre):
		if nombre not in self.definicionGestoresPorNombre:
			aAgregar = None
			if self.nombre is None:
				self.nombre = nombre
				self.definicionGestoresPorNombre[nombre] = self
				if self.gestorConjuntoPadre is not None:
					self.gestorConjuntoPadre.conjuntos.append(self)

		return self.definicionGestoresPorNombre[nombre]


	def conVariable(self, nombre, valor):
		self.variables[nombre] = valor
		return self

	def conSeccion(self, seccion):
		self.secciones.append(seccion)
		return self
	
	def obtenSubConjunto(self):
		derivado = self.__class__()
		derivado.definicionGestoresPorNombre = self.definicionGestoresPorNombre
		derivado.gestorConjuntoPadre = self
		return derivado

	def obtenConjuntoAlternativo(self):
		derivado = self.__class__()
		derivado.definicionGestoresPorNombre = self.definicionGestoresPorNombre
		derivado.gestorConjuntoPadre = self.gestorConjuntoPadre
		return derivado
