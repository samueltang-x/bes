import json
import configparser
from flask import request
import os
from app import server

logger = server.logger

# @server.route(server.config['ICCID2IMSI_URL'])
# def ICCID2IMSI():
#   response_headers = {'Content-type': 'application/json'}
#   #imsi = request.args.get('imsi')
#   iccid = request.args['iccid']
#   data_dir = server.config['ICCID2IMSI_DATA_DIR']
#   extention = server.config['ICCID2IMSI_DATA_FILE_EXTENSION']

#   if not iccid:
#     status_code = 400
#     data_file_name = path.join(data_dir, '400_iccid_missing' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#     return (response_body, status_code, response_headers)


#   data_file_name = path.join(data_dir, iccid + extention)

#   if os.path.exists(data_file_name):
#     with open(data_file_name) as data_file:
#       status_code = 200
#       response_body = data_file.read()
#   else:
#     status_code = 404
#     data_file_name = path.join(data_dir, '404_not_found' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#   return (response_body, status_code, response_headers)


# @server.route(server.config['MSISDN2IMSI_URL'],methods=['POST'])
# def MSISDN2IMSI():
#   response_headers = {'Content-type': 'application/json'}
#   #msisdn = request.args.get('msisdn')
#   #msisdn = request.args['msisdn']
#   msisdn = request.json['msisdn']
#   data_dir = server.config['MSISDN2IMSI_DATA_DIR']
#   extention = server.config['MSISDN2IMSI_DATA_FILE_EXTENSION']

#   # Return 400 Bad request if msisdn missing from request.
#   if not request.json or 'msisdn' not in request.json:
#     status_code = 400
#     data_file_name = path.join(data_dir, '400_msisdn_missing' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#     return (response_body, status_code, response_headers)


#   data_file_name = path.join(data_dir, msisdn + extention)

#   if os.path.exists(data_file_name):
#     with open(data_file_name) as data_file:
#       status_code = 200
#       response_body = data_file.read()
#   else:
#     status_code = 404
#     data_file_name = path.join(data_dir, '404_not_found' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#   return (response_body, status_code, response_headers)


# @server.route(server.config['IMSI2MSISDN_URL'],methods=['POST'])
# def IMSI2MSISDN_v2():
#   response_headers = {'Content-type': 'application/json'}
#   #imsi = request.args.get('imsi')
#   #imsi = request.args['imsi']
#   imsi = request.json['imsi']
#   data_dir = server.config['IMSI2MSISDN_DATA_DIR']
#   extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

#   # Return 400 Bad request if imsi missing from request.
#   if not request.json or 'imsi' not in request.json:
#     status_code = 400
#     data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#     return (response_body, status_code, response_headers)


#   data_file_name = path.join(data_dir, imsi + extention)

#   if os.path.exists(data_file_name):
#     with open(data_file_name) as data_file:
#       status_code = 200
#       response_body = data_file.read()
#   else:
#     status_code = 404
#     data_file_name = path.join(data_dir, '404_not_found' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#   return (response_body, status_code, response_headers)


# @server.route(server.config['IMSI2MSISDN_URL'], methods=['DELETE'])
# def releaseMsisdn():
#   response_headers = {'Content-type': 'application/json'}
#   #imsi = request.args.get('imsi')
#   imsi = request.args['imsi']
#   data_dir = server.config['IMSI2MSISDN_DATA_DIR']
#   extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

#   if not imsi:
#     status_code = 400
#     data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#     return (response_body, status_code, response_headers)


#   status_code = 200
#   response_body = '{}'

#   return (response_body, status_code, response_headers)


# @server.route(server.config['IMSI2MSISDN_URL'])
# def IMSI2MSISDN():
#   response_headers = {'Content-type': 'application/json'}
#   #imsi = request.args.get('imsi')
#   imsi = request.args['imsi']
#   data_dir = server.config['IMSI2MSISDN_DATA_DIR']
#   extention = server.config['IMSI2MSISDN_DATA_FILE_EXTENSION']

#   if not imsi:
#     status_code = 400
#     data_file_name = path.join(data_dir, '400_imsi_missing' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#     return (response_body, status_code, response_headers)


#   data_file_name = path.join(data_dir, imsi + extention)

#   if os.path.exists(data_file_name):
#     with open(data_file_name) as data_file:
#       status_code = 200
#       response_body = data_file.read()
#   else:
#     status_code = 404
#     data_file_name = path.join(data_dir, '404_not_found' + extention)
#     with open(data_file_name) as data_file:
#       response_body = data_file.read()

#   return (response_body, status_code, response_headers)


# @server.route(server.config['AUTH_URL'] + '/<imsi>')
# def authenticate(imsi):
#   response_headers = {'Content-type': 'application/json'}

#   data_dir = server.config['AUTH_DATA_DIR']
#   extention = server.config['AUTH_DATA_FILE_EXTENSION']

#   status_code = 200

#   data_file_name = path.join(data_dir, 'imsi-' + imsi + extention)
#   with open(data_file_name) as file_handler:
#     response_body = json.load(file_handler)

#   response_body_str = json.dumps(response_body)

#   return (response_body_str, status_code, response_headers)


def get_dict_attr(d, key):
  if isinstance(key, str):
    key = key.split('.')
  elif (not isinstance(key, list)) and (not isinstance(key, tuple)):
    raise KeyError('get_dict_attr(): key can be only str, list or tuple')
    
  if len(key) < 1:
    raise KeyError('get_dict_attr(): key lenght is 0')
  elif len(key) == 1:
    return d[key[0]]

  return get_dict_attr(d[key[0]], key[1:])


def get_res_file(req, path):
  path = path.lstrip('/')

  config = configparser.ConfigParser()
  config.read(r'config/router.conf')

  if not config.has_section(path):
    logger.debug('no config found for /' + path)
    return 'data/not-found.json'

  filters_str = config[path].get('response.file.filter', '')
  filters = filters_str.replace(' ', '').split(',')
  if len(filters) <= 0:
    return config[path].get('response.file.filter', 'data/not-found.json')

  file_name = ''
  if 'path' in filters:
    file_name = file_name + path.replace('/', '-')
    filters.remove('path')

  for filter_str in filters:
    filter = filter_str.split('.')
    if filter[0] == 'body':
      file_name = file_name + '_' + get_dict_attr(request.json, filter[1:])
    if filter[0] == 'args':
      file_name = file_name + '_' + request.args[filter[1]]

  file_name = 'data/' + file_name.lstrip('-_') + '.json'
  if os.path.exists(file_name):
    return file_name
  
  logger.debug('file %s not found', file_name)

  return 'data/not-found.json'

# TODO: to add other methods when needed
@server.route('/', methods=['GET', 'POST'], defaults={'path': 'root-path'})
@server.route('/<path:path>', methods=['GET', 'POST'])
def default_view(path):
  '''
  The default view function for all requests not yet catch
  TODO: other methods when needed, up to now only support GET and POST
  '''

  log_text = 'client request, %s %s\nheader: %s' % (request.method, request.path, str(request.headers))
  if request.method.upper() == 'GET':
    log_text = log_text + 'query string: {0}'.format(str(dict(request.args)))
  if request.method.upper() == 'POST':
    log_text = log_text + 'body: {0}'.format(str(request.json))

  logger.debug(log_text)

  res_file = get_res_file(request, path)
  logger.debug('respons file: %s', res_file)

  with open(res_file) as file_handler:
    res_data = json.load(file_handler)

  logger.debug('respond client, status: {status}\nheader: {header}\nbody: {body}'.format_map(res_data))
  return (json.dumps(res_data['body']), res_data['status'], res_data['header'])
