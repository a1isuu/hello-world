import logLol
from logLol import logging


logger = logging.getLogger(__name__)
logger.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='exemplo_2.log',
                    filemode='w',
                    level='logLol.DEBUG')

   