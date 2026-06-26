---
title: "Using Vendor-Specific Connections"
id: 4406817679639
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817679639-Using-Vendor-Specific-Connections
updated_at: 2022-04-06T06:07:33Z
---

# Using Vendor-Specific Connections

# Using Vendor-Specific Connections

Vendor-specific Connection elements are designed to make configuring a connection very simple.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575602711/introconn5_04.png)

As shown in the example above, a **Connection.MySQL** element has been added to the \_Settings definition in an application. Its attributes allow the developer to specify the server name, database name, and access credentials. At runtime, the required connection string will be created behind-the-scenes using this information.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575602839/introconn5_05.png)

Optional parameter elements, as shown above, can be added beneath the connection element. These provide the flexibility of including additional connection string parameters, if necessary. For example, the optional parameters for the MySQL connection include Compress, Connection Lifetime, Direct, Embedded, Port, Protocol, and Unicode. You can also enable special MySQL connection behavior, like use of User Defined Variables, by creating the parameter Allow\_User\_Variables and setting it to *True*.

The other attributes for Connection.MySQL and similar connection elements, are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID; referred to by otherelements that use this connection. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the datasource is presumed to have failed. For most datasources, the default value is *60* seconds. For MySQL, the default is *30* seconds. |
| Connection String | A fully-formed connection string for the database. If a value is defined here, all other attributes will be ignored and this string will be used to connect to the database. Any child parameter elements will be added to the connection string. |
| Port | The port number for the database, if the default number is not being used. |

In general, vendor-specific connections are much easier to configure than generic connection and developers should look to them first when creating applications.
