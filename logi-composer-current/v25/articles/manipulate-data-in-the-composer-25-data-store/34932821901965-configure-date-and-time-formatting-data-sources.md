---
title: "Configure Date and\u00a0Time Formatting  - Data Sources"
id: 34932821901965
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821901965-Configure-Date-and-Time-Formatting-Data-Sources
updated_at: 2026-05-26T22:09:52Z
---

# Configure Date and Time Formatting  - Data Sources

# Configure Date and Time Formatting - Data Sources

As a user with [data source privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), configure date and time for Time fields in a data source at creation, or later when you edit an existing source. This defines the default format for time fields as displayed in visuals, data details of visuals, and sample format fields for consistency across your organization.

There are three places to control the format of date and time information.

* Set the locale for users to display the appropriate order of fields, based on a user's geographical location. For example, users based in the United States and users based in Italy see different date order formats due to the local formatting of the fields. To define the location settings for users within your environment, ask your administrator or see [Specify A User's Regional Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932610886157-Specify-A-User-s-Regional-Settings).
* Configure the formats for Time fields in a data source configuration, as described in the rest of this topic. The order dates and times are presented in depend on the region (location) settings for your environment: you're changing the format of each time or date field to suit your organization's needs.
* Finally, you can [enable users to override the formatting](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933282294029-Control-How-Users-Interact-With-a-Visual) you've defined at the data source and for most visuals at the visual level. Find more visual formatting information in the following topics:
  + [Configure Date and Time Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263048077-Configure-Date-and-Time-Formatting-for-Visuals)
  + [Configure Number Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933278713485-Configure-Number-Formatting-for-Visuals)
  + [Format Time Table Data Using the Table Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933253788173-Format-Time-Table-Data-Using-the-Table-Context-Menu)
  + [Format Numeric Table Data Using the Table Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933268999949-Format-Numeric-Table-Data-Using-the-Table-Context-Menu)
  + [Available Visual Types](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933207922445-Available-Visual-Types)

**Note:** 
If you change the format for dates and times for a field used by current visuals in your data source, the formats used in the visual reflect those changes. If you adjust the granularity of a field in your data source, the change is reflected in the granularity modal of the visual after the change.

**Specify the format for Time fields in a data source configuration**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or write permission for this source.
2. Select **Sources** on the UI menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167930746381)). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. Select to edit the appropriate data source configuration, and switch to the [**Fields** tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields).
4. Locate the time field you want to modify. The **Data Type** column on the **Fields** tab must define the field as a **Time** field.
5. In the Settings sidebar menu, select the edit (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167940857485)) button to open the **Format** work area.

   ![Set the format options for your data source date and time](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167319545485 "Format date and time work area")

Not all fields may be available for all time formats.

| Format Option | Description |
| --- | --- |
| Year | Select **None**, **Numeric** (2024), **2-Digit** (24), **Narrow**, or **Short**. |
| Day Of Year | Select **None** or **Short**. |
| Quarter | Select **None**, **Range**, **Narrow**, **Numeric** (1-4), or **2-Digit** (01-04). Selections for Quarter are applied only if the time granularity is set to Quarter. Not all options may be available for all time fields. |
| Month | Select **None**, **Numeric** (1-12), **2-Digit** (01-12), **Long** (January, March), **Short** (Jan, Mar), or **Narrow** (J, M). |
| Week | Select **None**, **WeekStart**, **WeekEnd**, **Range**, **Narrow** (w1-w53), **Numeric** (1-53), or **2-Digit** (01-53). |
| Weekday | Select **Long** (Friday, Sunday), **Short** (Fri, Sun), **Narrow** (F, S), or **None**. The default is **None**, to show no day of the week. |
| Day | Select **None**, **Numeric** (1-7), **2-Digit** (01-07), **Narrow**, or **Short**. |
| Hour | Select **Numeric** (1-24) or **2-Digit** (01-24). |
| Hour12 | Select a 12 or 24 hour format option for Hour12.   * **Auto** displays the hour format defined in the source data. * **True** overrides the source format, displaying the hours in 12 hour format, with an appended **AM** or **PM**. * **False** overrides the source format, displaying the hours in 24 hour format. |
| Minute | Select **Numeric** (0-59) or **2-Digit** (00-59). |
| Second | Select **Numeric** (0-59) or **2-Digit** (00-59). |

6. The changes you make are reflected in the **Sample Date** preview field.
7. When you are finished formatting your date and time values, select **Apply** and examine your updates. If they are correct, select **Save** to save these changes to the source.
