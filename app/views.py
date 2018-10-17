from os import path
import json

from flask import request

from app import server


@server.route(server.config['ICCID2IMSI_URL'])
def ICCID2IMSI():
  response_headers = {'Content-type': 'application/json'}
  #imsi = request.args.get('imsi')
  iccid = request.args['iccid']
  data_dir = server.config['ICCID2IMSI_DATA_DIR']
  extention = server.config['ICCID2IMSI_DATA_FILE_EXTENSION']

  if not iccid:
    status_code = 400
    data_file_name = path.join(data_dir, '400_iccid_missing' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

    return (response_body, status_code, response_headers)


  data_file_name = path.join(data_dir, iccid + extention)

  if path.exists(data_file_name):
    with open(data_file_name) as data_file:
      status_code = 200
      response_body = data_file.read()
  else:
    status_code = 404
    data_file_name = path.join(data_dir, '404_not_found' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

  return (response_body, status_code, response_headers)


@server.route(server.config['MSISDN2IMSI_URL'],methods=['POST'])
def MSISDN2IMSI():
  response_headers = {'Content-type': 'application/json'}
  #msisdn = request.args.get('msisdn')
  #msisdn = request.args['msisdn']
  msisdn = request.json['msisdn']
  data_dir = server.config['MSISDN2IMSI_DATA_DIR']
  extention = server.config['MSISDN2IMSI_DATA_FILE_EXTENSION']

  # Return 400 Bad request if msisdn missing from request.
  if not request.json or 'msisdn' not in request.json:
    status_code = 400
    data_file_name = path.join(data_dir, '400_msisdn_missing' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

    return (response_body, status_code, response_headers)


  data_file_name = path.join(data_dir, msisdn + extention)

  if path.exists(data_file_name):
    with open(data_file_name) as data_file:
      status_code = 200
      response_body = data_file.read()
  else:
    status_code = 404
    data_file_name = path.join(data_dir, '404_not_found' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

  return (response_body, status_code, response_headers)


@server.route(server.config['IMSI2MSISDN_URL'],methods=['POST'])
def IMSI2MSISDN_v2():
  response_headers = {'Content-type': 'application/json'}
  #imsi = request.args.get('imsi')
  #imsi = request.args['imsi']
  imsi = request.json['imsi']
  data_dir = server.config['IMSI2MSISDN_DATA_DIR']
  extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

  # Return 400 Bad request if imsi missing from request.
  if not request.json or 'imsi' not in request.json:
    status_code = 400
    data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

    return (response_body, status_code, response_headers)


  data_file_name = path.join(data_dir, imsi + extention)

  if path.exists(data_file_name):
    with open(data_file_name) as data_file:
      status_code = 200
      response_body = data_file.read()
  else:
    status_code = 404
    data_file_name = path.join(data_dir, '404_not_found' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

  return (response_body, status_code, response_headers)


@server.route(server.config['IMSI2MSISDN_URL'], methods=['DELETE'])
def releaseMsisdn():
  response_headers = {'Content-type': 'application/json'}
  #imsi = request.args.get('imsi')
  imsi = request.args['imsi']
  data_dir = server.config['IMSI2MSISDN_DATA_DIR']
  extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

  if not imsi:
    status_code = 400
    data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

    return (response_body, status_code, response_headers)


  status_code = 200
  response_body = '{}'

  return (response_body, status_code, response_headers)


@server.route(server.config['IMSI2MSISDN_URL'])
def IMSI2MSISDN():
  response_headers = {'Content-type': 'application/json'}
  #imsi = request.args.get('imsi')
  imsi = request.args['imsi']
  data_dir = server.config['IMSI2MSISDN_DATA_DIR']
  extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

  if not imsi:
    status_code = 400
    data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

    return (response_body, status_code, response_headers)


  data_file_name = path.join(data_dir, imsi + extention)

  if path.exists(data_file_name):
    with open(data_file_name) as data_file:
      status_code = 200
      response_body = data_file.read()
  else:
    status_code = 404
    data_file_name = path.join(data_dir, '404_not_found' + extention)
    with open(data_file_name) as data_file:
      response_body = data_file.read()

  return (response_body, status_code, response_headers)


@server.route(server.config['GETENTITLEMENT_URL'],methods=['POST'])
def getEntitlement():
  response_headers = {'Content-type': 'application/json'}

  data_dir = server.config['GETENTITLEMENT_DATA_DIR']
  extention = server.config['GETENTITLEMENT_DATA_FILE_EXTENSION']

  if not request.json \
     or 'imsi' not in request.json \
     or 'entitlement-names' not in request.json:
    status_code = 400
    data_file_name = path.join(data_dir, '400_invalid_parameters' + extention)
    with open(data_file_name, 'r') as file_handler:
      response_body = json.load(file_handler)


    response_body_str = json.dumps(response_body)
    return (response_body_str, status_code, response_headers)

  imsi = request.json['imsi']
  entitlement_names = request.json['entitlement-names']


  data_file_name = path.join(data_dir, imsi + extention)

  if path.exists(data_file_name):
    with open(data_file_name) as file_handler:
      status_code = 200
      response_body = json.load(file_handler)
  else:
    status_code = 404
    data_file_name = path.join(data_dir, '404_not_found' + extention)
    with open(data_file_name) as file_handler:
      response_body = json.load(file_handler)

  response_body_str = json.dumps(response_body)
  return (response_body_str, status_code, response_headers)


@server.route(server.config['ESIMSUBSCRIPTION_URL'])
def queryESimSubscription():
  response_headers = {'Content-type': 'application/json'}

  data_dir = server.config['ESIMSUBSCRIPTION_DATA_DIR']
  extention = server.config['ESIMSUBSCRIPTION_DATA_FILE_EXTENSION']

  if 'eid' not in request.args and 'primaryImsi' not in request.args:
    status_code = 400
    data_file_name = path.join(data_dir, '400_invalid_parameters' + extention)
    with open(data_file_name, 'r') as file_handler:
      response_body = json.load(file_handler)

    response_body_str = json.dumps(response_body)
    return (response_body_str, status_code, response_headers)

  if 'eid' in request.args.keys():
    eid = request.args['eid']
    data_file_name = path.join(data_dir, 'eid_' + eid + extention)
    if path.exists(data_file_name):
      with open(data_file_name) as file_handler:
        status_code = 200
        response_body = json.load(file_handler)

      response_body_str = json.dumps(response_body)
      return (response_body_str, status_code, response_headers)

  if 'primaryImsi' in request.args.keys():
    primaryImsi = request.args['primaryImsi']
    data_file_name = path.join(data_dir, 'pimsi_' + primaryImsi + extention)
    if path.exists(data_file_name):
      with open(data_file_name) as file_handler:
        data = json.load(file_handler)
        status_code = data['status']
        response_body = json.dumps(data['body'])

      return (response_body, status_code, response_headers)


  status_code = 404
  data_file_name = path.join(data_dir, '404_not_found' + extention)
  with open(data_file_name) as file_handler:
    response_body = json.load(file_handler)

  response_body_str = json.dumps(response_body)
  return (response_body_str, status_code, response_headers)



@server.route(server.config['AUTH_URL'] + '/<imsi>')
def authenticate(imsi):
  response_headers = {'Content-type': 'application/json'}

  data_dir = server.config['AUTH_DATA_DIR']
  extention = server.config['AUTH_DATA_FILE_EXTENSION']

  status_code = 200

  data_file_name = path.join(data_dir, 'imsi-' + imsi + extention)
  with open(data_file_name) as file_handler:
    response_body = json.load(file_handler)

  response_body_str = json.dumps(response_body)

  return (response_body_str, status_code, response_headers)


