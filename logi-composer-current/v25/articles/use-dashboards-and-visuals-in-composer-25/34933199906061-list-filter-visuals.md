---
title: "List Filter Visuals"
id: 34933199906061
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933199906061-List-Filter-Visuals
updated_at: 2026-05-26T22:08:58Z
---

# List Filter Visuals

# List Filter Visuals

List filter visuals are based on a single attribute, metric, or time field in a data source. These visuals list the values of the selected data source field. They are supported by all Composer [data connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

You can select one or more of the field values in the list filter visual to quickly apply a filter to other visuals in the dashboard that subscribe to a [cross-visual filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107422477-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) for the field. Regular visual filters can also be applied to a list filter visual itself. Filters applied to the list filter visual are saved when the visual or dashboard are saved. However, any filtering performed using the list filter visual is not saved when the dashboard is saved and any data selections made on the list filter visual are not saved.

**Note:** 
A list filter visual cannot be converted to a different style, as other visual styles can using the [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). Likewise, other visual styles cannot be converted to the list filter visual style.

This topic describes:

* [Configure Settings for a Specific List Filter Visual](#Configur3)

For information on setting even time intervals, see [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals).

## Configure Settings for a Specific List Filter Visual

**Change the settings for a specific list filter visual**

1. Edit the list filter visual you want to modify. See [Edit Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933280606989-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select the settings icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167807945997)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The List Filter Settings sidebar for the visual appears.
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Style | Select **Fixed List** to display all available selection items in a selection list.  * If you select **Fixed List** along with Single Number of Selections, users see a list of items and can select one. * If you select **Fixed List** along with Multiple Number of Selections, users see a list of items and can select multiple. Select **Dropdown List** to display all available selection items in adrop-downlist.  * If you select **Dropdown List** along with Single Number of Selections, users can filter or scroll through a list of items and can select one. * If you select **Dropdown List** along with Multiple Number of Selections, users can filter, select, and scroll through a list of items and can select multiple values. * An additional option to Filter Values On is available when you select Dropdown List and Multiple Number of Selections. |
   | Display Column | Select  to select a different data source field for the list filter visual. |
   | Use Display Column as Value Column | Enable to use the information provided in the display column as selections for your users.  Disable to select a different field to provide selections to your users. |
   | Value Column | When **Use Display Column as Value Column** is disabled, you can select a different field to provide users selection items. |
   | Number of Selections | Specify whether only one or multiple data values can be selected in the visual. Select **Single** to allow users to select only one data value; select **Multiple** to allow users to select more than one value. **Multiple** is not allowed for time fields. The default is **Single**.  * If you select **Fixed List** along with **Single**, users see a list of items and can select one value. * If you select **Dropdown List** along with **Single**, users can filter or scroll through a list of items and can select one value. * If you select **Fixed List** along with **Multiple**, users see a list of items and can select multiple values. * If you select **Dropdown List** along with **Multiple**, users can filter, select, and scroll through a list of items and can select multiple values. |
   | "No Selection" Label | Supply a label for the visual option when no data is selected.  The default is **None**. This label is only available when Number of Selections is set to **Single**. |
   | Placeholder Text | Supply a label for the search field when no data is selected.  The default is **Search**. This label is only available when Number of Selections is set to **Multiple**. |
   | Filter Values On | This option is available only when Number of Selections is set to **Multiple**.  * Enable **Change** to filter values when the user makes a selection. * Enable **Submit** to filter values when the user selects the **Submit** button. The text of the Submit button can be changed. |
   | Submit Button Text | Only visible if **Submit** is enabled in Filter Values On. You can change the **Submit Button Text** to meet your users' needs. The default value is **Change**.  When a user selects the **Submit** button, their selected values are published and used by other visuals on the dashboard that use this list. |
5. Select the save icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167807948045)) to save the dashboard and the visual with its updated settings.
