import requests
import json

webhook_url = ""
def handler(event):
    message = {
        "channel": "<#notification-slack-channel>",
        "username": "<slack-bot-name>",
        "icon_emoji": ":uh-oh-sooj:",
        "attachments": [
            {
                "fallback": "CICD: <https://google.com/|open link here>", # Hyperlink
                "pretext": "CICD: <https://google.com/|open link here>",
                "color": "#34bb13",
                "fields": [
                    {
                        "title": "Server",
                        "value": "server is starting!!"
                    }
                ]
            }
        ]
    }

    response = requests.post(url=webhook_url, data=json.dumps(message))

