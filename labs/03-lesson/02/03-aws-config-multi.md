# AWS Config Multi Account Auditing

The cousin to AWS Cloudmapper on the Cloud Native side is AWS Config.  In this lab you'll deploy the config aggregator in your root account and deploy a collector in the production account.

All the findings will role up to a centralized console.

## Lab Instructions

1. In the us-west-2 region in the root account ( UnfederatedAdministrator ) deploy the template from `03-02/aws-config-organizations.yml`.  Observe the output.  This will create and output an S3 bucket to store config data.

> Don't forget to update the parameters on deploy to match YOUR org and account.

2. Deploy the `03-02/aws-config-member-account.yml` template using Cloudformation StackSets ( note this is different than what we have been doing ).  Observe the output.  Ensure that you've updated it to match the output of your first template.

3. Browse the rules you might deploy.  Go ahead and deploy one rule in the production account.  Which would be the best way to deploy rules to all your accounts?
* Console
* Cloudformation
* Stacksets

4. Try out some of the aggregator canned queries.