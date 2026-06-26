---
title: "Deployment for Java"
id: 4419723024791
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723024791-Deployment-for-Java
updated_at: 2022-07-17T02:07:15Z
---

# Deployment for Java

# Deployment for Java

The **Logi Info Scheduler Service for Java** runs on the Linux/UNIX or
Windows operating systems. It's distributed as part of the Logi Info
product and, regardless of the server type that you plan to run it on in
the end, in order to access its files it must first be installed on a
Windows machine, using the Windows product installer, as shown in [Deployment for Windows](https://devnet.logianalytics.com/hc/en-us/articles/4419723025687-Deployment-for-Windows). Naturally, during the process you select the Scheduler
Service for Java feature option, *not* the service for .NET.

The default installation location is:
C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java.
In the rest of this topic, the installation folder you specified, the
default or a custom location, will be abbreviated as
<installFolder>

## On a Windows Server

By default, the Scheduler Service for Java, installed on a Windows server,
isn't configured to start automatically. Instead, it's started by running:

<installFolder>\bin\Scheduler.bat.

When running the Scheduler Service for Java on Windows 7 or Windows Vista,
the User Account Control (UAC) system can interfere with normal operations
of the Scheduler, as the
<installFolder>\Log, \RunNowTasks
and
\Schedules
folders require Write file access permissions. There are two options to
resolve this: either disable UAC on the server, or use UAC to set the
privileges of these directories to allow Write access. This MSDN article
provides
[more information about UAC](https://docs.microsoft.com/en-us/windows/win32/uxguide/winenv-uac?redirectedfrom=MSDN)
should you need it.

If you wish to start the Scheduler service automatically, and you feel
comfortable directly modifying system-level configurations, use the
Registry editor to add a String value in

HK\_Local\_Machine\Software\Microsoft\Windows\CurrentVersion\Run

Set its Value Name to
LogiSchedulerJava
and its Value Data to
<installFolder>\bin\Scheduler.bat.

## On a Linux/UNIX Server

In order to subsequently install the Scheduler Service for Java on a
Linux/UNIX server, copy *all* of the subfolders and files from the
<installFolder>
on the Windows machine to the desired installation folder on your
Linux/UNIX server. That folder on your Linux/UNIX server now becomes your
<installFolder>
for the rest of this discussion.

The Scheduler is started by running
<installFolder>/bin/Scheduler.sh. Don't use a symbolic link for this, as it may lead to unstable
behavior.

To start the Java scheduler automatically, add a line to
/etc/rc.d/rc.local. The invocation should be similar to

/opt/LogiSchedulerJava/Scheduler.sh &

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The ampersand (&) at the end *is* significant: it
causes the application to load as a background process.

Due to the flexible nature of the Scheduler and its interactions with Logi
Info applications, you can install the Scheduler on a
*different server* than the application web server, separate from
Logi Info, if desired.
