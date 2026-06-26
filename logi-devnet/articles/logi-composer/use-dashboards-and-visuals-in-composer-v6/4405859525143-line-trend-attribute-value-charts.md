---
title: "Line Trend: Attribute Value Charts"
id: 4405859525143
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts
updated_at: 2021-09-21T01:30:05Z
---

# Line Trend: Attribute Value Charts

# Line Trend: Attribute Value Charts

Attribute value line charts are based on one metric, one attribute and one time attribute. Attribute value line charts are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference) except Cloudera Search. They are supported by Composer Apache Solr connectors for version 5.2 or later.

This topic describes:

* [*Configure Default Attribute Value Line Chart Settings for a Data Source*](#Configur)
* [*Configure Settings for a Specific Attribute Value Line Chart*](#Configur3)
* [*Configure Colors for a Specific Attribute Value Line Chart*](#Configur2)

For information on setting even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals).

## Configure Default Attribute Value Line Chart Settings for a Data Source

To configure the default settings for attribute value line charts for a data source configuration:

1. Edit the appropriate data source configuration. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) tab, select **Line Trend: Attribute Values**.

   If you want to be able to display the data collected by this data source configuration as an attribute value line chart, make sure the **Line Trend: Attribute Values** checkbox is selected.

   Default attribute value line chart settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group | Select the attribute by which the data should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data.  Valid granularity options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, **Quarter**, or **Year**. If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab of the data source definition is set at the correct granularity level.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Group Limit | Specify the number of attribute items to display on the visual. |
   | Group Sort | Select a metric or attribute by which the grouped attribute items should be sorted. You can also select the sorting order (**Ascending** or **Descending**). For metrics, you can define the default aggregation function: SUM, AVG, MAX, or MIN. See [*Metric Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021975-Metric-Aggregation-Functions). |
   | Trend Attribute | Select the trend attribute for the visual.  In the second (rightmost) box for this setting, specify the date and time granularity used to group the data.  Valid granularity options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, **Quarter**, or **Year**. If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab of the data source definition is set at the correct granularity level.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Trend Attribute Limit | Specify the maximum number of trend attributes to be displayed on the visual. |
   | Trend Attribute Sort | Shows the time parameter by which the trend attributes will be sorted. You can select the sorting order (**Chronological** or **Reverse Chronological**). |
   | Y Axis | Select the metric for the y-axis. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [*Metric Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021975-Metric-Aggregation-Functions). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382679/save-white-btn_40x23.png).

## Configure Settings for a Specific Attribute Value Line Chart

To change the settings for a specific attribute value line chart:

1. Edit the attribute value line chart you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747383319/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The Line Chart Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743735063/line-settings_288x500.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Style | Select **Line Chart** or **Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default. The **Area Chart** setting turns on the fill option for the line chart (fills the visual with appropriate colors between the lines). The **Line Chart** setting turns off the fill option (so only lines appear). |
   | Display as stacked | Slide this switch on (to the right) to display the visual as a stacked area chart. When turned on, the Stacking Style options become available. |
   | Stacking Style | Select one of the stacking styles: **Stacked** or **100% Stacked**. These options are only available if the **Display as stacked** switch is on.  * The **Stacked** setting is the default and displays the plotted lines in a stacked format. Stacked charts are best used to show how individual values in the data relate to all of the other values for the same data.  The **100% Stacked** option displays the plotted lines in a stacked format but as they relate to a cumulative whole. The y-axis cumulative total is always represented as 100% in a 100% stacked format and all individual values are presented as percentages of the whole. |
   | Line Thickness | Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) to save the dashboard and the visual with its updated settings.

## Configure Colors for a Specific Attribute Value Line Chart

To specify the color settings for a specific attribute value line chart using the Color sidebar:

1. Edit the visual you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743709975/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747387415/color-simple1-new_288x566.png)
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [*Specify Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4405859162903-Specify-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Slide the bar to the right if you want the legend to be displayed on the visual or to the left to hide the legend. You can manually select the color for each color in the legend using the color selector. |
   | Color Attribute | Select the attribute that affects the segment color in the visual. |
   | Group By Color Palette | If a color palette is specified for this visual type in the data source defaults, select the color palette for this specific visual. If a color range is selected this visual type in the data source defaults, this setting is not available. Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes). |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743710231/dash-save.png) to save the dashboard and the visual with its updated settings.
