# Create a Shared Bucket for Cloudformation

In this lab you will setup a shared space to host CloudFormation for the rest of your accounts.


## Lab Instructions

1. Run the following command: 
``` bash
aws s3api create-bucket \
--bucket cloudformation.us-west-2.${ACCOUNTID}.YOURDOMAIN \
--region us-west-2
--create-bucket-configuration \
LocationConstraint=us-west-2
```

2. Inside of `supplemental/02-02` there is a `policy.json` file.  Customize this file to match the name of your bucket and customize the `org-id` of your AWS Organization.  The `org-id` is available
by running `aws organizations describe-organization | jq Organization.Id`

3. Apply your bucket policy with the command:
``` bash
aws s3api \
put-bucket-policy \
--bucket $BUCKET_NAME \
--policy file://policy.json
```

4. Enable bucket versioning for integrity:
``` bash

aws s3api put-bucket-versioning \
--bucket $BUCKET_NAME \
--versioning-configuration \
Status=Enabled

```

Congratulations you now have a bucket to host cloudformation nested stacks that can be accessed by any account in your AWS Organization but not by the public.