---
title: "Communicating with the Scheduler"
id: 4419723258775
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723258775-Communicating-with-the-Scheduler
updated_at: 2022-07-17T02:05:41Z
---

# Communicating with the Scheduler

# Communicating with the Scheduler

The first step in using the Scheduler with a Logi application is to create a *connection* to the Scheduler service or daemon.

The **Connection.Scheduler** element is used, in a Logi application's \_Settings definition, to create this connection. The ID of this element is then used in other elements to connect them to the service.

The Scheduler has its own communication settings and Connection.Scheduler must be configured to match them in order for a connection to be made.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) For enhanced security, any Logi application that contains Process Tasks that will be called by a Logi Scheduler instance in a *different* Logi application needs to have a properly configured **Connection.Scheduler** element connecting it to the scheduler.

Default values are provided that allow communication "out of the box", but in case you wish to change them, the Connection.Scheduler attributes are:

| Attribute/Setting | Description |
| --- | --- |
| ID | (Required) Specifies a unique value identifying this connection; used by other elements to access the connection. |
| Pass Key | (Required) Specifies the pass key, a password-like string used to secure access to the Scheduler service. Must match the PassKey value set in the Scheduler service's \_Settings.lgx file. Tokens are supported in this attribute. *Default: myKey* |
| Port | Specifies the TCP/IP port used to gain access to the Scheduler service. Must match the Port value set in the Scheduler service's \_Settings.lgx file. Tokens are supported in this attribute. *Default: 56982* The Logi Scheduler supports multiple instances and a comma-delimited list of port values can be entered if multiple instances are being used. The order of the port numbers in the list must correspond with the order of names in the Server Name attribute. |
| Server Name | Specifies the name or IP address (IPv4) of the server computer where the Scheduler service is installed. Tokens are supported in this attribute. *Default: localhost* The Logi Scheduler supports multiple instances and a comma-delimited list of server names or IP addresses can be entered if multiple instances are being used. The order of the names in the list must correspond with the order of port numbers in the Port attribute. |

## The Scheduler's Settings File and Logs

In most cases, communication with the Logi Scheduler will work fine without any further configuration, using default values. However, details of the settings file are presented here in case custom configurations are desired.

The Scheduler's settings are stored in its own settings file. In a Windows environment, using default installation options, this is:  
  
(.NET) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\\_Settings.lgx  
(Java) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\\_Settings.lgx

In a Linux/UNIX environment, the Scheduler folders and files are installed in a folder selected by the developer, and the \_Settings.lgx file can be found there.

<Setting>   
<RemoteApi Port="56982" PassKey="*myKey*"/>   
<WebRequest Timeout="20"ConcurrencyLimit="5" Stagger="1" LoggingLevel="WARNING" />  
 </Setting>

The \_Settings.lgx file's default contents, shown above, contain a **RemoteApi** tag with **Port** and **PassKey** values, which need to match the Connection.Scheduler element attribute values discussed earlier.

In addition, the file can contain these **WebRequest** values, which can be altered manually if necessary:

* **Timeout**  - Specifies the number of minutes allowed for a task to complete before the 
  Scheduler abandons it. Default value: *20 minutes*.
* **ConcurrencyLimit**  - Specifies the maximum number of concurrently running requests/tasks allowed. When the limit is reached,
  additional scheduled tasks must wait for one of the other running tasks to
  complete before it can start. Default value: *5 tasks*.
* **Stagger**  - Specifies the number of seconds to wait before starting the next request/task. Default value:
  *1 second*.
* **LoggingLevel** - Specifies the logging level for events, using these values: *ERROR*, *WARNING*, *INFO*, *DEBUG,* or *NONE*.   
    
  The Scheduler Service for .NET logs operational events to files in (if default installation location was used):   
    
  C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Log  
    
  The Scheduler Service for Java logs events to files in <schedulerInstallFolder>/Log/LogiScheduler.log  
    
  The *INFO* logging level value provides a moderate amount of detail about Scheduler events in the logs, while the *DEBUG* value records every web request made, including creating a task, querying the task list, getting a task, updating a task, deleting a task,
  and
  many details
  about running tasks. This value should *not* be used casually, as it will generate many, many log entries. Default value: *WARNING*.
* **PollingFrequency** - (not shown) Specifies the number of seconds that elapse before the database is polled for a task to run. This should normally not be modified. Default value: *60 seconds*.
* **MaxFieldLength** - (not shown) Specifies the maximum length of the ProcessXML value, which is 4,000 characters by default. You may need to increase this limit if you're scheduling tasks with a very large number of, or very long, request parameters. *Note - If you provide a longer value here, you must also manually alter the associated column in your Scheduler database table to match*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) You may need to stop and restart the Logi Info Scheduler service or daemon after saving changes to this settings file.

The settings file also includes an explanatory comments section. This section includes example tags for configuring connections to database servers. These are used if you want to store your schedule task data in a networked SQL database rather than in the standard, file-based database. Information about configuring these connection can be found in [Scheduled Task Data Storage Options](https://devnet.logianalytics.com/hc/en-us/articles/4419723263127-Scheduled-Task-Data-Storage-Options).

Once you've added and configured a Connection.Scheduler element to your Logi application, you're ready to begin working with the other Scheduler elements.
