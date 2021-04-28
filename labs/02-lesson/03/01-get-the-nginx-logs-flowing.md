# Get System and Nginx Logs Flowing

In this lab we'll start sending systems logs from:
* Messages
* SecureLog
* Nginx as JSON 

to AWS CloudWatch for you to generate metrics on and analyze.

## Lab Instructions

Within `supplemental/02-03/nested-cloudformation-example-nginx` you have been given an update/patch from the operations team to enable CloudWatch logging.  Go ahead and open two shells similar to what you did in a prior lab.  One should be in the context of `unfederatedadministrator` and one should be `productionadmin`.  

1. Edit the necessary components of `mr-bluejays-parent.yml` and the `Makefile` with your environment specific information.  

2. Double check the `iam-role` to ensure that it has logs: permissions.  _It does ... just go observe it_

3. Examine the `ec2-stack.yml`.  Note what kind of changes have been made to the LaunchConfig.  Isn't CloudInit quite a bit cleaner?

4. In the terminal in the `unfederatedadministrator` role.  Go ahead and `make publish` to push the changed templates to the bucket.

5. In the terminal in the `productionadmin` role type `make update-stack`.

6. Wait for the stack to complete.  

7. Find the DNS name of the load balancer and make certain that you can visit the site.  Generate some traffic to the site using a tool of your choice.  `curl, dirbuster, webbrowser, etc`.

8. Navigate to CloudWatch logs and observe the new logs flowing into CloudWatch.  Think about how you might use these for detecting bad behavior.