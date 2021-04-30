# Single Sign On

In this lab we'll setup AWS SSO for the organization and see what that experience is like vs using our unfederated command line approach + MFA for log in.

## Lab Instructions

### To enable AWS SSO

1. Sign in to the AWS Management Console with your AWS Organizations management account credentials.
2. Open the AWS SSO console
3. Choose Enable AWS SSO.

> If you have not yet set up AWS Organizations, you will be prompted to create an organization. Choose Create AWS organization to complete this process.

4. When prompted to choose an identity source choose Manage Identities in AWS SSO.
5. Create a user inside of AWS SSO "donna.noble" and an Administrators group. This user will need to have a valid email address in order to register.
6. Attach the Administrator Access policy to the donna.noble user using a permission set mapping to the administrators group.  
7. Go to your email and verify the email of the user.
8. Add AWS accounts to the users profile.
9. Sign in as the user and enroll an MFA device.
10. Observe your "start URl in the SSO Console" make note of it.
11. Go and setup the aws cli to use sso using `aws configure sso` answer the prompts and log in
12. Perform some actions as the SSO user.  "Create something..."
13. Go and observe the events from your SSO user in Cloudtrail.  How are they different?
14. Finally go and disable your SSO user.  See how long it takes for AWS to revoke the session.  Report back on your success or failure of locking a user out in the Discord chat.
