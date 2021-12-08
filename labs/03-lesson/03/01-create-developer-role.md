# Creating a Developer Role in the Root Account

In this lab you'll use pre-created templates to push out a locked down developer role.

## Lab Instructions

1. In the root account, deploy the cloudformation template in `supplemental/03-03` called "developer-roles.yml".  
2. Add your user donna.noble to the group it creates.  The group can be found in the outputs.
3. Setup your aws-vault to assume the role you just created.

```bash
[profile developerrole]
role_session_name=donna.noble
source_profile=donna.noble
role_arn=arn:aws:iam::258748242541:role/DeveloperRole
mfa_serial=arn:aws:iam::258748242541:mfa/donna.noble
```

> My setup looks like the above

4. Use aws-vault to login to the console as that role.
5. Attempt to create a new IAM role without adding a permissions boundary.  Can you?
6. Now attempt to create a role attaching the permissions boundary.  Did it work?

Post your feelings about permissions boundaries in Discord.
