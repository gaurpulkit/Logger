import logging

TELEGRAM = {
  "channel": "<CHANNEL ID>",
  "bot": "<BOT TOKEN>"
}

DISCORD = {
  "botName": "<BOT NAME>",
  "webhook": "<DISCORD CHANNEL WEBHOOK URL>"
}

FILELOGGER = {
  "LogFolderLocation": "./Logs",
  "LogFileMode": 'a',
  "LogFormat": '%(asctime)s - %(message)s',
  "LogLevel":logging.INFO
}