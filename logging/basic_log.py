"""
Basic log file
"""
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= './logging/lumberjack.log', level= logging.DEBUG, format= LOG_FORMAT, filemode= 'w')

logger = logging.getLogger()

#Text messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry but I can't do that!")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
