# -*- coding: utf-8 -*-

from Herramienta.Proxy import Proxy
from Herramienta.Proxy import Struct

###--ServicioMapaTematico--###

class ServicioMapaTematico(object):
    def __init__(self):
        self.variables = {}
        self.conceptos = {}
        self.colorPorConcepto = {}
    
    def agregaVariableFiltro(self, variable, valor):
        self.variables[variable] = valor
        return self

    def obtenConcepto(self, nombreConcepto):
        concepto = None
        if nombreConcepto not in self.conceptos:
            self.conceptos[nombreConcepto] = {}

        elementoProxy = ServicioMapaTematicoConcepto(self)
        elementoProxy.nombreConcepto = nombreConcepto
        elementoProxy.concepto = self.conceptos[nombreConcepto]
        return elementoProxy

    def obtenRepresentacion(self, formato = u"XML", info = {}):
        servicioMapaTematicoRenderizador = None

        if type(info) is dict:
            info = Struct(**info)

        # TODO Inyectar proveedor
        if formato == u"XML":
            servicioMapaTematicoRenderizador = ServicioMapaTematicoRenderizadorXML(self)

        if servicioMapaTematicoRenderizador is not None:
            servicioMapaTematicoRenderizador.info = info
            return servicioMapaTematicoRenderizador.obtenRepresentacion()

###--ServicioMapaTematicoConcepto--###

class ServicioMapaTematicoConcepto(Proxy):
    def agregaVariableConValorEnConcepto(self, variable, valor):
        self.concepto[variable] = valor
        return self
    
    def estableceColorEnConcepto(self, nombreColor):
        self.colorPorConcepto[self.nombreConcepto] = nombreColor
        return self

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
        contenidoConcepto += self.__obtenRepresentacionValor(u"Color", colorPorConcepto, u"color")

        for llave in concepto:
            valor = concepto[llave]
            contenidoConcepto += self.__obtenRepresentacionValor(llave, valor, "")

        return self.__actualizaSegunVariables(salida, locals())

    def __obtenRepresentacionValor(self, llave, valor, tipoValor = None):
        salida = u'''
            <valor nombre="$$llave" $$atributos>$$valor</valor>
        '''

        atributos = ""
        atributos = atributos if tipoValor is not None and len(tipoValor) == 0 else atributos + u' tipo-valor="$$tipoValor" '

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
