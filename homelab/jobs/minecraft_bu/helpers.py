
import requests
from datetime import datetime

def today():
    tmp = datetime.today().strftime('%Y%m%d')
    return tmp

def send_webhook(url, message, username, embeds = None):
    """
    Send a message to a webhook.
    see https://gist.github.com/Bilka2/5dd2ca2b6e9f3573e0c2defe5d3031b2
    """
    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content" : message,
        "username" : username
    }
    #leave this out if you dont want an embed
    #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = embeds
    result = requests.post(url, json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


