# Athena and VPC Flow Logs

In yesterday's lab we learned to use Athena to query 
CloudTrail logs.  But some events may not show up in AWS CloudTrail.  In this lab we are going to use VPC flow logs to tell another piece of the story.

## Lab Instructions

1. Navigate to AWS Athena in the console of the security tools account in region us-west-2.  `aws-vault login securityorgadmin`

2. In query editor, optionally change the Database dropdown from cloudtrailanalysis to default. This may keep things cleaner to see what is happening. Or just leave cloudtrailanalysis if you wish.

3. Run a query to create your VPC flow logs partitions:
```
CREATE EXTERNAL TABLE IF NOT EXISTS vpc_flow_logs_000000000000 (
version int, account string, interfaceid string, sourceaddress string, destinationaddress string,
sourceport int, destinationport int, protocol int, numpackets int,
numbytes bigint, starttime int, endtime int, action string, logstatus string )
PARTITIONED BY (`date` date)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' LOCATION 's3://organization-flow-logs.us-west-2.125649083455/AWSLogs/772285020568/vpcflowlogs/us-west-2/'
TBLPROPERTIES ("skip.header.line.count"="1")
```
> Be sure to update your bucket name in this with YOUR bucket for VPC flow logs. Also update the account name in the s3 path to the logs.

Note: After the fact to load a specific day you can run:

```
ALTER TABLE vpc_flow_logs_000000000000
ADD PARTITION (date='YYYY-MM-dd')
location 's3://your_log_bucket/prefix/AWSLogs/{account_id}/vpcflowlogs/{region_code}/YYYY/MM/dd';
```

4. Run this query to see some results:
```
select * from vpc_flow_logs_000000000000 limit 10;
```

5.  Run some queries from slide 14 to end of slides in lesson 004 from today.  Ensure that you can generate top talkers.  

6.  Craft your own set of interesting queries that you think might be useful in an incident and share your top query in discord.
