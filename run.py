#!venv/bin/python

from app import server, config
import logging

server_options = config.create_srv_options()

# Default setting for logging.
if server_options['debug']:
  log_level = logging.DEBUG
else:
  log_level = logging.INFO

FORMAT = '%(asctime)-15s [bes] %(levelname)-8s %(message)s'
logging.basicConfig(level=log_level, format=FORMAT)

server.run(**server_options)
