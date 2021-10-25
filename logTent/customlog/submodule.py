import sys
import custom_logger
import logging


class SubClass(object):

  def __init__(self):
    # NOK (no idea why since by default (no name parameter), it should return the root logger)
    #log = logging.getLogger()
    #log.info('message from SubClass / __init__')

    # OK (works as expected)
    #log = logging.getLogger('root')
    #log.info('message from SubClass / __init__')

    # OK (works as expected)
    log = custom_logger.getLogger('root')
    log.info('message from SubClass / __init__')


  def SomeMethod(self):
    # OK but I'd have to define `log` for every method, which is unacceptable
    # Please see question below all code snippets
    log = custom_logger.getLogger('root')
    log.info('message from SubClass / SomeMethod')