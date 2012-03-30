#!/usr/bin/python
# -*- coding: utf-8 -*-

import Servicio.ServicioMapaTematico as smt
import Servicio.ServicioMapaTematicoRepresentable
import Servicio.ServicioGestorConjuntos as sgc
import Servicio.ServicioGestorConjuntosRepresentable

import random

cuartiles = [u"Primer cuartil", u"Segundo cuartil", u"Tercer cuartil", u"Cuarto cuartil"]
coloresCuartiles = [u"008000", u"000080", u"c86400", u"ff0000"]
entidadesFederativas = [u'Aguascalientes',u'Baja California',u'Baja California Sur',u'Campeche',u'Coahuila de Zaragoza',u'Colima',u'Chiapas',u'Chihuahua',u'Distrito Federal',u'Durango',u'Guanajuato',u'Guerrero',u'Hidalgo',u'Jalisco',u'México',u'Michoacán de Ocampo',u'Morelos',u'Nayarit',u'Nuevo León',u'Oaxaca',u'Puebla',u'Querétaro Arteaga',u'Quintana Roo',u'San Luis Potosí',u'Sinaloa',u'Sonora',u'Tabasco',u'Tamaulipas',u'Tlaxcala',u'Veracruz de Ignacio de la Llave',u'Yucatán',u'Zacatecas']

def obtenMapaEstadistico():
    mapaEstadistico = smt.ServicioMapaTematico()
    cuartilPorEntidadFederativa = []
    
    nCuratiles = len(cuartiles)
    for iterador in range(len(entidadesFederativas)):
        cuartilPorEntidadFederativa.append(random.randint(0, nCuratiles - 1))
    
    indice = 0
    for cuartil in cuartiles:
        concepto =  mapaEstadistico.obtenConcepto(cuartil)
        concepto.estableceColorEnConcepto(coloresCuartiles[indice])

        for iteradorEntidades in range(len(entidadesFederativas)):
            if cuartilPorEntidadFederativa[iteradorEntidades] == indice:
                concepto.agregaVariableConValorEnConcepto(entidadesFederativas[iteradorEntidades], random.randint(1, 100))

        indice += 1

    return mapaEstadistico


def obtenMapaEstadisticoEnConjunto():
    conjunto = sgc.ServicioGestorConjuntos().conNombre(u"Indicadores ENOE / Bienestar 2010").conVariable(u"Indicador", u"Bienestar").conVariable(u"País", u"México").conVariable(u"Año", u"2010")

    conjunto.obtenSubConjunto().conNombre(u"Indicador Bienestar Nacional 2010 1er Trimestre").conVariable(u"Trimestre", u"1").conSeccion(obtenMapaEstadistico())
    conjunto.obtenSubConjunto().conNombre(u"Indicador Bienestar Nacional 2010 2do Trimestre").conVariable(u"Trimestre", u"2").conSeccion(obtenMapaEstadistico())
    conjunto.obtenSubConjunto().conNombre(u"Indicador Bienestar Nacional 2010 3er Trimestre").conVariable(u"Trimestre", u"3").conSeccion(obtenMapaEstadistico())
    conjunto.obtenSubConjunto().conNombre(u"Indicador Bienestar Nacional 2010 4to Trimestre").conVariable(u"Trimestre", u"4").conSeccion(obtenMapaEstadistico())
    
    return conjunto


    if __name__ == "__main__":
        pass