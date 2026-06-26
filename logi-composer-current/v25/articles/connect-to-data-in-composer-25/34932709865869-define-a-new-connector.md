---
title: "Define a New Connector"
id: 34932709865869
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector
updated_at: 2026-05-26T22:10:18Z
---

# Define a New Connector

# Define a New Connector

Connector definitions make a connector server available to authorized users on the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page. They make it possible for you to connect to a specific type of data store (such as Impala or Elasticsearch). More than one connector definition can be created for a connector server.

**Define a new connector in the** Composer **environment**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Connectors** from the menu. The Managed Connector Services work area opens.
3. In the Connector Servers section of the Manage Connector Services page, verify that a connector server has been registered for the type of connector you want to define. If it has not, register one. See [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers) and [Register a New Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742145165-Register-a-New-Connector-Server).
4. In the Connectors section of the Manage Connector Services page, select **Add Connector Server** The Create New Connector page appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167442916237)
5. On the Create New Connector page, specify the following information in the input boxes.

   | Input Box | Description |
   | --- | --- |
   | Connector | Specify a unique name for the new connector. A short name is recommended due to the limited space on the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page to display the icon and name. |
   | Connector Description | Optionally, specify a description of the connector. |
   | Enable this Connector | Slide this switch on or off to enable or disable the connector on the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page. |
   | Connector Server | Select the connector server definition that should be used for this connector. |
   | Storage Type | This value is automatically set by Composer after you have selected the connector server. |
   | Connector Image | The default image is retrieved from the connector server. If you want to change the image, select **Choose File** to select a custom icon for the connection type. The requirements for the icon are as follows:  * PNG or SVG format * Resolution (min/max): 72 x 72 px or 160 x 160 px * Max file size: 50 Kb Select **Restore Default** to restore the image to the default image for the connector server type. |
   | Connector Parameters | The connector parameter information is generated from the selected connector server.  Configure or customize the connection parameters, as needed. These are the values that appear on the Connections page or Connection tab when a user defines a new [connection](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932706697357-Manage-Data-Store-Connections) or a new [data source configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) or edits an existing one.  The following fields help you customize the parameters to meet your needs:  * **Order:** Use the arrows to move the parameters up or down and change the order in which the parameters are listed on the Connections page (connection definition) or Connection tab (data source configuration). * **Required:** Select this checkbox to make the parameter required for validating the connection. Clear the checkbox if the parameter is not required. * **Visible:** Select this checkbox to show optional parameters on the Connections page or Connection tab. Clear the checkbox to hide the parameter. * **User Attribute:** Select this checkbox to use custom attributes for the parameter when you set up connections using this connector. See [Use User Attributes for Connection Parameters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932716668301-Use-User-Attributes-for-Connection-Parameters). * **Parameter:** The internal parameter name. No changes can be made. * **Parameter Type:** The type of parameter. No changes can be made. * **Label:** Specify the label for the parameter. This is the field name that will be used for the parameter on the Connections page or Connection tab. * **Help Text:** Provide help text for the parameter. It will be displayed when you select the help icon associated with the input box for the parameter. Select **Restore Default** to restore the connector parameters to the defaults for the connector server type. |
6. When you have made the required changes, select **Register**. The new connector displays in the **Connector** section of the **Manage Connector Services** page. If you enabled it, it is also visible on the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page where you maintain [data source configurations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources).
