# Apply some SCPs

In this lab you will work with the terraform blueprint in `supplemental/04-02`.
It's been pre-stubbed out to show you how SCPs are formed and a couple of methods
for how to attach them.

# Lab Instructions

1. Using the UnfederatedAdministrator role get your "root-id" using 
`aws organizations list-roots | jq '.Roots[0].Id' -r`.  Update the var files
with your org-root respectively.

2. Enable all the aws organizations features including SCPs using the command:
`aws organizations enable-all-features` don't worry if you get an error.

3. Run `make plan` and see what terraform is going to do.

4. Navigate to the SCPs in the organizations console and observe the state prior to application.

5. Run `make apply` and then also observe the result of the application.

6. Add an OU to bind the region restrictions to in `tf.vars` using the OU ID and apply.  Change roles in the console to verify that you can no longer use the regions not in the allow list.

7. Modify the terraform file to create another OU list for specific policy binding.  Optionally add one policy of your choice to the terraform file. 