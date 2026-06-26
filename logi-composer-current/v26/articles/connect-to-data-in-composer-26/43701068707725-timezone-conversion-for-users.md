---
title: "Timezone Conversion for Users"
id: 43701068707725
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068707725-Timezone-Conversion-for-Users
updated_at: 2026-05-29T14:11:04Z
---

# Timezone Conversion for Users

# Timezone Conversion for Users

Displaying the source data in dashboards and visualizations in the timezone of individual users instead of the default timezone stored at the source. Additionally, you can convert a `TIME` field to a custom timezone.

**Note:** 
If you are upgrading from an earlier version of Logi Composer, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute. See [Upgrade Workflow](#Upgrade).

The functionality is available in the following data sources and for the data stored in the UTC timezone:

* MS SQL
* Snowflake
* MongoDB
* BigQuery
* Hive
* SparkSQL
* Impala
* PostgreSQL
* Redshift

## Enable `TIME` Conversion To User Timezones

Before you convert a `TIME` field for use by users, define their timezone in user regional settings. Next, convert the `TIME` field in the source.

### Define a User's Timezone

1. Log in as an administrator or a user who has been assigned to a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [Switch Tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052090125-Switch-Tenants).
2. Select **Users and Groups** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243253187981)). The Users and Groups page work area opens.
3. Select **Users** to see a list of all the user definitions that have been defined for the account.
4. Select a user, then select the **Regional Settings** tab.
5. Select the **Time Zone** for the user from the options available in the drop-down selector.
6. Select **Save** to save the user definition.

### Convert a `TIME` Field of a Source

When you convert field, your software creates a derived field that includes the `User.timeZone` system attribute used as an interpolated value, for example `to_timezone(TIME_field, '${User.timeZone|UTC}'))`. Use the created derived field in dashboards and visualizations. The data will be recalculated using the account of each individual user with the custom timezone.

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243253187981)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. Select a source to open it, then select a time field in the **Fields** tab.
4. Select the **Settings**sidebar menu, then select **Convert** and the **Convert to User Timezone** option to convert the data type. A field conversion modal window opens.
5. In the Time to Time Zone Conversion work area, define a **Label** for the newly created field, then select **User Time Zone** for the Time Zone field if not already selected.
6. Select **Save** to create the new field.

### Alternative: Convert a Timezone Once Using a Function

You can convert a field with the `TIME` data type into a selected timezone manually using the `to_timezone` function. Specify the function as shown below to return static timezone conversion.

| Syntax | Example | Use Case |
| --- | --- | --- |
| `to_timezone(TIME_field, 'IANA timezone identifier')` | `to_timezone(TIME_field, 'Europe/Kyiv')` | Converts a field `TIME_field` from its UTC stored timezone to the selected timezone, `Europe/Kyiv`. |

**Important:** 
Conversion is available only for `TIME` fields stored in the UTC timezone at the data source. Conversions performed on the data stored in a custom timezone may be inaccurate.

## Upgrade Workflow

If you are upgrading from an earlier version of Logi Composer, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute.

When you upgrade to the latest version of Logi Composer this feature triggers the following changes:

* Custom user attributes you manually created with the name the `User.timeZone` in earlier Logi Composer versions (23.2 and earlier) are automatically converted to the system attributes if their value corresponds to the IANA timezone standard ISO 8601 (for example, `‘Europe/Kyiv’, ‘UTC+5’`).
* All custom user attributes `User.timeZone` that do not correspond to the IANA timezone standard are removed.

To ensure a smooth upgrade process, select an upgrade workflow ahead of updating Logi Composer depending on your needs:

* If you want to start using your custom attribute `User.timeZone` for timezone conversion purposes, the attribute will be automatically changed to the system value at upgrade. To ensure this takes place, verify before upgrade that the values of the attribute are provided in IANA format before you upgrade Logi Composer.
* If you want to preserve your custom attribute for other purposes, we recommend renaming the attribute before you upgrade Logi Composer. For example, change `User.timeZone` to `User.timeZone_custom`. Don't change the value of the attributes before running the upgrade script.

## API Changes

The APIs in `/api/users` has been expanded to include the `"timeZone": "string"` parameter. This displays the user's timezone formatted as an IANA timzeone identifier, ISO 8601 (for example, "Europe/Kyiv"). The default value is `UTC`.

**Important:** `User.timeZone` is now a reserved system attribute to support this feature. See [Upgrade Workflow](#Upgrade) for alternative approaches.

### Payload Changes

#### Logi Composer v23.2 and earlier:

{
"id": "string",
"fullname": "string",
"email": "string",
"accountId": "string",
"name": "string",
"password": "string",
"localeSettingsId": "string",
"languageLocaleId": "string"
}

#### Logi Composerv23.3 and later:

{
"id": "string",
"fullname": "string",
"email": "string",
"accountId": "string",
"name": "string",
"password": "string",
"localeSettingsId": "string",
"languageLocaleId": "string",
"timeZone": "Europe/Kyiv"
}
