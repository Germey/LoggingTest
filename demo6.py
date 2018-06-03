import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARN)

# Log
logger.debug('Debugging')
logger.critical('Critical Something')
logger.error('Error Occurred')
logger.warning('Warning exists')
logger.info('Finished')
