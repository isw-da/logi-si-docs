---
title: "Use User Attributes for Connection Parameters"
id: 34932716668301
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932716668301-Use-User-Attributes-for-Connection-Parameters
updated_at: 2026-05-26T22:10:17Z
---

# Use User Attributes for Connection Parameters

# Use User Attributes for Connection Parameters

User attributes (variables) can be used for the connection parameters in a connection definition. Attributes can be defined for the full connection string, the host name, the port number, the cluster name, the user name, or the password, and any other parameters supported by the connector. The attributes are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your environment. This topic describes how to set up this functionality.

* [Step 1: Review and Select Connector Parameters for Which Attributes Can Be Used](#Step)
* [Step 2: Define Custom Attributes](#Step2)
* [Step 3: Define Connections Using User Attributes](#Step3)

You can also insert variables directly in the connection parameters of a connection definition. See [Insert Variables for Connection Parameters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932732148493-Insert-Variables-for-Connection-Parameters).

## Step 1: Review and Select Connector Parameters for Which Attributes Can Be Used

**Review and select connector parameters for which user attributes can be used**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Connectors** from the menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167973150989)). The Manage Connector Services page appears.
3. In the Connectors section of the page, select connector parameters to review. Alternatively, you can create a new connector definition and review and modify the parameters in the new definition. See [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector).

   Either the Edit Connector or the Create New Connector page for the connector appears.
4. Review the connector parameters that appear at the bottom of the Edit Connector or Create New Connector page.
5. In the following Impala connector definition, the **User Attribute** checkbox is selected for the USER\_NAME and PASSWORD parameters. The user definitions in this instance must include custom attributes for these parameters (see [Step 2](#Step2)) and the connection definitions for this Impala connector must select the appropriate custom attributes as user credentials (see [Step 3](#Step3)).

   ![Use this work area to customize the fields for this connector, including use of User Attributes](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167454031501 "Connector Parameters work area")
6. Alter the other connector parameters, as needed.

   * If a connector parameter is required, make sure its **Required** checkbox is selected. Depending on the connector server, some parameters are already selected because they are required.
   * If a connector parameter should be visible (especially if the parameter is required) when the connection definition is created, make sure its **Visible** checkbox is selected.

   For information about all connector parameters, see [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector).
7. Select **Save** to save the connector parameters.

## Step 2: Define Custom Attributes

A custom attribute must be defined for every connector parameter for which you selected the **User Attribute** checkbox in [Step 1](#Step). The only exceptions are the context variables `${User.composerUserName}`, `${User.accountId}`, and `${User.credentials}`. These built-in attributes which automatically exist and can be used connect the currently logged in user.

* `${User.composerUserName}`, `${User.accountId}`: include to insert the name or account ID of the user that is currently logged in.
* `${User.credentials}`: include to pass the session ID or trusted access token (in embedded environments) of the user.

You can define custom attributes in several ways:

* Individually for every user who needs to create data sources from a connection or using the connector. If you use this method, the variable names must be the same for each user. See [Specify Custom User Attributes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932642529293-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [Use Lightweight Directory Access Protocol (LDAP)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933132827149-Use-Lightweight-Directory-Access-Protocol-LDAP) and [Configure Composer to Support SAML](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933168056717-Configure-Composer-to-Support-SAML).

**Note:** JavaScript and HTML Source files used for embedding must be encoded in UTF-8 without BOM.

The same custom attribute key name must be defined and used in all the user definitions of the users expected to use this connection.

## Step 3: Define Connections Using User Attributes

**Define connections using user attributes**

1. Log in as an system admin.
2. Create or edit a connection using the connector you updated in [Step 1](#Step). See [Add Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932713955597-Add-Data-Store-Connections) and [Modify Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932714462221-Modify-Data-Store-Connections).
3. If a connection parameter is identified as a user attribute, up and down arrows appear in the connection parameter field on the Connections and Connection Details work areas. Use these arrows to select the custom attribute you want to use for the connection from list shown in the **Select Custom Attribute** drop-down menu.

   ![Select custom attributes you have defined in your environment to use in connections](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167973152781 "Connection Details work area")

   **Note:** 
   If the [connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector) associated with the connection type for the connection definition has **not** been defined with the **User Attribute** checkbox selected (the **User Attribute** checkbox *was* selected in [Step 1](#Step)) for the USER\_NAME or PASSWORD parameters, the Select Custom Attribute drop-down menu is not available and you must manually enter the custom attribute in `${User.<custom-attribute-name>}` format. See [Insert Variables for Connection Parameters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932732148493-Insert-Variables-for-Connection-Parameters). Note that the custom attributes in this case do not use the same format as when you select them from the drop-down menu.
4. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
5. Select **Save** to save the connection.
