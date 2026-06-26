---
title: "Using DataHub with Logi Info"
id: 4406640373783
section: "Using DataHub v2.2 With Logi Info"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640373783-Using-DataHub-with-Logi-Info
updated_at: 2022-04-01T15:51:14Z
---

# Using DataHub with Logi Info

# Using DataHub with Logi Info

**Logi DataHub** is separate Logi product that is used to retrieve and prepare data, which it stores in its own repository database. That data is available as "Dataviews", which can be accessed as a datasource in Logi Info applications. This topic discusses how to access and use dataviews in Logi Info apps.

* [About DataHub](#About)
* [Connecting to Dataviews](#Connecting)
* [Dataviews in the Metadata Builder Wizard](#MDBW)

## About DataHub

Logi DataHub is a data virtualization product that connects to multiple sources, caches data for high-performance, and prepares data in intuitive ways, so you can deliver efficient reporting and analysis that doesn't affect transactional systems.

DataHub includes *DataSmart* profiling, which automatically identifies the types and formats of your data and provides easy ways of enriching it through new calculations and manipulation of multi-part data.

It uses its own repository database to store prepared data and that database can be accessed by a Logi Info application just like any other datasource.

## Connecting to Dataviews

Logi Info applications use a special Connection element, **Connection.DataHub**, in the \_Settings definition to connect to dataviews:

![](https://devnet.logianalytics.com/hc/article_attachments/5160432758935/withinfo_01.png)

This Connection element is available in Logi Info v12.0.036 SP2 and later. It provides a single connection point to all of the dataviews available in the DataHub repository database.

The element's attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required)  Specifies an element identifier, unique within the application. |
| Server | (Required)  Specifies the name of the server hosting the DataHub repository database. |
| User | (Required)  Specifies a user name for accessing the DataHub repository database. The standard installed database user name is *postgres*. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the DataHub repository is presumed to have failed. The default value is *60* seconds. |
| Connection String | Specifies a full connection string to the DataHub repository database. If a value is defined here, it will override all other attributes for this element and be used for the connection to the database. |
| Database | Specifies The name of the DataHub repository database. The standard installed database user name (the default value) is *logidatahub*. |
| Password | Specifies a password for accessing the DataHub repository database. |
| Port | Specifies the port address of the DataHub repository database. The standard installed database port number (the default value) is *5029*. |
| SQL Syntax | Specifies the type of database server. The value is used by ActiveSQL datalayers which must know the database type to generate correct SQL statements. |

Once the connection has been made, then dataviews are available using the standard Logi Studio data retrieval elements and tools:

![](https://devnet.logianalytics.com/hc/article_attachments/5160411114007/withinfo_02.png)

In the example shown above, Studio's Database Browser tool is being used to explore the DataHub repository.

## Dataviews in the Metadata Builder Wizard

Logi Info installations that include the [Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/1500009515322-Install-the-Self-Service-Reporting-Module) add-on enable the **Active Query Builder** and **Metadata** elements in Logi Studio.

The Active Query Builder allows Analysis Grid users to determine what dataset to work with, by giving them a way to interactively select tables and joins, at runtime.

The tables, views, columns, and relationships are available for use with the Active Query Builder are determined by building a "metadata file", associated with a Connection element, which enumerates all of the database objects that will be available to users for selection in the Analysis Grid. The Metadata element provides a tool, the [Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009516142-Use-the-Metadata-Builder-Wizard) wizard**,** which is used during development to create the file.

The Metadata Builder wizard can create metadata files for DataHub dataviews.

![](https://devnet.logianalytics.com/hc/article_attachments/5160421354903/withinfo_03.png)

To do this, the Metadata element is added as child of the Connection.DataHub element in \_Settings, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5160432700439/withinfo_04.png)

The Metadata Builder wizard is then used, as shown above, to create the metadata file for the DataHub dataview.

![](https://devnet.logianalytics.com/hc/article_attachments/5160453600279/withinfo_05.png)

The Active Query Builder is then able to use the DataHub metadata and display it in the Analysis Grid interface, as shown above.
