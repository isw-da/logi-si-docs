---
title: "Event Logging to File"
id: 360051534474
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051534474-Event-Logging-to-File
updated_at: 2024-09-11T17:40:30Z
---

# Event Logging to File

# Intro

The following is a sample solution to capture Event Logging activity to standard file logging systems.

This solution does not cover strategies on what details to capture (e.g. additional session information) or how to analyze recorded activity (e.g. how to use recorded activity to identify amount of time user spent analyzing data).

The solution is a plugin that ‘serializes' PluginParameters key-value pairs and adds to a Logger. Pass necessary information to plugin as parameter values.

The solution is a sample implementation to demonstrate approach. It should be extended for complex requirements.

# Java

Tomcat, web server used by most non-Windows customers, uses JULI to log web server activity. Another, common library is Log4J, which just happens to be packaged with the Info engine. Log4j supports granular control over target destination, including file and database options. It allows for writing app log files separate from web server log files, with simple configuration. It also supports better file name patterning.

The attached Java plugin solution provides two classes:

1. SimpleLogging uses java.util.logging to log to Tomcat's default logging mechanism (JULI) based on configuration defined in conf/logging.properties. Logs are appended to catalina.out (default).
2. SimpleLoggingWithLog4j uses log4j library. It relies on configuration defined in WEB-INF/classes/log4j.properties file to record logs under specific file pattern

## Steps to implement

### JULI / Tomcat default logging mechanism:

1. Define Process / task to call plugin; define parameters to forward relevant information to log

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360082583393)

```
        <Task  
  
               ID="log"  
  
               >  
  
               <Procedure  
  
                       ID="logger-SimpleLogging"  
  
                       JavaPluginVersion="Version10"  
  
                       PluginMethod="logEvent"  
  
                       PluginName="com.logianalytics.plugins.SimpleLogging"  
  
                       Type="PluginCall"  
  
                       >  
  
                       <PluginParams  
  
                              AppName="@Function.AppVirtualPath~"  
  
                              EventDuration="@Request.EventDuration~"  
  
                              EventName="@Request.EventName~"  
  
                              EventTime="@Request.EventTime~"  
  
                              EventTimePrecise="@Request.EventTimePrecise~"  
  
                              ReportID="@Request.ReportID~"  
  
                              RowCount="@Request.RowCount~"  
  
                              SQL="@Request.SQL~"  
  
                              UserName="@Function.UserName~"  
  
                       />  
  
                       <Note  
  
                              Note="SimpleLogging uses Tomcat&apos;s default logging configuration"  
  
                       />  
  
               </Procedure>  
  
        </Task>
```

2. Enable Event Logging under \_Settings. Add specific activities to log.

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360081452334)

```
      <EventLogging  
  
               LogEvents="True"  
  
               >  
  
               <LogEvent  
  
                       EventName="SessionStart"  
  
                       ID="logSessionStart"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
               <LogEvent  
  
                       EventName="BuildReport"  
  
                       ID="logBuildReport"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
               <LogEvent  
  
                       EventName="RunSQL"  
  
                       ID="logRunSQL"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
        </EventLogging>
```

3. Place SimpleLogging.jar under <APP PATH>\WEB-INF\lib
4. Start Tomcat and run application
5. Monitor <TOMCAT PATH>\logs\catalina.out OR console to confirm log information is captured. E.g.

![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/360082583453)![mceclip3.png](https://devnet.logianalytics.com/hc/article_attachments/360082583493)

### Log4J logging mechanism:

Difference in implementation is:

1. In PluginCall procedure, set Assembly Name to logianalytics.plugins.SimpleLoggingWithLog4j
2. Update WEB-INF/classes/log4j.properties to define log file properties. Tomcat variables are available, but app context may not be. So, app name must be defined. Sample properties file.

```
#Stock definition  
  
#log4j.rootLogger=FATAL, CONSOLE  
  
#log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender  
  
#log4j.appender.CONSOLE.layout=org.apache.log4j.SimpleLayout  
  
   
  
#app logger option  
  
log4j.rootLogger=INFO, file  
  
   
  
# file  
  
log4j.appender.file=org.apache.log4j.DailyRollingFileAppender  
  
#log4j.appender.file.File=c:\\logs\\SSMJava12_6.log  
  
log4j.appender.file.File=${catalina.base}/logs/<APP NAME>.log  
  
log4j.appender.DatePattern='-'yyyy-MM-dd  
  
#log4j.appender.file.MaxFileSize=10MB  
  
#log4j.appender.file.MaxBackupIndex=10  
  
log4j.appender.file.layout=org.apache.log4j.PatternLayout  
  
log4j.appender.file.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n  
  
   
  
   
  
# Console - not referenced for rootLogger, so logs will not be displayed in console  
  
log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender  
  
log4j.appender.CONSOLE.layout=org.apache.log4j.SimpleLayout  
  
 
```

3. Check for log file creation in folder defined in properties file

![mceclip4.png](https://devnet.logianalytics.com/hc/article_attachments/360081452414)

## .Net Log4Net logging mechanism:

Reference: <https://codeshare.co.uk/blog/how-to-set-up-and-configure-error-logging-in-net-with-log4net/>

### Steps to Implement

1. Define Process / task to call plugin; define parameters to forward relevant information to log

![mceclip5.png](https://devnet.logianalytics.com/hc/article_attachments/360082583653)

```
<?xml version="1.0" encoding="utf-8"?>  
  
<Process  
  
       ID="Logging"  
  
       >  
  
       <Task  
  
             ID="log"  
  
             >  
  
             <Procedure  
  
                    ID="logger-SimpleLogging"  
  
                    JavaPluginVersion="Version10"  
  
                    PluginMethod="logEvent"  
  
                    PluginName="EventLoggingToFile.dll"  
  
                    PluginTypeName="EventLoggingToFile.SimpleLogging"  
  
                    Type="PluginCall"  
  
                    >  
  
                    <PluginParams  
  
                           AppName="@Function.AppVirtualPath~"  
  
                           EventDuration="@Request.EventDuration~"  
  
                           EventName="@Request.EventName~"  
  
                           EventTime="@Request.EventTime~"  
  
                           EventTimePrecise="@Request.EventTimePrecise~"  
  
                           ReportID="@Request.ReportID~"  
  
                           RowCount="@Request.RowCount~"  
  
                           SQL="@Request.SQL~"  
  
                           UserName="@Function.UserName~"  
  
                    />  
  
             </Procedure>  
  
       </Task>  
  
       <ideTestParams  
  
             EventDuration=""  
  
             EventName=""  
  
             EventTime=""  
  
             EventTimePrecise=""  
  
             rdTaskID=""  
  
             ReportID=""  
  
             RowCount=""  
  
             SQL=""  
  
       />  
  
</Process>
```

 2. Enable Event Logging under \_Settings. Add specific activities to log.

```
      <EventLogging  
  
               LogEvents="True"  
  
               >  
  
               <LogEvent  
  
                       EventName="SessionStart"  
  
                       ID="logSessionStart"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
               <LogEvent  
  
                       EventName="BuildReport"  
  
                       ID="logBuildReport"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
               <LogEvent  
  
                       EventName="RunSQL"  
  
                       ID="logRunSQL"  
  
                       >  
  
                       <Action  
  
                              ID="log"  
  
                              Process="Logging"  
  
                              TaskID="log"  
  
                              Type="Process"  
  
                       />  
  
               </LogEvent>  
  
        </EventLogging>
```

 3. Copy DLLs – EventLoggingToFile.dll and log4net.dll – to \_Plugins folder

4. Copy AssemblyInfo.cs under Properties folder at root of application  
This files directs application to initialize Log4Net when application starts.

 5. Update web.config with log4net logging pattern. Sample configuration below writes to date-based files under Logs folder under application root.

```
  <configSections>  
  
    <section name="log4net" type="log4net.Config.Log4NetConfigurationSectionHandler, log4net"/>  
  
  </configSections>  
  
  <log4net>  
  
    <root>  
  
      <level value="ALL" />  
  
      <!--<appender-ref ref="ConsoleAppender" />-->  
  
      <appender-ref ref="RollingFileAppender" />  
  
    </root>  
  
    <appender name="ConsoleAppender" type="log4net.Appender.ConsoleAppender">  
  
      <layout type="log4net.Layout.PatternLayout">  
  
        <conversionPattern value="%date %level %logger - %message%newline" />  
  
      </layout>  
  
    </appender>  
  
    <appender name="RollingFileAppender" type="log4net.Appender.RollingFileAppender">  
  
      <file type="log4net.Util.PatternString" value="Logs\TraceLog.%property{log4net:HostName}.txt" />  
  
      <appendToFile value="true" />  
  
      <rollingStyle value="Date" />  
  
      <maxSizeRollBackups value="5" />  
  
      <maximumFileSize value="5MB" />  
  
      <staticLogFileName value="true" />  
  
      <layout type="log4net.Layout.PatternLayout">  
  
        <conversionPattern value="%date [%thread] %level %logger - %message%newline" />  
  
      </layout>  
  
    </appender>  
  
  </log4net>
```

 6. Restart IIS to ensure logger is initialized.

 7. Run app and review logs folder for activity.

Click [here](https://devnet.logianalytics.com/hc/article_attachments/360082592833) to download Net.zip.

Click [here](https://devnet.logianalytics.com/hc/article_attachments/360082592813) to download Java.zip.
