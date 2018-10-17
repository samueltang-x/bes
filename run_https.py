#!flask/bin/python
from app import server
server.run(host=server.ip,port=server.https_port,ssl_context=server.ssl_context,debug=True)
