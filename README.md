# Logger
A Python Module to create logs on Discord, Telegram or a local file

## Installation
Either
```bash
pip install Logger-Zuj3brusu
```
Or
```bash
pip install git+git://github.com/Zuj3brusu/Logger.git
```

## Usage
### Initialization
```python
from Logger import logger

# Creating a Logger object
loggerObject = logger.Logger()
```

#### Initialize Discord Logger (Optional / Only needed to send Discord Logs)
One way to do this is to directly set the values of DcUrl and DcBotName while initializing the logger. Another way to do this is
```python
# Set the values of Discord Webhook url and Bot Name
loggerObject.setDiscord(DcUrl = <Channel Webhook>, DcBotName = <Name of the Bot>)

# Start the Discord Logger
loggerObject.startDiscordLogger()
```


#### Initialize Telegram Logger (Optional / Only needed to send Telegram Logs)
One way to do this is to directly set the values of TgChatID and TgbotAPI while initializing the logger. Another way to do this is
```python
# Set the values of Telegram Chat ID and Bot API
loggerObject.setTelegram(TgChatID = <Chat ID>, TgbotAPI = <Bot API>)

# Start the Telegram Logger
loggerObject.startDiscordLogger()
```


#### Initialize FileLogger
While the FileLogger is initialized by default, you can still change any/all of the parameters.
One way to do this is to directly set the values of FileLogger parameters while initializing the logger. Another way to do this is
```python
# Set the values of Telegram Chat ID and Bot API
loggerObject.setFileLogger(
	LogFolderLocation = <LogFolderLocation>,
	LogFileName       = <LogFileName>,
	LogFileMode       = <LogFileMode>,
	LogFormat         = <LogFormat>,
	LogLevel          = <LogLevel>
	)

# Start the FileLogger
loggerObject.startFileLogger()
```


### Sending a log
Logs can be sent using any/all Logger(s). You just need to set the values of parameters to `True` for the Loggers for which you want to send the logs.

`print` Determines whether to print success or error messages.
```python
log="Hello World"

loggerObject.send(log,discord=True,telegram=True,filelogs=True,print=True)
```

## Thanks for checking it out!
