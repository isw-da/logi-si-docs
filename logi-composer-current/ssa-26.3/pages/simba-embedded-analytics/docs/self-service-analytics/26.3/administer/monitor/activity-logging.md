> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Activity Logging

The Self-Service Analytics server records user and server-based activities in log files. These files can be used by Self-Service Analytics administrators to troubleshoot issues that may occur with the Self-Service Analytics server (for example, activities related to setting up data sources or creating visuals and dashboards).

Self-Service Analytics logs activities in `zoomdata-activity.log`. By default, logging to this file is enabled. Some activity types are not automatically logged. To determine which activities are logged by default, see the [Activities Log Reference Sheet](#activities-log-reference-sheet).

<Warning>
  Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release. Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Self-Service Analytics's [User Auditing](#user-auditing) feature.
</Warning>

This page covers the following topics:

* [Configure the Activity Log](#configure-the-activity-log)
* [Enable or Disable the Logging of Specific Activities](#enable-or-disable-the-logging-of-specific-activities)
* [Determine Whether an Activity Is Being Logged](#determine-whether-an-activity-is-being-logged)
* [Example of Self-Service Analytics Activity Logging Monitored by Fluentd](#example-of-self-service-analytics-activity-logging-monitored-by)

If you want to use unified logging, see [Set Up Unified Logging Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging). Fluentd unified logging is not enabled by default.

<h2 id="configure-the-activity-log">
  Configure the Activity Log
</h2>

The activity log defaults can be configured through properties set in the `zoomdata.properties` file. See [Configure Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov) for more information about modifying property files.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>log.file.count</td>
      <td>Number of log files to keep</td>
      <td>1</td>
    </tr>

    <tr>
      <td>activity.log.file.size</td>
      <td>Maximum log file size in Mb</td>
      <td>10</td>
    </tr>

    <tr>
      <td>activity.logs.dir</td>

      <td>
        File path to store log files. Verify that this log directory has all the necessary permissions and that the owner of the directory is set to `zoomdata`.

        <br />

        The `/home` directory cannot be used for logging.
      </td>

      <td>
        Linux: /opt/zoomdata/logs/

        <br />

        Windows: \<install-path>/logs/
      </td>
    </tr>
  </tbody>
</table>

<h2 id="enable-or-disable-the-logging-of-specific-activities">
  Enable or Disable the Logging of Specific Activities
</h2>

Enabling or disabling the logging of specific activities is performed via a series of REST API calls or by directly updating the appropriate activity property in the `zoomdata.properties` file. For a list of the activities that can be logged and the file in which they can be logged, see the [Activities Log Reference Sheet](#activities-log-reference-sheet).

To enable or disable logging for a specific activity using the REST API, run the following cURL command:

```bash theme={null}
curl -u supervisor: <password> -XPUT 'http://<host>:<port>/composer/api/system/activity/type/<activityType> ' -H "Content-Type: application/vnd.composer.v3+json" --data '<option>'
```

* `<host>:<port>` - Specify the host IP address and port of the Self-Service Analytics instance.
* `<activityType>` - Specify the name of selected activity (for example, `AUTHENTICATION` or `USER`).
* `<option>` - Specify either `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.

To enable or disable logging for a specific activity by changing the appropriate activity property in the properties file:

1. Locate the `zoomdata.properties` file. For information about accessing Self-Service Analytics configuration (properties) files, see [Configure Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov).

2. Add or edit the appropriate activity property in the file using the following format:

   ```
   activity.<activity-name>=<option>
   ```

   Activity names (`<activity-name>`) are listed in the [Activities Log Reference Sheet](#activities-log-reference-sheet).

   For `<option>`, specify either `true` or `false`. Set the value to `true` to enable the selected activity output or `false` to disable it.

3. Save the properties file.

4. Restart Self-Service Analytics microservices. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h2 id="determine-whether-an-activity-is-being-logged">
  Determine Whether an Activity Is Being Logged
</h2>

To determine whether a specific activity type is being logged in the log file, run the following cURL command:

```bash theme={null}
curl -u supervisor: <password> -XGET 'http://<host>:<port>/composer/api/system/activity/type/<activityType>'
```

* `<host>:<port>` - Specify the address of the instance on which Self-Service Analytics is installed.
* `<activityType>` - Specify the type of selected activity (for example, `AUTHENTICATION` or `USER`). For a list of the activities that can be logged, see the [Activities Log Reference Sheet](#activities-log-reference-sheet).

<h2 id="example-of-self-service-analytics-activity-logging-monitored-by">
  Example of Self-Service Analytics Activity Logging Monitored by Fluentd
</h2>

This example shows how to set up Fluentd to monitor Self-Service Analytics activity log files. It does not show how to connect your Fluentd service to an external data store or how to pipe the log information to the external data store.

Before you use this example, make sure Fluentd is installed. Next, create a log file and grant the `td-agent` service permissions to write to it. Finally, modify the `td-agent.conf` file.

### Linux

Create the file `/opt/zoomdata/logs/zoomdata-activity.log.pos` and run the following command to grant the `td-agent` service permissions to write to it:

```bash theme={null}
chmod 777 /opt/zoomdata/logs/zoomdata-activity.log.pos
```

Finally, modify the `td-agent.conf` file in the `/etc/td-agent` folder using the template below.

### Windows

Create the file `<install-path>/logs/zoomdata-activity.log.pos`. Grant the `td-agent` service permissions to read, write and execute permission to the owner, group and public.

Finally, modify the `td-agent.conf` file in the `/etc/td-agent` folder using the template below. Replace `pattern /zoomdata/service/health` with `<install-path>/service/health`.

### Template

* Substitute Self-Service Analytics fully qualified log file name for `<logfile>` and `<logfilen>` (for example, `opt/zoomdata/logs/zoomdata-activity.log`) for Linux, or `<install-path>/logs/zoomdata-activity.log` for Windows. Self-Service Analytics log files names are provided in [Self-Service Analytics Log Files Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).
* For each log file you select, specify rules in `<rule>` sections for the information you want to extract from the Self-Service Analytics log files.

```xml theme={null}
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

<h2 id="manage-activity-logs">
  Manage Activity Logs
</h2>

The Self-Service Analytics server records user- and server-based activities in log files. These files can be used by administrators to troubleshoot issues that may occur with the Self-Service Analytics server, for example, activities related to setting up data sources or creating visuals and dashboards. When Self-Service Analytics is installed in your network environment, a log file is created.

By default, activity logging is enabled, but some activities are not logged by default. For details, see the [Activities Log Reference Sheet](#activities-log-reference-sheet).

<Warning>
  Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release. Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Self-Service Analytics's [User Auditing](#user-auditing) feature.
</Warning>

You can enable or disable activity logging by calling REST API endpoints. See Activity Logging. A list of the types of activities that are logged can be found in the [Activities Log Reference Sheet](#activities-log-reference-sheet).

For more information about other Self-Service Analytics log files, see [Self-Service Analytics Log Files Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).

<h2 id="user-auditing">
  User Auditing
</h2>

User auditing allows you as a Self-Service Analytics administrator or client application administrator to track your users' access and actions to data considered sensitive. This includes tracking:

* What period of time any user interacted with data from dashboards, visuals, sources, and custom SQL queries.
* How the data was accessed: directly in the Self-Service Analytics user interface, via an API, or as embedded objects in your applications.
* Actions performed with the data.
* For all sensitive data your applications need to track data access for, such as regulated industry information, PII, HIPAA, GDPR, and more.

Write your audit logs to the PostgreSQL database installed with Self-Service Analytics, or an alternative PostgreSQL database of your choice. This enables your administrators to access and manage the data collected to suit your organization's needs.

The following topics cover enabling, configuring, and consuming user auditing and user audit data:

* [Enable and Configure User Auditing](#enable-and-configure-user-auditing)
* [Consuming Audit Data](#consuming-audit-data)
* [User Auditing for Multi Tenancy Environments](#user-auditing-for-multi-tenancy-environments)
* [Enable User Audit Data for Self-Service Analytics User Accounts](#enable-user-audit-data-for-self-service-analytics-user-accounts)
* [Enable User Audit Data for Multi Tenant Accounts](#enable-user-audit-data-for-multi-tenant-accounts)

<h2 id="enable-and-configure-user-auditing">
  Enable and Configure User Auditing
</h2>

Write your audit logs to the PostgreSQL database installed with Self-Service Analytics, or an alternative PostgreSQL database of your choice. Create the database, update the `zoomdata.properties` file, and restart Self-Service Analytics to begin capturing audit events.

<Note>
  If you expect a large number of user audit events, accumulating a significant amount of information over time, consider using a separate PostgreSQL database.
</Note>

### Create a Database

Create the database for user auditing. There are two ways to do so:

<Note>
  PostgreSQL databases are the only supported database type.
</Note>

1. Bootstrap creation. When you install or upgrade Self-Service Analytics using a `bootstrap-zoomdata` script, a user audit data table is created on the local PostrgreSQL instance. The user audit database is named `zoomdata-user-auditing`, and installed at the same location as the Logi metadata for your Self-Service Analytics instance.
2. Manual creation. To use a separate database or PostgreSQL instance from your Self-Service Analytics metadata database, edit the `zoomdata.properties` file to reflect the target parameters to use. Set the default value of `destination.params.password` to the same database password used in your default PostgreSQL database. Self-Service Analytics creates the collections automatically in that database as needed.

### Enable User Auditing

After you have created or linked your database, copy these properties into the `zoomdata.properties` file.

```properties theme={null}
user-auditing.enabled=true user-auditing.destination.name=PostgreSQL user-auditing.destination.type=postgresql user-auditing.destination.schema=public user-auditing.destination.collection=audit_records user-auditing.destination.collection-per-account=false user-auditing.destination.params.user_name=${db.username:zoomdata} user-auditing.destination.params.password=${db.password:} user-auditing.destination.params.jdbc_url=jdbc:postgresql://localhost:5432/zoomdata-user-auditing user-auditing.tenant.attribute=
```

Required and optional properties include:

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>enabled</td>
      <td>false</td>
      <td>Use to enable or disable user auditing. Default is false, to disable user auditing. To enable, set to true. Required.</td>
    </tr>

    <tr>
      <td>destination.name</td>
      <td>PostgreSQL</td>
      <td>The name of the type of database. Only PostgreSQL is supported.</td>
    </tr>

    <tr>
      <td>destination.type</td>
      <td>postgresql</td>
      <td>The database type. Only postgresql is supported.</td>
    </tr>

    <tr>
      <td>destination.schema</td>
      <td>public</td>

      <td />
    </tr>

    <tr>
      <td>destination.collection</td>

      <td />

      <td>
        The name of the collection of the user audit data. Use to separate data by accounts to prevent access to audit data by unauthorized users.

        <br />

        For example, `audit_records<Account ID>`.
      </td>
    </tr>

    <tr>
      <td>destination.collection-per-account</td>
      <td>false</td>

      <td>
        Default is false, to disable

        <br />

        To enable, set to true and include a field for Account ID in destination.collection.
      </td>
    </tr>

    <tr>
      <td>destination.params.user\_name</td>
      <td>zoomdata</td>

      <td>
        The user name sent to the database to write audit data.

        <br />

        Required.
      </td>
    </tr>

    <tr>
      <td>destination.params.password</td>

      <td />

      <td>The password sent to the database to write audit data. Required. Can be the same as your default PostgreSQL database.</td>
    </tr>

    <tr>
      <td>destination.params.jdbc\_url</td>
      <td>jdbc:postgresql://localhost:5432/zoomdata-user-auditing</td>

      <td>
        The path to the audit data database. This can be the same database as the user audit schema as shown, or a separate database or partition, as needed.

        <br />

        Required.
      </td>
    </tr>

    <tr>
      <td>tenant.attribute</td>

      <td />

      <td>Include any new or existing user attribute to support data capture by tenant customer users. Use in addition to account information that is always captured and retained in the database.</td>
    </tr>
  </tbody>
</table>

<h3 id="restart-self-service-analytics">
  Restart Self-Service Analytics
</h3>

Restart Self-Service Analytics to begin capturing audit events.

If you used the bootstrap script to install Self-Service Analytics and audit setup, the audit database table is created when the first event is logged. Test your setup by performing any of the event-triggering actions.

If you have set up your database manually, set up the [Data Writer microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#data-writer-microservice) to support the user audit processes.

<h2 id="enable-user-audit-data-for-self-service-analytics-user-accounts">
  Enable User Audit Data for Self-Service Analytics User Accounts
</h2>

Audit data for Self-Service Analytics users, including administrators, are not visible to other Self-Service Analytics accounts. You define this level of separation in the database in one of three ways:

* [Tables](#tables-for-a-self-service-analytics-account): Configure Self-Service Analytics to collect and write user audit data to different tables, then give users database access only to their own audit data table.
* [Views](#views-by-self-service-analytics-account): Disable user auditing by account, then give users access to their own audit data, using specific views and database access rights.
* [Row level security](#row-level-security-in-the-database): Disable user auditing by account, then configure row level security, limiting access for each user to their own data.

<Warning>
  Database tables that contain user audit data are created automatically when you first trigger an audit event. Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.
</Warning>

<h3 id="tables-for-a-self-service-analytics-account">
  Tables for a Self-Service Analytics Account
</h3>

1. Use separate collections for accounts by defining `user-auditing.destination.collection-per-account=true` in the `zoomdata.properties` file.
2. Generate an audit event for all accounts to trigger audit data table creation.
3. Create user database accounts for each user. Define user access rights for each user to query only their own account's audit data table.
4. Create connections to the audit database using each account.

<h3 id="views-by-self-service-analytics-account">
  Views by Self-Service Analytics Account
</h3>

1. Disable use of separate collections for accounts by defining `user-auditing.destination.collection-per-account=false` in the `zoomdata.properties` file.
2. Generate an audit event for any account to trigger audit data table creation.
3. Create a view for each account that filters the audit data table, using a condition such as `accountID='<Account ID>'`.
4. Create user database accounts for each user. Define user access rights for each user to query only their own account's audit data view.
5. Create connections to the audit database using each account.

<h3 id="row-level-security-in-the-database">
  Row Level Security in the Database
</h3>

1. Enable user auditing by defining `user-auditing.destination.collection-per-account=false` in the `zoomdata.properties` file.
2. Generate an audit event for any account to trigger audit data table creation.
3. Create user database accounts for each user, and configure row level security for the audit data table to limit users to their own data. For example, use a filter such as `accountID='<Account ID>`.
4. Create connections to the audit database using each account.

<h2 id="enable-user-audit-data-for-multi-tenant-accounts">
  Enable User Audit Data for Multi Tenant Accounts
</h2>

Configure user auditing for tenants to restrict access to user audit data to their own user tenant data. Self-Service Analytics system administrators can see aggregated data for all tenants in the Self-Service Analytics account.

You can define this level of separation in the database in one of several ways, depending on tenant connection creation privileges.

<Warning>
  Database tables that contain user audit data are created automatically when you first trigger an audit event. Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.
</Warning>

### Tenants Without Connection Creation Permissions

In environments where tenants do not have permission to create connections, you can set up and use user attribute value, such as `${User.tenant}` define row level filters to limit access to user audit data.

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. As a system administrator, create connection and data sources for the audit data in Self-Service Analytics.
5. Add a row level filter to the data source. Compare the column tenant with the user attribute you created. In this example, `tenant=${User.tenant}`

### Tenants With Connection Creation Permissions

If your tenants do have permission to create connections, there are two ways to restrict user audit data access: by setting up views at the tenant level, or applying row level security. Use the features of your database to control access to the data, once attributes are defined and applied.

#### Views Per Tenant

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. Create a view for each tenant that filters the audit data table, using a condition such as `tenant='<Tenant>'`.
5. Create user database accounts for each tenant. Define access rights for account user to query only their own tenant audit data table.
6. Create connections to the audit database using each user database account.

#### Row Level Security

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. Create a separate database user for each tenant, and configure row level security for each account user to query only their own tenant audit data table, using a condition such as `tenant='<Tenant>'`
5. Create connections to the audit database using each user database account.

<h2 id="user-auditing-for-multi-tenancy-environments">
  User Auditing for Multi Tenancy Environments
</h2>

Self-Service Analytics supports two different levels of separation for user audit data. By default, user audit data is separated between tenant accounts. If needed, you can further separate user audit data within a Self-Service Analytics tenant account by adding and using a custom attribute to separate the data.

Use Self-Service Analytics to write audit data to a single table in your database or multiple tables to suit your organization's needs.

<Warning>
  Database tables that contain user audit data are created automatically when you first trigger an audit event. Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.
</Warning>

<h3 id="separation-between-self-service-analytics-tenant-accounts">
  Separation Between Self-Service Analytics Tenant Accounts
</h3>

Audit data for Self-Service Analytics users, including administrators, are not visible to other tenant accounts. You define this level of separation in the database in one of three ways:

* Tables: Configure Self-Service Analytics to collect and write user audit data to different tables, then give users database access only to their own audit data table.
* Views: Disable user auditing by tenant account, then give users access to their own audit data, using specific views and database access rights.
* Row level security: Disable user auditing by tenant account, then configure row level security, limiting access for each user to their own data.

See [Enable User Audit Data for Self-Service Analytics User Accounts](#enable-user-audit-data-for-self-service-analytics-user-accounts).

### Separation Between Tenants

Configure user auditing for tenants to restrict access to user audit data to their own user tenant data. Self-Service Analytics system administrators can see aggregated data for all tenants in the Self-Service Analytics tenant account.

You can define this level of separation in the database in one of several ways, depending on tenant connection creation privileges.

* If tenant users do not have permission to create new connections, add a user attribute value, then make the data available by applying the appropriate row level filter to that value.

* If tenant users do have permission to create new connections, you must set up database-level access control mechanisms.

  * Views per tenant: Define a tenant attribute, then define what user audit data users can access, using specific views and database access rights.
  * Database level row level security: Define a tenant attribute, then configure row level security for the audit table data, allowing users access to appropriate user audit data through individual user database accounts.

See [Enable User Audit Data for Multi Tenant Accounts](#enable-user-audit-data-for-multi-tenant-accounts).

<h2 id="consuming-audit-data">
  Consuming Audit Data
</h2>

Users with appropriate access can review your audit data in one of three ways:

* Create visuals and a dedicated dashboard using Self-Service Analytics.
* Direct database queries using any third-party tool.
* Add the user auditing database as a source and connection, then export the information using the Self-Service Analytics API.

<h3 id="consume-audit-data-using-self-service-analytics">
  Consume Audit Data Using Self-Service Analytics
</h3>

Use Self-Service Analytics to create a User Auditing dashboard.

1. [Create a connection](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections) to your user auditing database.
2. [Create a source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#define-a-source) from this connection.
3. [Create a dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) for User Auditing with visuals as needed.

<Note>
  If you use a table visualization for user auditing data, add [cross-visual filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov#apply-cross-visual-filtering-to-dashboard-visuals) such as List Filters and Tree Maps for a contextual look at your data.
</Note>

<h3 id="consume-audit-data-using-third-party-tools">
  Consume Audit Data Using Third-Party Tools
</h3>

You can use any third-party tools you prefer to access the information for user auditing. Access to the tool or to the database using that tool should be restricted to appropriate users.

<h2 id="activities-log-reference-sheet">
  Activities Log Reference Sheet
</h2>

This reference sheet lists the types of activities and corresponding fields that are logged in the Self-Service Analytics activity log. By default, activity logging is enabled with a few exceptions (described later in this topic).

### Activity Logging Defaults

The following table lists the activities that are logged by default and those that are not. Activities that are not logged by default must have logging manually enabled. See Activity Logging.

<Warning>
  Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release. Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Self-Service Analytics's [User Auditing](#user-auditing) feature.
</Warning>

<table>
  <thead>
    <tr>
      <th>Activity Log File</th>
      <th scope="col">Activities Logged by Default</th>
      <th scope="col">Activity Not Logged by Default</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`zoomdata-activity.log`</td>
      <td>[account](#account-account-maintenance) <br />[authentication](#authentication-user-authentication) <br />[group](#group-group-maintenance) <br />[SOURCE](#source-data-source-maintenance) <br />[USER](#user-user-account-maintenance) <br />[VIS](#vis-visual-maintenance)</td>
      <td>[raw\_data\_export](#raw-data-export-text-search) <br />[raw\_data\_export\_csv](#raw-data-export-csv-data-export-to-csv) <br />[upload](#upload-flat-file-upload)</td>
    </tr>
  </tbody>
</table>

If logging or specific activity logging is disabled in a previous version, the disabled status is retained after an upgrade.

<h3 id="common-log-fields">
  Common Log Fields
</h3>

For each activity, the following common fields are logged as part of each activity record:

| Field Name | Description |
| - | - |
| user | contains information about the tenant user and the actions performed |
| accountID | contains the user's current tenant ID |
| userGroups | list of the groups to which the user belongs |
| IP | contains IP address from which the event has been performed |

Additional fields are logged as part of each [activity](#activity-log-fields).

<h3 id="activity-log-fields">
  Activity Log Fields
</h3>

The following activity types can be logged by Self-Service Analytics. For each activity, specific fields are logged, in addition to the [common fields](#common-log-fields).

* [account: Account Maintenance](#account-account-maintenance)
* [authentication: User Authentication](#authentication-user-authentication)
* [group: Group Maintenance](#group-group-maintenance)
* [raw\_data\_export: Text Search](#raw-data-export-text-search)
* [raw\_data\_export\_csv: Data Export to CSV](#raw-data-export-csv-data-export-to-csv)
* [source: Data Source Maintenance](#source-data-source-maintenance)
* [upload: Flat File Upload](#upload-flat-file-upload)
* [user: User Account Maintenance](#user-user-account-maintenance)
* [vis: Visual Maintenance](#vis-visual-maintenance)

<h4 id="account-account-maintenance">
  `account`: Account Maintenance
</h4>

This activity is logged when a Self-Service Analytics tenant account is created, updated, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field Name | Description |
| - | - |
| activityType | account |
| status | CREATED / UPDATED / DELETED |
| accountId | Generated tenant account ID |
| name | Name of the tenant account from which the event has been triggered |
| createdBy | User who created this tenant account. |
| createdDate | Tenant account creation date |
| lastModifiedBy | User who modified the tenant account |
| disabled | TRUE / FALSE |

<h4 id="authentication-user-authentication">
  `authentication`: User Authentication
</h4>

This activity is logged while user authentication at login. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>authentication</td>
    </tr>

    <tr>
      <td>status</td>
      <td>SUCCEEDED / FAILED</td>
    </tr>

    <tr>
      <td>authenticationType</td>
      <td>BASE, SAML, LDAP, x.509</td>
    </tr>
  </tbody>
</table>

<h4 id="group-group-maintenance">
  `group`: Group Maintenance
</h4>

This activity is logged when a user group is created, updated, or updated. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>groupId</td>
      <td>Group ID</td>
    </tr>

    <tr>
      <td>label</td>
      <td>Name of the group</td>
    </tr>

    <tr>
      <td>description</td>
      <td>Group description added by the user</td>
    </tr>

    <tr>
      <td>group</td>
      <td>Privileges that have been assigned for the group</td>
    </tr>
  </tbody>
</table>

<h4 id="raw-data-export-text-search">
  `raw_data_export`: Text Search
</h4>

This activity is logged when a text search (applicable only for Elasticsearch, Apache Solr, and Cloudera Search sources) is performed using the `/api/stream/search` endpoint. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>raw\_data\_export</td>
    </tr>

    <tr>
      <td>status</td>
      <td>SUCCEEDED</td>
    </tr>

    <tr>
      <td>exportType</td>
      <td>REST (view details) FILE (export file)</td>
    </tr>

    <tr>
      <td>count</td>
      <td>Number of exported rows</td>
    </tr>

    <tr>
      <td>storageType</td>
      <td>Data source</td>
    </tr>

    <tr>
      <td>query</td>
      <td>Queries sent to the data source</td>
    </tr>

    <tr>
      <td>cid</td>
      <td>Created ID</td>
    </tr>

    <tr>
      <td>actionStartedOn</td>
      <td>Export start time</td>
    </tr>

    <tr>
      <td>duration</td>
      <td>Request processing time</td>
    </tr>
  </tbody>
</table>

<h4 id="raw-data-export-csv-data-export-to-csv">
  `raw_data_export_csv`: Data Export to CSV
</h4>

This activity is logged when a user exports the raw data to a CSV file. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>raw\_data\_export\_csv</td>
    </tr>

    <tr>
      <td>status</td>
      <td>SUCCEEDED</td>
    </tr>

    <tr>
      <td>count</td>
      <td>Number of exported rows</td>
    </tr>

    <tr>
      <td>location</td>
      <td>DB or FILE</td>
    </tr>

    <tr>
      <td>file</td>
      <td>location=FILE - the full path to the file in local file system</td>
    </tr>

    <tr>
      <td>cid</td>
      <td>Created ID</td>
    </tr>

    <tr>
      <td>actionStartedOn</td>
      <td>Export start time</td>
    </tr>

    <tr>
      <td>duration</td>
      <td>Request processing time</td>
    </tr>
  </tbody>
</table>

<h4 id="source-data-source-maintenance">
  `source`: Data Source Maintenance
</h4>

This activity is logged when a source is created, updated, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>source</td>
    </tr>

    <tr>
      <td>status</td>
      <td>SAVED, UPDATED, DELETED</td>
    </tr>

    <tr>
      <td>sourceId</td>
      <td>Generated source ID</td>
    </tr>

    <tr>
      <td>sourceName</td>
      <td>Name of the source</td>
    </tr>

    <tr>
      <td>streamType</td>
      <td>Demo\_record, CSV, API</td>
    </tr>

    <tr>
      <td>storageType</td>
      <td>Data source type</td>
    </tr>

    <tr>
      <td>sourceAsString</td>
      <td>Contains microservice info about the data source</td>
    </tr>

    <tr>
      <td>sourceDescription</td>
      <td>Source description added by the user</td>
    </tr>
  </tbody>
</table>

<h4 id="upload-flat-file-upload">
  `upload`: Flat File Upload
</h4>

This activity is logged when a user uploads the flat file while creating a new data source. Logging for this activity is disabled by default. After you have manually enabled logging for this activity, its log records are captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>upload</td>
    </tr>

    <tr>
      <td>status</td>
      <td>SUCCEEDED</td>
    </tr>

    <tr>
      <td>source</td>
      <td>Data source ID to which the file will be uploaded</td>
    </tr>

    <tr>
      <td>fileName</td>
      <td>Name of the uploaded file</td>
    </tr>

    <tr>
      <td>contentType</td>
      <td>Type of the uploaded file</td>
    </tr>

    <tr>
      <td>filesize</td>
      <td>Size of the uploaded file</td>
    </tr>
  </tbody>
</table>

<h4 id="user-user-account-maintenance">
  `user`: User Account Maintenance
</h4>

This activity is logged when user account is created, updated, assigned to or removed from a group, or deleted. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

| Field | Value |
| - | - |
| activityType | user |
| status | CREATED / UPDATED / DELETED |
| userID | |
| userName | |
| userFullname | |
| email | |
| subjectUserGroups | Groups which a user belongs to |
| userOrigin | NATIVE / SAML / LDAP |
| accounts | Tenant accounts, which a user is assigned to |

<h4 id="vis-visual-maintenance">
  `vis`: Visual Maintenance
</h4>

This activity is logged when a visual is created or updated. Logging for this activity is enabled by default and captured in the `zoomdata-activity.log` file.

The following fields are recorded for this activity:

<table>
  <thead>
    <tr>
      <th scope="col">Field</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr />

    <tr>
      <td>activityType</td>
      <td>vis</td>
    </tr>

    <tr>
      <td>status</td>
      <td>CREATED / UPDATED</td>
    </tr>

    <tr>
      <td>visualizationID</td>

      <td />
    </tr>

    <tr>
      <td>visualizationName</td>

      <td />
    </tr>
  </tbody>
</table>
