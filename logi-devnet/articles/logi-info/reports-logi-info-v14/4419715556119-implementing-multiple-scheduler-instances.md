---
title: "Implementing Multiple Scheduler Instances"
id: 4419715556119
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715556119-Implementing-Multiple-Scheduler-Instances
updated_at: 2022-07-17T02:23:02Z
---

# Implementing Multiple Scheduler Instances

# Implementing Multiple Scheduler Instances

Support for storing task data in networked databases, discussed in [Scheduled Task Data Storage Options](https://devnet.logianalytics.com/hc/en-us/articles/4419723263127-Scheduled-Task-Data-Storage-Options), allows **multiple instances** of the Scheduler service to run at the same time, on multiple servers, creating a fault-tolerant configuration. If one of the Scheduler instances goes down, the remaining instances will continue to function.

A multi-instance configuration is *not* supported when using the standard embedded VistaDB (.NET) or Derby (Java) file databases.

Assuming you've already set up data storage on networked database server, the first step in using multiple instances is to install the Scheduler service on multiple servers and configure the Scheduler's \_Settings.lgx file as desired. To facilitate this, the Scheduler service can be installed independently
of the full Logi Info product.

For the purpose of this discussion, let's assume you've installed the Scheduler on four separate servers, with these settings file values:

| Server Name or IP Address | Port | Pass Key | MySQLServer |
| --- | --- | --- | --- |
| Production1 | 56982 | myKey | adminData2 |
| Production2 | 56012 | myKey | adminData2 |
| 184.32.43.6 | 56982 | myKey | adminData2 |
| 38.60.200.11 | 56034 | myKey | adminData2 |

Note that each of the Scheduler services has been configured to access the same networked database server where the Scheduler task data is stored.

![](https://devnet.logianalytics.com/hc/article_attachments/7522762080151/usingsched_11.png)

Now, to engage the instances, in the application's \_Settings definition, the Connection.Scheduler element's **Port** and **Server Name** attributes must be given a comma-delimited string of the ports and names/addresses, as shown above. Notice that the first port number in the list correlates to the first server name in the list, the second port to the second server, and so on.

Having multiple Scheduler service instances will *not* result in a task being run more often than its designated frequency.
