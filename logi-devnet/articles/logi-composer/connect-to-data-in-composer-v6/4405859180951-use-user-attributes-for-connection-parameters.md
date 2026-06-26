---
title: "Use User Attributes for Connection Parameters"
id: 4405859180951
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters
updated_at: 2021-09-21T01:27:08Z
---

# Use User Attributes for Connection Parameters

# Use User Attributes for Connection Parameters

User attributes (variables) can be used for the connection parameters in a connection definition. Attributes can be defined for the full connection string, the host name, the port number, the cluster name, the user name, or the password, and any other parameters supported by the connector. The attributes are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your Composer installation. This topic describes how to set up this functionality.

* [*Step 1: Review and Select Connector Parameters for Which Attributes Can Be Used*](#Step)
* [*Step 2: Define Custom Attributes*](#Step2)
* [*Step 3: Define Connections Using User Attributes*](#Step3)

You can also insert variables directly in the connection parameters of a connection definition. See [*Insert Variables for Connection Parameters*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919063-Insert-Variables-for-Connection-Parameters).

## Step 1: Review and Select Connector Parameters for Which Attributes Can Be Used

To review and select connector parameters for which user attributes can be used:

1. Log into Composer as a supervisor.
2. Select **Connectors** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Manage Connector Services page appears.
3. In the Connectors section of the page, select the connector whose parameters you want to review. Alternatively, you can create a new connector definition and review and modify the parameters in the new definition. See [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector).

   Either the Edit Connector or the Create New Connector page for the connector appears.
4. Review the connector parameters that appear at the bottom of the Edit Connector or Create New Connector page.
5. If you want to be able to select a custom attribute as the value for a connection parameter, make sure the **User Attribute** checkbox is selected.

   In the following Elasticsearch connector definition, the User Attribute checkbox is selected for the USER\_NAME and PASSWORD parameters. The user definitions in this Composer instance must include custom attributes for these parameters (see [Step 2](#Step2)) and the connection definitions for this Elasticsearch connector must select the appropriate custom attributes as user credentials (see [Step 3](#Step3)).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743922455/connector-parms_768x221.png)
6. Alter the other connector parameters, as needed.

   * If a connector parameter is required, make sure its **Required** checkbox is selected. Depending on the connector server, some parameters are already selected because they are required.
   * If a connector parameter should be visible (especially if the parameter is required) when the connection definition is created, make sure its **Visible** checkbox is selected.

   For information about all connector parameters, see [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector).
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png) to save the connector parameters.

## Step 2: Define Custom Attributes

A custom attribute must be defined for every connector parameter for which you selected the **User Attribute** checkbox in [Step 1](#Step). The only exceptions are the Composer context variables `${User.composerUserName}` and `${User.accountId}`, which automatically exist and can be used to insert the name or account ID of the user that is currently logged in.

You can define custom attributes in several ways:

* Individually for every user definition that will need to create data sources from a connection or will need to create connections using the connector. If you use this method, the variable names must be the same for each user. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer) and [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).

The same custom attribute key name must be defined and used in all the user definitions of the users expected to use this connection.

## Step 3: Define Connections Using User Attributes

To define connections using user attributes:

1. Log into Composer as an administrator.
2. Create or edit a connection using the connector you updated in [Step 1](#Step). See [*Add Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859165335-Add-Data-Store-Connections) and [*Modify Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859167767-Modify-Data-Store-Connections).
3. If a connection parameter is identified as a user attribute, up and down arrows appear in the connection parameter box on the Connections page. Use these arrows to select the custom attribute you want to use for the connection from the Select Custom Attribute drop-down menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743922199/add-connection-usrattr_768x295.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the [connector](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector) associated with the connection type for the connection definition has **not** been defined with the **User Attribute** checkbox selected (the **User Attribute** checkbox *was* selected in [Step 1](#Step)) for the USER\_NAME or PASSWORD parameters, the Select Custom Attribute drop-down menu is not available and you must manually enter the custom attribute in `${User.<custom-attribute-name>}` format. See [*Insert Variables for Connection Parameters*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919063-Insert-Variables-for-Connection-Parameters). Note that the custom attributes in this case do not use the same format as when you select them from the drop-down menu.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747451799/validate-btn.png) to validate the connection. If the connection is valid, it is saved.
