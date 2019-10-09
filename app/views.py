import json
import configparser
from flask import request
import os
from app import server

logger = server.logger

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

  # TODO: move logging to sepearte module utils, and attach via decorator.
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
