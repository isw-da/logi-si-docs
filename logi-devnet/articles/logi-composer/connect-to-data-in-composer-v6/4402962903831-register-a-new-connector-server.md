---
title: "Register a New Connector Server"
id: 4402962903831
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402962903831-Register-a-New-Connector-Server
updated_at: 2021-08-07T17:29:49Z
---

# Register a New Connector Server

# Register a New Connector Server

Before you can register a new connector server, be sure that you have obtained and installed it. See [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4402955468311-Obtain-Additional-Connector-Servers) and contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4402955592087-Contact-Technical-Support) to obtain the connector server code.

Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port.

To register a new connector server in the Composer environment:

1. Log into the UI as a supervisor and select **Connectors** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955649943-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)).
2. In the Connector Servers section of the Manage Connector Services page, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959567895/add-connector-server.png). The Register New Connector Server page appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952911511/connector-server-new_384x313.png)
3. On the Register New Connector Server page, specify the following information in the input boxes.

   | Input Box | Description |
   | --- | --- |
   | Connector Server Name | Specify a unique name for the new connector server. |
   | Connector Server Type | The new connector server can be added using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
   | Server URL | If you selected the HTTP protocol, specify the URL for the connector server. If you selected the socket protocol, specify the host and port details. For a list of default Composer ports, see [*Default Port Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402955646103-Default-Port-Reference). |
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952911767/register.png).

After the connector server is registered, add and enable at least one connector for it. See [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4402962897815-Define-a-New-Connector) and [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4402962899351-Enable-and-Disable-Connectors).
