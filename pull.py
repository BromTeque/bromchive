# Automatic git pull for mod repositories via cron

import os
import git
import time
import logging

# Variables
getTime = str(int(time.time()))
outputDirectory = os.path.join("./logs/" + getTime)


logging.basicConfig(filename=getTime+".log", level=logging.INFO)

