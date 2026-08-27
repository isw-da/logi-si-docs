---
title: "Register a New Connector Server"
id: 43701042690957
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server
updated_at: 2026-08-26T07:11:30Z
---

# Register a New Connector Server

# Register a New Connector Server

Before you can register a new connector server, be sure that you have obtained and installed it. See [Obtain Additional Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024898061-Obtain-Additional-Connector-Servers) and contact insightsoftware [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to obtain the connector server code.

Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port.

## Register a New Connector Server in Your Environment

1. Log in as a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Connectors** from the menu. The Managed Connector Services work area opens.
3. In the Connector Servers section of the Manage Connector Services page, select **Add Connector Server**. The Register New Connector Server page appears.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48418019568397)
4. On the Register New Connector Server page, specify the following information in the input fields.

   | Input Field | Description |
   | --- | --- |
   | Connector Server Name | Specify a unique name for the new connector server. |
   | Connector Server Type | Add the connector server using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
   | Server URL | If you selected the HTTP protocol, specify the URL for the connector server. If you selected the socket protocol, specify the host and port details. For a list of default Composer ports, see [Default Port Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701123718157-Default-Port-Reference). |
5. Select **Register**.

After the connector server is registered, add and enable at least one connector for it. See [Define a New Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993403661-Define-a-New-Connector) and [Enable and Disable Connectors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024705037-Enable-and-Disable-Connectors).

### Register the Dundas BI (Managed) Connection Server

To use this connector, you must make the user interface available in your instance. Disabled by default, you can enable the user interface option as part of your post installation or post upgrade tasks. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

After you have made this interface available, you can then register the server by providing the following information:

| Input Field | Description |
| --- | --- |
| Connector Server Name | Specify a unique name for this connector server. |
| Connector Server Type | Add the connector server using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
| Server URL | * If you selected the HTTP protocol, specify the URL for the connector server. * If you selected the socket protocol, specify the host and port details.   `http://dundasbi-dundas-bi-edc:8013/connector`  Depending on how your environment is set up, this may default to port 8013. Depending on your configuration, this may be set to 8080. Verify the exact port in use in the environment hosting the data source. |

After you have registered this connector server, you can [enable and disable](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024705037-Enable-and-Disable-Connectors) it as you would any other connector server.
