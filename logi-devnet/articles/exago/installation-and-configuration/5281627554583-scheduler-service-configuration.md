---
title: "Scheduler Service Configuration"
id: 5281627554583
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration
updated_at: 2023-04-03T17:52:19Z
---

# Scheduler Service Configuration

# Scheduler Service Configuration

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

To configure the **Scheduler Service**, edit the file `<Sched>\eWebReportsScheduler.xml`.

The following settings are available:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Settings that can be `true` or `false` are case sensitive and must use lower case.  
> Be sure to explicitly set the smtp\_server, smtp\_enable\_ssl, smtp\_user\_id, and smtp\_password settings for each Scheduler Service.

`<smtp_server>` — The SMTP server (and optional port number) used by the Scheduler Service to email reports. In *v2021.1.15+*, by default, connections are made on port 587 if not otherwise specified. Examples: `smtp.office365.com`, `smtp.myemailserver.net:465`

`<smtp_enable_ssl>` — Set to `true` to enable SSL.

`<smtp_user_id>` — The user id that is used to login into the SMTP server.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If the user id is set to a null or empty value or *DefaultCredentials*, the value automatically defaults to the user’s current credentials. For anonymous emailing, see [Credential-less SMTP v2018.1+](#Credenti)

`<smtp_password>` — The password that is used to login into the SMTP server. This value is only considered when using the user id as an SSL credential.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If the password is set to a null or empty value, the value automatically defaults to the user’s current credentials.

`<smtp_from>` — The ‘From’ email address used in the report emails.

`<smtp_from_name>` — The ‘From’ name used in the report emails.

`<error_report_to>` — The email address to send error reports to.

`<channel_type>` — `tcp` or `http` — must match the setting of the **Remote Host** in the Admin Console [Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings)

`<port>` — The port number of the .NET remoting object used to communicate with Exago; this should also be entered in the Admin Console [Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings)

`<working_directory>` — The directory where scheduled documents and temporary files are written. The default setting `[INSTALLDIR]working` creates a `working` folder in the Scheduler Service’s installation location.

`<default_job_timeout>`pre-v2019.2.31pre-v2020.1.14pre-v2021.1.2 — The maximum number of seconds any report execution is allowed. If an execution reaches a maximum number of seconds, the job is marked Abended and an email will be sent to the address specified under `<error_report_to>`. Email jobs use default\_job\_timeout exclusively for timing out the connection to the SMTP server.

For *v2019.2.31+*, *v2020.1.14+* and *v2020.1.2+*, this value is ignored. Use `smtp_timeout` to limit SMTP connection time and `max_job_execution_minutes` exclusively.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> `<default_job_timeout>` and `<max_job_execution_minutes>` work in conjunction. They should both be set to the same time period. Note that `<default_job_timeout>` is set in seconds and `<max_job_execution_minutes>` is set in minutes.

`<smtp_timeout>`v2019.2.31+v2020.1.14+v2021.1.2+ — limit connection time to the SMTP server in seconds. The default is *30*.

`<report_path>` — A path to specify where to save reports when ‘Email Scheduled Reports’ is set to `false` in the Admin Console. For more details, see [Saving Scheduled Reports to a Repository](#Saving)

`<sleep_time>` — The time interval (in seconds) used for polling for scheduled reports to execute.

`<simultaneous_job_max>` — The maximum number of report executions that can occur simultaneously. This setting is based on the resources available of the server where the Scheduler Service is installed.

`<logging>` — Logging is on by default. To turn logging off, set to `OFF` (in all-caps). To configure logging, edit the **Logging Settings** in the `eWebReportsScheduler.exe.config` file.

`<flush_time>` — The number of hours that a completed, deleted, aborted or abended (*v2021.1.6+*) job will be saved for viewing in the ![MainLeftPaneScheduleManager.png](https://devnet.logianalytics.com/hc/article_attachments/5432206444439/mainleftpaneschedulemanager.png) **Schedule Manager**. Set to *0* to flush jobs immediately upon completion. Set to *-1* to disable automatic flushing only at the direction of an Exago Support Analyst. Flushing should be done automatically at all other times. The default value is *24* in *v2021.1.9+*.

`<sync_flush_time>` — The number of hours that a completed, deleted, or aborted Remote Execution job will be saved in the Scheduler Service’s job list. Set to *0* to flush jobs immediately upon completion (default). Set to *-1* to disable automatic flushing only at the direction of an Exago Support Analyst. Flushing should be done automatically at all other times.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Synchronous jobs are never displayed in the ![MainLeftPaneScheduleManager.png](https://devnet.logianalytics.com/hc/article_attachments/5432206444439/mainleftpaneschedulemanager.png) **Schedule Manager**, even if this value is *greater than 0*.

`<email_addendum>` — Text that will be added at the end of email body. Use `n` to insert lines.

`<external_interface>` — Overrides the Admin Console’s setting for the External Interface, a deprecated extensibility feature that should not be used for new installations.

`<abend_upon_report_error>` — This controls how the scheduling service should proceed if an error occurs while loading or executing a report. The default `true` will stop the running the schedule and set the status to *Abended*. Set to `false` to continue running the schedule and maintain the status as ‘Ready’.

`<ip_address>` — Binding IP address for the Scheduler Service. Most commonly used when the server has multiple Network Interface Cards (NICs).

`<encrypt_schedule_files>` — Set to `true` to encrypt the files created by the Scheduler Service. All existing schedules are irreversibly encrypted the next time the service is started and the plain-text schedule files are removed.

`<max_temp_file_age>` — The number of minutes between each flush of the temp files created by the scheduling service. The default is 1440 minutes (24 hours).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Setting `<max_temp_file_age>` too low may result in errors as temp files are used during report execution and for interactive HTML capabilities when using remote execution. It is not recommended setting this value any lower than 60 minutes. Execution cache files will not be flushed.

`<email_retry_time>` — In the case an email fails to send, the number of minutes to wait before retrying to send the email. After five failed attempts the schedule will set itself to ‘Aborted’. The default is 10 minutes.

`<max_job_execution_minutes>`v2016.2.12+ — Maximum amount of time (in minutes) to run an execution job before timing out. If the job times out, the schedule will be marked as Aborted.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> pre-v2019.2.31pre-v2020.1.14pre-v2021.1.2
>
> `<default_job_timeout>` and `<max_job_execution_minutes>` work in conjunction. They should both be set to the same time period. Note that `<default_job_timeout>` is set in seconds and `<max_job_execution_minutes>`is set in minutes.
>
> For *v2019.2.31+*, *v2020.1.14+* and *v2020.1.2+*, `<default_job_timeout>` is no longer applicable.

`<secure_channel>`v2016.3+ — Set to `true` to allow receipt of encrypted data from hosts. The setting [Use Secure Scheduler Remoting Channel](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings#Use)must be `true` in the Admin Console/XML configuration file.

`<security_protocol>`v2016.3.4+ — Specify which security protocol(s) the scheduler should use. Possible values: `Ssl3, Tls, Tls11, Tls12, Tls13` (*.NET v4.6+*). Separate multiple values with commas (,).

`<service_name_tag>`— For manual installation of Scheduler Services using Visual Studio [installutil.exe](https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool), this field is appended to the end of the service name. Useful for installing multiple services on the same server. *installutil.exe* must be in the same folder as the scheduler configuration file.

`<webappbaseurl>` — Set to the virtual directory URL where the Exago BI Web Application is installed. In Cross-Origin Resource Sharing (CORS) environments, setting this flag ensures that images are correctly loaded.

`<load_assembly_in_external_domain>`v2018.1+ — Set to *True* to load Assembly Data Sources in an external domain, as opposed to the application domain. When *True*, this feature also should be enabled in the [appSettings.config](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings#appSetti) and the [eWebReportsScheduler.exe.config](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings#eWebRepo) files.

## Example XML File

```
<?xml version="1.0" encoding="utf-8" ?>
<eWebReportScheduler>
  <smtp_server>smtp.office365.com:587</smtp_server>
  <smtp_enable_ssl>true</smtp_enable_ssl>
  <smtp_user_id>[email protected]</smtp_user_id>
  <smtp_password>notmypassword#1234</smtp_password>
  <smtp_from>[email protected]</smtp_from>
  <smtp_from_name>Exago Scheduler</smtp_from_name>
  <error_report_to>[email protected]</error_report_to>
  <channel_type>tcp</channel_type>
  <port>2011</port>
  <working_directory>[INSTALLDIR]working</working_directory>
  <default_job_timeout>3600</default_job_timeout>
  <sleep_time>15</sleep_time>
  <simultaneous_job_max>10</simultaneous_job_max>
  <logging>on</logging>
  <flush_time>-1</flush_time>
  <sync_flush_time>0</sync_flush_time>
  <email_addendum></email_addendum>
  <external_interface></external_interface>
  <report_path>[INSTALLDIR]</report_path>
  <abend_upon_report_error>true</abend_upon_report_error>
  <ip_address></ip_address>
  <security_protocol></security_protocol>
  <encrypt_schedule_files></encrypt_schedule_files>
  <max_temp_file_age>1440</max_temp_file_age>
  <email_retry_time>10</email_retry_time>
  <queue_service></queue_service>
  <load_assembly_in_external_domain>false</load_assembly_in_external_domain>
</eWebReportScheduler>
```

## Starting and Changing Scheduler Services

The Windows Service will have to be manually started for new installations of the Scheduler. Starting the service will create the working directory as set in `<working_directory>` described above.

If any changes are made to the configuration (detailed above) the service must be stopped and restarted for the changes to take effect.

For starting and stopping Scheduler Services on Linux servers, refer to [Scheduler and Monitoring Services](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux#Schedule).

## Credential-less SMTP v2018.1+

The values for `<smtp_user_id>`, `<smtp_password>`, `<smtp_from>`, and `<smtp_from_name>` cannot be removed or left blank. Otherwise, these values will be reset to their default or throw an error when attempting to send an email.

To set up anonymous report emailing:

* Set `<smtp_user_id>` to *NoSmtpCredentials*
* Set `<smtp_password>` to any non-null value

## Saving Scheduled Reports to a Repository

Instead of sending report output as an email, the output file can be saved to a file repository instead. To enable this:

1. Provide a **Report Path** in the Scheduler Service’s configuration file. This is the location where the Scheduler Service will save the report output files. Add the `<report_path>` element if it does not yet exist and set the location of the repository.

   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > for *pre-v2020.1*:
   >
   > This report path is the location of the scheduled report output archive, and should be different than Exago’s **Report Path** configuration setting.
2. In the **Admin Console** set ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Scheduler Settings** > **Email Scheduled Reports** to *False.*

After applying these settings, generic scheduled reports (that is the schedule does not run as a batch) will be saved directly to the specified repository rather than being sent via email.

If the  ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Scheduler Settings** > **Show Schedule Delivery Type Options** setting is *True*, users can select whether to save a scheduled report to the specified repository or to send it via email.

Output files will be saved to the `<report_path>` directory with the file name based on the **Scheduler Service**‘s working file GUID with \_Download appended. For example, `855b5857-38ee-473f-8f2c-f3ce36393ef2_Download.pdf`.

#### Server Events for Handling Scheduled Reports

The [Global Event: OnScheduledReportExecuteSuccess](https://devnet.logianalytics.com/hc/en-us/articles/5281591294615-Global-Event-OnScheduledReportExecuteSuccess), if defined, is called after a scheduler executes a file, but before emailing it or saving it to disk. This event can override the default email or archival operations. For example, the file names could be changed to better reflect their user and content, or files could be uploaded to an FTP server or other location.

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").
