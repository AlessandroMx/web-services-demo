# Servicios REST básicos (GET y REST)
## Instrucciones de Uso
### Correr los servicios:
1. Tener instalado Python 3.5 (o superior).
2. Instalar los siguientes packages de python a través de pip:
    1. pip install cherrypy
    2. pip install cherrypy_cors
3. Modificar el archivo 'web_services.py' en la línea cherrypy.config.update({'server.socket_host': '3.51.55.92'}), poner IP suya o localhost...
4. Correr los servicios con el comando `python web_services.py`
5. Verificar que el servidor este corriendo checando que en consola salga el mensaje "ENGINE Bus STARTED"
6. En caso de que falte algún módulo, instalarlo por medio del pip (o conda).

### Probar servicios:
1. Meterse a algún navegador (de preferencia Chrome).
2. Ir al path del archivo 'index.html' de este proyecto.
3. Dar click en el botón de 'Click para probar!'.
4. Verificar que salga un mensaje con el siguiente contenido "¡JSON recibido y enviado de manera exitosa!".
5. Verificar en consola el string "aloha!" (el que se mandó de prueba desde el test.js).

### Información a tener en cuenta:
1. Se utilizó Python para levantar servicios web, a través de light-framework CherryPy.
2. Se requiere de internet para correr la web app.
3. El cherrypy_cors es esencial para evitar conflictos por el CORS.