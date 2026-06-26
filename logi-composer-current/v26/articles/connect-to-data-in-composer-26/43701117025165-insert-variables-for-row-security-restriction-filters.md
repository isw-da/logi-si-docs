---
title: "Insert Variables for Row Security Restriction Filters"
id: 43701117025165
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117025165-Insert-Variables-for-Row-Security-Restriction-Filters
updated_at: 2026-05-29T14:08:28Z
---

# Insert Variables for Row Security Restriction Filters

# Insert Variables for Row Security Restriction Filters

Variables can be inserted as values for any restriction filter in a row security definition. The variables are passed to the connection string via custom attributes specified in the user definition or dynamically in the custom attributes specified in the SAML or LDAP configurations for your Composer installation.

You can also specify user attributes for use in the connection parameters of a connection definition. See [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).

**Note:** 
If a you use a variable in a row security definition, but don't define a corresponding custom attribute the user, an error message appears when the user attempts to view a dashboard on which the row security is applied.

## Step 1: Define Custom Attributes for the Variables

A custom attribute must be defined for every variable you want to use. The only exceptions are the Composer context variables `${User.composerUserName}`, `${User.accountId}`, and `${User.credentials}`. These built-in attributes which automatically exist and can be used connect the currently logged in user.

You can define custom attributes in several ways:

* Individually for every user. If you use this method, the variable names must be the same for every user. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).
* Dynamically in the LDAP or SAML configurations for your Composer instance. See [Use Lightweight Directory Access Protocol (LDAP)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162285837-Use-Lightweight-Directory-Access-Protocol-LDAP) and [Configure Composer to Support SAML](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162439437-Configure-Composer-to-Support-SAML).

Details about specifying custom attribute values are provided in [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).

## Step 2: Using Variables in Row Security

**Use variables in row security**

1. Log into Composer as a user in a group that has been granted the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) *and* who also has **read** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Follow the instructions in [Restrict Access to Data Using Row Security](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069473293-Restrict-Access-to-Data-Using-Row-Security) to add or modify a row security definition. When you get to the step where you select values for the restriction filter, specify the custom attribute (variable) you defined in Step 1 as a value for the filter. If custom attributes are defined, they can be directly entered using the following syntax:

   ${User.<custom-attribute-name>}
3. Save the row security definition and close the Row Security dialog, as described in [Restrict Access to Data Using Row Security](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069473293-Restrict-Access-to-Data-Using-Row-Security).

## Row Security Filter Errors

When a custom user attribute, used as a variable in a row security filter, is invalid (for example, it cannot be parsed as a value of a required type), a generic error message is given and a detailed message is logged describing what is wrong with the row security filter.
