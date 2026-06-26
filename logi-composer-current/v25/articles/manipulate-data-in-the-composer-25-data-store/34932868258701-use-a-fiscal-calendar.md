---
title: "Use a Fiscal Calendar"
id: 34932868258701
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868258701-Use-a-Fiscal-Calendar
updated_at: 2026-05-26T22:07:06Z
---

# Use a Fiscal Calendar

# Use a Fiscal Calendar

**Note:** 
Fiscal Calendars functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.

**Important:** This is an experimental feature.

After a user with appropriate privileges has [defined one or more fiscal calendars](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932899325325-S-Define-a-Fiscal-Calendar) to your environment, you can use these calendars in any of your sources.

**Select an alternative calendar**

1. Open and [edit an existing source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890384781-Edit-a-Data-Source) or create a [new source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source).
2. Navigate to the [Global Settings tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab) and select an available calendar listed under **Alternative Calendars Settings**.

   **Note:** The default calendar is used for all sources unless you specifically select an alternative calendar.
3. Select one or more calendars for your source as needed. Clear the checkbox for a calendar to not use that specific calendar with this source and prevent fiscal time field conversion.
4. After completing your changes, select **Save Settings** to make available your selected calendars to new and existing visuals that use this source.

**Create a Time (FISCAL) field for your selected calendar**

1. After you have [selected one or more calendars](#select) for your source, navigate to the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) to convert a time field to a time field that uses one of the calendars you have added to this source.
2. Select the time field you want to use in the list of available fields.
3. Select the **Convert** option in the Data Details work area on the Settings tab. Select the option presented, **Convert to Fiscal Time** to open a conversion dialog.
4. Enter a **Label** for the new derived field, and select a **Fiscal Calendar** from the list of available options. **Save** your changes.
5. Your new derived field is added to the list of available fields with a data type of **Time (Fiscal)**. It is similar to standard time fields, with the exception that you cannot define a **Time Zone** for this new derived field.

**Note:** Alternatively, you can select **Add Derived Field** from the Fields tab and create the field using the `to_chrono_datetime` function. Include the `calendar_id` and `dateTime` field in the editor.

Once created, you can use this new field in visuals, expressions, filters, and using presets as needed.

* Objects that use a fiscal time field are marked with a **FISCAL** indicator.

* When you export data that relies on fiscal calendars, the data is presented in the appropriate date and time format.
* If you remove an alternative calendar from your source, you cannot make new derived fields based on that calendar.
