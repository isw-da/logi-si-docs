---
title: "Using Special-Purpose Connections"
id: 4419715395863
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715395863-Using-Special-Purpose-Connections
updated_at: 2023-03-22T20:27:57Z
---

# Using Special-Purpose Connections

# Using Special-Purpose Connections

Special-purpose connections are used to connect to specific web services or to special OS services for the Logi Scheduler and other facilities. All require credentials to authenticate the connection.

![](https://devnet.logianalytics.com/hc/article_attachments/7522839133335/introconn5_08.png)

In the example shown above, a **Connection.Web Service** element has been added to the \_Settings definition. The attributes identify specific aspects of the web service. As with all connections, a unique ID is required so that it can be referenced later by datalayer elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) For developers connecting to their *own* web service, the WSDL document specified in this connection element's required WSDL URL attribute must be "valid", meaning that it can contain no errors that would cause it to fail to compile. A document that's readable but that will not compile is invalid and will cause the connection to fail.

Connection.Web Service has an optional child element, **Connector Property Parameters**, which makes it possible to connect to a web service which requires special
authentication and proxy settings.

![](https://devnet.logianalytics.com/hc/article_attachments/7522839138455/introconn5_09.png)

In the next example, shown above, a **Connection.REST** element has been added to the \_Settings definition. Its **Url Host** attribute identifies the web service host address, and other attributes are used to provide user credentials, if required. As with all connections, a unique ID is required so that it can be referenced later by datalayer elements.

## Connection.REST with Windows Domain Authentication

The Connection.REST element includes an attribute that lets you use Windows domain authentication, also known as "integrated security", with your connection. To enable this, set the connection element's **IntegratedSecurity** attribute to *True* and leave the **Username** and **Password** attribute values blank. The integrated security credentials that the application is running
under will be used for the connection.
