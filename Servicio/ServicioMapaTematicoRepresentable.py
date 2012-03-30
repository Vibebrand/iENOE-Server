# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy
from Herramienta.Proxy import Struct


###--ServicioMapaTematicoRenderizadorXML--###

class ServicioMapaTematicoRenderizadorXML(Proxy):
    '''
    Clase que genera el XML necesario para renderizar un tipo ServicioMapaTematico
    @see http://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
    '''
    def obtenRepresentacion(self):
        salida = u'''
            <seccion nombre="$$nombreSeccion">
                $$contenidoSeccion
            </seccion>
        '''

       # TODO Considerar más información complementaria 
        nombreSeccion = getattr(self.info, u"nombreSeccion", u"Indicadores Color Mexico")
        contenidoSeccion = ""

        for nombreConcepto in self.conceptos:
            concepto = self.conceptos[nombreConcepto]
            colorPorConcepto = None if nombreConcepto not in self.colorPorConcepto else self.colorPorConcepto[nombreConcepto]

            contenidoSeccion += self.__obtenRepresentacionConcepto(nombreConcepto, concepto, colorPorConcepto)

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenRepresentacionConcepto(self, nombreConcepto, concepto, colorPorConcepto = None):
        salida = u'''
            <concepto nombre="$$nombreConcepto">
                $$contenidoConcepto
            </concepto>
        '''

        contenidoConcepto = ""
        contenidoConcepto += self.__obtenRepresentacionValor(u"Color", colorPorConcepto, tipo_valor = u"color")

        for llave in concepto:
            valor = concepto[llave]
            contenidoConcepto += self.__obtenRepresentacionValor(llave, valor)

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenRepresentacionValor(self, llave, valor, **argumentos):
        salida = u'''
            <valor nombre="$$llave" $$atributos>$$valor</valor>
        '''

        atributos = ""

        for elemento in argumentos:
            atributos += u'{0}= "{1}" '.format(elemento, argumentos[elemento])

        return self.__actualizaSegunVariables(salida, locals())

    def __actualizaSegunVariables(self, informacion, locales):
        '''
            Substitucion de elementos con variables definidas en los metodos que le invocan
            @see http://stackoverflow.com/questions/1041639/get-a-dict-of-all-variables-currently-in-scope-and-their-values
        '''
        informacionAnterior = ""

        while informacion != informacionAnterior:
            informacionAnterior = informacion
            for llave in locales:
                informacion  = informacion.replace(u"$$" + llave, unicode(locales[llave]))

        return informacion



# Enlazador de Representacion
# Ref: http://code.activestate.com/recipes/52192-add-a-method-to-a-class-instance-at-runtime/

from Servicio.ServicioMapaTematico import ServicioMapaTematico
from Herramienta.Proxy import Struct

def obtenRepresentacion(self, formato = u"XML", info = {}):
    servicioMapaTematicoRenderizador = None

    if type(info) is dict:
        info = Struct(**info)

    # TODO Inyectar proveedor
    if formato == u"XML":
        servicioMapaTematicoRenderizador = ServicioMapaTematicoRenderizadorXML(self)

    if servicioMapaTematicoRenderizador is not None:
        servicioMapaTematicoRenderizador.info = info
        servicioMapaTematicoRenderizador.formato = formato
        return servicioMapaTematicoRenderizador.obtenRepresentacion() 


setattr(ServicioMapaTematico, "obtenRepresentacion", obtenRepresentacion)
