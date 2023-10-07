import requests
import json

webhook_url = ""
pipeline_link_ex = """
https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/<PIPELINE-NAME>/executions/fd70db0f-26f6-4899-b199-8a26957fc4bd/timeline?region=us-east-1&referer_source=codestar-notifications&referer_medium=chatbot
"""

basic_pipeline_link = """
https://us-west-2.console.aws.amazon.com/codesuite/codepipeline/pipelines/<PIPELINE-NAME>/view?region=us-west-2
"""
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

