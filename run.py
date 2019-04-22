#!venv/bin/python
from app import server
server.run(host=server.ip,port=server.port,debug=True)
