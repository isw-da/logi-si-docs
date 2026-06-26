---
title: "Installing Logi Scheduler for Java"
id: 4419707644055
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707644055-Installing-Logi-Scheduler-for-Java
updated_at: 2022-07-17T02:07:27Z
---

# Installing Logi Scheduler for Java

# Installing Logi Scheduler for Java

Logi Info includes the Logi Scheduler for Java, which runs on **Windows** or **Linux**. In simple terms, the Scheduler is a proprietary application that runs "in the background" on your server as either a Windows service or as a Linux/UNIX daemon.

Services of this type are generally configured to start up when their host computer is started and therefore run automatically with little user intervention. From a performance perspective, they pose little overhead as they consume very few resources and spend most of their time idling.

When the Scheduler "runs" an event from its database, it does so by calling a specified task in a process definition in a Logi Info application. That task can then run reports, send emails, export data, etc.

When you run the Logi Info installation and elect to install the Logi Scheduler for Java, it places all of its files in:

C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java

To install the scheduler on a production server, you need to copy the contents of this folder to it, in the directory of your choice.

Due to the nature of the Scheduler and its interactions with Logi reports, you can install the Scheduler on a different server than the web server, if desired.

## For Windows

The Scheduler is started by running *<yourDirectory>\*bin\Scheduler.bat.
If you wish to start Logi Scheduler for Java automatically in Windows, then
use the Registry editor to add a String value in

HK\_Local\_Machine\Software\Microsoft\Windows\CurrentVersion\Run

named LogiSchedulerJava and set its data value to
the path to Scheduler.bat, for example:

C:\Program
Files\LogiXML IES Dev\LogiXML Scheduler Service Java\bin\Scheduler.bat

When running Scheduler for Java, the Windows User Account Control (UAC) system can interfere with normal operations. The Log, RunNowTasks, and Schedules directories require Write file access and may be blocked by UAC. Options to resolve this included disabling UAC and using UAC to set the file permissions of these directories to allow Write access.

## For Linux/UNIX

The Scheduler is started by running *<yourDirectory>/*bin/Scheduler.sh.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The use of symbolic links in Linux for this
application should be avoided as they may lead to unstable behavior.
If you wish to start Logi Scheduler for Java automatically in Linux, add a
line to /etc/rc.d/rc.local. The invocation should
be similar to

/opt/rdScheduler/Scheduler.sh
&

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The ampersand (&) at the end is significant: it causes the
application to load as a background process.

Logi Scheduler for Java logs events to the Linux Syslog. Normally these
events do not require monitoring but, if issues do occur, the logs can be
reviewed for diagnostic clues. The Linux Syslog utility does not permit remote
access by default, so to enable this functionality, the /etc/init.d/syslog
file needs to be modified. In it, the line invoking syslogd needs to be modified
to include the -r option.
