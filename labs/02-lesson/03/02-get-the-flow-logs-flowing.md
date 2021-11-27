# Get the Flow Logs Flowing

In this lab you'll apply a Cloudformation stack sthat sends VPC Flow logs to Cloudwatch logs.  Then you'll also create a log sink in S3 in the security tools account and archive flow logs in S3.

## Lab Instructions

1. From your terminal get a web browser open in the `productionadmin` role.  `aws-vault login productionadmin`

2. In the us-west-2 region navigate to the CloudFormation section.  Examine the networking stack for your shoe store app and note the VPC-ID.

3. Start the Create Stack process in CloudFormation.  Upload the template from `supplemental/02-03/vpc-flow-logs-to-cloudwatch`.  Pass in your VPC-ID as a parameter.  

4. Generate some traffic to the site and observe the results in CloudWatch.

5. From your terminal get a web browser open in the `securityorgadmin` role.  `aws-vault login securityorgadmin` apply the template that is called `flow-logs-security-tools.yml` from `vpc-flow-logs-to-s3`.  This sets up a log sink within your security tools account in the form of an s3 bucket.  Be sure to pass in your own ORG ID as a parameter to this stack. Once the stack deployment completes, look at the stack's Resources tab and note the ForeignAccountS3Bucket ID that was created to hold the flow logs.

6. Log out and go back to a browser session in the `productionadmin` role.  `aws-vault login productionadmin`
add an additional stack for the `flow-logs-production-acct.yml`.  Pass in your VPC-ID and the new S3 bucket ID for flow logs as parameters.  You're now shipping flow logs to S3 AND CloudWatch.  

7. Change back to the `security tools` account after a bit and observe the artifacts in the S3 bucket for flow logs that was setup by the flow-logs-security-tools.yml account.
