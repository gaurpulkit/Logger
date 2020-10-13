# Importing Logger
from Logger import logger

# Creating a Logger object
loggerObject = logger.Logger()

# Sending a log
log="Hello World"
loggerObject.send(log,discord=True,telegram=True,filelogs=True)