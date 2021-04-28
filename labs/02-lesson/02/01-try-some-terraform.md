# Try some terraform

Even though we're using CloudFormation for most of the class we should
get at least _some_ exposure to Terraform.  In this lab you will deploy
a simple terraform example script and observe the artifacts.

## Lab Instructions

1. In your virtual machine supplemental materials `02-02` folder there is a terraform example.
In order to use it simply assume the unfederatedAdministrator role within the terraform example directory:
`aws-vault exec unfederatedadmin`

2. Run the following commands:
`terraform init`
`terraform plan`

> Observe the artifacts and output of these two commands.  Terraform is telling you
exactly what it intends to change about the environment.

To create the resources in the example simply run `terraform apply`.


Observe the artifacts created by terraform.  Look inside of your directory.  Any new files on disk?
You may note the presence of a new tfstate file.  Examine this file to see how terraform tracks
changes and could be the source of an accidental credential leak.

> Optional extra work: Deploy "Sad Cloud" in one of your accounts if you choose.  Note: This will 
create more resources than planned for the class and could increase spend.  `terraform destroy` will remove
any resources created by terraform when you are finished.