# Setting Up Multi-Account Cloudtrail

In this lab you're going to enable multi-org CloudTrail.  A _basic_ course would have you enable this in just one account.  We're going to start with "non-easy" mode.  Consolidated logging to a single account.  This account will be a new "security tools" account.

You will also setup athena for the CloudTrail using supplemental materials.

## Lab Instructions

1. Inside the root account enable AWS Organizations.  Via the "create organization" button.  Take note of the organization ID in a text file.  You will need this through the class.

    <img src="images/1-a.jpeg" height="100">
    <img src="images/1-b.jpeg" height="100">
    <img src="images/1-c.jpeg" height="100">
    <img src="images/1-d.jpeg" height="100">

2. Try making some OUs.  Make one for Security and one for Production at a minimum.

    <img src="images/2-a.jpeg" height="100">
    <img src="images/2-b.jpeg" height="100">
    <img src="images/2-c.jpeg" height="100">

3. Click the "Add Account" button and add a security account.  _Note: This is a full AWS Account that is now subordinate to your root account_.  Leave the role name blank and it will auto-create an admin role that you can assume.

    <img src="images/3-a.jpeg" height="100">
    <img src="images/3-b.jpeg" height="100">
    <img src="images/3-c.jpeg" height="100">

4. Use the AWS Organizations UI to move that account into the Security OU.  Take note of the account ID.

    <img src="images/4-a.jpeg" height="100">
    <img src="images/4-b.jpeg" height="100">
    <img src="images/4-c.jpeg" height="100">

5. Log into the AWS Console with the IAM User "donna.noble" (or the account name you chose), and once again using the Account menu click "switch roles".  Put in the ID of the new account and in the role name go ahead and type in `OrganizationAccountAccessRole`.

    <img src="images/5-a.jpeg" height="100">
    <img src="images/5-b.jpeg" height="100">

6. There are several Cloudformation templates for this lesson.  They need to be applied in the following order with the specified accounts:

    <img src="images/6-0-a.jpeg" height="100">
    <img src="images/6-0-b.jpeg" height="100">

    1. `supplemental/01-04/cloudtrail-configuration.yml`
        * Create in the Root Account
        * Take note of the Physical Id for the KMS Key created under the Resources tab (Logical ID: CloudTrailCMK)

            <img src="images/6-1-a.jpeg" height="100">
            <img src="images/6-1-b.jpeg" height="100">
            <img src="images/6-1-c.jpeg" height="100">
            <img src="images/6-1-d.jpeg" height="100">
            <img src="images/6-1-e.jpeg" height="100">
            <img src="images/6-1-f.jpeg" height="100">

    2. `supplemental/01-04/cloudtrail-configuration-security-tools-bucket.yml`
        * Create in the Security Account

            <img src="images/6-2-a.jpeg" height="100">

        * On the Specify stack details step:
            * Update the `KMS Key Id` Parameter to match the KMS Key generated in the previous stack creation
            * Update the `organization id` Parameter to match the Organization Id from Step 1.

                <img src="images/6-2-b.jpeg" height="100">

        * Take note of the Physical ID for the bucket that is created under the Resources tab (Logical ID: ForeignAccountS3Bucket)

            <img src="images/6-2-c.jpeg" height="100">

    3. `supplemental/01-04/cloudtrail-configuration-security-tools.yml`
        * Switch back to the Root Account
        * Using the stack created in step 6.1, "Update" the cloudtrail stack and use "Replace Current Template" to apply the new .yml file.

            <img src="images/6-3-a.jpeg" height="100">
            <img src="images/6-3-b.jpeg" height="100">

        * On the Specify stack details step:
            * Update the `CloudTrailBucket` Parameter
            * Update the `SecurityToolsAccountId` Parameter

                <img src="images/6-3-c.jpeg" height="100">


7. After that visit the CloudTrail UI in the organization account, edit the CloudTrail that was created, and enable the "Enable for all accounts in my organization" option to apply the setting to all accounts.

    <img src="images/7-d.jpeg" height="100">

**BONUS**

9. Apply the athena-configuration-security-tools.yml in the security tools account and run some queries.  The reference sheet for this is [Incident Response](https://github.com/easttimor/aws-incident-response)
10. Setup the athena auto partitioner available here: [Partitioner](https://github.com/duo-labs/cloudtrail-partitioner)

> File any questions in the class chat.  

If you want to see some "malicious" traffic you can deploy the "key-leak" simulation.  But do note: that this will place some random .jpgs in any S3 buckets it can write to.
