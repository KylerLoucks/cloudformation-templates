import requests
import json
import boto3
import pprint

client = boto3.client('codepipeline', region_name="us-west-2")

response = client.get_pipeline_execution(
    pipelineName='pipeline-test-kloucks',
    pipelineExecutionId='adf18297-de6f-4e1e-ae07-dd7d9e79aee3'
)

# example pipeline execution response:
get_execution_response = {
    'pipelineExecution': {
        'pipelineName': 'pipeline-test-kloucks',
        'pipelineVersion': 1,
        'pipelineExecutionId': 'adf18297-de6f-4e1e-ae07-dd7d9e79aee3',
        'status': 'InProgress',
        'artifactRevisions': [
            {
                'name': 'SourceOutput',
                'revisionId': 'ddbe7ef257512f9455e9b74a5ebe8ef831e615b7',
                'revisionSummary': '{"ProviderType":"GitHub","CommitMessage":"initial commit"}',
                'revisionUrl': 'https://us-west-2.console.aws.amazon.com/codesuite/settings/connections/redirect?connectionArn=arn:aws:codestar-connections:us-west-2:570351108046:connection/221894bb-cd29-4356-ba84-c0cd816af416&referenceType=COMMIT&FullRepositoryId=cloud303-kloucks/documentdb-example&Commit=ddbe7ef257512f9455e9b74a5ebe8ef831e615b7'
            }
        ]
    },
    'ResponseMetadata': {
        'RequestId': 'b53a3ba6-be65-4ba6-a032-c9ebfc913658',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'b53a3ba6-be65-4ba6-a032-c9ebfc913658',
            'date': 'Tue, 10 Oct 2023 17:54:13 GMT',
            'content-type': 'application/x-amz-json-1.1',
            'content-length': '808',
            'connection': 'keep-alive'
        },
        'RetryAttempts': 0
    }
}


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

