---
title: "Insert Variables for Connection Parameters"
id: 43700993364749
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993364749-Insert-Variables-for-Connection-Parameters
updated_at: 2026-05-29T14:11:33Z
---

# Insert Variables for Connection Parameters

# Insert Variables for Connection Parameters

Variables can be inserted for any connection parameter in a connection definition. The variables are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your environment.

You can also specify user attributes for use in the connection parameters of a connection definition. See [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).

## Step 1: Define Custom Attributes for the Variables

A custom attribute must be defined for every variable you want to use. The only exceptions are the Composer context variables `${User.composerUserName}`, `${User.accountId}`, and `${User.credentials}`. These built-in attributes which automatically exist and can be used connect the currently logged in user.

You can define custom attributes in several ways:

* Individually for every user. If you use this method, the variable names must be the same for every user. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [Use Lightweight Directory Access Protocol (LDAP)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162285837-Use-Lightweight-Directory-Access-Protocol-LDAP) and [Configure Composer to Support SAML](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162439437-Configure-Composer-to-Support-SAML).

Details about specifying custom attribute values are provided in [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).

## Step 2: Define Connections Using Variables

**Define connections using variables**

1. Log in as an system admin.
2. Create or edit a connection definition. See [Add Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections) and [Modify Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections).
3. If custom attributes have been defined, they can be directly entered in a connection parameter field on the Connections page using the following syntax:

   ${User.<custom-attribute-name>}

   The same custom attribute key name must be defined and used in all the user definitions of the users expected to use this connection.

   For example:

   ![Define your custom attributes if defined in your environment](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242720703373 "Add Connection work area")

   **Note:** 
   If the [connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993403661-Define-a-New-Connector) associated with the connection type for the connection definition has been defined with the [**User Attribute** checkbox](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters) selected for the USER\_NAME or the PASSWORD parameters, a [custom user attribute](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes) **must** be defined for the user creating the connection and for any users using the connection. In this scenario, the Add Connection screen allows you to select the custom user attribute from a **Select Custom Attribute** drop-down menu, as shown below. Note that the custom attributes in this case are not shown using the same format as when you specify them manually. For complete information, see [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).

   ![Select custom attributes you have defined in your environment to use in connections](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242757613837 "Connection Details work area")
4. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
5. Select **Save** to save the connection.
