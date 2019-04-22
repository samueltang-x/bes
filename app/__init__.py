import logging
from flask import Flask

# Default setting for logging.
log_level = logging.DEBUG
FORMAT = '%(asctime)-15s [bes] %(levelname)-8s %(message)s'
logging.basicConfig(level=log_level, format=FORMAT)

server = Flask(__name__)
server.config.from_object('config')
server.ip = server.config['IP']
server.port = server.config['PORT']
server.https_port = server.config['HTTPS_PORT']
server.certificate = server.config['SSL_CERTIFICATE']
server.key = server.config['SSL_KEY']
server.ssl_context = (server.certificate, server.key)

from app import views
