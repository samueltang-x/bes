import logging
from flask import Flask

# Default setting for logging.
log_level = logging.DEBUG
FORMAT = '%(asctime)-15s [bes] %(levelname)-8s %(message)s'
logging.basicConfig(level=log_level, format=FORMAT)

server = Flask(__name__)

from app import views
