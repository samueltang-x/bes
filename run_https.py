#!venv/bin/python

from app import server, config

server.run(**config.create_srv_options())
