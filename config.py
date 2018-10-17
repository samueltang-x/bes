IP = '10.175.147.186'
PORT = 28080
HTTPS_PORT = 28081
SSL_CERTIFICATE = './ssl/pic_chain_wildcard.pem'
SSL_KEY = './ssl/pic_key_wildcard.pem'



AUTH_URL = '/esintegration/v.10/authentication_vector'
AUTH_DATA_DIR = './data/auth/'
AUTH_DATA_FILE_EXTENSION = '.json'

ICCID2IMSI_URL = '/esintegration/v1.0/esim/imsi'
ICCID2IMSI_DATA_DIR = './data/iccid2imsi/'
ICCID2IMSI_DATA_FILE_EXTENSION = '.json'

IMSI2MSISDN_URL = '/esintegration/v1.0/useridentities/msisdn'
IMSI2MSISDN_DATA_DIR = './data/imsi2msisdn/'
IMSI2MSISDN_DATA_FILE_EXTENSION = '.json'

MSISDN2IMSI_URL = '/esintegration/v1.0/useridentities/imsi'
MSISDN2IMSI_DATA_DIR = './data/msisdn2imsi/'
MSISDN2IMSI_DATA_FILE_EXTENSION = '.json'

GETENTITLEMENT_URL = '/esintegration/v1.0/entitlements'
GETENTITLEMENT_DATA_DIR  = './data/entitlements/'
GETENTITLEMENT_DATA_FILE_EXTENSION = '.json'

ESIMSUBSCRIPTION_URL = '/esintegration/v1.0/esim/subscriptions'
ESIMSUBSCRIPTION_DATA_DIR  = './data/esimsubscriptions/'
ESIMSUBSCRIPTION_DATA_FILE_EXTENSION = '.json'
