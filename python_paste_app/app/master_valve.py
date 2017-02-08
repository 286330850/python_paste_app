import os

from paste import httpserver
from paste.deploy import loadapp

if __name__== '__main__':
    cfg_file = 'paste.ini'
    app = 'main'
    
    wsgi_app = loadapp("config:%s" % os.path.abspath(cfg_file), name=app)
    httpserver.serve(wsgi_app)
    