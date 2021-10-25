import logging

class LoggerDemo:
    def sample_logger(self):
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
        #ch = logging.StreamHandler()
        fh = logging.FileHandler("demologfile.log")
        #formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        #ch.setFormatter(formatter)
        fh.setFormatter(formatter1)
        logger.addHandler(ch)
        logger.addHandler(fh)

        #logger.debug('This message should go to the log file')
        #logger.info('So should this')
        #logger.warning('And this, too')
        #logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

ld = LoggerDemo()
ld.sample_logger()
