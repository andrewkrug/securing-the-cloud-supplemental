# Setting Up Billing Alarms

As we discussed earlier.  Billing alarms and billing anomaly detection is integral
to the early detection of security incidents.  In fact in many cases billing alarms
are the simplest way to detect a security breach.  ( Cryptocurrency mining comes to mind )

In this lab we are going to use my CDK bootstrap and project to deploy billing alarms to your root account.  Since all subordinate accounts will roll up to this account it is the 
**only** place that you will need to deploy billing monitoring.

## Lab Instructions 

1. Inside of your Kali VM for the course ... first bootstrap the CDK.  You can do so by running the following commands to get the python environment set up and cdk installed. If you have an issue here's how to install [installation-instruction](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).  
   * In the `supplemental/01-03` is a CDK project.  `cd` into that directory.
   * `sudo npm install -g aws-cdk`
   * `sudo apt install python3-venv`
   * `python3 -m venv .`
   * `pip3 install -r requirements.txt`
2. Run `aws-vault exec unfederatedadmin` to login to the admin role for the root account.
3. Run `cdk bootstrap` once to setup the CDK in your root account.
4. Run `cdk deploy --parameters EmailDistributor=YOUREMAIL` to deploy the billing alarm stack.  Be sure to change the email. The parameter is case sensitive.
5. Log in to the AWS Console and see the result in the "Billing" Section.

This seems easy.  But ... lots of heavy lifting has been done here to set up the alarms for you.  Click around a bit and explore the budget options.
