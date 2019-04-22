import configparser
import ssl
from app import server

logger = server.logger

VERSION_MAP = {
  'tls1.0': ssl.TLSVersion.TLSv1,
  'tls1.1': ssl.TLSVersion.TLSv1_1,
  'tls1.2': ssl.TLSVersion.TLSv1_2,
  'tls1.3': ssl.TLSVersion.TLSv1_3,
}


def create_ssl_ctx(config):
  ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  ssl_conf = config['ssl']
  server_cert = ssl_conf['server_cert']
  private_key = ssl_conf['private_key']
  logger.info('server certificate: {0}, private key: {1}'.format(server_cert, private_key))
  ssl_ctx.load_cert_chain(certfile=server_cert, keyfile=private_key)

  min_ver = ssl_conf.get('min_ssl_version', 'tls1.1')
  if min_ver:
    logger.info('set the lowest supported tls version to: ' + min_ver)
    ssl_ctx.minimun_version = VERSION_MAP[min_ver]
    
  max_ver = ssl_conf.get('max_ssl_version', '')
  if max_ver:
    logger.info('set the highest supported tls version to: ' + max_ver)
    ssl_ctx.maximum_version = VERSION_MAP[max_ver]

  ciphers = ssl_conf.get('cipher_list', '')
  if ciphers:
    logger.info('set ciphers list: ' + ciphers)
    ssl_ctx.set_ciphers(ciphers)

  if ssl_conf.getboolean('verify_client', False):
    logger.info('client cert authentication enabled.')
    ssl_ctx.verify_mode = ssl.CERT_REQUIRED

    ca_file = ssl_conf('ca_file', '')
    ca_path = ssl_conf('ca_path', '')

    if (not ca_file) and (not ca_path):
      raise ValueError('as least one of ca_file and ca_path should be configured when client cert auth enabled')
    if not ca_file:
      ca_file = None
    if not ca_path:
      ca_path = None

    logger.info('set client cert authentication: cafile: {0}, capath: {1}'.format(ca_file, ca_path))
    ssl_ctx.load_verify_locations(ca_file, ca_path)

  return ssl_ctx


def create_srv_options():
  config_file = r'config/server.conf'

  config = configparser.ConfigParser()
  config.read(config_file)
  options = {}

  options['port'] = config['general'].getint('port', 18080)
  options['host'] = config['general'].get('ip', '0.0.0.0')
  options['debug'] = config['general'].getboolean('debug', False)

  https = config['general'].getboolean('https', True)

  if https:
    options['ssl_context'] = create_ssl_ctx(config)

  logger.info('server options: ' + str(options))
  return options