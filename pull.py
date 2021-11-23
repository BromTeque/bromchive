# Automatic git pull for mod repositories via cron

import os
import git
import time
import logging

# Variables
getTime = str(int(time.time()))
outputFile = os.path.join("./.logs/" + getTime + ".log")


logging.basicConfig(filename=outputFile, level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')