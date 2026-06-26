---
title: "Insert Variables for Connection Parameters"
id: 4405850919063
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850919063-Insert-Variables-for-Connection-Parameters
updated_at: 2021-09-21T01:27:09Z
---

# Insert Variables for Connection Parameters

# Insert Variables for Connection Parameters

Variables can be inserted for any connection parameter in a connection definition. The variables are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your Composer installation.

* [*Step 1: Define Custom Attributes for the Variables*](#DefCustAttr)
* [*Step 2: Define Connections Using Variables*](#Step2)

You can also specify user attributes for use in the connection parameters of a connection definition. See [Use User Attributes for Connection Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters).

## Step 1: Define Custom Attributes for the Variables

A custom attribute must be defined for every variable you want to use. The only exceptions are the Composer context variables `${User.composerUserName}` and `${User.accountId}`, which automatically exist and can be used to insert the name or account ID of the user that is currently logged in.

You can define custom attributes in several ways:

* Individually for every user definition. If you use this method, the variable names must be the same for every user. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer) and [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).

Details about specifying custom attribute values are provided in [Specify Custom User Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).

## Step 2: Define Connections Using Variables

To define connections using variables:

1. Log into Composer as an administrator.
2. Create or edit a connection definition. See [*Add Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859165335-Add-Data-Store-Connections) and [*Modify Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859167767-Modify-Data-Store-Connections).
3. If custom attributes have been defined, they can be directly entered in a connection parameter box on the Connections page using the following syntax:

   ```
   ${User.<custom-attribute-name>}
   ```

   The same custom attribute key name must be defined and used in all the user definitions of the users expected to use this connection.

   For example:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743921943/add-connection-usrattr1_384x494.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the [connector](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector) associated with the connection type for the connection definition has been defined with the [**User Attribute** checkbox](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters) selected for the USER\_NAME or the PASSWORD parameters, a [custom user attribute](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes)**must** be defined for the user creating the connection and for any users using the connection. In this scenario, the Add Connection screen allows you to select the custom user attribute from a **Select Custom Attribute** drop-down menu, as shown below. Note that the custom attributes in this case are not shown using the same format as when you specify them manually. For complete information, see [*Use User Attributes for Connection Parameters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743922199/add-connection-usrattr_768x295.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747451799/validate-btn.png) to validate the connection. If the connection is valid, it is saved.
