#Python logging is a module that allows you to track events that occur while your program is running. 
#This file can be used for logging to record information about errors, warnings, and other events that occur during program execution.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y %H_%M_%S')}.log"

#Creates a pth to currecnt directory with the name logs
log_path = os.path.join(os.getcwd(), "logs")
#Creates a folder in current directory
os.makedirs(log_path, exist_ok= True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,filename = LOG_FILEPATH, format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
