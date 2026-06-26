---
title: "Connecting to HP Vertica"
id: 4406818113815
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818113815-Connecting-to-HP-Vertica
updated_at: 2022-04-06T06:10:15Z
---

# Connecting to HP Vertica

# Connecting to HP Vertica

In order to use HP Vertica, you need to use a specific Connection element, **Connection.Vertica**, to connect your Logi application to a Vertica database.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562954007/workvertica_02.png)

As shown above, the **Connection.Vertica** element is added to the **\_Settings** definition, beneath the Connections element. Its attributes are then set appropriately for the Vertica datasource.
The **Vertica Parameters** element, a child of the connection element, can be used to supply additional parameters for connecting to the Vertica database.

## Attributes

The Connection.Vertica element attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies an element ID, unique across the application. |
| Vertica Database | (Required) Specifies the name of the Vertica database to be accessed. |
| Vertica Server | (Required) Specifies the name of the Vertica server to be accessed. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the database is presumed to have failed. The default value is *60* seconds. |
| Vertica Backup Server | Specifies a string containing the host name or IP address of one or more alternate Vertica servers to connect to if the primary Vertica server connection fails. Multiple servers may be specified in a comma-separated list.  The host name or IP address can also include a colon followed by the port number for the database. The default port is *5433*. |
| Vertica Connection String | Specifies a full JDBC connection string to the Vertica database. If specified, it will override all other attribute values for this Connection element. If any Vertica Parameter elements are present, they will be processed and added to the connection string. |
| Vertica Load Balance | Specifies whether the client will allow its connection to be redirected to another host in the Vertica database. This setting only has an effect if the server has also enabled load balancing. The default value is *False*. |
| Vertica Password | Specifies the password associated with the Vertica database user name. |
| Vertica Port | Specifies the Vertica database port address. The default value is *5433*. |
| Vertica SSL | Specifies whether to use SSL for this connection. The default value is *False*. |
| Vertica User | Specifies the Vertica database user name. |

## Special Drivers Required: Vertica 8.1

Vertica driver files can be found in the "driver folder":*<yourLogiAppFolder>*\rdTemplate\rdDriver\Vertica\v8.1.x

1. To use Vertica with Logi Info Studio, copy Vertica.Data.dll from the driver folder to

C:\Program Files\LogiXML IES Dev\LogiStudio\bin 
The path above is for the default Logi Info installation, and will vary if you installed Logi Info in a folder other than the default installation folder.

2. For a .NET-based Logi application - Copy the file Vertica.Data.dll from the driver folder to *<yourLogiAppFolder>*\bin.  
   For a Java-based Logi application - Copy the file vertica-jdbc-8.1.1-0.jar from the driver folder to *<yourLogiAppFolder>\*WEB-INF\lib.

Vertica 8.1 drivers are backwards compatible to Vertica server version 7.1.

## Special Drivers Required: Vertica 7.2.3

Vertica driver files can be found in the "driver folder": *<yourLogiAppFolder>*\rdTemplate\rdDriver\Vertica.

1. To use Vertica with Logi Info Studio, copy Vertica.Data.dll from the driver folder to

C:\Program Files\LogiXML IES Dev\LogiStudio\bin 
The path above is for the default Logi Info installation, and will vary if you installed Logi Info in a folder other than the default installation folder.

2. For a .NET-based Logi application - Copy the file Vertica.Data.dll from the driver folder to *<yourLogiAppFolder>*\bin.  
   For a Java-based Logi application - Copy the file vertica-jdbc-7.2.3-0.jar from the driver folder to *<yourLogiAppFolder>\*WEB-INF\lib.

Vertica 7.2 drivers are not backwards compatible with earlier versions.

## Special Drivers Required: Vertica Versions Prior to 7.2.3

For a **.NET** Logi application, you will need to *download* the Vertica **ADO.NET driver** and place it in the <yourLogiApp>\bin folder. The driver is available from the [My Vertica community web site](https://my.vertica.com/), which requires you to register and login. Version 6.1.3.0 or later is required.  
For a **Java** Logi application, you will also to *download* the Vertica **JDBC driver** and place it in the <yourLogiApp>/WEB-INF/lib folder. The driver is available from the [My Vertica community web site](https://my.vertica.com/), which requires you to register and login. Version 6.1.3.0 or later is required.
In either case, if you want to be able to use Logi Studio's **Database Browser** and **SQL Query Builder** tools while working with Vertica, you must download the Vertica ADO.NET driver mentioned above and place it in the bin folder of your Logi Info installation, typically C:\Program Files\LogiXML IES Dev\Logi Studio\bin.
If use of the Vertica ADO.NET driver is *not* possible, you can use a **Studio Connection** element to provide a separate connection for use by Studio's tools:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562954135/workvertica_03.png)

The Studio Connection element has no attributes and is simply a parent element for another non-Vertica Connection element, as shown above. That connection element is used by Studio's tools, such as the Database Browser, Web Metadata Builder, etc., during development instead of the primary connection that's used by the Logi Engine to access data at runtime.
