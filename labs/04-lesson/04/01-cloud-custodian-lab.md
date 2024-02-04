# Cloud Custodian Lab

In this lab we're going to use CNCF cloud custodian to create a security
automation.  We'll apply a policy that allows custodian to take actions on resources when they don't meet certain criteria.

## Lab Instructions

1. Change directory into the supplemental/04-04 folder.  Using the same trick from yesterday that we used to run CloudMapper go ahead and run
```
export $(aws-vault exec unfederatedadmin --no-session -- env | grep ^AWS | xargs) 

docker run -it \
    -v $(pwd)/output:/home/custodian/output \
    -v $(pwd)/policy.yml:/home/custodian/policy.yml \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
    -e AWS_DEFAULT_REGION=us-west-2 \
        cloudcustodian/c7n run -v -s /home/custodian/output /home/custodian/policy.yml
```

This will run custodian in a docker container. Custodian will do some things, output will be saved into the output/ directory, and then it will exit out.

> If you get a permission denied error, try adding "sudo" in front of the docker command.

2. Get an interactive prompt in your custodian container

```bash
export $(aws-vault exec unfederatedadmin --no-session -- env | grep ^AWS | xargs) 

docker run -it \
    -v $(pwd)/output:/home/custodian/output \
    -v $(pwd)/policy.yml:/home/custodian/policy.yml \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
    -e AWS_DEFAULT_REGION=us-west-2 \
    --entrypoint /bin/bash \
    cloudcustodian/c7n 
```

3. At the docker container prompt, try a dry run (-d) of the sample policy in custodian: `custodian run -d -s output/ policy.yml` or consult the help with `custodian run --help`

> There is a good chance you likely have one or more unused Security Groups as part of the labs that build and teardown Mr. BlueJay's Shoe store infrastructure. So, if you point custodian at your Production account, you might have an entry to clean up an unused Security Group. Check output/security-groups-unused-delete/resources.json for the group-id for that Security Group. After doing a dry run and seeeing a candidate, let custodian actually clean it up for you. Before and after the real run, do `aws ec2 describe-security-groups --group-id sg-0f20d716639fbfe7c` and replace that group-id with any found by custodian. You should see it before custodian cleans it up, and this should return a "does not exist" after custodian has done its work.

4. See if you can craft a policy to detect and avoid the mistake you are trying to prevent.
