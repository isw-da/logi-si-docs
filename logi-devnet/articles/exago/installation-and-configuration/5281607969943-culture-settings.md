---
title: "Culture Settings"
id: 5281607969943
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281607969943-Culture-Settings
updated_at: 2024-04-03T09:03:33Z
---

# Culture Settings

# Culture Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Culture Settings**.

---

## Introduction

The **Culture Settings** give administrators control over formats and symbols that vary amongst geographic location. These settings can be overwritten for a specific user or group of users by modifying the Role. See [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles).

## Settings

The following settings are available:

### Date Format

The format of date values. May be any .NET standard (for example, *MM/dd/yyyy*).

### Time Format

The format of time values. May be any .NET standard (for example, *h:mm:ss tt*).

### DateTime Format

The format of date-time values. May be any .NET standard (for example *M/d/yy h:mm tt*).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> For more information on .NET Date, Time, and DateTime format strings please visit [this MSDN topic](http://msdn.microsoft.com/en-us/library/8kb3ddd4%28v=vs.71%29.aspx).

### Date Time Values Treated As

Choose to format DateTime as Date or DateTime values. To change this setting for specific columns see [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Column metadata overrides culture settings.

### Numeric Separator Symbol

Symbol used to separate 3 digit groups (ex. thousandths) in numeric values. The default is a comma (,).

### Numeric Currency Symbol

Symbol prefixed to numeric values to represent currency. The default is the US currency symbol ($).

### Numeric Decimal Symbol

Symbol used for numeric decimal values. The default is a period (.).

### Numeric Decimal Places

The default number of decimal places to show when a cell format is set to display a **Number** or when column metadata or the data source identifies the value is a number data type. This value is also the default value presented to users in the [Report Designer Cell Formatting dialog](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting). Default is *-1* which will show two decimal places. Values between -1 and 8 are accepted.

### Currency Decimal Places

The default number of decimal places to show when a when column metadata or the data source identifies the value is a currency data type. Default is *-1* which will show two decimal places. Values between -1 and 8 are accepted.

### Apply Numeric Decimal Places to General Cell Formatting

Set to true to apply the Numeric Decimal Places to any cell that has Cell Formatting set to General but contains a number. Default value is *false*.

### Apply General Currency Right Alignment

Set to true to cause currency values to appear right-aligned by default in report cells.

### Server Time Zone Offset

A decimal value used to convert server to client time (the negation is used to convert client to server time). This offset is not applied to data coming from Data Sources. It is utilized by Exago features like the Scheduler Service. Set to *0* to use server time or null to use the External Interface (a deprecated extensibility feature) to calculate the time zone change. This value should be set to *0* if a **Time Zone Name** is selected.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> A **Server Time Zone Offset** is only required if a **Client Time Zone Name** cannot be provided. Otherwise, all scheduling calculations will be performed using the provided time zone information.

### Time Zone Name

Default geopolitical location of the client as determined by the IANA time zone database (for example, America/New\_York). Utilized by Exago to properly resolve scheduling issues centering around DST and other non-linear time zone conflicts. The setting is also used for other time and date related features in the application such as Date/Time functions like Now().

For a full list of official IANA time zones and their relative UTC offsets, see [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on Wikipedia.
