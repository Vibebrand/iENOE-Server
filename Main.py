import hashlib
import web
import os
import json
from mimerender import mimerender

def hashfile(filepath):
    sha1 = hashlib.sha1()
    fileZise = os.path.getsize(filepath)
    contenido = None
    try:
        with open(filepath, 'rb') as f:
            contenido = f.read()
    finally:
        print "Finalizado lectura de archivo:", filepath
    if contenido is not None:
        sha1.update("blob " + str(fileZise)  + "\0" + contenido)
        return sha1.hexdigest()
    return ""

urls = (
    '/(.*)', 'greet'
)

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
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

if __name__ == "__main__":
    app.run()
