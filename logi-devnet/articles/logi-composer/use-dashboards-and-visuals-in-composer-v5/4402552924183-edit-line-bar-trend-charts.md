---
title: "Edit Line &\u00a0Bar Trend Charts"
id: 4402552924183
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552924183-Edit-Line-Bar-Trend-Charts
updated_at: 2021-09-15T02:22:59Z
---

# Edit Line & Bar Trend Charts

# Edit Line & Bar Trend Charts

Line and bar trend charts are based on two metrics and a time attribute.
They are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference), except Cloudera Search, and by Composer Apache Solr connectors for version 5.2 or later.

This topic describes:

* [*Configuring Default Line & Bar Trend Chart Settings for a Data Source*](#Configur)
* [*Configuring Colors for a Specific Line & Bar Trend Chart*](#Configur2)

For information on setting even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537753623-Even-Time-Intervals).

## Configuring Default Line & Bar Trend Chart Settings for a Data Source

To configure the default settings for line & bar trend charts for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Line & Bars Trend**.

   If you want to be able to display the data collected by this data source configuration as a line & bar chart, make sure the **Line & Bars Trend** checkbox is selected.

   Default line & bar chart settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Trend Attribute | Select the time trend attribute for the visual.  In the second (rightmost) box for this setting, specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Trend Attribute Limit | Specify the number of time attribute items. |
   | Trend Attribute Sort | Shows the time parameter by which the trend attributes will be sorted. You can select the sorting order (**Chronological** or **Reverse Chronological**). |
   | Y1 Axis | Select a metric to use for the bars on your visual. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Y2 Axis | Select a metric to use for the line on your visual. You can also define the default aggregation function used for the metric values: SUM, AVG, MAX, MIN, or (for some data sources) LAST VALUE. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Y1 Color | Select a color for the Y1 bars on your visual. |
   | Y2 Color | Select a color for the Y2 line on your visual. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).

## Configuring Colors for a Specific Line & Bar Trend Chart

To specify the color settings for a specific line & bar trend chart using the Color sidebar:

1. Edit the visual you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [chart drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763899159/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763916695/color-line-bar2_288x181.png)
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [*Specifying Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4402552732823-Specifying-Colors).

   | Setting | Description |
   | --- | --- |
   | Y2 Color | Select a color for the Y2 line on your visual. |
   | Y1 Color | Select a color for the Y1 bars on your visual. |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.
