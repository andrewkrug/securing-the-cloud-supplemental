# Running CloudMapper Auditing

Cloudmapper is one of my favorite projects for auditing AWS.  Built by Scott Piper it is a super practical implementation of a variety of auditors.  In this lesson we'll run it in at least one account and generate a report.  

## Lab Instructions

1. Inside of your course vm go ahead and pull the cloudmapper source code down onto the box.  If you're using the standard structure you'll need to do the following:

* `mkdir -p ~/workspace`
* `cd ~/workspace`
* `git clone https://github.com/duo-labs/cloudmapper.git`
* `sudo apt-get install docker.io -y`
* `sudo systemctl start docker`

2. Now lets get ready to run some cloudmapper inside of our accounts.

```bash

sudo docker build -t cloudmapper .

```

> This builds a docker container with all the cloudmapper dependencies.  This is super important because Kali comes with python 3.9 and it breaks some depends in cloudmapper.

3. Now let's prepare to run the container.

```bash

export $(aws-vault exec unfederatedadmin --no-session -- env | grep ^AWS | xargs) 

sudo docker run -ti \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
    -v ~/workspace/cloudmapper/:/opt/cloudmapper/ \
    -p 8000:8000 \
    cloudmapper /bin/bash

```

You should then see a prompt like this:

```bash
root@53861704dc5d:/opt/cloudmapper#
```

Run `python cloudmapper.py configure discover-organization-accounts`

Examine the file it writes out "config.json"

4. Now let's go collect some audit data!
```bash
python cloudmapper.py collect --account YOUR_ACCOUNT
```

> Note: Ensure that you've used your root account ID here.  Following this you can definitely exit the container and assume the other two roles and audit those accounts as well. 

5. Observe the JSON files generated in account-data within the cloudmapper folder.  Pretty easy to understand that cloudmapper is doing pattern matching.

6. Generate audit findings!  Run `python cloudmapper.py report --account YOUR_ACCOUNT`

> Observe the result in /web, particularly web/account-data/report.html in a browser.

7. You can now also run `python cloudmapper.py webserver`

Congratulations on running your first audit report.  For extra credit here's a great video from Julien Vehent and Scott Piper discussing CloudMapper.  https://youtu.be/9DOMdW6_sYE
