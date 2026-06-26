---
title: "Activity Logging"
id: 34933086348813
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933086348813-Activity-Logging
updated_at: 2026-05-26T22:07:42Z
---

# Activity Logging

# Activity Logging

The Composer server records user and server-based activities in log files. These files can be used by Composer administrators to troubleshoot issues that may occur with the Composer server (for example, activities related to setting up data sources or creating visuals and dashboards).

Composer logs activities in `zoomdata-activity.log`. By default, logging to this file is enabled. Some activity types are not automatically logged. To determine which activities are logged by default, see the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

**Important:** 
Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.
Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's [User Auditing](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933076803085-User-Auditing) feature.

This page covers the following topics:

* [Configure the Composer Activity Log](#Configur2)
* [Enable or Disable the Logging of Specific Activities](#Enabling)
* [Determine Whether an Activity Is Being Logged](#Determin)
* [Example of Composer Activity Logging Monitored by Fluentd](#Example)

If you want to use unified logging, see [Set Up Unified Logging Using Fluentd](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933100105229-Set-Up-Unified-Logging-Using-Fluentd). Fluentd unified logging is not enabled by default.

## Configure the Composer Activity Log

The Composer activity log defaults can be configured through properties set in the `zoomdata.properties` file. See [Configure Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer) for more information about modifying property files.

| Property | Description | Default |
| --- | --- | --- |
| log.file.count | Number of log files to keep | 1 |
| activity.log.file.size | Maximum log file size in Mb | 10 |
| activity.logs.dir | File path to store log files. Verify that this log directory has all the necessary permissions and that the owner of the directory is set to `zoomdata`.  The `/home` directory cannot be used for logging. | Linux: /opt/zoomdata/logs/  Windows: <install-path>/logs/ |

## Enable or Disable the Logging of Specific Activities

Enabling or disabling the logging of specific activities is performed via a series of REST API calls or by directly updating the appropriate activity property in the `zoomdata.properties` file. For a list of the activities that can be logged and the file in which they can be logged, see the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

To enable or disable logging for a specific activity using the REST API, run the following cURL command:

curl -u supervisor: <password> -XPUT 'http://<host>:<port>/composer/api/system/activity/type/<activityType> ' -H "Content-Type: application/vnd.composer.v3+json" --data '<option>'

* `<host>:<port>` - Specify the host IP address and port of the Composer instance.
* `<activityType>` - Specify the name of selected activity (for example, `AUTHENTICATION` or `USER`).
* `<option>` - Specify either `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.

To enable or disable logging for a specific activity by changing the appropriate activity property in the properties file:

1. Locate the `zoomdata.properties` file. For information about accessing Composer configuration (properties) files, see [Configure Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer).
2. Add or edit the appropriate activity property in the file using the following format:

   activity.<activity-name>=<option>

   Activity names (`<activity-name>`) are listed in the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

   For `<option>`, specify either
   `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.
3. Save the properties file.
4. Restart Composer microservices. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

## Determine Whether an Activity Is Being Logged

To determine whether a specific activity type is being logged in the log file, run the following cURL commsand:

curl -u supervisor: <password> -XGET 'http://<host>:<port>/composer/api/system/activity/type/<activityType>'

* `<host>:<port>` - Specify the address of the instance on which Composer is installed.
* `<activityType>` - Specify the type of selected activity (for example, `AUTHENTICATION` or `USER`). For a list of the activities that can be logged, see the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

## Example of Composer Activity Logging Monitored by Fluentd

This example shows how to set up Fluentd to monitor Composer activity log files. It does not show how to connect your Fluentd service to an external data store or how to pipe the log information to the external data store.

Before you use this example, make sure Fluentd is installed. Next, create a log file and grant the `td-agent` service permissions to write to it. Finally, modify the `td-agent.conf` file.

### Linux

Create the file `/opt/zoomdata/logs/zoomdata-activity.log.pos` and run the following command to grant the `td-agent` service permissions to write to it:

chmod 777 /opt/zoomdata/logs/zoomdata-activity.log.pos

Finally, modify the `td-agent.conf` file in the `/etc/td-agent` folder using the template below.

### Windows

Create the file `<install-path>/logs/zoomdata-activity.log.pos`. Grant the `td-agent` service permissions to read, write and execute permission to the owner, group and public.

Finally, modify the `td-agent.conf` file in the `/etc/td-agent` folder using the template below. Replace `pattern /zoomdata/service/health` with `<install-path>/service/health`.

### Template

* Substitute Composer fully qualified log file name for `<logfile>` and `<logfilen>` (for example, `opt/zoomdata/logs/zoomdata-activity.log`) for Linux, or `<install-path>/logs/zoomdata-activity.log` for Windows. Composer log files names are provided in [Composer Log Files Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097277069-Composer-Log-Files-Reference).
* For each log file you select, specify rules in `<rule>` sections for the information you want to extract from the Composer log files.

<source>  
 @type forward
@id input1
port 24224
</source>
<source>
@type tail
path `<logfile>`[,`<logfilen>`]...
pos\_file zoomdata-activity.log.pos
tag all.activity
format json
refresh\_interval 1
</source>
<match all.activity>
@type rewrite\_tag\_filter
<rule>
key activityType
pattern ^ACCOUNT$
tag account\_logs
</rule>
<rule>
key activityType
pattern ^AUTHENTICATION$
tag authentication\_logs
</rule>
<rule>
key activityType
pattern ^SOURCE$
tag source\_logs
</rule>
<rule>
key activityType
pattern ^RAW\_DATA\_EXPORT$
tag raw\_data\_export\_logs
</rule>
<rule>
key activityType
pattern ^RAW\_DATA\_EXPORT\_CSV$
tag raw\_data\_export\_csv\_logs
</rule>
<rule>
key activityType
pattern ^UPLOAD$
tag upload\_logs
</rule>
<rule>
key activityType
pattern ^USER$
tag user\_logs
</rule>
<rule>
key activityType
pattern ^VIS$
tag vis\_logs
</rule>
<rule>
key activityType
pattern ^GROUP$
tag group\_logs
</rule>
</match>
### Uncomment the section below to shift Zoomdata eventDates (UTC by default) to another timezone
### Adjust the quoted value in `Time.zone\_offset("EDT")` below to the desired timezone value
### Additional details: https://docs.ruby-lang.org/en/2.4.0/Time.html#method-c-zone\_offset
#<filter \*\_logs>
# @type record\_transformer
# enable\_ruby true
# <record>
# eventDate ${(Time.parse(record["eventDate"]).utc + Time.zone\_offset("EDT")).strftime("%Y-%m-%d %H:%M:%S.%L")}
# </record>
#</filter>
#type topology timeline data as json
<filter topology\_performance\_logs>
@type record\_transformer
enable\_ruby true
<record>
timeline ${record["timeline"].to\_json}
</record>
</filter>
#expand topology timeline json to new keys (attributes)
<filter topology\_performance\_logs>
@type parser
key\_name timeline
reserve\_data true
<parse>
@type json
</parse>
</filter>
#derive source information from the request payload
<filter vis\_command\_logs>
@type record\_transformer
enable\_ruby true
<record>
source\_id ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["id"] end}
source\_name ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["name"] end}
source\_type ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["subStorageType"] end}
source\_schema ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["schema"] end}
source\_collection ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["collection"] end}
connection\_id ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["connectionId"] end}
</record>
</filter>
#exclude health check requests
#<filter request\_logs>
# @type grep
# <exclude>
# key uri
# pattern /zoomdata/service/health
# </exclude>
#</filter>
#send fluent log entries to stdout
<match fluent.\*\*>
@type stdout
</match>
