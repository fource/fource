import logging

LOG_FILE_PATH = '/var/log/fource.log'

# Sentry for catching exceptions
SENTRY_DSN = None

# create logger
logger = logging.getLogger('FOURCE')
logger.setLevel(logging.DEBUG)

# create File handler
fh = logging.FileHandler(LOG_FILE_PATH)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(fh)
