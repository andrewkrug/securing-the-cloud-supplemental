# Cloud Custodian Lab

In this lab we're going to use captial one cloud custodian to create a security
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

You will custodian fire up and print some things out.

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

3. See if you can craft a policy to detect and avoid the mistake you are trying to prevent.