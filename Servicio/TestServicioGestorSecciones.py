# -*- coding: utf-8 -*-

import unittest
import Servicio.ServicioGestorSecciones as sgs

class TestServicioGestorSecciones(unittest.TestCase):

    def obtenSeccionBase(self):
        seccion = sgs.ServicioGestorSecciones().conNombreSeccion("seccion1").conTipoConcepto("tipoConcepto1")
        concepto = seccion.conConcepto().conNombreConcepto("nombreConcepto1")
        valor1 = concepto.conValor().conNombreValor("valor1").conValorAplicado("valorAplicado1")
        valor2 = concepto.conValor().conNombreValor("valor2").conValorAplicado("valorAplicado2")
        valor3 = concepto.conValor().conNombreValor("valor3").conValorAplicado("valorAplicado3")

        return seccion, concepto, valor1, valor2, valor3

    def revisaEquidadElementos(self, elementos, valores):
        tipoLambda = type(lambda: None)
        for indice in range(len(elementos)):
            valorEjecutado = elementos[indice]() if isinstance(elementos[indice], tipoLambda) and elementos[indice].__name__ == '<lambda>' else elementos[indice]
            self.assertEqual(valorEjecutado, valores[indice], "Elemento en posicion {0} difiere: '{1}' != '{2}'".format(indice, valorEjecutado, valores[indice]))

    def testTiposValoresHeredados(self):
        (seccion, concepto, valor1, valor2, valor3) = self.obtenSeccionBase()

        self.revisaEquidadElementos([seccion.propiedades["tipo_valor"], 
            concepto.concepto["tipo_valor"], 
            valor1.valor["tipo_valor"], 
            valor2.valor["tipo_valor"], 
            valor3.valor["tipo_valor"]], [None, None, None, None, None, None])
        
        # Asignación de tipo padre y evaluación en tipos heredados

        tipoValorEsperadoSeccion = "tipoValorEsperado"
        tipoValorEsperadoConcepto = "tipoValorEsperadoConcepto"
        tipoValorEsperadoValor1 = "tipoValorEsperadoValor1"

        seccion.conTipoValor(tipoValorEsperadoSeccion)

        self.revisaEquidadElementos([seccion.propiedades["tipo_valor"], 
            concepto.concepto["tipo_valor"], 
            valor1.valor["tipo_valor"], 
            valor2.valor["tipo_valor"], 
            valor3.valor["tipo_valor"]], [tipoValorEsperadoSeccion, tipoValorEsperadoSeccion, tipoValorEsperadoSeccion, tipoValorEsperadoSeccion, tipoValorEsperadoSeccion, tipoValorEsperadoSeccion])
        

        concepto.conTipoValor(tipoValorEsperadoConcepto)
        valor1.conTipoValor(tipoValorEsperadoValor1)

        self.revisaEquidadElementos([seccion.propiedades["tipo_valor"], 
            concepto.concepto["tipo_valor"], 
            valor1.valor["tipo_valor"], 
            valor2.valor["tipo_valor"], 
            valor3.valor["tipo_valor"]], [tipoValorEsperadoSeccion, tipoValorEsperadoConcepto, tipoValorEsperadoValor1, tipoValorEsperadoConcepto, tipoValorEsperadoConcepto])

        '''
        a.propiedades["conceptos"][0]["valores"][0]["tipo_valor"]()
        a.propiedades["conceptos"][0]["valores"][1]["tipo_valor"]()
        a.propiedades["conceptos"][0]["valores"][2]["tipo_valor"]()
        '''