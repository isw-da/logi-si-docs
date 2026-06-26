---
title: "Scheduled Task Data Storage Options"
id: 4419723263127
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723263127-Scheduled-Task-Data-Storage-Options
updated_at: 2022-07-17T02:23:01Z
---

# Scheduled Task Data Storage Options

# Scheduled Task Data Storage Options

The Scheduler Service for .NET normally stores its scheduled task data using an embedded instance of **VistaDB,** a text-based database; for the Scheduler Service for Java, an embedded instance of **Apache Derby** is used.

The *scope* of the Scheduler database is significant, as it can contain records for scheduled events for *multiple*  Logi applications on the same web server. It's important to keep this in mind when developing applications using the Scheduler, so that the correct application is identified when creating or modifying stored data.

For developers upgrading from early versions of Logi Info, which used the **Windows Task Scheduler** to schedule reports, there is no way to import or migrate schedules established in the Windows Task Scheduler into the Logi Scheduler. However, any legacy scheduled events created with the Windows Task Scheduler will still run in later Logi Info versions.

## Backing Up the Scheduler Database Files

As mentioned earlier, the default Logi Scheduler configuration stores scheduled event information in embedded database files that can be backed up using any standard file copy or backup methods. The relevant files are:

(Windows .NET) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Schedules.vdb3  
(Windows Java)C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Schedules\\*.\*  
(Linux/UNIX) <installFolder>/Schedules/\*.\*

These files can even be backed up from within a Logi Process definition, so the Scheduler can schedule and run its own backup. See the [Scheduler Console](https://devnet.logianalytics.com/hc/en-us/articles/360050242853-Scheduler-Console-Sample-Application) sample application for an example of how this is done.

## Using a Database Server

You have the option of storing Scheduler task data in a networked **Microsoft SQL Server**, **Oracle**, **MySQL** or, in Logi Info v12.5+, **PostgreSQL**database.

If you choose to use Microsoft SQL Server, for the best performance, we recommend that it be **SQL Server 2008** or later, in order to avoid the "8KB page size" issue found in older SQL Server versions. This script *will* also work with earlier SQL Server versions but you may experience performance degradation *if* the data in your fields exceeds 8KB *and* the number of stored Scheduler tasks is large (exceeding 8KB triggers behind-the-scenes row splitting in older
SQL Server versions).

In order to use one of these SQL database servers, you must first create the Tasks table in a database of your choice, and then configure the Scheduler's \_Settings.lgx file to use it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522761884567/usingsched_10_430x283.png)

In your Scheduler installation folder, fourexample SQL scripts shown above have been provided to help you create
the Tasks table, and they include comments about their use. Modify a copy of the appropriate script and run it on your database server to create the table.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Using a *case-sensitive* database? The Scheduler service issues a SQL query that uses *mixed case*: "SELECT
TaskID, ProcessXml, RunAs FROM Tasks WHERE..." so be sure to edit the example script you use to create the table to match this case.

<Setting>   
<RemoteApi Port="56982" PassKey="*myKey*"/>   
<WebRequest Timeout="20"ConcurrencyLimit="5" Stagger="1" LoggingLevel="WARNING"
/>  
 <Connection Type="MySql" ID="MySQL" MySqlServer="YourDatabaseServerName"  
 MySqlDatabase="YourDatabase" MySqlUser="YourUser" MySqlPassword="YourPassword" />  
</Setting>

To complete the configuration, you must edit the Scheduler service's \_Settings.lgx file to include a connection element for the database server you're going to use. The settings file is distributed with example connection elements in its comments section; copy the code for your database server type, paste it into the file as shown above, and configure it.

Stop and restart the Scheduler service to begin sending Scheduled task data to the database.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) If you have concerns about the security of the database credentials stored in the Scheduler's \_Settings.lgx file, you can use the Batch Obfuscation Tool (see [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio)) installed with Logi Studio to obfuscate the file. This is done from
a command prompt (Windows only) with a command like this (assumes default Logi
Info installation location):

C:\Program Files\LogiXML IES Dev>LogiObfuscation "C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\\_Settings.lgx" *yourPassword*/obfuscate

A similar command, using the /deobfuscate argument, can be used to de-obfuscate the file for maintenance.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Logi Analytics has no way to de-obfuscate the file for you if you forget your password.

If you wish to transfer existing data from the default database files into a SQL database, you will find that there are export tools for both VistaDB and Derby, either built-in or available online, that allow you to export data in a variety of formats (CSV, XML, etc.) for subsequent insertion into SQL databases.

## Use Custom Table and Schema in Database

If you do not want to use the default table 'Tasks', you have the option to use a custom table and schema in your database. First you must add two new attributes, Schema and Table, to the Connection element via the settings file: %LogiXML Scheduler ServiceHome%/\_Settings.lgx. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) By default, no Connection element is required. Java installations default to the embedded Derby database. DotNet installations default to the embedded VistaDB database.

If you want to use a networked database, then a Connection element is necessary. Choose one of the elements (Schema or Table) and supply the necessary local information. Place it inside the <Setting></Setting> tag to activate it, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522702080023/custom_table__1041x537.png)

Only the MySql, Oracle, PostgreSQL and SQL Server databases are currently supported for networked Scheduler access.

### Sample MySQL Server Connection:

<Connection Type="MySql" ID="MySQL" MySqlServer="localhost" MySqlDatabase="test" MySqlUser="root" MySqlPassword="1234" MySQLSchema="test" MySQLTable="Tasks 1"/>

<Connection Type="MySql" ID="MySQL" MySqlServer="localhost" MySqlDatabase="test" MySqlUser="root" MySqlPassword="1234" />

### Sample Oracle Connection:

<Connection Type="Oracle" ID="Oracle" OracleServer="qad10.jinfonet.com.cn" OracleDatabase="PDBORCL" OracleUser="LOGIINFO" OraclePassword="TEST1234" />

<Connection Type="Oracle" ID="Oracle" OracleServer="qad10.jinfonet.com.cn" OracleDatabase="PDBORCL" OracleSchema="LOGIINFO" OracleTable="TASKS 3" OracleUser="LOGIINFO" OraclePassword="TEST1234" OracleSequence="TASKS 3\_SEQ" />

### Sample SQL Server Connection:

<Connection Type="SqlServer" ID="SqlServer" SqlServer="qad10.jinfonet.com.cn" SqlServerDatabase="REPDEV22303" SqlServerUser="REPDEV22303" SqlServerPassword="Test1234" />

<Connection Type="SqlServer" ID="SqlServer" SqlServer="qad10.jinfonet.com.cn" SqlServerDatabase="REPDEV22303" SqlServerUser="REPDEV22303" SqlServerPassword="Test1234" Schema="REPDEV22303" Table="Tasks1"/>

<Connection Type="SqlServer" ID="SqlServer" SqlServer="qad10.jinfonet.com.cn" SqlServerDatabase="REPDEV22303" SqlServerUser="REPDEV22303" SqlServerPassword="Test1234" Schema="REPDEV22303" Table="Task s2"/>

### Sample PostgreSQL Connection:

<Connection Type="PostgreSQL" ID="PostgreSQL" PostgreSQLServer="qad13.jinfonet.com.cn" PostgreSQLDatabase="logiinfo" PostgreSQLUser="repdev22303" PostgreSQLPassword="Test1234"/>

<Connection Type="PostgreSQL" ID="PostgreSQL" PostgreSQLServer="qad13.jinfonet.com.cn" PostgreSQLDatabase="logiinfo" Schema="repdev22303" Table="tasks1" PostgreSQLUser="repdev22303" PostgreSQLPassword="Test1234"/>

<Connection Type="PostgreSQL" ID="PostgreSQL" PostgreSQLServer="qad13.jinfonet.com.cn" PostgreSQLDatabase="logiinfo" Schema="repdev22303" Table="task s2" PostgreSQLUser="repdev22303" PostgreSQLPassword="Test1234"/>
