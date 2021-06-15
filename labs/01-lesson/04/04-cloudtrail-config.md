# Setting Up Multi-Account Cloudtrail

In this lab you're going to enable multi-org CloudTrail.  A _basic_ course would have you enable this in just one account.  We're going to start with "non-easy" mode.  Consolidated logging to a single account.  This account will be a new "security tools" account.

You will also setup athena for the CloudTrail using supplemental materials.

## Lab Instructions

1. Inside the root account enable AWS Organizations.  Via the "create organization" button.  Take note of the organization ID in a text file.  You will need this through the class.

2. Try making some OUs.  Make one for Security and one for Production at a minimum.

3. Click the "Add Account" button and add a security account.  _Note: This is a full AWS Account that is now subordinate to your root account_.  Leave the role name blank and it will auto-create an admin role that you can assume.

4. Use the AWS Organizations UI to move that account into the Security OU.  Take note of the account ID.

5. Log into the AWS Console with the IAM User "donna.noble" (or the account name you chose), and once again using the Account menu click "switch roles".  Put in the ID of the new account and in the role name go ahead and type in `OrganizationAccountAccessRole`.

6. There are several Cloudformation templates for this lesson.  They need to be applied in the following order with the specified accounts:
    1. `supplemental/01-04/cloudtrail-configuration.yml`
        * Create in the Root Account
        * Take note of the Physical Id for the KMS Key created under the Resources tab (Logical ID: CloudTrailCMK)
    2. `supplemental/01-04/cloudtrail-security-tools-bucket.yml`
        * Create in the Security Account
        * On the Specify stack details step:
            * Update the `KMS Key Id` Parameter to match the KMS Key generated in the previous stack creation
            * Update the `organization id` Parameter to match the Organization Id from Step 1.
        * Take note of the Physical ID for the bucket that is created under the Resources tab (Logical ID: ForeignAccountS3Bucket)
    3. `supplemental/01-04/cloudtrail-security-tools-bucket.yml`
        * Create in the unfederatedadministrator role

* Switch back to the unfederatedadministrator role in the root account and update the cloudtrail stack "Replace current template" ( cloudtrail-configuration-security-tools.yml ).  Note: you'll need to update the `CloudTrailBucket` and `SecurityToolsAccountId` parameters to match your configuration.  

7. After that visit the CloudTrail UI in the organization account, edit the CloudTrail that was created, and enable the "Enable for all accounts in my organization" option to apply the setting to all accounts.

**BONUS** 

9. Apply the athena-configuration-security-tools.yml in the security tools account and run some queries.  The reference sheet for this is [Incident Response](https://github.com/easttimor/aws-incident-response)
10. Setup the athena auto partitioner available here: [Partitioner](https://github.com/duo-labs/cloudtrail-partitioner)

> File any questions in the class chat.  

If you want to see some "malicious" traffic you can deploy the "key-leak" simulation.  But do note: that this will place some random .jpgs in any S3 buckets it can write to.
