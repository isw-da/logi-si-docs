---
title: "Connecting to Hadoop "
id: 4419722947479
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722947479-Connecting-to-Hadoop
updated_at: 2022-07-17T02:24:17Z
---

# Connecting to Hadoop 

# Connecting to Hadoop

For a .NET Logi application, use the **Connection.ODBC** element to
connect your Logi application to a the datasource.

For a Java Logi application, use the **Connection.JDBC** element. Logi
Info supports Apache Hive 0.13.0 with Hortonworks 2.1 or Cloudera 5.0
Impala, and include supporting drivers and libraries for them.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Hadoop drivers were deprecated from Info Java. The following libraries were removed: hadoop-core-0.20.2.jar,
hive-exec-0.13.0.jar,
hive-jdbc-0.13.0.jar,
hive-service-0.13.0.jar,
libfb303-0.9.1.jar, and
libthrift-0.9.1.jar.

## Special ODBC Drivers Required

For .NET applications, depending on which Hadoop implementation you're
connecting to, you'll need to *download and install* either the
[Cloudera ODBC Driver for Impala](https://www.cloudera.com/downloads/connectors/impala/odbc/2-5-36.html)
or the
[Hortonworks Hive ODBC Driver](https://hortonworks.com/downloads/). Select the proper driver version and Windows version (32- or 64-bit)
for your application (a 32-bit driver is required for a 32-bit Logi app,
and a 64-bit driver for a 64-bit app). You can install 32- and/or 64-bit
drivers on a 64-bit machine.

The links provided point to web pages that include the drivers and
installation guides. In general, all the default values can be used. After
installation, **restart** the computer.

## ODBC Data Source Configuration

For .NET applications, once you have a driver installed, you'll need to
configure a ODBC data source to use it. This is done using the Windows
**ODBC Data Source Administrator** utility.

On Windows platforms, this tool is typically launched from Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Administrative Tools![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Data Sources, or Start Menu![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Control Panel![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Administrative Tools![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Data Sources. These shortcuts launch the utility that matches the OS,
i.e. on a 32-bit OS they launch the 32-bit utility, on a 64-bit OS, the
64-bit utility.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
If you want to configure a 32-bit data source on a 64-bit machine, you
*must* use the *32-bit version* of the Data Source
Administrator. This is the source of many confusing problems when what
appears to be a perfectly configured ODBC DSN does not work because it is
loading the wrong kind of driver. You can't access the 32-bit Data Source
Administrator from the Start Menu or Control Panel in 64-bit Windows.
Instead, you must manually launch
C:\WINDOWS\SysWOW64\odbcad32.exe.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809920279/workhadoop_03_477x402.png)

In the following examples, the Hortonworks driver will be shown, but the
information also generally applies to the Cloudera driver. In the Data
Source Administrator, shown above, select the **System DSN** tab and
click **Add**. Select your new driver from the list and click
**Finish**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
This *must* be created as a System DSN, *not* a User DSN.
A User DSN will not be found by the web server and a "Data source
name not found" error will occur.

![](https://devnet.logianalytics.com/hc/article_attachments/7522840684695/workhadoop_04_312x428.png)

The Driver Setup dialog box, shown above, will be displayed. Fill-in the
information as suggested above, making appropriate changes for the
Cloudera driver. Detailed information about the purpose of each field is
available in the
[*Cloudera*](https://docs.cloudera.com/documentation/other/connectors/hive-odbc/2-6-5/Cloudera-ODBC-Driver-for-Apache-Hive-Install-Guide.pdf)
and
[*Hortonworks*](http://hortonworks.com/wp-content/uploads/2013/04/Hortonworks-Hive-ODBC-Driver-User-Guide.pdf)*DSN Installation Guides*. Authentication configuration is
discussed in [Cloudera and Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419715321111-Cloudera-and-Kerberos-Authentication-).

Once you've entered appropriate data, click **Test** to validate the
connection. Click **OK** to save the DSN setup.

![](https://devnet.logianalytics.com/hc/article_attachments/7522813330071/workhadoop_05.png)

Your new data source should appear in the System DSN list, as shown above.
Click **OK** to exit the utility. Now you're ready to use the
driver.

## Making the Connection

For .NET applications, use a **Connection.ODBC** element to make the
connection. For a Java applications, use the
**Connection.JDBC** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809952919/workhadoop_06_551x142.png)

The example above shows a **Connection.ODBC** element in the
**\_Settings** definition, beneath the Connections element. Its
Connection String attribute is then set to use the new ODBC datasource, by
DSN name.
