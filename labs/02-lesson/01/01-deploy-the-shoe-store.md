# Lab 1 - Setting up the Shoe Store

In this lab you will set up Mr. BlueJay's Shoe store.  Remember Mr. BlueJay is a ruthless business person and likely has cut
as many corners as possible to get the store up and running swiftly.  In fact the engineering team may not even be responsible
for much of the configuration.  They likely contracted out to one or more third parties.  You job as the solo security salary is
to deploy the application and have a keen eye for mistakes in the configuration.  

Throughout this lesson we will evolve Mr. BlueJays toward a more secure design.

## Prerequisites

* Create an AWS Account in your AWS Organization - Production
* Setup the ability to assume the OrganizationAccountAccessRole in your `~/.aws/config` _an example is provided below_
* Ensure you can access in the browser and on the command line using aws-vault : `aws-vault exec productionadmin && aws sts get-caller-identity`

Example .aws/config to be used with aws-vault cli:
```bash
    [profile productionadmin]
    role_session_name = donna.noble
    source_profile = donna.noble
    role_arn = arn:aws:iam::125649083455:role/OrganizationAccountAccessRole
    mfa_serial = arn:aws:iam::258748242541:mfa/donna.noble
```

> Don't forget this can only be deployed in the us-west-2 region of AWS.

## Lab Instructions

1. Assume the OrganizationAccountAccessRole within your production account.
2. Select the `us-west-2` region.
3. Deploy the CloudFormation template using a method of your choosing CLI or Console and name it "BlueJays-Production".  Go ahead and take all the defaults.
4. Observe the resources forming in your account as they are forming.  It may take up to 10-minutes for the instance to come online.  In the mean time you can click on any resource formed to see that in the console.
5. In the EC2 console find the load balancer DNS name and ensure you can navigate to the site.  Note: You can also run: `export AWS_DEFAULT_REGION=us-west-2 && aws elbv2 describe-load-balancers | grep -i dns`

## Improve the template

1. Make a copy of the template in a location of your choosing.  Achieve the following goals:
    * Add metadata to the template to indicate where it came from
    * Re-pack AMI so the AMI is maintained by your account
    * Restrict the job that uploads reports to ONLY the verbs that it needs in order to perform ( this will involve modifying the IAM role )
    * Move the instance into three new subnets which do not issue public IPs

    > Note you will need to refer back to lesson 2 slides for references on some of these tasks.

2. Bonus Lab:  The instances are presently zero touch.  But for the purpose of incident response and debugging go ahead and add the Amazon Systems Manager agent to the image and configure the IAM policy so that you can use Systems Manager agent.