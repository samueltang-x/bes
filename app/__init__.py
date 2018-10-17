from flask import Flask

server = Flask(__name__)
server.config.from_object('config')
server.ip = server.config['IP']
server.port = server.config['PORT']
server.https_port = server.config['HTTPS_PORT']
server.certificate = server.config['SSL_CERTIFICATE']
server.key = server.config['SSL_KEY']
server.ssl_context = (server.certificate, server.key)

from app import views
