---
title: "Scheduler Settings"
id: 5281608723095
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Scheduler Settings

# Scheduler Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Scheduler Settings**.

---

Reports can be emailed or scheduled for recurring automated delivery to an email address. The **Scheduler Settings** are used to configure these services. Before adjusting the settings, ensure that the **Scheduler Service** is installed, running, and set to automatically start. For more information see **[Installing the Scheduler Service](https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service)**.

The Remote Execution service can be used to move processing to a different server or to provide load balancing across multiple servers. For more information see **[Remote Execution](https://devnet.logianalytics.com/hc/en-us/articles/5281588803095-Remote-Execution)**.

## Settings

### Enable Report Scheduling

Enables/Disables scheduling and remote execution functionality in the application.

If *False,* will override **Show Report Scheduling Option**, **Show Email Report Options**, & **Show Schedule Manager** also to *False*.

If *False*, **Enable Remote Report Execution** is ignored.

### Show Report Scheduling Option

Enables/Disables the ![ScheduleAddSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432210118551/scheduleaddsmall.png)**Schedule Report** option when right-clicking on a report in the Report Tree. Set to *False* to disable users from scheduling reports.

### Show Email Report Options

Enables/Disables the ![EmailReportSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432210153367/emailreportsmall.png)**Email Report** option when right-clicking on a report in the Report Tree.

### Show Schedule Reports Manager

Enables/Disables the **Schedule Manager ![MainLeftPaneScheduleManager.png](https://devnet.logianalytics.com/hc/article_attachments/5432206444439/mainleftpaneschedulemanager.png)** icon on the Main Menu.

### Show Schedule No End Date Option

Enables/Disables users ability to create a schedule that never ends. Set to *False* to force users to set an end date limit to the schedule.

### Show Schedule Intraday Recurrence Option

Enables/Disables options in the Recurrence tab of the Schedule Wizard to allow a schedule to repeat throughout the day.

### Scheduler Manager User View Level

Controls what information each user can see in the Schedule Manager. These levels utilize the Parameters companyId and userId. There are three possible values:

* **Current User:** Can only view and delete report jobs that have been created by that user. This setting will hide the Host and Company Id columns of the Schedule Manager.
* **All Users in Current Company:** User can only view and delete report schedules for their company. This setting will hide the Host column of the Schedule Manager.
* **All Users in All Companies:** User can view and delete report schedules for all companies (administrator).

For more information, see **[User Identification](https://devnet.logianalytics.com/hc/en-us/articles/5281619919255-User-Identification)**.

### Email Scheduled Reports

Set to *False* to have the Scheduling Service save reports to a file repository instead of attaching them to emails.

### Enable Batch Reports

Set to *True* to allow users to schedule reports which are filtered separately for each recipient user. Batch reporting requires a table or other data structure containing email addresses for the intended recipients associated with a key used to filter the reports. For more information see [Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281531476375-Scheduling-Reports)

### Show Schedule Delivery Type Options

Enables/disables user option to choose the output type (that is email or save report to repository) with each schedule. When *True*, the default value will reflect whatever is set in the **Email Scheduled Reports** setting.

### Use Secure Scheduler Remoting Channel

Enables/disables encrypting of data Set to true to cause data sent to remote schedulers to be encrypted. Each scheduler config file must also have `<secure_channel>` set to true.

### Schedule Remoting Host

Sets the protocol, server and port to the **Scheduler Service**. Separate multiple remoting hosts with a comma or semicolon. Click the **Test Connection** ![CheckmarkAdmin.png](https://devnet.logianalytics.com/hc/article_attachments/5432158412439/checkmarkadmin.png) icon to test the connection between the Web Application and the Scheduler Services.

The protocol and port must match the **Scheduler Service**‘s `channel_type` and `port`configuration settings, respectively.

#### Examples

```
http://localhost:2001
```

```
http://SchedulerOne:2001,tcp://SchedulerTwo:2001
```

### Enable Remote Report Execution

Set to *True* to enable [Remote Execution](https://devnet.logianalytics.com/hc/en-us/articles/5281588803095-Remote-Execution) of reports by one or more Scheduler Services. **Enable Report Scheduling** must also be *True* and a value must be provided for the **Remote Execution Remoting Host**.

Set to *False* to disable this behavior.

For more information, review the [Remote Execution](https://devnet.logianalytics.com/hc/en-us/articles/5281588803095-Remote-Execution) topic.

### Enable Execution Cache

Enables/disables users to use an execution cache for their reports. An execution cache refreshes report data on a schedule, and report execution calls use the cached data instead of querying the data source each time the report is executed.

This dropdown will only display *False* until all conditions in the Enabling Execution Caching section of the [Execution Caching](https://devnet.logianalytics.com/hc/en-us/articles/5281645120919-Execution-Caching) topic are met. Then, this setting can be changed to *True* to enable the feature.

## User Cache Visibility Level

Controls what visibility permissions users can assign to **[Execution Caches](https://devnet.logianalytics.com/hc/en-us/articles/5281645120919-Execution-Caching)**. Available levels utilize the parameters **companyId and userId**. There are three possible values:

* **User:** Users can only view cached report data for caches that they have created.
* **Company:** Users can permit cached data to be visible to all other users in the user’s company. Users can also select the **User** option.
* **Global:** Users can permit cached data to be visible to all other users for all other companies. Users can also select the **Company** or **User** options.

### Enable Access to Data Sources Remotely

When *True*, all calls, including populating Filter Value dropdowns and retrieving Data Object/Data Object schemas made to the Data Sources are handled by the **Remote Execution Remoting Host**, or the **Schedule Remoting Host** if no **Remote Execution Remoting Host** is defined.

When *False*, the Scheduler Services will only make calls to the Data Sources during report execution. All other calls are handled by the Web Application.

Enabling this feature is helpful when white listing connections to Data Sources, and connections should only originate from the the designated Remote Execution Remoting or Schedule Remoting Hosts as opposed to the Web Application servers; or when the Scheduler Services and the databases are on the same firewall level but the Web Application is not.

### Remote Execution Remoting Host

Specifies the Scheduler Services to use for remote execution. Separate multiple servers with commas or semicolons. Click the **Test Connection** ![CheckmarkAdmin.png](https://devnet.logianalytics.com/hc/article_attachments/5432158412439/checkmarkadmin.png) icon to test the connection between the Web Application and the Scheduler Services.

The protocol and port must match the **Scheduler Service**‘s `channel_type` and `port`configuration settings, respectively.

#### Example

```
http://MyHttpServer1:2001,tcp://MyTcpServer:2001
```

### Custom Queue Service

Specifies the web or assembly queue service for custom scheduler management and load balancing. Click the **Test Connection** ![CheckmarkAdmin.png](https://devnet.logianalytics.com/hc/article_attachments/5432158412439/checkmarkadmin.png) icon to test the connection between the Web Application and the Queue Service. See [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue).

### Delete Schedules upon Report Deletion

When a report is deleted corresponding schedules can be deleted automatically by Exago. Set to *True* to enable this behavior.

### Default Email Subject

Set a default subject that will be displayed in the schedule report wizard. May include parameters.

### Default Email Body

Sets a default body that will be displayed in the schedule report wizard. May include parameters.

### Password Requirement (for pdf and excel documents)

Requires a password for PDF or Excel file export. This parameter can be made up of the following values:

* **A:** requires an upper case letter for each **‘A’**
* **a:** requires a lower case letter for each **‘a’.**
* **n:** requires a numeric character for each **‘n’**
* **4:** password must have at least **4** characters

For example, ‘AAnna6’ would require a password of at least six characters with 2 capitals, 1 lower case and 2 numeric characters.

### Custom Scheduler Recipient Window

Provides URL, height and width for custom Scheduler Recipient window. This is a deprecated extensibility feature and should not be used in new installations.

### Show “Reply To” Field in the Scheduler “Recipients” Tab

Displays the email specified in the userEmail parameter in the Recipients tab when scheduling a report. Any replies to the scheduled report will be sent to this email address instead.
