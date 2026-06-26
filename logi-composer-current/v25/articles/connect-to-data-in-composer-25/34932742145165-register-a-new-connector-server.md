---
title: "Register a New Connector Server"
id: 34932742145165
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742145165-Register-a-New-Connector-Server
updated_at: 2026-05-26T22:10:15Z
---

# Register a New Connector Server

# Register a New Connector Server

Before you can register a new connector server, be sure that you have obtained and installed it. See [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers) and contact insightsoftware [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to obtain the connector server code.

Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port.

**Register a new connector server in your** Composer **environment**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Connectors** from the menu. The Managed Connector Services work area opens.
3. In the Connector Servers section of the Manage Connector Services page, select **Add Connector Server**. The Register New Connector Server page appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167375173005)
4. On the Register New Connector Server page, specify the following information in the input boxes.

   | Input Box | Description |
   | --- | --- |
   | Connector Server Name | Specify a unique name for the new connector server. |
   | Connector Server Type | The new connector server can be added using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
   | Server URL | If you selected the HTTP protocol, specify the URL for the connector server. If you selected the socket protocol, specify the host and port details. For a list of default Composer ports, see [Default Port Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097511949-Default-Port-Reference). |
5. Select **Register**.

After the connector server is registered, add and enable at least one connector for it. See [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector) and [Enable and Disable Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932710074509-Enable-and-Disable-Connectors).
