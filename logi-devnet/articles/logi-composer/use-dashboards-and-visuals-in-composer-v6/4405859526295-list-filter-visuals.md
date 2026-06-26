---
title: "List Filter Visuals"
id: 4405859526295
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859526295-List-Filter-Visuals
updated_at: 2021-09-21T01:30:06Z
---

# List Filter Visuals

# List Filter Visuals

List filter visuals are based on a single attribute, metric, or time field in a data source. These visuals list the values of the selected data source field. They are supported by all Composer[data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).

You can select one or more of the field values in the list filter visual to quickly apply a filter to other visuals in the dashboard that subscribe to a [cross-visual filter](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) for the field. Regular visual filters can also be applied to a list filter visual itself. Filters applied to the list filter visual are saved when the visual or dashboard are saved. However, any filtering performed using the list filter visual is not saved when the dashboard is saved and any data selections made on the list filter visual are not saved.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) A list filter visual cannot be converted to a different style, as other visual styles can using the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). Likewise, other visual styles cannot be converted to the list filter visual style.

This topic describes:

* [*Configure Default List Filter Visual Settings for a Data Source*](#Configur)
* [*Configure Settings for a Specific List Filter Visual*](#Configur3)

For information on setting even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals).

## Configure Default List Filter Visual Settings for a Data Source

To configure the default settings for list filter visuals for a data source configuration:

1. Edit the appropriate data source configuration. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab, select **List Filter**.

   If you want to be able to display the data collected by this data source configuration as a list filter visual, make sure the **List Filter** checkbox is selected.

   Default list filter visual settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Display Value | Select an attribute, metric, or time field for the list filter visual.  If you select a time field, a date and time granularity box appears to the right of the field. Select the date and time granularity used to group the data.  Valid granularity options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, **Quarter**, or **Year**. If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab of the data source definition is set at the correct granularity level.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Display Value Limit | Specify the maximum number of values to display in a list filter visual. |
   | Display Value Sort | By default, the field selected is the same as the field selected for **Display Value**. A default sorting order is also selected, but you can select a different one. Valid values for the sorting order vary, based on the field that is selected. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382679/save-white-btn_40x23.png).

## Configure Settings for a Specific List Filter Visual

To change the settings for a specific list filter visual:

1. Edit the list filter visual you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747383319/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The List Filter Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743734167/list-filter-settings_288x475.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Column | Select  to select a different data source field for the list filter visual. |
   | Display Style | Only the Fixed List display style is available. It is automatically selected. |
   | Number of Selections | Specify whether only one or multiple data values can be selected in the visual. Select **Single** to allow users to select only one data value; select **Multiple** to allow users to select more than one value. **Multiple** is not allowed for time fields. The default is **Single**. |
   | "No Selection" Label | Supply a label for the visual option when no data is selected. The default is **None**. This label is only available when Number of Selections is set to **Single**. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) to save the dashboard and the visual with its updated settings.
