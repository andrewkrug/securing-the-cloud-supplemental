# Setting Up Multi-Account Cloudtrail

In this lab you're going to enable multi-org CloudTrail.  A _basic_ course would have you enable this in just one account.  We're going to start with "non-easy" mode.  Consolidated logging to a single account.  This account will be a new "security tools" account.

You will also setup athena for the CloudTrail using supplemental materials.

## Lab Instructions

1. Inside the root account enable AWS Organizations.  Via the "create organization" button.  Take note of the organization ID in a text file.  You will need this through the class.

2. Try making some OUs.  Make one for Security and one for Production at a minimum.

3. Click the "Add Account" button and add a security account.  _Note: This is a full AWS Account that is now subordinate to your root account_.  Leave the role name blank and it will auto-create an admin role that you can assume.

4. Use the AWS Organizations UI to move that account into the Security OU.  Take note of the account ID.

5. Once again using the Account menu click "switch roles".  Put in the ID of the new account and in the role name go ahead and type in `OrganizationAccountAccessRole`.

6. There are several Cloudformation templates for this lesson.  They need to be applied in the following order:
* In the organization account or "root" account you set up on day one deploy ( cloudtrail-configuration ) make note of the output for the KMS Key it created.

* In the security tools account: deploy the consolidated logging bucket ( cloudtrail-security-tools-bucket.yml ) note that you'll need to update the parameters to match the KMS Key Id from the parent account.  Make note of the name of the bucket it creates by observing the resources tab.

* Switch back to the unfederatedadministrator role in the root account and update the cloudtrail stack "replace the stack with" ( cloudtrail-configuration-security-tools ).  Note: that you'll need to ensure the parameters match your configuration.  

7. After that visit the CloudTrail UI in the organization account and enable this as an "Organization Trail" to apply the setting to all accounts.

**BONUS** 
9. Apply the athena-configuration-security-tools.yml in the security tools account and run some queries.  The reference sheet for this is [Incident Response](https://docs.google.com/document/d/1h3LtDswLAFypfeWhlppu2qhWa1FbRMdbubrddM3Z1Bs/edit?usp=sharing)
10. Setup the athena auto partitioner available here: [Partitioner](https://github.com/duo-labs/cloudtrail-partitioner)

> File any questions in the class chat.  

If you want to see some "malicious" traffic you can deploy the "key-leak" simulation.  But do note: that this will place some random .jpgs in any S3 buckets it can write to.
