# -*- coding: utf-8 -*-

class Proxy:
    '''
    Permite realizar el patrón de diseño Proxy
    @see http://lib.bioinfo.pl/courses/view/333
    '''
    def __init__(self, subject):
        self.__subject = subject
        
    def __getattr__( self, name ):
        return getattr( self.__subject, name )


class Struct:
    '''
    Genera un objeto a partir de un dicionario.
    @see http://stackoverflow.com/questions/1305532/convert-python-dict-to-object/1305663#1305663
    '''
    def __init__(self, **entries): 
        self.__dict__.update(entries)