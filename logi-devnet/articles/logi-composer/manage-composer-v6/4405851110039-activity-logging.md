---
title: "Activity Logging"
id: 4405851110039
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851110039-Activity-Logging
updated_at: 2021-09-21T01:29:01Z
---

# Activity Logging

# Activity Logging

The Composer server records user and server-based activities in log files. These files can be used by Composer administrators to troubleshoot issues that may occur with the Composer server (for example, activities related to setting up data sources or creating visuals and dashboards).

Composer logs activities in `zoomdata-activity.log`. By default logging to this file is enabled, however some activity types are not automatically logged. To determine which activities are logged by default, see the [*Activities Log Reference Sheet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859433111-Activities-Log-Reference-Sheet).

This page covers the following topics:

* [*Configure the Composer Activity Log*](#Configur2)
* [*Enable or Disable the Logging of Specific Activities*](#Enabling)
* [*Determine Whether an Activity Is Being Logged*](#Determin)
* [*Example of Composer Activity Logging Monitored by Fluentd*](#Example)

If you want to use unified logging, see [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd). Fluentd unified logging is not enabled by default.

## Configure the Composer Activity Log

The Composer activity log defaults can be configured through properties set in the `zoomdata.properties` file. See [*Configure Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer) for more information about modifying property files.

| Property | Description | Default |
| --- | --- | --- |
| zoomdata.activity.log.file.max.index | Number of log files to keep | 1 |
| zoomdata.activity.log.file.size | Maximum log file size in Mb | 10 |
| zoomdata.activity.logs.dir | File path to store log files. Verify that this log directory has all the necessary permissions and that the owner of the directory is set to `zoomdata`.  The `/home` directory cannot be used for logging. | /opt/zoomdata/logs/ |
| zoomdata.activity.logging.file | Enable / disable activity logging to file | true |

## Enable or Disable the Logging of Specific Activities

Enabling or disabling the logging of specific activities is performed via a series of REST API calls or by directly updating the appropriate activity property in the `zoomdata.properties` file. For a list of the activities that can be logged and the file in which they can be logged, see the [*Activities Log Reference Sheet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859433111-Activities-Log-Reference-Sheet).

To enable or disable logging for a specific activity using the REST API, run the following cURL command:

```
curl -u supervisor: <password> -XPUT 'http://<host>:<port>/composer/api/system/activity/type/<activityType> ' -H "Content-Type: application/vnd.composer.v2+json" --data '<option>'
```

* `<host>:<port>` - Specify the host IP address and port of the Composer instance.
* `<activityType>` - Specify the name of selected activity (for example, `AUTHENTICATION` or `USER`).
* `<option>` - Specify either `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.

To enable or disable logging for a specific activity by changing the appropriate activity property in the properties file:

1. Locate the `zoomdata.properties` file. For information about accessing Composer configuration (properties) files, see [*Configure Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer).
2. Add or edit the appropriate activity property in the file using the following format:

   ```
   activity.<activity-name>=<option>
   ```

   Activity names (`<activity-name>`) are listed in the [*Activities Log Reference Sheet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859433111-Activities-Log-Reference-Sheet).

   For `<option>`, specify either
   `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.
3. Save the properties file.
4. Restart Composer microservices. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

## Determine Whether an Activity Is Being Logged

To determine whether a specific activity type is being logged in the log file, run the following cURL command:

```
curl -u supervisor: <password> -XGET 'http://<host>:<port>/composer/api/system/activity/type/<activityType>'
```

* `<host>:<port>` - Specify the address of the instance on which Composer is installed.
* `<activityType>` - Specify the type of selected activity (for example, `AUTHENTICATION` or `USER`). For a list of the activities that can be logged, see the [*Activities Log Reference Sheet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859433111-Activities-Log-Reference-Sheet).

## Example of Composer Activity Logging Monitored by Fluentd

This example shows how to set up Fluentd to monitor Composer activity log files. It does not show how to connect your Fluentd service to an external data store or how to pipe the log information to the external data store.

Before you use this example, make sure Fluentd is installed. Then create file `/opt/zoomdata/logs/zoomdata-activity.log.pos` and run the following command to grant the `td-agent` service permissions to write to it:

```
chmod 777 /opt/zoomdata/logs/zoomdata-activity.log.pos
```

Then modify the `td-agent.conf` file in the `/etc/td-agent` folder using the following template.

* Substitute Composer fully qualified log file name for `<logfile>` and `<logfilen>` (for example, , `opt/zoomdata/logs/zoomdata-activity.log`). Composer log files names are provided in [*Composer Log Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405851142167-Composer-Log-Files).
* For each log file you select, specify rules in `<rule>` sections for the information you want to extract from the Composer log files.

```
<source>  
  @type forward
  @id input1
  port 24224
</source>
<source>
  @type tail
  path <logfile>[,<logfilen>]...
  pos_file zoomdata-activity.log.pos
  tag all.activity
  format json
  refresh_interval 1
</source>
<match all.activity>
  @type rewrite_tag_filter
  <rule>
    key     activityType
    pattern ^ACCOUNT$
    tag     account_logs
  </rule>
  <rule>
    key     activityType
    pattern ^AUTHENTICATION$
    tag     authentication_logs
  </rule>
  <rule>
    key     activityType
    pattern ^SOURCE$
    tag     source_logs
  </rule>
  <rule>
    key     activityType
    pattern ^VIS_DEF$
    tag     vis_def_logs
  </rule>
  <rule>
    key     activityType
    pattern ^RAW_DATA_EXPORT$
    tag     raw_data_export_logs
  </rule>
  <rule>
    key     activityType
    pattern ^RAW_DATA_EXPORT_CSV$
    tag     raw_data_export_csv_logs
  </rule>
  <rule>
    key     activityType
    pattern ^UPLOAD$
    tag     upload_logs
  </rule>
  <rule>
    key     activityType
    pattern ^USER$
    tag     user_logs
  </rule>
  <rule>
    key     activityType
    pattern ^VIS$
    tag     vis_logs
  </rule>
  <rule>
    key     activityType
    pattern ^GROUP$
    tag     group_logs
  </rule>
  <rule>
    key     activityType
    pattern ^SECURITY_KEY$
    tag     security_key_logs
  </rule>
  <rule>
    key     activityType
    pattern ^OAUTH_CLIENT$
    tag     oauth_client_logs
  </rule>
  <rule>
    key     activityType
    pattern ^OAUTH_TOKEN$
    tag     oauth_token_logs
  </rule>
</match>

### Uncomment the section below to shift Zoomdata eventDates (UTC by default) to another timezone
### Adjust the quoted value in `Time.zone_offset("EDT")` below to the desired timezone value
### Additional details: https://docs.ruby-lang.org/en/2.4.0/Time.html#method-c-zone_offset
#<filter *_logs>
#  @type record_transformer
#  enable_ruby true
#  <record>
#     eventDate ${(Time.parse(record["eventDate"]).utc + Time.zone_offset("EDT")).strftime("%Y-%m-%d %H:%M:%S.%L")}
#  </record>
#</filter>

#type topology timeline data as json
<filter topology_performance_logs>
  @type record_transformer
  enable_ruby true
    <record>
      timeline ${record["timeline"].to_json}
    </record>
</filter>

#expand topology timeline json to new keys (attributes)
<filter topology_performance_logs>
  @type parser
  key_name timeline
  reserve_data true
  <parse>
    @type json
  </parse>
</filter>

#derive source information from the request payload
<filter vis_command_logs>
  @type record_transformer
  enable_ruby true
  <record>
    source_id ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["id"] end}
    source_name ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["name"] end}
    source_type ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["subStorageType"] end}
    source_schema ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["schema"] end}
    source_collection ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["collection"] end}
    connection_id ${if record["status"] == "STARTED" then JSON.parse(record["request"])["source"]["storageConfiguration"]["connectionId"] end}
  </record>
</filter>

#exclude health check requests
#<filter request_logs>
#  @type grep
#  <exclude>
#    key uri
#    pattern /zoomdata/service/health
#  </exclude>
#</filter>

#send fluent log entries to stdout
<match fluent.**>
  @type stdout
</match>
```
