from . import discord as dc
from . import telegram as tg
from . import fileLogger as fl
from datetime import datetime
import os, os.path
from config import TELEGRAM, DISCORD, FILELOGGER

# Telegram Tokens
TgChatID=TELEGRAM.get("channel")
TgbotAPI=TELEGRAM.get("bot")

# Discord Tokens
DcBotName=DISCORD.get("botName")
DcUrl=DISCORD.get("webhook")

# File Logger
LogFolderLocation=FILELOGGER.get("LogFolderLocation")
LogFileMode=FILELOGGER.get("LogFileMode")
LogFormat=FILELOGGER.get("LogFormat")
LogLevel=FILELOGGER.get("LogLevel")

# Getting Today's Date for LogFileName
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y")
LogFileName=dt_string+'.log'

# Making the Logs Directory
if not os.path.exists(LogFolderLocation):
    os.makedirs(LogFolderLocation)

class Logger:
    def __init__(self):
        self.discordBot=dc.Discord(url=DcUrl,botname=DcBotName)
        self.telegramBot=tg.Telegram(chatID=TgChatID,botAPI=TgbotAPI)
        self.fileLogger=fl.FileLogger(filename=LogFolderLocation+'/'+LogFileName,filemode=LogFileMode,
        format=LogFormat,level=LogLevel)

    def send(self,message="",discord=True,telegram=True,filelogs=True):
        if discord:
            self.discordBot.send(message,noPrint=True)
        if telegram:
            self.telegramBot.send(message,noPrint=True)
        if filelogs:
            self.fileLogger.log(message)