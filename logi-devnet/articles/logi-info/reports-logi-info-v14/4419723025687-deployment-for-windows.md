---
title: "Deployment for Windows"
id: 4419723025687
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723025687-Deployment-for-Windows
updated_at: 2022-07-17T02:24:05Z
---

# Deployment for Windows

# Deployment for Windows

In a Windows environment, installation of the
**Logi Info Scheduler Service for .NET** is accomplished as part of the
Logi Info product installation. However, it's not selected for
installation by default - you need to select the
**Custom** installation option and indicate that it be installed. You
can run the installation program again at any time and modify the
installation to include the Scheduler if you need to.

![](https://devnet.logianalytics.com/hc/article_attachments/7522822883991/introscheduler_01.png)

As shown above, you must click the icon next to the Scheduler item and
select "This feature will be installed on the local hard drive."
from the drop-down list of options.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) There are separate
schedulers for .NET and Java applications.

By default, the .NET scheduler files will be installed to:
C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service.
In the rest of this topic, the installation folder you specified, the
default or a custom location, will be abbreviated as
<installFolder>.

![](https://devnet.logianalytics.com/hc/article_attachments/7522793597079/introscheduler_02.png)

After installation is complete, you can use your Windows administrative
tools to examine your services. The
**Logi Info Scheduler Service** should appear as shown above, its
status should be "Started", and it should be configured to start
automatically.

Due to the flexible nature of the Scheduler and its interactions with Logi
Info applications, you can install the Scheduler on a
*different server* than the application web server, separate from
Logi Info, if desired.

## With Logi Apps Using Logi Security and AuthNT

If you're planning to use the Scheduler to run secure Logi applications
that use the "AuthNT" authentication source, then you need to
configure the Scheduler service to log on using an account that can be
authenticated *in the domain*. The default installation configuration
uses the Local System account, which is only valid on the local machine.
This configuration is independent of setting the **Run As** name for
Scheduler tasks or the **Scheduler User Name** in the\_Settings
definition.

If the Logi application is using any Active Directory groups to filter
domain users, then the domain account used by the Scheduler must also
belong to those groups. The account doesn't have to be an Administrator on
the server running Scheduler, but it does need these minimum permissions
to accessthe Scheduler database, log errors, etc.:

| Folder or File | Permission |
| --- | --- |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service | Read |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Schedules.vdb3 | Read, Write |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Log | Read, Write, Create |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\RunNowTasks | Read, Write, Create, Delete |

To change the account being used by the Scheduler:

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522812364311/introscheduler_03.png)

In the Services administrative tool, double-click the Logi Info Scheduler
Service to view its properties, as shown above, then select the
**Log On** tab. Check **This account:** and provide valid domain
account information and click OK. Then stop and restart the Scheduler
service.
