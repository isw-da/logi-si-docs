---
title: "Schedule Task Databases"
id: 4406817630743
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817630743-Schedule-Task-Databases
updated_at: 2022-04-06T06:07:19Z
---

# Schedule Task Databases

# Schedule Task Databases

The Scheduler Service for .NET normally stores its scheduled task data
using an embedded instance of **VistaDB,** a text-based database; for
the Scheduler Service for Java, an embedded instance of
**Apache Derby** is used.

You also have the option of storing the data instead in a networked
**Microsoft SQL Server**, **Oracle**, **MySQL** or, in Logi Info
v12.5+, **PostgreSQL** database. In order to use one of these SQL
database servers, you must first create the Tasks table in a database of
your choice, and then configure the Scheduler's
\_Settings.lgx
file appropriately, as described in[Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406818028311-Using-Logi-Scheduler). Example SQL scripts for creating the Tasks table on each of the
supported database servers are installed with the Scheduler in its
<installFolder>
for your use.
