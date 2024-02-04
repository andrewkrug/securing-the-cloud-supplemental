# Setting up for the course

You'll need exactly two things in order to attend the class.  

1. The Course Virtual Machine
2. A totally empty NEW AWS Account. (maybe unless you're attending the private version where we host these)  Please don't use
an existing account.  We're probably going to mess it up.

If you are attending the private version of the course with hosted AWS accounts please skip to that section of the document. [Hosted Lab Instructions](#hosted-lab-instructions)

# Lab Downloads

The following link is a ~ 2 GB VM which includes many of the tools you will need during the course:

For the course please use:

[https://s3-us-west-2.amazonaws.com/securing-the-cloud.andrewkrug.com/vm/latest/packer-securing-the-cloud.ova](https://s3-us-west-2.amazonaws.com/securing-the-cloud.andrewkrug.com/vm/latest/packer-securing-the-cloud.ova)

Subsequent courses will pin to specific versions of the OVA as we address errata.

`MD5 for the file (packer-securing-the-cloud.ova) = 3515201cf00064faf273ea2daebd9df1`
`SHASUM for the file ('packer-securing-the-cloud.ova') = 225de14b3e15a650254d9fdd3f42ac1cd25ddd9f`

username: vagrant
password: vagrant

> This is from Hashicorp Vagrant which I use to generate the OVA

This will download “packer-securing-the-cloud.ova”. Simply import it into your VM software of choice. The file was created with vmWare Fusion on Mac OS but I’ve verified that it will successfully load in VMware Workstation Player 15 as well. If vmWare asks you to upgrade the format you can go ahead and skip it.

It would be helpful (but not required) if you made the following changes to your VM environment:
1) Enable copy/paste between host and VM

The VM must have the ability to access the internet as you will be interacting with AWS. At a minimum, DNS and HTTP/HTTPS are needed, and one lab will require outbound SSH.

Your VM software should have support pages on how to complete each of the above steps. 

# Chat During Training & Webcasts

Join the Antisiphon Discord server: [Join Our Server!](https://discord.gg/antisyphon)

All students of the paid class will be given a special role so they can access the private Discord channel. If you don’t have that yet, check your inbox for an email from us about it or reach out to training@wildwesthackinfest.com

For an errata please open a github issue on this repository or make a pull request to fix it for someone else.

Thanks!

# AWS Account Setup

For creating a NEW AWS Account simply follow the instructions here:

[https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account)

You will need a personal credit card or at least a visa gift card with a balance in order to open it.  You should not incur more than $50.00 in charges on that account during the course.  At the end we will shut everything down using an open source tool to scorch the earth of any resources and ultimately close this account.

You may elect to keep the account beyond the course but keep in mind you will be responsible for any charges you incur.

# Hosted Lab Instructions

For select deliveries of Securing the Cloud Foundations we host the infrastructure and accounts that learners will use
it is still highly reccomended that when the course is over you maintain your own lab environment because there are some labs you just can not do without your own sandbox.

To access the Securing the Cloud hosted lab visit:

[Single Signon for Secuing the Cloud]('https://resilientsecuritylabs.awsapps.com/start')

1. Attempt to signin using the e-mail address you registered for the course with.  
