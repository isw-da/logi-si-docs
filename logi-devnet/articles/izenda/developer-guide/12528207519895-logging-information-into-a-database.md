---
title: "Logging Information Into a Database"
id: 12528207519895
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207519895-Logging-Information-Into-a-Database
updated_at: 2023-02-23T15:16:03Z
---

# Logging Information Into a Database

# Logging Information Into a Database

In order to adjust log4net to write to a particular database, as opposed to the flat .log file there are a few steps that you need to take.

Note: Depending on whether you are using the .NET Framework or .NET Core API resources, the configuration steps may vary. Please refer to the appropriate section below based on your setup.

## Using .NET Framework API

* Creating the Logging Database

  + On your database sever, create an empty database with a meaningful name to easily identify its contents (ex. Izenda Logs)
  + Within this table, create one table, entitled Log, with the query below:

    ```
    CREATETABLE[dbo].[Log]([Id][int]IDENTITY(1,1)NOTNULL,[Date][datetime]NOTNULL,[Thread][varchar](255)NOTNULL,[Level][varchar](50)NOTNULL,[Logger][varchar](255)NOTNULL,[Message][varchar](4000)NOTNULL,[Exception][varchar](2000)NULL)
    ```
* Open the web.config file in your API folder

  + in `<configSections>` replace the current `<sectionname="log4net">` with the following:

    ```
    <sectionname="log4net"type="log4net.Config.Log4NetConfigurationSectionHandler, log4net, Version=2.0.8.0, Culture=neutral, PublicKeyToken=669e0ddf0bb1aa2a"/>
    ```
* Lower on the same web.config file, there is a element (line 14). Remove this and all of its contents (Lines 14 through 52)

  + Replace the removed section with the following, noting to add your connection string to the log database:

    ```
    <log4net><root><levelvalue="DEBUG"/><appender-refref="ADONetAppender"/></root><appendername="ADONetAppender"type="log4net.Appender.ADONetAppender"><bufferSizevalue="1"/><connectionTypevalue="System.Data.SqlClient.SqlConnection, System.Data, Version=2.0.8.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"/><connectionStringvalue="[YOUR CONNECTION STRING TO THE IZENDA LOGS DATABASE HERE]"/><commandTextvalue="INSERT INTO Log ([Date],[Thread],[Level],[Logger],[Message],[Exception]) VALUES (@log_date, @thread, @log_level, @logger, @message, @exception)"/><parameter><parameterNamevalue="@log_date"/><dbTypevalue="DateTime"/><layouttype="log4net.Layout.RawTimeStampLayout"/></parameter><parameter><parameterNamevalue="@thread"/><dbTypevalue="String"/><sizevalue="255"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%thread"/></layout></parameter><parameter><parameterNamevalue="@log_level"/><dbTypevalue="String"/><sizevalue="50"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%level"/></layout></parameter><parameter><parameterNamevalue="@logger"/><dbTypevalue="String"/><sizevalue="255"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%logger"/></layout></parameter><parameter><parameterNamevalue="@message"/><dbTypevalue="String"/><sizevalue="4000"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%message"/></layout></parameter><parameter><parameterNamevalue="@exception"/><dbTypevalue="String"/><sizevalue="2000"/><layouttype="log4net.Layout.ExceptionLayout"/></parameter></appender></log4net>
    ```

    Note: The bufferSize value is currently set to 1. You can adjust this value to change the frequency with which the logs get pushed into the database.

## Using .NET Core API

* Creating the Logging Database

  + On your database sever, create an empty database with a meaningful name to easily identify its contents (ex. Izenda Logs)
  + Within this table, create one table, entitled Log, with the query below:

    ```
    CREATETABLE[dbo].[Log]([Id][int]IDENTITY(1,1)NOTNULL,[Date][datetime]NOTNULL,[Thread][varchar](255)NOTNULL,[Level][varchar](50)NOTNULL,[Logger][varchar](255)NOTNULL,[Message][varchar](4000)NOTNULL,[Exception][varchar](2000)NULL)
    ```
* Open the log4net.config file in your API folder

  + In `<root>` replace the current `<appender-ref>` elements with the ADONetAppender. Please refer the following as example:

    ```
    <root><appender-refref="ADONetAppender"/></root>
    ```
* Lower on the same log4net.config file, there are two appender elements. Remove this and all of its contents (Lines 8 through 38)

  + Replace the removed section with the following, noting the reference to appsetting.json for the connectionStringFile:

    ```
    <appendername="ADONetAppender"type="MicroKnights.Logging.AdoNetAppender, MicroKnights.Log4NetAdoNetAppender"><bufferSizevalue="1"/><connectionTypevalue="System.Data.SqlClient.SqlConnection,System.Data,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089"/><connectionStringNamevalue="log4net"/><connectionStringFilevalue="appsettings.json"/><commandTextvalue="INSERT INTO Log ([Date],[Thread],[Level],[Logger],[Message],[Exception]) VALUES (@log_date, @thread, @log_level, @logger, @message, @exception)"/><parameter><parameterNamevalue="@log_date"/><dbTypevalue="DateTime"/><layouttype="log4net.Layout.RawTimeStampLayout"/></parameter><parameter><parameterNamevalue="@thread"/><dbTypevalue="String"/><sizevalue="255"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%thread"/></layout></parameter><parameter><parameterNamevalue="@log_level"/><dbTypevalue="String"/><sizevalue="50"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%level"/></layout></parameter><parameter><parameterNamevalue="@logger"/><dbTypevalue="String"/><sizevalue="255"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%logger"/></layout></parameter><parameter><parameterNamevalue="@message"/><dbTypevalue="String"/><sizevalue="4000"/><layouttype="log4net.Layout.PatternLayout"><conversionPatternvalue="%message"/></layout></parameter><parameter><parameterNamevalue="@exception"/><dbTypevalue="String"/><sizevalue="2000"/><layouttype="log4net.Layout.ExceptionLayout"/></parameter></appender>
    ```

    Note: The bufferSize value is currently set to 1. You can adjust this value to change the frequency with which the logs get pushed into the database.
* Open the appsettings.json file in your API folder

  + Add a “connectionStrings” parameter that points to your Log database similar to the below:

    ```
    {"Logging":{"LogLevel":{"Default":"Warning"}},"httpHandlers":{},"AllowedHosts":"*","AppSettings":{"Settings":{"defaultlandingpage":"Views/DefaultLandingPage.html","izendaapiprefix":"api","izendapassphrase":"vqL7SF+9c9FIQEKUOhSZapacQgUQh","responseserverpath":"rs","izenda.mssql.trimcharacters":"","izenda.mysql.trimcharacters":"","izenda.oracle.trimcharacters":"","izenda.postgre.trimcharacters":";","izenda.redshift.trimcharacters":"","izenda.elasticsearch.trimcharacters":"","izenda.mongo.trimcharacters":""}},"connectionStrings":{"log4net":"[YOUR CONNECTION STRING TO THE IZENDA LOGS DATABASE HERE]"}}
    ```
* Download the MicroKnights.Log4NetAdoNetAppender.dll file from our Utilities page from the Upgrade tab in the [Customer Portal](https://app.izenda.com).

  + Add this assembly file to the root of your API directory.
