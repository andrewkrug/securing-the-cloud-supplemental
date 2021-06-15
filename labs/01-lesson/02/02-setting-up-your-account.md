# AWS Account Setup - Basic Hygeine

One of the most important parts of setting up a brand new AWS account is ensuring
you do the right things for the root user and follow basic hygeine for the rest of the account.  
On Day One, in the second lesson "Account Setup", we walked through what you need to do
in order to lock down the root account, get notifications for abuse, and setup an IAM User to use going forward.

## Lab Instructions

1. Navigate to the account menu at the top right hand corner of the screen.  
Click "My Account" and update the contact information for the account.  Ensure that you populate the "Alternate Contacts" with email addresses.

    <img src="images/1-a.jpeg" alt="'My Account' link location in dropdown Menu" height="150">
    <img src="images/1-b.jpeg" alt="Location of 'Alternate Contacts' on Account landing page" height="150">
    <img src="images/1-c.jpeg" alt="Example of filling out Alternate Contacts form" height="150">
    <img src="images/1-d.jpeg" alt="Example of a successful Alternate Contact form sav" height="150">

2. In the same screen under "Configure Security Challenge Questions" configure your
security challenge questions.  The answers to these can be nonsense strings you put in your password manager.  

    <img src="images/2-a.jpeg" height="150">
    <img src="images/2-b.jpeg" height="150">
    <img src="images/2-c.jpeg" height="150">

3. In the left panel navigate to "Billing preferences".  Ensure that "Receiving PDF Invoices By Email" is checked.  Uncheck receive "Free Tier Usage Alerts" unless you really want them.  Lastly ensure that "Receive Billing Alerts" is checked.

    <img src="images/3-a.jpeg" height="150">
    <img src="images/3-b.jpeg" height="150">

4. Now that you have set that up.  We're going to lock down the root user account.  At the top right in the account window navigate to 
"My Security Credentials".  Under "Mult-factor authentication(MFA)" click the "Activate MFA" button and follow the steps to enroll an MFA device.  Depending on your device you may need to install an App like Google Authenticator, Authy, FreeOTP, Duo, or the like.   TOTP in particular is favored over webauthn because you can also back up the "secret key" used to seed the generator.  Once you have enrolled an MFA device.  Log out and log back in.

    <img src="images/4-a.jpeg" height="150">
    <img src="images/4-b.jpeg" height="150">
    <img src="images/4-c.jpeg" height="150">
    <img src="images/4-d.jpeg" height="150">
    <img src="images/4-e.png" height="150">
    <img src="images/4-f.png" height="150">
    <img src="images/4-g.jpeg" height="150">
    <img src="images/4-h.jpeg" height="150">
    <img src="images/4-i.jpeg" height="150">
    <img src="images/4-j.jpeg" height="150">

5. Your root user has MFA and we're just about ready to put it away.  But first, we need to enable viewing billing and configuring billing as other users.  In the same "My Account" screen near the bottom there is a panel called "IAM User and Role Access to Billing Information".  Click "Edit" in the top right of the panel and check the box that says "Activate IAM Access".  Click "Update".

    <img src="images/5-a.jpeg" height="150">
    <img src="images/5-b.jpeg" height="150">
    <img src="images/5-c.jpeg" height="150">

6. Now we're ready to add our first user.  There are two CloudFormation templates in the course's [lesson-2 supplemental](/supplemental/01-02) materials.  Go ahead and apply them in order (instructions below).  These will setup your very first user and roles.
Should you choose not to customize the name of the user in the parameter your first user login will be `donna.noble`.  _named after my cat_.

    1. Navigate to Services | CloudFormation and then Create Stack. Upload the template file beginning with `00-`

        <img src="images/6-a.jpeg" height="150">
        <img src="images/6-b.jpeg" height="150">
        <img src="images/6-c.jpeg" height="150">

    2. Name your Stack (suggested: unfederated-iam-roles)

        <img src="images/6-d.jpeg" height="150">

    3. Accept the default Stack options, then on the next page ensure you check the Capabilities checkbox before you Create the Stack. The stack may take a few minutes to complete.

        <img src="images/6-e.jpeg" height="150">
        <img src="images/6-f.jpeg" height="150">
        <img src="images/6-g.jpeg" height="150">
        <img src="images/6-h.png" height="150">

    4. Deploy the second template beginning with `01-` in the same way, naming the stack "my-first-user". Copy the `donna.noble` account's password generated in Outputs.

        <img src="images/6-i.jpeg" height="150">
        <img src="images/6-j.jpeg" height="150">
        <img src="images/6-k.jpeg" height="150">
        <img src="images/6-l.jpeg" height="150">
        <img src="images/6-m.jpeg" height="150">
        <img src="images/6-n.jpeg" height="150">

7. Navigate to Services | IAM dashboard.  Copy the sign-in URL and paste it in a local doc for future reference.  Log out as the root user OR use another Firefox container or Chrome Profile to sign in as your first user at that sign in link.  You should not be able to do anything EXCEPT go to IAM/Users/${YOUR USER} and enroll an MFA device.  This
is a guardrail setup by the policy we just applied when the first user was created.  

    <img src="images/7-a.jpeg" height="150">
    <img src="images/7-b.jpeg" height="150">
    <img src="images/7-c.jpeg" height="150">
    <img src="images/7-d.jpeg" height="150">
    <img src="images/7-e.jpeg" height="150">    

8. Repeat the steps from step 4 to enroll an MFA device for `donna.noble` or ${YOUR USER}.  Log out and log back in.

9. When you created the `00-` stack you also created a couple of roles.  Navigate to the same account menu at the top right and `Switch Roles`.  The account ID is the same as the account ID from the console login link.  There are two roles you can switch to: `UnfederatedAdministrator` and `UnfederatedRead`.  Try setting up each one and switching between them.  Note what the console looks like to go between roles.  You can come up with your own color coding system for Admin vs. Read.

    <img src="images/9-a.jpeg" height="150">
    <img src="images/9-b.jpeg" height="150">
    <img src="images/9-c.jpeg" height="150">
    <img src="images/9-d.jpeg" height="150">
    <img src="images/9-e.jpeg" height="150">

10. Now it's time to setup AWS Vault ( command line access ).  AWS Vault is super handy!  It's readily installed in your course VM ( Kali Linux box ).  Or if you're attending on your own machine **at your own risk** install the CLI following the instructions [here](https://github.com/99designs/aws-vault)

11. First we'll need to generate an Access Key to use with `aws-vault`. Navigate to IAM | Users | ${YOUR_USER} | Security Credentials, then click "Create access key". Download the .csv or otherwise save the credentials.

    <img src="images/11-a.jpeg" height="150">
    <img src="images/11-b.jpeg" height="150">
    <img src="images/11-c.jpeg" height="150">
    <img src="images/11-d.jpeg" height="150">
    <img src="images/11-e.jpeg" height="150">
    <img src="images/11-f.jpeg" height="150">

12. Setup an `aws-vault` set of credentials using the command `aws-vault add ${username}`.  This will take you through a wizard to enter the Access Key credentials you just generated and set a password to protect the local vault it saves them in.

    <img src="images/12-a.jpeg" height="150">
    <img src="images/12-b.png" height="150">
    <img src="images/12-c.png" height="150">

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

    > Note: You'll need to replace the _ARN_ with your generated ARN and ${YOUR_USER}.

    <img src="images/12-d.png" height="150">
    <img src="images/12-e.jpeg" height="150">

13.  Run `aws-vault exec unfederatedadmin` and give it your second factor for the `donna.noble` user.

<img src="images/13-a.jpeg" height="150">

14.  Run `aws sts get-caller-identity` which is the aws equivalent of `whoami` in Linux.  If this is successful you have done everything correctly!

<img src="images/14-a.png" height="150">

15.  Finally let's stop entering usernames and passwords in the web console.  Try `aws-vault login unfederatedadmin` and your browser will open inside of the role you've just exec'ed into.  Pretty Cool!

<img src="images/console-login-animation.gif">

16.  Type `env | grep -i AWS` to observe just how AWS does this.

17.  If you need to rotate your credentials ( they expire after an hour ) type `unset AWS_VAULT` and repeat the process above using `aws-vault exec $PROFILE`.

Congratulations!  You now have an account with basic hygeine.  Account is MFA enabled.  Credentials protected in an encrypted store.  Using short lived credentials to login to the console and on the CLI.  Doing better than most corps :) 

