# -*- coding: utf-8 -*-

import hashlib
import os

def hashfile(filepath):
    '''
        Obtiene el identificador de un archivo determinado
        @see http://stackoverflow.com/questions/552659/assigning-git-sha1s-without-git
        @see http://stackoverflow.com/questions/1869885/calculating-sha1-of-a-file
    '''
    sha1 = hashlib.sha1()
    contenido = None
    try:
        fileZise = os.path.getsize(filepath)
        with open(filepath, 'rb') as f:
            contenido = f.read()
    finally:
        print "Finalizado lectura de archivo:", filepath
    if contenido is not None:
        sha1.update("blob " + str(fileZise)  + "\0" + contenido)
        return sha1.hexdigest()
    return ""
