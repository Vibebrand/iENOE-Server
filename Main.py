#!/usr/bin/python
# -*- coding: utf-8 -*-

import Servicio.ServicioMapaTematico as smt
import random

cuartiles = ["Primer cuartil", "Segundo cuartil", "Tercer cuartil", "Cuarto cuartil"]
coloresCuartiles = ["008000", "000080", "c86400", "ff0000"]
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

if __name__ == "__main__":
    '''
    @see http://stackoverflow.com/questions/713847/recommendations-of-python-rest-web-services-framework
    '''
    import web
    import json
    from mimerender import mimerender

    urls = (
        '/(.*)', 'greet'
    )

    render_xml = lambda message: '<message>%s</message>'%message
    render_json = lambda **args: json.dumps(args)
    render_html = lambda message: u'<html><body><h1>Sistema iENOE</h1><p>enfocado en la presentación de los indicadores más relevantes de la ENOE</p></body></html>'
    render_txt = lambda message: message

    class greet:
        @mimerender(
            default = 'html',
            html = render_html,
            xml  = render_xml,
            json = render_json,
            txt  = render_txt
        )
        
        def GET(self, name):
            if not name: 
                name = 'world'
            return {'message': 'Hello, ' + name + '!'}
        
    app = web.application(urls, globals())
