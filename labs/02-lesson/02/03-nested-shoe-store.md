# Deploy the same shoe store using nested templates

In this lab you will delete the single stack version of Mr. Bluejays shoe store and recreate it using nested stacks.

## Lab Instructions

1. Ensure that you have a production account created within your organization.  If this doesn't exist yet navigate to AWS Organizations and "add account".  Name the account "production" in order to match the examples.  Go ahead and set it up using skills you learned in lesson 1.  You'll need to assume the OrganizationAccountAccessRole to do the work.

Example of `~/.aws/config:

```
[profile productionadmin]
role_session_name=donna.noble
source_profile=donna.noble
role_arn=arn:aws:iam::772285020568:role/OrganizationAccountAccessRole
mfa_serial=arn:aws:iam::258748242541:mfa/donna.noble
```

2.  Open two terminals side by side.  For this you'll need one to be `aws-vault exec unfederatedadministrator` and one to be `aws-vault exec productionadmin`.  You might take the time to run `aws sts get-caller-identity` in order to see that the two are different.  

3. Navigate to `supplemental/02-02/nested-cloudformation` in both shells.  You'll notice a `Makefile`.  Edit that Makefile to include your S3_PROD_BUCKET_NAME from the root account.  

4. In the shell that is running in unfederatedadministrator run `make publish` this will upload all those templates to the s3 bucket.

5. In your shell that is productionadmin pop open a browser using `aws-vault login productionadmin` and navigate to cloudformation in us-west-2.  Apply the `s3-stack.yml` then apply the `iam-role.yml`.  On successful application of these two stacks observe the resources they have created.  They both use the cloudformation exports feature we discussed earlier today.  They also notably separate concerns of who can create IAM Users vs Resources.

6. Edit the `mr-bluejays-parent.yml` stack to set parameters unique to your account. The only parameter you MUST change is the s3 bucket name of where you are hosting your Cloudformation and the ami-id around line 69 should be updated to use YOUR packed AMI from a prior lab.

7.  Again in the productionadmin shell run `make create-stack`.  Go and observe the stack rolling out in your production account.  See how nested stacks roll out.  Try visiting the site.

8. After the site is live.  Make a trivial change.  Maybe to a tag name.  Then run `make update-stack` to observe how this handles changes.  

9. At the end of your day run `make clean` to delete the stack so you don't incurr charges overnight.