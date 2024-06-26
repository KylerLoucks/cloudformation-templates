# Organization CloudTrail Templates

# Usage

1. Deploy the [S3 Audit Logs Template](/security-tools/cloudtrail-organization/organization-trail-audit-logs.yml) template into the designated `Audit` AWS Account

2. Deploy the [Organization CloudTrail template](/security-tools/cloudtrail-organization/organization-trail.yml) into the designated AWS Organization `Management` (Payer) Account

> [!Note]
> All of the child accounts in the organization no longer need CloudTrail enabled.
> If they have CloudTrail enabled, twice as many objects will be written. One to their designated bucket, and a second time to the new Organization Audit Bucket.
> It is advised that you delete these trails and their buckets.


# Audit Logs Template
## Parameters
The list of parameters used:

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
Description: Name of the Organization Management Account's organizational CloudTrail
Default: cloudtrail-organization

> [!Note]
> This param match the value used for the `pCloudTrailName` parameter in the `Organization Trail` template


# Organization Trail Template
### pAuditAccountId:
Type: String
Description: Account ID of the designated Audit account that CloudTrail aggregates logs. (Audit Account needs S3 Bucket template deployed first)

### pCloudTrailName:
Type: String
Description: Name of the Organization CloudTrail
Default: cloudtrail-organization

> [!Note]
> This must match the `pManagementAccountTrailName` parameter used in the `Audit Logs` template



