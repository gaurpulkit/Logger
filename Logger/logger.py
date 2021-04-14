from . import discord as dc
from . import telegram as tg
from . import fileLogger as fl
import logging
from datetime import datetime
import os
import os.path

# Getting Today's Date for LogFileName
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y")

# File Logger Info
LogFolderLocation = './Logs'
LogFileName = dt_string+'.log'
LogFormat = '%(asctime)s - %(message)s'
LogFileMode = 'a'
LogLevel = logging.INFO

# Making the Logs Directory
if not os.path.exists(LogFolderLocation):
    os.makedirs(LogFolderLocation)


class Logger:
    def __init__(self, DcUrl=None, DcBotName=None,
        TgChatID=None, TgbotAPI=None, LogFolderLocation=LogFolderLocation,
        LogFileName=LogFileName, LogFileMode=LogFileMode, LogFormat=LogFormat,
        LogLevel=LogLevel):
        self.DcUrl = DcUrl
        self.DcBotName = DcBotName
        self.TgChatID = TgChatID
        self.TgbotAPI = TgbotAPI
        self.LogFolderLocation = LogFolderLocation
        self.LogFileName = LogFileName
        self.LogFileMode = LogFileMode
        self.LogFormat = LogFormat
        self.LogLevel = LogLevel
        self.discordInitialized = False
        self.telegramInitialized = False

        if self.DcUrl is not None and self.DcBotName is not None:
            self.discordBot = dc.Discord(url=self.DcUrl, botname=self.DcBotName)
            self.discordInitialized = True
            
        if self.TgbotAPI is not None and self.TgChatID is not None:
            self.telegramBot = tg.Telegram(
                        chatID=self.TgChatID, botAPI=self.TgbotAPI)
            self.telegramInitialized = True

        self.fileLogger = fl.FileLogger(filename=self.LogFolderLocation+'/'+self.LogFileName,
            filemode=self.LogFileMode, format=self.LogFormat, level=self.LogLevel)

    def setTelegram(self, TgChatID=None, TgbotAPI=None):
        self.TgChatID = TgChatID
        self.TgbotAPI = TgbotAPI

    def setDiscord(self, DcUrl=None, DcBotName=None):
        self.DcUrl = DcUrl
        self.DcBotName = DcBotName

    def setFileLogger(LogFolderLocation=LogFolderLocation,
        LogFileName=LogFileName, LogFileMode=LogFileMode, LogFormat=LogFormat,
        LogLevel=LogLevel):
        self.LogFolderLocation = LogFolderLocation
        self.LogFileName = LogFileName
        self.LogFormat = '%(asctime)s - %(message)s'
        self.LogLevel = logging.INFO

    def startDiscordLogger(self):
        if self.DcUrl is None or self.DcBotName is None:
            raise Exception("Discord Url or botname not set")
        self.discordBot = dc.Discord(url=self.DcUrl, botname=self.DcBotName)
        self.discordInitialized = True

    def startTelegramLogger(self):
        if self.TgChatID is None or self.TgbotAPI is None:
            raise Exception("Telegram Channel ID or Bot API not set")
        self.telegramBot = tg.Telegram(
            chatID=self.TgChatID, botAPI=self.TgbotAPI)
        self.telegramInitialized = True

    def startFileLogger(self):
        self.fileLogger = fl.FileLogger(filename=self.LogFolderLocation+'/'+self.LogFileName,
            filemode=self.LogFileMode, format=self.LogFormat, level=self.LogLevel)

    def send(self, message="", discord=False, telegram=False, filelogs=True, print=True):
        # This is used to avoid conflict with the inbuilt function print
        noPrint = not print

        if discord:
            if not self.discordInitialized:
                raise Exception("Discord Bot Uninitialized")
            self.discordBot.send(message,noPrint=noPrint)
        if telegram:
            if not self.telegramInitialized:
                raise Exception("Telegram Bot Uninitialized")
            self.telegramBot.send(message,noPrint=noPrint)
        if filelogs:
            self.fileLogger.log(message)
