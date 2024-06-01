# s3
# Description
Template creates an S3 bucket to aggregate CloudTrail Organizational Trail logs. Typically deployed into an Audit account as part of an AWS Organization.


## Parameters
The list of parameters for this template:

### pOrganizationId:
Type: String
Description: AWS Organization ID. (e.g. o-abcdefghijk)
> [!Note]
> You can find this ID by navigating to the [AWS Organizations Console](https://us-east-1.console.aws.amazon.com/organization) under `Organization ID`

### pManagementAccountId:
Type: String
Description: AWS Account ID of the Organization Management Account

### pManagementAccountTrailName:
Type: String
Description: Name of the Organization Management Account's CloudTrail organizational trail

### Hipaa
  pHipaaClient:
    Type: String
    Description: Client to follow HIPAA compliance (Affects Bucket Lifecycle retention)
    Default: false
    AllowedValues:
      - true
      - false


## Resources
The list of resources this template creates:

### S3BucketPolicy 
Type: AWS::S3::BucketPolicy  
### S3Bucket 
Type: AWS::S3::Bucket  

## Outputs
The list of outputs this template exposes:

### TemplateVersion 
Description: Template Version 


# Usage

1. Deploy an `Organizational` CloudTrail into the Management (Payer) account of the AWS Organization.
- You can do so by deploying the [cloud303-aws-security-tools.yml](/security-tools/cloud303-aws-security-tools.yml) template.
- After you deploy this template, navigate to the cloudtrail created, click edit, and check the box that says: `Enable for all accounts in my organization`


2. Deploy this Audit S3 Bucket CloudFormation template into the designated AWS organization `Audit` account.

> [!Note]
> All of the child accounts in the organization no longer need CloudTrail enabled.
> If they have CloudTrail enabled, twice as many objects will be written. One to their designated bucket, and a second time to the new Organization Audit Bucket.
> It is advised that you delete these trails and their buckets.