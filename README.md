
## Configuration files.

1. config.py

    configurations about IP/port and SSL related parameters.
    Plan to migrate this config file to configparser style.

1. router.conf

    `response.file.filter`: to specify how to find the name of response files, vaule should be separaterd with semicomma.
    Support values as below:

        path: the URI path of request
        body.imsi: the value of attribute imsi in body, (request.json). Multiple and nested attributes could be used.
        args.eid: the value of argment eid in query string. Multiple argments could be used.


## Check server status.
    ./bes.sh status

## Start the server.
    ./bes.sh start
  
    Note:
        You can provide http or https to start server on http or https respectively.
        For example: `./bes.sh start http`
        By default it starts on https.

## Stop the server.
    ./bes.sh stop
	
## setup development environment
`pip3 install -r requirements.txt`

exantng/xiangyuan.tang@ericsson.com
