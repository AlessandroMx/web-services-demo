import cherrypy
import cherrypy_cors
import json

@cherrypy.expose
class WebServices(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, data='datos enviados por GET...'):
        """
        Método GET para enviar información en formato string.
        Al recibirlo, únicamente obtiene el string enviado por usuario.
        
        Args:
            data: String
        
        Return:
            El return de ejemplo es el string recibido por el servicio.
        """
        return data
    
    def POST(self, json_data):
        """
        Método POST para enviar objetos en formato JSON.
        Al recibirlo, únicamente obtiene el contenido del key del objeto
        enviado.
        
        Args:
            json_data: Objeto
        
        Return:
            El return de ejemplo es un string. Puede cambiarse a enviar un
            objeto en formato JSON.
        """
        print(json_data)
        return 'heelloo'

if __name__ == '__main__':
    cherrypy_cors.install()
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'cors.expose.on': True,
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update({'server.socket_host': '3.51.55.92'})
    cherrypy.config.update({'server.socket_port': 9002})
    cherrypy.quickstart(WebServices(), '/', conf)
