---
title: "Insert Variables for Row Security Restriction Filters"
id: 4405859332631
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859332631-Insert-Variables-for-Row-Security-Restriction-Filters
updated_at: 2021-09-21T01:28:22Z
---

# Insert Variables for Row Security Restriction Filters

# Insert Variables for Row Security Restriction Filters

Variables can be inserted as values for any restriction filter in a row security definition. The variables are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your Composer installation.

* [*Step 1: Define Custom Attributes for the Variables*](#DefCustAttr)
* [*Step 2: Using Variables in Row Security*](#Step2)

You can also specify user attributes for use in the connection parameters of a connection definition. See [Use User Attributes for Connection Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If a variable is used in a row security definition, but a corresponding custom attribute is not defined for the user, an error message appears when the user attempts to view a dashboard on which the row security is applied.

## Step 1: Define Custom Attributes for the Variables

A custom attribute must be defined for every variable you want to use. The only exceptions are the Composer context variables `${User.composerUserName}` and `${User.accountId}`, which automatically exist and can be used to insert the name or account ID of the user that is currently logged in.

You can define custom attributes in several ways:

* Individually for every user definition. If you use this method, the variable names must be the same for every user. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer) and [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).

Details about specifying custom attribute values are provided in [Specify Custom User Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).

## Step 2: Using Variables in Row Security

To use variables in row security:

1. Log into Composer as a Composer administrator, a user in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) *and* who also has **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.
2. Follow the instructions in [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security) to add or modify a row security definition. When you get to the step where you select values for the restriction filter, specify the custom attribute (variable) you defined in Step 1 as a value for the filter. If custom attributes are defined, they can be directly entered using the following syntax:

   ```
   ${User.<custom-attribute-name>}
   ```
3. Save the row security definition and close the Row Security dialog, as described in [Restrict Access to Data Using Row Security](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).

## Row Security Filter Errors

When a custom user attribute, used as a variable in a row security filter, is invalid (for example, it cannot be parsed as a value of a required type), a generic error message is given and a detailed message is logged describing what is wrong with the row security filter.
