# Challenge

There is no solution provided for this.  But ... given the examples you already have access to do the following:

1. Create a template that creates a group for securityauditors
2. Add your user to the securityaudit group
3. Delegate access to that group to assume a security audit role
4. Create a security audit role in the root account that MUST have MFA in order for users to assume
5. Create a security audit role in the rest of the accounts that does not require MFA but allows any root account user to assume it.
6. Attempt to assume this role on your cli and use it to run cloudmapper.

> If you complete this lab please PR in your template to the classes supplemental material with `yourname-templatename.yml` in order to avoid conflicts.  You'll get credit in future classes for being the author!