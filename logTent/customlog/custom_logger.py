import logging
import logging.handlers
import os
import sys


def getLogger(name='root', loglevel='INFO'):
  logger = logging.getLogger(name)

  # if logger 'name' already exists, return it to avoid logging duplicate
  # messages by attaching multiple handlers of the same type
  if logger.handlers:
    return logger
  # if logger 'name' does not already exist, create it and attach handlers
  else:
    # set logLevel to loglevel or to INFO if requested level is incorrect
    loglevel = getattr(logging, loglevel.upper(), logging.INFO)
    logger.setLevel(loglevel)
    fmt = '%(asctime)s %(filename)-18s %(levelname)-8s: %(message)s'
    fmt_date = '%Y-%m-%dT%T%Z'
    formatter = logging.Formatter(fmt, fmt_date)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if logger.name == 'root':
      logger.warning('Running: %s %s',
                     os.path.basename(sys.argv[0]),
                     ' '.join(sys.argv[1:]))
    return logger