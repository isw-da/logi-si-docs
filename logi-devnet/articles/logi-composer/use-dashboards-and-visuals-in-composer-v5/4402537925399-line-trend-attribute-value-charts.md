---
title: "Line Trend: Attribute Value Charts"
id: 4402537925399
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537925399-Line-Trend-Attribute-Value-Charts
updated_at: 2021-09-15T02:22:58Z
---

# Line Trend: Attribute Value Charts

# Line Trend: Attribute Value Charts

Attribute value line charts are based on one metric, one attribute and one time attribute. Attribute value line charts are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference) except Cloudera Search. They are supported by Composer Apache Solr connectors for version 5.2 or later.

This topic describes:

* [*Configuring Default Attribute Value Line Chart Settings for a Data Source*](#Configur)
* [*Configuring Settings for a Specific Attribute Value Line Chart*](#Configur3)
* [*Configuring Colors for a Specific Attribute Value Line Chart*](#Configur2)

For information on setting even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537753623-Even-Time-Intervals).

## Configuring Default Attribute Value Line Chart Settings for a Data Source

To configure the default settings for attribute value line charts for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Line Trend: Attribute Values**.

   If you want to be able to display the data collected by this data source configuration as an attribute value line chart, make sure the **Line Trend: Attribute Values** checkbox is selected.

   Default attribute value line chart settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group | Select the attribute by which the data should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Group Limit | Specify the number of attribute items to display on the visual. |
   | Group Sort | Select a metric or attribute by which the grouped attribute items should be sorted. You can also select the sorting order (**Ascending** or **Descending**). For metrics, you can define the default aggregation function: SUM, AVG, MAX, or MIN. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Trend Attribute | Select the trend attribute for the visual.  In the second (rightmost) box for this setting, specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Trend Attribute Limit | Specify the maximum number of trend attributes to be displayed on the visual. |
   | Trend Attribute Sort | Shows the time parameter by which the trend attributes will be sorted. You can select the sorting order (**Chronological** or **Reverse Chronological**). |
   | Y Axis | Select the metric for the y-axis. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).

## Configuring Settings for a Specific Attribute Value Line Chart

To change the settings for a specific attribute value line chart:

1. Edit the attribute value line chart you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753439511/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Line Chart Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763916439/line-settings_192x330.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Style | Select **Line Chart** or **Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default. The **Area Chart** setting turns on the fill option for the line chart (fills the visual with appropriate colors between the lines). The **Line Chart** setting turns off the fill option (so only lines appear). |
   | Line Thickness | Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.

## Configuring Colors for a Specific Attribute Value Line Chart

To specify the color settings for a specific attribute value line chart using the Color sidebar:

1. Edit the visual you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763899159/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763908887/color-simple1-new_288x533.png)
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [*Specifying Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4402552732823-Specifying-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Slide the bar to the right if you want the legend to be displayed on the visual or to the left to hide the legend. You can manually select the color for each color in the legend using the color selector. |
   | Color Attribute | Select the attribute that affects the segment color in the visual. |
   | Color Palette | If a color palette is specified for this visual type in the data source defaults, select the color palette for this specific visual. If a color range is selected this visual type in the data source defaults, this setting is not available. |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.
