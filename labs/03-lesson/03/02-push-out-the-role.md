# Creating a Developer Role in the ALL THE ACCOUNTS

In this lab you'll create a developer role in the other accounts using StackSets

## Lab Instructions

1. Remember stacksets from the AWS Config lab? It's tucked away in the burger menu of the CloudFormation console.
2. Create a new stack set and limit it to your production OU. (you can get the OU ID from the organizations page.)  Apply the Cloudformation template from `supplemental/03-03` that's intended for stack sets.  You need only apply this one to the us-west-2 region.
3. Try to assume those roles in your subordinate accounts.  
