import custom_logger
import submodule

log = custom_logger.getLogger('root', loglevel='DEBUG')

log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')

a = submodule.SubClass() # this should produce a log message
a.SomeMethod()           # so should this