import logging

class custLogger:
    def custLogger(self, loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(custLogger.__name__)
        logger.setLevel(loglevel)

        fh = logging.FileHandler("automation.log")
 
        formatter1 = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')

        fh.setFormatter(formatter1)
        
        logger.addHandler(fh)
        return logger


