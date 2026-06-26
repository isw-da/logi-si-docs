---
title: "Application and Performance Logging"
id: 5281670339479
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281670339479-Application-and-Performance-Logging
updated_at: 2022-05-03T22:08:45Z
---

# Application and Performance Logging

# Application and Performance Logging

An administrator can configure how Exago handles logging in order to change or extend functionality.

## Logging Defaults

By default Exago saves a log file `WebReportsLog.txt` to the application’s **Temp** path. The logger maintains a lock on the file for the lifespan of the application. The log file cannot be edited or deleted without restarting the application or releasing the lock.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> As of *v2018.1*, the .NET API logs to the file `<Temp>\WebReportsApiLog.txt`

There are five configurable verbosity levels for the logger. By default, Exago logs at the *Info* level. Set the level by changing the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Other Settings** > **Write Log File** setting.

* *None* — Turns logging off.
* *Error* — Logs application errors.
* *Warn* — Logs application warnings, which may be indicative of problems in the configuration, as well as all **Error** messages.
* *Info* — Logs SQL statements, number of rows returned from each statement, and report execution information, as well as all **Warn** and **Error** messages. Report execution information includes the following:
  + Execution start — Start time, @userId@ and @companyId@ parameter values, full report name and filter summary.
  + Execution end — End time, runtime, @userId@ and @companyId@ parameter values and full report name.
* *Debug* — Logs a variety of debugging information that can be used to time specific parts of the application as well as all **Info**, **Warn**, and **Error** messages.
  > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
  >
  > Setting the log level to **DEBUG** in a production environment can have unintended performance consequences. Only use **DEBUG** level logging in production temporarily and under advisement from the Exago Support, Services or Development teams.

## log4net

The logger can load its configuration from a file and continually watch the file for changes. A config file can be used to lock or unlock the log file, change the log file name and path, as well as customize and extend logging capability.

A custom log configuration file overrides the application’s configuration settings.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Enabling or disabling logging with `log4net` will require restarting the web server.

To use a custom log configuration:

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

1. Create a file named `log4net.config` in the `<WebApp>\Config` directory of the Exago Web Application, or open the `<Sched>\eWebReportsScheduler.exe.config` for the Scheduler Service. The following shows a sample config file:  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > For versions *pre-v2019.2.32*, *pre-v2020.1.15*, or *pre-v2021.1.3*, replace `#%-3property{ThreadId}` with `#%-3thread` in the `conversionPattern` nodes.

   ```
   <log4net>
      <appender name="RollingFile" type="log4net.Appender.RollingFileAppender">
         <file value="WebReportsLog.txt" />
         <layout type="log4net.Layout.PatternLayout">
            <conversionPattern value="%date #%-3property{ThreadId} %-5level [%-8.8property{ReportId}][%-8.8property{SessionId}] - %message%newline" />
         </layout>
         <maxSizeRollBackups value="10" />
         <maximumFileSize value="1MB" />
         <rollingStyle value="Size" />
      </appender>
      <appender name="PerfRollingFile" type="log4net.Appender.RollingFileAppender">
         <file value="WebReportsPerfLog.txt" />
         <layout type="log4net.Layout.PatternLayout">
            <conversionPattern value="%date #%-3property{ThreadId} %-5level %logger [%-8.8property{ReportId}][%-8.8property{SessionId}] - %message%newline" />
         </layout>
         <maxSizeRollBackups value="10" />
         <maximumFileSize value="1MB" />
         <rollingStyle value="Size" />
      </appender>
      <root>
         <level value="DEBUG" />
         <appender-ref ref="RollingFile" />
      </root>
      <!-- Set logging level to DEBUG and use logger define at the ROOT level -->
      <logger name="Exago Logger">
         <level value="DEBUG" />
      </logger>
      <!-- Disable Performance Logging 
       <logger name="Perf Logger">        <level value="OFF" />    </logger>-->
      <!-- Enable Perf Logging in general log file -->
      <logger name="Perf Logger">
         <level value="INFO" />
      </logger>
      <!-- Perf logging in its own file 
       <logger name="Perf Logger" additivity="False">        <level value="INFO" />        <appender-ref ref="PerfRollingFile" />    </logger>-->
   </log4net>
   ```
2. Determine the type of logging needed: either **Application**, **Performance** or both.
3. Edit the `log4net.config` file as follows:

### Anatomy of the `log4net.config` file

For full details about the `log4net.config` file, refer to Apache’s  [official log4net documentation](https://logging.apache.org/log4net). Below are some common changes that can be made that apply to Exago.

#### Appenders

The **`appender`** sections control the log output. There can be separate log files output for both the standard Exago application log and for performance logging. In the example two appenders are defined, one named *RollingFile* and the other *PerfRollingFile* which can be used for application and performance logging, respectively.

##### Change Log File Location

This node determines the location of the log file. This should be a fully qualified file path.

```
<file value="PathToLog.txt" />
```

##### Changing the Logging Pattern

```
<conversionPattern value="%date %-5level [%property{SessionId}] %message%newline" />
```

Configures which information is logged and the format of how it is written.

See **[Apache log4Net SDK Documentation – PatternLayout Class](https://logging.apache.org/log4net/log4net-1.2.13/release/sdk/log4net.Layout.PatternLayout.html)** for details on how to format the `conversionPattern`.

##### Unlock the Log File

```
<lockingModel type="log4net.Appender.FileAppender+ExclusiveLock" />
```

Configures the locking model in use for the log file. To temporarily disable the write lock, you can use: `log4net.Appender.FileAppender+MinimalLock`

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This will result in a performance reduction until it is reset.

#### Loggers

The `root` and `logger` nodes establish *loggers* that receive information from Exago and then send it to the *appenders* that actually write the files.

The *Exago Logger* is used by the main application. The *Perf Logger* records application performance. By default, logs will n be passed to the the **root** logger unless their corresponding **additivity** attribute is *False*.

In the example file, both **Application** logging (via the `<logger name="Exago Logger">` node) and **Performance** logging (via the `<logger name="Perf Logger">` node) are enabled. They will capture the data then will use the `<root>` logger since the **additivity** attribute is not specified. The `<root>` logger uses the *RollingFile*`appender`, so both the Application and Performance log data will be written to the same file.

To write the application and performance logs to different files, comment out the `<logger name="Perf Logger">` node and uncomment the `<logger name="PerfLogger" additivity="False">` node. The log level and destination appender are then further defined:

##### Change Logging Level of a Logger

Specifies the Exago logging level: OFF, ERROR, INFO, or DEBUG.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Setting the log level to **DEBUG** in a production environment can have unintended performance consequences. Only use **DEBUG** level logging in production temporarily and under advisement from the Exago Support, Services or Development teams.

```
<level value="INFO" />
```

##### Change Appender a Logger Uses

Specify the name of an appender in the ref attribute of this node.

```
<appender-ref ref="PerfRollingFile"
```

### Resolving log4net.dll version conflicts

Exago uses a specific version of the log4net.dll file that is shipped with the application. When a .NET embedding application implements a different version of log4net, there can be conflicts. The solution is to add a runtime assembly binding redirect to the web.config file. See [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings).

#### Example

```
<dependentAssembly>
   <assemblyIdentity name="log4net" publicKeyToken="669e0ddf0bb1aa2a" culture="neutral" />
   <bindingRedirect oldVersion="1.2.11.0" newVersion="1.2.15.0" />
</dependentAssembly>
```

See **[Redirecting Assembly Versions (MSDN)](https://docs.microsoft.com/en-us/dotnet/framework/configure-apps/redirect-assembly-versions)** for more information.

## Troubleshooting log4net

log4net does provide the ability to troubleshoot logging. Should you need to troubleshoot, add the following to Exago’s web.config file below `appSettings`:

```
<system.diagnostics> 
	<trace autoflush="true">
		<listeners>
			<add name="textWriterTraceListener" type="System.Diagnostics.TextWriterTraceListener"                 initializeData="C:tmplog4net.txt" /> 
		</listeners> 
	</trace>
</system.diagnostics>
```

In addition to the above, add the following entry to the appSettings collection:

```
<add key=”log4net.Internal.Debug” value=”true”/>
```

Save the file, refresh IIS and give IIS\_IUSRS full permission to the folder where logging logs are set to be stored. In the example above, that would be “C:\tmp”. Then, attempt to execute Exago reports and check the logging log file to see why Exago logging is failing.

## Logging to a SQL Database

The following will describe the necessary steps to store Exago logging information in a database. The sample referenced here is configured for MS SQL Server, [but log4net provides examples for other database types.](https://logging.apache.org/log4net/release/config-examples.html)

1. Create a new database table to store the log transactions

   ```
   CREATE TABLE [dbo].[exagoweb] (
   [id] [int] IDENTITY (1, 1) NOT NULL,
   [timestamp] [datetime] NOT NULL,
   [logger] [varchar] (255) NOT NULL,
   [thread] [varchar] (255) NOT NULL,
   [level] [varchar] (50) NOT NULL,
   [reportId] [varchar] (255) NOT NULL,
   [sessionId] [varchar] (255) NOT NULL,
   [message] [varchar] (4000) NOT NULL
   )
   ```
2. Use the following example log4net configuration file as a reference to configure log4net logging to the database:

   ```
   <log4net>
      <appender name="AdoNetAppender" type="log4net.Appender.AdoNetAppender">
         <bufferSize value="100" />
         <connectionType value="System.Data.SqlClient.SqlConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
         <connectionString value="database connection string" />
         <commandText value="INSERT INTO exagoweblog ([timestamp],[logger],[thread],[level],[reportId],[sessionId],[message]) VALUES (@timestamp, @logger, @thread, @level, @reportId, @sessionId, @message)" />
         <parameter>
            <parameterName value="@timestamp" />
            <dbType value="DateTime" />
            <layout type="log4net.Layout.RawTimeStampLayout" />
         </parameter>
         <parameter>
            <parameterName value="@logger" />
            <dbType value="String" />
            <size value="255" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%logger" />
            </layout>
         </parameter>
         <parameter>
            <parameterName value="@thread" />
            <dbType value="String" />
            <size value="255" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%-3thread" />
            </layout>
         </parameter>
         <parameter>
            <parameterName value="@level" />
            <dbType value="String" />
            <size value="50" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%-5level" />
            </layout>
         </parameter>
         <parameter>
            <parameterName value="@reportId" />
            <dbType value="String" />
            <size value="255" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%-8.8property{ReportId}" />
            </layout>
         </parameter>
         <parameter>
            <parameterName value="@sessionId" />
            <dbType value="String" />
            <size value="255" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%-8.8property{SessionId}" />
            </layout>
         </parameter>
         <parameter>
            <parameterName value="@message" />
            <dbType value="String" />
            <size value="4000" />
            <layout type="log4net.Layout.PatternLayout">
               <conversionPattern value="%message" />
            </layout>
         </parameter>
      </appender>
      <root>
         <level value="INFO" />
         <appender-ref ref="AdoNetAppender" />
      </root>
   </log4net>
   ```
3. Restart the web server and relaunch Exago.

You should no longer see information being saved to disk, and should see entries being populated in the database table instead.
