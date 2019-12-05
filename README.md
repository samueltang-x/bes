
## Configuration files.

1. config/server.conf

    configurations about IP/port and SSL related parameters.

1. config/router.conf

    `response.file.filter`: to specify how to find the name of response files from directory `data`, vaule should be separaterd with semicomma.
    Support values as below:

        path: the URI path of request (the slash '/' will be replaced with '-' as actual filename)
        body.imsi: the value of attribute imsi in body, (request.json). Multiple and nested attributes could be used.
        args.eid: the value of argument eid in query string. Multiple argments could be used.
		
        for example, with config
	        [factory/product]
	        response.file.filter = path, args.id, body.category
	    request GET /factory/product?id=123 -H 'content:type: application/json' -d '{"category":"IT"}' will try get response with content from file data/factory-product_123_IT.json.

	
## setup development environment
Requirement: Python 3.7<br>
change directory to root dir of the repo, then run below commands.

    source venv/bin/activate
    pip3 install -r requirements.txt

exantng/xiangyuan.tang@ericsson.com
