# Nested CloudFormation Example

This nested cloudformation example is designed to be used in your AWS Organization with your CloudFormation bucket that was setup
earlier in the course.

## Using this template

1. Fork this project
2. Update the bucket name in the Makefile
3. Update the AMI ID with an AMI inside your own account ( for security )
4. Publish the templates using `make publish`
5. Deploy a testing environment using `make create-stack`
6. Iterate on it using `make update-stack`

> Caution: update-stack doesn't generate change sets.  So you might take the services down if you're tinkering.