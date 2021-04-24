# Sample Queries we ran against Cloudwatch Logs Insights

## Nginx Logs

```
fields @timestamp, @message | sort @timestamp desc | limit 20
```
> Show the last 20 messages for a log stream

```
fields @timestamp, status
| stats count(*) by status
| sort @timestamp desc
| limit 2000
```
> Count all the status codes for the last 2000 messages inside of a sliding window

```
fields @timestamp, remote_addr
| stats count(*) by remote_addr
| sort @timestamp desc
| limit 2000
```
> Show the counts of "top talkers" inside of the sliding window

## Secure Log

```
fields @timestamp, @message, @user 
| filter @message like /TTY=/ 
| parse @message "sudo: * :" as @user 
| stat count(*) group by @user
```
> Show the counts of logins across the fleet by user.  Note: This parses out the username and adds it to the structured data as an attribute.
