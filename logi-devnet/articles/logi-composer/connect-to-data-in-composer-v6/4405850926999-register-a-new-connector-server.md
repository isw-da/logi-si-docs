---
title: "Register a New Connector Server"
id: 4405850926999
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850926999-Register-a-New-Connector-Server
updated_at: 2024-05-24T08:26:18Z
---

# Register a New Connector Server

# Register a New Connector Server

Before you can register a new connector server, be sure that you have obtained and installed it. See [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers) and contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) to obtain the connector server code.

Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port.

To register a new connector server in the Composer environment:

1. Log into the UI as a supervisor and select **Connectors** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)).
2. In the Connector Servers section of the Manage Connector Services page, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743919511/add-connector-server.png). The Register New Connector Server page appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743920535/connector-server-new_384x313.png)
3. On the Register New Connector Server page, specify the following information in the input boxes.

   | Input Box | Description |
   | --- | --- |
   | Connector Server Name | Specify a unique name for the new connector server. |
   | Connector Server Type | The new connector server can be added using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
   | Server URL | If you selected the HTTP protocol, specify the URL for the connector server. If you selected the socket protocol, specify the host and port details. For a list of default Composer ports, see [*Default Port Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851144087-Default-Port-Reference). |
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747451287/register.png).

After the connector server is registered, add and enable at least one connector for it. See [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector) and [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919959-Enable-and-Disable-Connectors).
