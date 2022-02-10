"""We wont create a log file"""

import logging

name = 'honey'

logging.info("Program started")
logging.debug(f"{name} ran the program")
logging.warning("This will get printed!")