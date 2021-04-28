# AWS Account Setup - Basic Hygeine

One of the most important parts of setting up a brand new AWS account is ensuring
you do the right things for the root user and basic hygeine for the rest of the account
on day one in the first lesson "account setup" we walked through what you need to do
in order to lock down the root account and get notifications for abuse.

## Lab Instructions

1. Navigate to the account menu at the top right hand corner of the screen.  
Click "My Account" and update the contact information for the account.  Ensure that you populate the "Alternate Contacts" with email addresses.

2. In the same screen under "Configure Security Challenge Questions" configure your
security challenge questions.  The answers to these can be nonsense strings you put in your password manager.  

3. In the left panel navigate to "Billing preferences".  Ensure that "Receiving PDF Invoices By Email" is checked.  Uncheck receive "Free Tier Usage Alerts" unless you really want them.  Lastly ensure that "Receive Billing Alerts" is checked.

4. Now that you have set that up.  We're going to lock down the root user account.  At the top right in the account window navigate to 
"My Security Credentials".  Under "Mult-factor authentication(MFA)" click the "Activate MFA" button and follow the steps to enroll an MFA device.  Depending on your device you may need to install an App like Google Authenticator, Authy, FreeOTP, Duo, or the like.   TOTP in particular is favored over webauthn because you can also back up the "secret key" used to seed the generator.  Once you have enrolled an MFA device.  Log out and log back in.

5. Your root user has MFA and we're just about ready to put it away.  But first, we need to enable viewing billing and configuring billing as other users.  In the same "My Account" screen near the bottom there is a panel called "IAM User and Role Access to Billing Information".  Click "Edit" in the top right of the panel and check the box that says "Activate IAM Access".  Click "Update".

6. Now we're ready to add our first user.  In the course supplemental materials there are two templates in [lesson-1 supplemental](supplemental/01-01) there are two CloudFormation templates.  Go ahead and apply them.  Apply the one beginning with `00-` prior to the one beginning with `01-`.  This will setup your very first user.
Should you choose not to customize the name of the user in the parameter your first user login will be `donna.noble`.  _named after my cat_.  The first user's password will be output in the CloudFormation stack outputs.  

7. Navigate to the IAM dashboard in your account.  Copy the login link and paste it in a doc.  Log out as the root user OR in another Firefox container or Chrome Profile sign in as your first user at that sign in link.  You should not be able to do anything EXCEPT go to IAM/Users/${YOUR USER} and enroll an MFA device.  This
is a guardrail setup by the policy we just applied when the first user was created.  

8. Repeat the steps from step 4 to enroll an MFA device for `donna.noble` or ${YOUR USER}.  Log out and log back in.

9. When you created the `00-` stack you also created a couple of roles.  Navigate to the same account menu at the top right and `Switch Roles`.  The account ID is the same as the account ID from the console login link.  There are two roles you can switch to `UnfederatedAdministrator` and `UnfederatedRead`.  Try setting up each one and switching between them.  Note what the console looks like to go between roles.  You can come up with your own color coding system for Admin vs. Read.

10. Now it's time to setup AWS Vault ( command line access ).  AWS Vault is super handy!  It's readily installed in your course VM ( Kali Linux box ).  Or if you're attending on your own machine **at your own risk** install the CLI following the instructions [here](https://github.com/99designs/aws-vault)

11. Setup an `aws-vault` set of credentials using the command `aws-vault add ${username}`.  This will take you through a wizard to enter your credentials.

Following this you'll need to edit your `.aws/config` file to include a modified version of the following

```
[default]
region=us-west-2
output=json

[profile donna.noble]
mfa_serial=arn:aws:iam::258748242541:mfa/donna.noble

[profile unfederatedadmin]
role_session_name=donna.noble
source_profile=donna.noble
role_arn=arn:aws:iam::258748242541:role/UnfederatedAdministrator
mfa_serial=arn:aws:iam::258748242541:mfa/donna.noble
```

> Note: You'll need to replace the _ARN_ with your respective ARNs and usernames.

12.  Run `aws-vault exec unfederatedadmin` and give it your second factor for the `donna.noble` user.

13.  Run `aws sts get-caller-identity` which is the aws equivalent of `whoami` in Linux.  If this is successful you have done everything correctly!

14.  Finally let's stop entering usernames and passwords in the web console.  Try `aws-vault login unfederatedadmin` and your browser will open inside of the role you've just exec'ed into.  Pretty Cool!

15.  Type `env | grep -i AWS` to observe just how AWS does this.

16.  If you need to rotate your credentials ( they expire after an hour ) type `unset AWS_VAULT` and repeat the process above using `aws-vault exec $PROFILE`.

Congratulations!  You now have an account with basic hygeine.  Credentials protected in an encrypted store.  Using short lived credentials to login to the console and on the CLI.  Doing better than most corps :) 

