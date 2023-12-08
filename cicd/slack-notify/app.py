import requests
import json
import boto3
import pprint
import time

# client = boto3.client('codepipeline', region_name="us-west-2")

# response = client.get_pipeline_execution(
#     pipelineName='pipeline-test-kloucks',
#     pipelineExecutionId='adf18297-de6f-4e1e-ae07-dd7d9e79aee3'
# )

# # example pipeline execution response:
# get_execution_response = {
#     'pipelineExecution': {
#         'pipelineName': 'pipeline-test-kloucks',
#         'pipelineVersion': 1,
#         'pipelineExecutionId': 'adf18297-de6f-4e1e-ae07-dd7d9e79aee3',
#         'status': 'InProgress',
#         'artifactRevisions': [
#             {
#                 'name': 'SourceOutput',
#                 'revisionId': 'ddbe7ef257512f9455e9b74a5ebe8ef831e615b7',
#                 'revisionSummary': '{"ProviderType":"GitHub","CommitMessage":"initial commit"}',
#                 'revisionUrl': 'https://us-west-2.console.aws.amazon.com/codesuite/settings/connections/redirect?connectionArn=arn:aws:codestar-connections:us-west-2:570351108046:connection/221894bb-cd29-4356-ba84-c0cd816af416&referenceType=COMMIT&FullRepositoryId=cloud303-kloucks/documentdb-example&Commit=ddbe7ef257512f9455e9b74a5ebe8ef831e615b7'
#             }
#         ]
#     },
#     'ResponseMetadata': {
#         'RequestId': 'b53a3ba6-be65-4ba6-a032-c9ebfc913658',
#         'HTTPStatusCode': 200,
#         'HTTPHeaders': {
#             'x-amzn-requestid': 'b53a3ba6-be65-4ba6-a032-c9ebfc913658',
#             'date': 'Tue, 10 Oct 2023 17:54:13 GMT',
#             'content-type': 'application/x-amz-json-1.1',
#             'content-length': '808',
#             'connection': 'keep-alive'
#         },
#         'RetryAttempts': 0
#     }
# }



# pipeline_link_ex = """
# https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/<PIPELINE-NAME>/executions/fd70db0f-26f6-4899-b199-8a26957fc4bd/timeline?region=us-east-1&referer_source=codestar-notifications&referer_medium=chatbot
# """

# basic_pipeline_link = """
# https://us-west-2.console.aws.amazon.com/codesuite/codepipeline/pipelines/<PIPELINE-NAME>/view?region=us-west-2
# """

red_color = "#D00000", # Red color for failure

webhook_url = ""
def handler(event):
    execution_id = "fd70db0f-26f6-4899-b199-8a26957fc4bd"
    region = "us-east-1"
    account_id = "958570784942"
    pipeline_name = "kloucks-cicd-notifier"
    commit_message = "initial commit. testing testing testing testing testing testing testing testing testing testing testing testing testing testing testing testing"
    status_icon = ":fuc-boi-sooj:"
    error_code = "jobFailed"
    execution_summary = "No Connection found with ARN: arn:aws:codestar-connections:us-west-2:570351108046:connection/97b1df2a-3fa6-4974-a257-421e44194a79"

    if len(commit_message) > 120:
        commit_message = f"{commit_message[:119]}..."

    commit_id = "9549f198ad2c35df4196b132dd4a434a365424a0"
    commit_id_short = commit_id[:7]
    message = {
        "channel": "webhooks", # Override channel to send messages to
        "username": "CI Helper", # Override display name
        "icon_emoji": ":uh-oh-sooj:",
        "attachments": [
            {
                "fallback": f"{status_icon} *<https://google.com/|AWS CodePipeline | {region} | {account_id} >*", # Hyperlink
                "pretext": f"{status_icon} *<https://google.com/|AWS CodePipeline | {pipeline_name} | {region} | {account_id} >*",
                "color": "#34bb13",
                "fields": [
                    {
                        "title": f"Pipeline STARTED",
                        "value": f"""
                                Commit Message: _{commit_message}_\nCommit: <https://google.com/|*{commit_id_short}*>
                            """
                    },
                    {
                        "title": f"Failure Reason",
                        "value": f"{error_code}\n```\n{execution_summary}\n```"
                    },
                    {
                        "title": "Stage",
                        "value": "DEV-Approval",
                        "short": True
                    },
                    {
                        "title": "Action",
                        "value": "ManualApproval",
                        "short": True
                    }
                ],
                "footer": f"AWS CodePipeline | Execution: *<https://google.com|{execution_id} >*",
                "footer_icon": "https://a.slack-edge.com/production-standard-emoji-assets/13.0/google-medium/1f6a8.png", # You can replace this with the URL of your desired footer icon
                "ts": time.time()
            }
        ]
    }

    response = requests.post(url=webhook_url, data=json.dumps(message))

handler({}, {})
