import logging

logging.debug('Debugging information')
logging.debug("{0}{1}".format(1, 2))
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

