import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARN)
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%Y/%m/%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Log
logger.debug('Debugging')
logger.critical('Critical Something')
logger.error('Error Occurred')
logger.warning('Warning exists')
logger.info('Finished')
