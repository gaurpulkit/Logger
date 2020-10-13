import requests
import json

class Telegram:
    def __init__(self,message=" ",chatID="", botAPI="", disable_notification=True):
        print("Telegram Bot initiated")
        self.url = "https://api.telegram.org/bot%s/sendMessage" % botAPI
        self.data={}
        self.data["text"] = message
        self.data["chat_id"] = chatID
        self.data["disable_notification"]=disable_notification

    def message(self,message,disable_notification=True):
        self.data["text"] = message
        self.data["disable_notification"] = disable_notification

    def send(self,message="",noPrint=False):
        if message != "":
            self.message(message)
        result = requests.post(self.url, data=json.dumps(self.data), headers={"Content-Type": "application/json"})
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if not noPrint:
                print(err)
        else:
            if not noPrint:
                print("Telegram message successfully sent, code {}.".format(result.status_code))


# ref : https://medium.com/@wk0/send-and-receive-messages-with-the-telegram-api-17de9102ab78
# https://medium.com/@dnagikh/to-send-messages-to-your-private-channels-you-have-to-get-your-channels-internal-id-db1088f6ef4
# https://core.telegram.org/bots/api#available-methods
# Bot must be an admin of Channel 