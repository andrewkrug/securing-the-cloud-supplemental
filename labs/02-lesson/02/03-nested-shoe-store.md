# Deploy Mr. Bluejays Shoe Store using nested templates

In this lab you will delete the single stack version of Mr. Bluejays shoe store and recreate it using nested stacks.

## Lab Instructions

### Prerequisites

Ensure you have an AWS Account created within the Production organization in your account.  

If an AWS Account in your Production organization does not exist, navigate to AWS Organizations and "add account".  

Name the account "production" in order to match the examples.  

You may want to refer to the instructions in [01-lesson/04/04-cloudtrail-config.md from Lesson 1](https://github.com/andrewkrug/securing-the-cloud-supplemental/blob/main/labs/01-lesson/04/04-cloudtrail-config.md) if you need a refresher on how to complete this. 

## Steps

1. You will need to assume the OrganizationAccountAccessRole to do the work.

Example of `~/.aws/config:

```
[profile productionadmin]
role_session_name=donna.noble
source_profile=donna.noble
role_arn=arn:aws:iam::772285020568:role/OrganizationAccountAccessRole
mfa_serial=arn:aws:iam::258748242541:mfa/donna.noble
```

2.  Open two terminal shells side by side. You will be assuming a unique role in each terminal. 

In Terminal 1: `aws-vault exec unfederatedadministrator` 
In Terminal 2: `aws-vault exec productionadmin`  

You may want to run `aws sts get-caller-identity` in confirm your roles in the two terminals are different.  

3. Navigate to `supplemental/02-02/nested-cloudformation-example` in both shells.  

You will notice a `Makefile`.  Edit that Makefile to include your S3_PROD_BUCKET_NAME from the root account.  

4. In the shell that is running in unfederatedadministrator, run `make publish` - this will upload the templates to the named S3 bucketfrom the `Makefile`

5. In the shell that is running in productionadmin,  open a browser by running `aws-vault login productionadmin` 

Navigate to CloudFormation in us-west-2.  

Apply the `s3-stack.yml` template, then apply the `iam-role.yml` template.

Observe the resources these two stacks have created after successful application of the templates.  Both stacks use the CloudFormation exports feature, and divide the functionalities of who can create IAM Users vs Resources.

6. Edit the `mr-bluejays-parent.yml` stack to set the parameters unique to your account. 

**You MUST change the S3 bucket name of where you are hosting your CloudFormation, and the ami-id near line 69 should be updated to use YOUR packed AMI from a prior lab.**

7.  In the shell that is running in productionadmin,  run `make create-stack`.  

Observe the stack rolling out in your production account.  Note how the nested stacks roll out.  Try visiting the site while the the stack is rolling out. 

8. Wait until the site is live.  Make any small change to the site, perhaps a tag name change. Run `make update-stack` to observe how this handles changes.  

9. When you are finished with this lab, run `make clean` to delete the stack so you don't incur unnecessary charges. 
