from settings import Config
config = Config()

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'US/Central'
BROKER_POOL_LIMIT=None

# Log debug messages to console
def dlog(str):
  if config["VERBOSE"]:
    print 'DEBUG: %s' % str

if config["HEROKU_DB"]:
  import os
  url = os.environ.get('BROKER_URL')
else:
  url = 'redis://localhost:6379/0'

BROKER_URL = url
CELERY_RESULT_BACKEND = url

dlog('Broker_Url %s' % url)

