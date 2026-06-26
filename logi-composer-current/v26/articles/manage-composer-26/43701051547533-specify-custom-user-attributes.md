---
title: "Specify Custom User Attributes"
id: 43701051547533
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes
updated_at: 2026-05-29T14:07:07Z
---

# Specify Custom User Attributes

# Specify Custom User Attributes

You can define custom attributes for a user's definition if you are logged in as a Logi Composer system administrator, tenant administrator, or a user who is assigned to a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

Use custom attributes to store values that can be used as [parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters), or variables, in [connection definitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters), data source [row security filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117025165-Insert-Variables-for-Row-Security-Restriction-Filters), and in [custom SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#Custom).

A primary use of custom attributes is for user credential pass-through. Add credentials to a user's custom attributes so users with access to a particular data source connected to your instance can use these saved credentials to maintain access privileges for that source within Logi Composer.

**Note:** User attributes set for users via the UI or using LDAP user definitions are encrypted when stored in metadata. To specify the encryption modes, see [Change the Encryption Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode).

Custom attributes are defined using the **Custom Attributes** tab when you edit the user.

When you reference custom attributes in connecton definitions, action URLs, attribute definitions, or a data source's custom SQL, they take the form of `${User.<custom-attribute-name>}`.

This section covers the following topics:

* [Supplied Context Variables](#Supplied)
* [Add A Custom Attribute for a User](#Add)
* [Remove a Custom Attribute from a User](#Remove)
* [Specify Multivalue (Array) Custom Attributes](#Specify)
* [Specify Numeric Values in Custom Attributes](#Specify2)
* [Specify Time Values in Custom Attributes](#Specify3)

## Supplied Context Variables

The following context variables are provided with Logi Composer.

* `${User.composerUserName}`: include to insert the name of the user who is currently logged in.
* `${User.accountId}`: include to insert the user account ID of the user who is currently logged in.
* `${User.credentials}`: include to pass the session ID or trusted access token (in embedded environments) of the user.

You do not need to create custom user attributes for the user name or account ID. Use these supplied context variables instead.

## Add A Custom Attribute for a User

**Add a custom attribute for a user**

1. Access the Custom Attributes tab for the user. See [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users) or [Modify Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021873037-Modify-Users).
2. Select Add Custom Attribute. A blank line is added to the Custom Attributes tab.
3. Supply values for the attribute, as described in the following table:

   | Tab Field | Description |
   | --- | --- |
   | Key | Specify the name of the custom attribute. The name cannot include braces. |
   | Value | Specify one or more values for the custom attribute. See below for more options. |
   | Usage | Shows how the attribute appears in the text entry fields of the application. |
   | Secure | Select this checkbox if you want to encrypt the custom attribute values. |
   | Delete | Select the delete button to remove the attribute. |
4. When you have specified all values, select **Save** to save the user.

## Remove a Custom Attribute from a User

**Remove a custom attribute from a user**

1. Access the Custom Attributes tab for the user. See [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users) or [Modify Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021873037-Modify-Users). The defined custom attributes are listed.
2. Select the delete button corresponding to the attribute you want to remove.
3. When are done removing your specific attributes, select **Save** to save the user.

## Specify Multivalue (Array) Custom Attributes

For multivalue user attributes (arrays), the elements must be comma-separated and contain no redundant white spaces between elements. These multivalue custom attributes should only be used as arrays in INCLUDE and EXCLUDE filter operations. With all other filter operations, the custom attribute values are used as-is.

For example, an INCLUDE or EXCLUDE row security filter that uses a multivalue custom attribute containing the array (`["apples", "oranges", "bananas"]`) will interpret the values as three separate values, splitting the values on commas.

However, an EQUAL or NOT EQUAL row security filter using the same multivalue custom attribute would interpret the array values as a single value (`"apples,oranges,bananas"`).

Null values in multivalue custom attributes are processed as a special text marker - `[Null]`.

## Specify Numeric Values in Custom Attributes

Numeric value in custom attributes are supported as integers or floating-point values represented as text.

## Specify Time Values in Custom Attributes

For date-time values, the following formats are supported:

* ISO-8601 format with optional milliseconds (but no timezone): `yyyy-MM-ddTHH:mm:ss[.SSS]`
* Logi Composer's default API time format: `yyyy-MM-dd HH:mm:ss.SSS`, milliseconds required.

Unix time stamp format (seconds/milliseconds) is not supported for date-time values.

The BETWEEN filter operator expects an array with two elements.

When you use a time-value custom attribute as a filter variable for a filter using BETWEEN, two explicit elements must be specified (for example `start_date` and `end_date`). The dates can be specified as static date-time values, dynamic time patterns, or single-value user attributes.

Specifications such as `[${User.date_array}]`, with the `date_array` attribute containing two elements are not supported.
