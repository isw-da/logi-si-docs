---
title: "Specify Custom User Attributes"
id: 4405850862359
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes
updated_at: 2021-09-21T01:26:32Z
---

# Specify Custom User Attributes

# Specify Custom User Attributes

You can define custom attributes for a user definition if you are logged in as a Composer account administrator or as a user who is assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

Custom attributes provide a way for administrators to store values that can be used as parameters, or variables, in [connection definitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters), [data source row security filters](https://devnet.logianalytics.com/hc/en-us/articles/4405859332631-Insert-Variables-for-Row-Security-Restriction-Filters), and in [custom SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab).

A primary use of custom attributes is for user credential pass-through. This means that if users have access to a particular data source that has been connected to Composer, their credentials can be saved on this page so that their access privileges are maintained for that source within Composer.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) User attributes set in regular Composer user definitions via the UI or in LDAP user definitions are encrypted when stored in metadata. To specify the encryption mode, see [*Change the Encryption Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode).

Custom attributes are defined using the **Custom Attributes** tab in the user definition editor.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743941271/user-custom-attr_480x306.png)

When custom attributes are referenced in connection definitions, action URLs, attribute definitions, or data source custom SQL, they take the form: `${User.<custom-attribute-name>}`.

Custom attributes can also be specified dynamically in the LDAP or SAML configurations for your Composer instance. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer) and [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).

This section covers the following topics:

* [*Supplied Context Variables*](#Supplied)
* [*Adding a Custom Attribute in a User Definition*](#Adding)
* [*Removing a Custom Attribute from a User Definition*](#Removing)
* [*Specifying Multivalue (Array) Custom Attributes*](#Specifyi)
* [*Specifying Numeric Values in Custom Attributes*](#Specifyi2)
* [*Specifying Time Values in Custom Attributes*](#Specifyi3)

## Supplied Context Variables

The following context variables are provided with Composer.

* `${User.composerUserName}` can be used to insert the name of the user that is currently logged in.
* `${User.accountId}` can be used to insert the account ID of the user that is currently logged in.

You do not need to create custom user attributes for the user name or account ID.  Use these supplied context variables instead.

## Adding a Custom Attribute in a User Definition

To add a custom attribute to a user definition:

1. Access the **Custom Attributes** tab for the user definition. See [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850861463-Add-User-Definitions) or [*Modify User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859121047-Modify-User-Definitions).
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743941527/add-cust-attr-btn_151x24.png). A blank line is added to the Custom Attributes tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747460503/custom-attr-tab_480x307.png)
3. Supply values for the attribute, as described in the following table.

   | Tab Field | Description |
   | --- | --- |
   | **Key** | Specify the name of the custom attribute in Composer displays. The name cannot include braces. |
   | **Value** | Specify one or more values for the custom attribute. See [*Specifying Multivalue (Array) Custom Attributes*](#Specifyi), [*Specifying Numeric Values in Custom Attributes*](#Specifyi2), and [*Specifying Time Values in Custom Attributes*](#Specifyi3). |
   | **Usage** | Shows how the attribute appears in text entry fields of the Composer application. |
   | **Secure** | Select this checkbox if you want to encrypt the custom attribute values. |
   | **Delete** | Select  to remove the attribute. |
4. When all values have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747458071/save-blue-supervisor-btn_63x22.png) to save the user definition.

## Removing a Custom Attribute from a User Definition

To remove a custom attribute from a user definition:

1. Access the **Custom Attributes** tab for the user definition. See [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850861463-Add-User-Definitions) or [*Modify User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859121047-Modify-User-Definitions).

   The defined custom attributes are listed.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743941911/delete-black-x_14x14.png) corresponding to the attribute you want to remove.
3. When all attributes have been updated (or removed), as necessary, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747458071/save-blue-supervisor-btn_63x22.png) to save the user definition.

## Specifying Multivalue (Array) Custom Attributes

For multivalue user attributes (arrays), the elements must be comma-separated and contain no redundant white spaces between elements. These multivalue custom attributes should only be used as arrays in INCLUDE and EXCLUDE filter operations. With all other filter operations, the custom attribute values are used as-is. For example, an INCLUDE or EXCLUDE row security filter that uses a multivalue custom attribute containing the array (["apples", "oranges", "bananas"]) will interpret the values as three separate values, splitting the values on commas. However, an EQUAL or NOT EQUAL row security filter using the same multivalue custom attribute would interpret the array values as a single value ("apples,oranges,bananas").

Null values in multivalue custom attributes are processed as a special text marker - [Null].

## Specifying Numeric Values in Custom Attributes

Numeric value in custom attributes are supported as integers or floating-point values represented as text.

## Specifying Time Values in Custom Attributes

For date-time values, the following formats are supported:

* ISO-8601 format with optional milliseconds (but no timezone): `yyyy-MM-ddTHH:mm:ss[.SSS]`
* Composer's default API time format: `yyyy-MM-dd HH:mm:ss.SSS`, milliseconds required.

Unix time stamp format (seconds/milliseconds) is not supported for date-time values

The BETWEEN filter operator expects an array with two elements. When you use a time-value custom attribute as a filter variable for a filter using BETWEEN, two explicit elements must be specified (for example `start_date` and `end_date`). The dates can be specified as static date-time values, dynamic time patterns, or single-value user attributes. Specifications such as `[${User.date_array}]`, with the `date_array` attribute containing two elements are not supported.
