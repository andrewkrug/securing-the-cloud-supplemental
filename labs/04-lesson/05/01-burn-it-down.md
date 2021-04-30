# Tearing down your accounts

Each account is going to need to be disconnected from the billing org and all the resources removed.  

You could also remove all the resources and then leave the account for future use.
AWS accounts with zero resources don't cost anything.

## Running AWS Nuke in Docker
In a directory with a nuke-config.yml like supplemental/05-01/

```bash
export $(aws-vault exec unfederatedadmin --no-session -- env | grep ^AWS | xargs) 

docker run \
    --rm -it \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
    -v `pwd`:/home/aws-nuke/ \
    quay.io/rebuy/aws-nuke:v2.11.0 \
    -c /home/aws-nuke/nuke-config.yml \
    --profile default
```

## Lab Instructions

1. Detach all of your SCPs.
2. Disable the "OrganizationTrail"
3. If you delegated AccessAnalyzer to the SecurityTools account.  Go remove that delegation.
3. In each account run: https://github.com/rebuy-de/aws-nuke sparing the AWS
OrganizationAccountAccessRole.  Work your way up from the bottom to the org root. You can stop here if you like.  Effectively the environment will just idle.  Prior to running nuke you'll need to update the config and also set an alias for the account. ( This can be a random string )
4. To close up shop on the accounts completely you will need to reset the root user password of each subordinate account using the email you specified when you clicked "add account".
5. Sign into each account as the "root user" and click "leave organization" on the "My Organization" page of the account drop down.  After you have successfully left the organization you can go to "My Account" and click "Close Account".

> Note: That accounts that haven't been active for 7 days can not leave the organization.  Accounts in closure will take 30-days to fully close.