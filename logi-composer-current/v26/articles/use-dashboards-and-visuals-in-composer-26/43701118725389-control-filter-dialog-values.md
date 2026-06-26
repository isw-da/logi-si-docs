---
title: "Control Filter Dialog Values"
id: 43701118725389
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118725389-Control-Filter-Dialog-Values
updated_at: 2026-05-29T14:10:52Z
---

# Control Filter Dialog Values

# Control Filter Dialog Values

You can control the behavior of filter dialogs by data source. These controls are set on the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) of the [data source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [Control Attribute Field Filters](#ctrl001).
* For number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [Control Number Field Filters](#ctrl002).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [Control Time Field Filters](#ctrl003).

**Note:** In this release, the user interface and workflows have changed from previous releases. If you are running an earlier release, see [Filters in Earlier Releases](#v25.3).

## Control Attribute Field Filters

**Control attribute field filters**

1. Edit the data source for which you want to control attribute field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the Output in your source, then **Expand View** of the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) to access the Filter Values panel.
3. Locate your field (Data Type: Attribute) and select it.
4. Select (check) **Only Allow Custom Values** in the sidebar menu.
5. When your changes are complete, select **Save**.

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data on the visual by the attribute. You will be required to enter the values to filter. Add at least one value or custom value for the attribute to the filter.

![Use to select values, wildcard, or keyset filter information](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242542679437 "Filter Values Select Values work area")

**Add a value**

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.
2. Type a value into the search box and select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243232600589 "add icon"). Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   ![Enter a value, such as rings, to add](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242533271309 "Filter Values Select Values work area")
3. The value is added to the list of selected values.

   ![Review your included values, deselect or remove if needed](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242542899597 "Filter Values Select Values work area")
4. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   For more information about setting attribute filters, see [Set an Attribute Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133345293-Set-an-Attribute-Filter).

## Control Number Field Filters

**Control number field filters**

1. Edit the data source for which you want to control number field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the Output in your source, then **Expand View** of the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) to access the Filter Values panel.
3. Locate your field (Data Type: Number) and select it.
4. Select to enable **Custom Range** in the Filter Values panel.
5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **Min** and **Max** boxes or use the arrows in the boxes to increment and decrement the values.

   **Note:** Custom range values can be numbers or numbers with scientific notation.
6. Select **Save** to apply the custom filter range.

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the number field you specified a custom range for. The values show as default in the filter are the custom range you specified in the data source configuration.

![Define your range of values here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242543002253 "select values filter work area")

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

For more information about setting numeric filters, see [Set a Numeric Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter).

## Control Time Field Filters

**Control the default time field filter and time bar ranges**

1. Edit the data source for which you want to control time field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the Output in your source, then **Expand View** of the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) to access the Filter Values panel.
3. Locate your field (Data Type: Time) and select it.
4. Change **Source of Filter Values** to **Static Overrid**e to enable Custom Range in the Filter Values panel.
5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   ![select a date and time for your filter](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242519248781 "calendar popup")
6. Select **Save** to apply the custom filter range.

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [Set a Time Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter).

![Set the start and end time of your data set for this filter](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242522216845 "select values time range")

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

## Filters in Earlier Releases

You can control the behavior of filter dialogs by data source. These controls are set on the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) of the [data source configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [Controlling Attribute Field Filters](#Controll).
* For number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [Controlling Number Field Filters](#Controll2).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [Controlling Time Field Filters](#Controll3).

### Controlling Attribute Field Filters

**Control attribute field filters**

1. Edit the data source configuration for which you want to control attribute field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) in the data source work area.
3. Locate the attribute field in the field table on the Fields tab.
4. Select (check) **Only Allow Custom Values** in the sidebar menu.
5. When your changes are complete, select **Save**.

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data on the visual by the attribute. You will be required to enter the values to filter. Add at least one value or custom value for the attribute to the filter.

![Use to select values, wildcard, or keyset filter information](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242542679437 "Filter Values Select Values work area")

**Add a value**

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.
2. Type a value into the search box and select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243232600589 "add icon"). Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   ![Enter a value, such as rings, to add](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242533271309 "Filter Values Select Values work area")
3. The value is added to the list of selected values.

   ![Review your included values, deselect or remove if needed](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242542899597 "Filter Values Select Values work area")
4. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   For more information about setting attribute filters, see [Set an Attribute Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133345293-Set-an-Attribute-Filter).

### Controlling Number Field Filters

**Control number field filters**

1. Edit the data source configuration for which you want to control number field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) in the data source creation work area.
3. Locate the number field in the field table on the **Fields** tab.
4. Select to enable Custom Range in the sidebar menu.
5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **From** and **To** boxes or use the arrows in the boxes to increment and decrement the values. Custom range values can be numbers or numbers with scientific notation.
6. Select **Save** to apply the custom filter range.

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the number field you specified a custom range for. The values show as default in the filter are the custom range you specified in the data source configuration.

![Define your range of values here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242550987661 "select values filter work area")

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

For more information about setting numeric filters, see [Set a Numeric Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter).

### Controlling Time Field Filters

**Control the default time field filter and time bar ranges**

1. Edit the data source configuration for which you want to control time field filters. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) in the data source configuration.
3. Locate the time field in the field table on the **Fields** tab.
4. Select to enable Custom Range in the sidebar menu.
5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   ![select a date and time for your filter](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242543545357 "calendar popup")
6. Select **Save** to apply the custom filter range.

**Note:** 
If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab).

To test this, create a new dashboard visual or filter snippet using the data source. Then filter the data by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [Set a Time Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter).

![Set the start and end time of your data set for this filter](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242534148237 "select values time range")

When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.
