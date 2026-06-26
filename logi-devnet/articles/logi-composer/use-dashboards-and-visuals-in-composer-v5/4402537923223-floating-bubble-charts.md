---
title: "Floating Bubble Charts"
id: 4402537923223
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537923223-Floating-Bubble-Charts
updated_at: 2021-09-15T02:22:55Z
---

# Floating Bubble Charts

# Floating Bubble Charts

Floating bubble charts are based on two metrics and two attributes. Floating bubble charts are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference) except Cloudera Search. They are supported by Composer Apache Solr connectors for version 5.2 or later.

The default settings used for floating bubble charts vary, based on the data source selected for the chart.

This topic describes:

* [*Configuring Default Floating Bubble Chart Settings for a Data Source*](#Configur)
* [*Configuring Colors for a Specific Floating Bubbles Chart*](#Configur2)

## Configuring Default Floating Bubble Chart Settings for a Data Source

To configure the default floating bubble chart settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Floating Bubbles**.

   If you want to be able to display the data collected by this data source configuration as a floating bubble chart, make sure the **Floating Bubbles** checkbox is selected.

   Default floating bubble chart settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group 1 | Select the attribute by which Group 1 data should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Group 1 Limit | Specify the number of Group 1 attribute items to display on the visual. |
   | Group 1 Sort | Select a Group 1 metric or attribute by which the Group 1 attribute items should be sorted. You can also select the sorting order (**Ascending** or **Descending**). For metrics, you can define the default aggregation function: **SUM**, **AVG**, **MAX**, or **MIN**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Group 2 | Select the attribute by which Group 2 data should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Group 2 Limit | Specify the number of Group 2 attribute items to display on the visual. |
   | Group 2 Sort | Select a Group 2 metric or attribute by which the Group 2 attribute items should be sorted. You can also select the sorting order (**Ascending** or **Descending**). For metrics, you can define the default aggregation function: **SUM**, *AVG*, **MAX**, or **MIN**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Y Axis | Select the metric for the y-axis. You can also define the default aggregation function used for the metric values: **SUM**, **AVG**, **MAX**, **MIN**, or (for some data sources) **LAST VALUE**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Size | Select the metric that affects the size of the bubbles in the visual. You can also define the default aggregation function used for the metric values: **SUM**, **AVG**, **MAX**, **MIN**, or (for some data sources) **LAST VALUE**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).

## Configuring Colors for a Specific Floating Bubbles Chart

To specify the color settings for a specific floating bubbles chart using the Color sidebar:

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
