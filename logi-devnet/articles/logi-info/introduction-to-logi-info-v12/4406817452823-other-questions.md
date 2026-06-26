---
title: "Other Questions"
id: 4406817452823
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817452823-Other-Questions
updated_at: 2022-04-06T06:06:10Z
---

# Other Questions

# Other Questions

This topic provides answers to other frequently-asked and entry-level technical
support questions:

1. [Is it possible to schedule Logi reports to run and be distributed on
   a regular basis?](#Scheduler)
2. [How can I continue to manage older reports that are scheduled through
   the Windows Task Scheduler?](#OlderReports)
3. [Can I store the schedules that the Logi Scheduler uses in a SQL
   database?](#database)
4. [Can I use more than one instance of the Logi Scheduler, in a
   clustered-server set up?](#instance)
5. [Is there some way to find out at runtime what the file system path is
   to my application on the web server](#AppPhysPath)?
6. [Is there some way to find out at runtime what the URL of my
   application is?](#AppURL)

## 1. Is it possible to schedule Logi reports to run and be distributed on a regular basis?

Yes. Logi products include the Logi
Scheduler, a special Windows service or Java daemon, that manages and
executes scheduled events. For more information, see
[Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406822420503-Logi-Scheduler).

## 2. How can I continue to manage older reports that are scheduled through the Windows Task Scheduler?

Prior to release 9.5, scheduled reports were managed using the Logi Server
Manager as an interface for the Windows Task Scheduler. The Server Manager
no longer includes this ability and reports are scheduled using the Logi
Scheduler, but you can run the Windows Task Scheduler from the Windows
Start Menu and still manage older scheduled tasks.

## 3. Can I store the schedules that the Logi Scheduler uses in a SQL database?

Yes. It's possible to configure the Logi Scheduler to use a MySQL, Oracle,
or MS SQL Server database to store scheduled task data, rather than using
the default embedded database files. This is discussed in detail in
[Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406822420503-Logi-Scheduler).

## 4. Can I use more than one instance of the Logi Scheduler, for example, in a clustered-server set up?

Yes. If you're storing scheduled task data in one of the supported
database servers (see #3 above), you can configure multiple Logi Scheduler
instances on different servers, creating a fault-tolerant arrangement.

## 5. Is there some way to find out at runtime what the file system path is to my application on the web server?

Yes. The @Function.AppPhysicalPath~ token will provide a fully-qualified
path that includes your application folder. You can use this token as part
of a file path to other folders within your application for exports, data,
etc. For more information, see [Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406817899415-Token-Reference).

## 6. Is there some way to find out at runtime what the URL of my application is?

Yes. One approach is to add a Session variable in your application's
Global.asax
or
rdPage.aspx
file, using the following code:
<% Session("webpath") =
Request.ServerVariables("URL") %>
then reference it in your report as
@Session.webpath~, andanother is to add this to a Label formatted as HTML:
<\*script\*> document.write(document.location.href);
<\*/script\*>
(remove the asterisks which were added here to prevent the example from
being interpreted as script in this document).
