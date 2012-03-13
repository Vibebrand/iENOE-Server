#!/usr/bin/python
# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    app.run()
