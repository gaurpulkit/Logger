# Logger
A Python Module to create logs on Discord, Telegram or a local file

## Usage
```
from Logger import logger

# Creating a Logger object
loggerObject = logger.Logger()

# Sending a log
log="Hello World"
loggerObject.send(log,discord=True,telegram=True,filelogs=True)
```
