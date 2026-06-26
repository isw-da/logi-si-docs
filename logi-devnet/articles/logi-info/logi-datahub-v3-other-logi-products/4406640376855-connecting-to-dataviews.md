---
title: "Connecting to Dataviews"
id: 4406640376855
section: "Logi DataHub v3 & Other Logi Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640376855-Connecting-to-Dataviews
updated_at: 2022-04-01T03:13:27Z
---

# Connecting to Dataviews

# Connecting to Dataviews

Logi Info applications use a special Connection element, **Connection.Logi DataHub v3**, in the \_Settings definition to connect to dataviews:

![](https://devnet.logianalytics.com/hc/article_attachments/5160432758935/withinfo_01.png)

This Connection element is available in Logi Info v12.0.036 SP2 and later. It provides a single connection point to all of the dataviews available in the Logi DataHub v3 repository database.

The element's attributes are:

| **Attribute** | **Description** |
| --- | --- |
| ID | (Required)  Specifies an element identifier, unique within the application. |
| Server | (Required)  Specifies the name of the server hosting the Logi DataHub v3 repository database. |
| User | (Required)  Specifies a user name for accessing the Logi DataHub v3 repository database. The standard installed database user name is *postgres*. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the Logi DataHub v3 repository is presumed to have failed. The default value is *60* seconds. |
| Connection String | Specifies a full connection string to the Logi DataHub v3 repository database. If a value is defined here, it will override all other attributes for this element and be used for the connection to the database. |
| Database | Specifies The name of the Logi DataHub v3 repository database. The standard installed database user name (the default value) is *logiLogi DataHub v3*. |
| Password | Specifies a password for accessing the Logi DataHub v3 repository database. |
| Port | Specifies the port address of the Logi DataHub v3 repository database. The standard installed database port number (the default value) is *5029*. |
| SQL Syntax | Specifies the type of database server. The value is used by ActiveSQL dataLayers which must know the database type to generate correct SQL statements. |

Once the connection has been made, then dataviews are available using the standard Logi Studio data retrieval elements and tools:

![](https://devnet.logianalytics.com/hc/article_attachments/5160411114007/withinfo_02.png)

In the example shown above, Studio's Database Browser tool is being used to explore the Logi DataHub v3 repository.
