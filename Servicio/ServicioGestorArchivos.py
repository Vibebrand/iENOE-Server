# -*- coding: utf-8 -*-

import hashlib
import os

def hashfile(filepath):
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
