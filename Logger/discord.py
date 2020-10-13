import requests
import json

class Discord:
    def __init__(self,message=" ", url="",
        botname="",embed=False,embedDiscription="",embedTitle=""):
        print("Discord Bot initiated")
        self.url = url #webhook url, from here: https://i.imgur.com/aT3AThK.png
        self.data = {}
        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        self.data["content"] = message
        self.data["username"] = botname

        if embed:
            self.data["embeds"] = []
            embed = {}
            #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
            embed["description"] = embedDiscription
            embed["title"] = embedTitle
            self.data["embeds"].append(embed)

    def message(self,message,embedTitle="",embedMode=1):
        if not embedMode:
            self.data["content"] = message
            self.data["embeds"] = []
        if embedMode:
            self.data["content"] = ""
            self.data["embeds"] = []
            embed = {}
            embed["description"] = message
            embed["title"] = embedTitle
            self.data["embeds"].append(embed)

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
                print("Discord message successfully sent, code {}.".format(result.status_code))



#Reference : https://gist.github.com/Bilka2/5dd2ca2b6e9f3573e0c2defe5d3031b2