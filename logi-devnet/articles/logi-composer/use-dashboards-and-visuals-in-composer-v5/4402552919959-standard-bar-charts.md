---
title: "Standard Bar Charts"
id: 4402552919959
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552919959-Standard-Bar-Charts
updated_at: 2021-09-15T02:22:54Z
---

# Standard Bar Charts

# Standard Bar Charts

Standard bar charts are based on one metric and one or two attributes, as follows:

* **Plain**: Based on 1 metric and 1 attribute
* **Clustered**: Based on 1 metric and 2 attributes
* **Stacked**: Based on 1 metric and 2 attributes
* **100% Stacked**: Based on 1 metric and 2 attributes

Standard bar charts are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference).

This topic describes:

* [*Configuring Default Bar Chart Settings for a Data Source*](#Configur)
* [*Configuring Settings for a Specific Bar Chart*](#Configur3)
* [*Configuring Colors for a Specific Bar Chart*](#Configur2)
* [*Understanding Visual Color Condition Thresholds*](#ColorCondThresh)

## Configuring Default Bar Chart Settings for a Data Source

To configure default standard bar chart settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Bars**.

   If you want to be able to display the data collected by this data source configuration as a standard bar chart, make sure the **Bars** checkbox is selected.

   Default standard bar chart settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group | Select the attribute by which the data should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Group Limit | Specify the number of attribute items to display on the visual. |
   | Group Sort | Select a metric or attribute by which the Group attribute items should be sorted. You can also select the sorting order (**Ascending** or **Descending**). For metrics, you can define the default aggregation function: **SUM**, **AVG**, **MAX**, or **MIN**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Sub-Group | Select the attribute by which the other attributes should be grouped.  If you select a date or time attribute, a second box appears to the right for this setting. Use this second box to specify the date and time granularity used to group the data. Valid granularities are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month** or **Year**.  If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab is set at the correct granularity level. For each field, the available granularity options include all options starting from **Year** down to the granularity level specified for this field on the **Fields** tab.  The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds). |
   | Sub-Group Limit | Specify the number of attribute items to be displayed for each attribute that you have selected in the **Sub-Group** list. This option only appears if you have selected a subgroup. |
   | Metric | Select the metric by which you want to analyze the selected attribute. You can also define the default aggregation function used for the metric values: **SUM**, **AVG**, **MAX**, **MIN**, or (for some data sources) **LAST VALUE**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
   | Bar Color | Select the metric that will be depicted by the bar color. You can also define the default aggregation function used for the metric values: **SUM**, **AVG**, **MAX**, **MIN**, or (for some data sources) **LAST VALUE**. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).

## Configuring Settings for a Specific Bar Chart

To change the settings for a specific bar chart:

1. Edit the bar chart you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [chart drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753439511/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Bar Chart Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763923223/bar-standard-settings_192x322.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Orientation | Select Horizontal or Vertical orientation for the bars. |
   | Subgroup | Slide on (to the right) the **Enable Subgroup** slider to enable a subgroup style. After enabling a subgroup style, select the style for the chart: **Cluster Bar Chart**, **Stacked Bar Chart**, or **100% Stacked Bar Chart**. |
   | Labels | Slide the **Show Labels**, **Absolute Values**, and **Relative Values** sliders on (to the right) to enable these label options. |
   | Style | Specify the bar thickness for the chart. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.

## Configuring Colors for a Specific Bar Chart

To specify the color settings for a specific bar chart using the Color sidebar:

1. Edit the visual you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763899159/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438231/color-heatmap2_192x493.png)
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [*Specifying Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4402552732823-Specifying-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Slide the bar to the right if you want the legend to be displayed on the visual or to the left to hide the legend. |
   | Color Metric | Select the metric that affects the segment color in the visual. |
   | Color Palette | If a color palette is specified for this visual type in the data source defaults, select the color palette for this specific visual. If a color range is selected for visuals in the data source defaults, this setting is not available. |
   | Color Mode | Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen. Either specific distinct colors will be used or a gradient of colors will be used.  (This is equivalent to the Legend Type default settings on the Visuals tab of the data source configuration.) |
   | Threshold Mode | If you selected the **Gradient** color mode, this setting cannot be changed. If you selected the Distinct Colors color mode, select either **Auto** or **Manual** from the drop-down list. **Auto** will automatically assign thresholds and colors for the visual. **Manual** allows you to change the thresholds and colors used on the visual. |
   | Number of colors | Specify the number of colors to use for the visual. |
   | Color Rules | Color rules allow you to change the colors for each color used for the visual. In addition, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual. See [*Understanding Visual Color Condition Thresholds*](#ColorCondThresh). |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.

## Understanding Visual Color Condition Thresholds

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.
* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.
* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Composer automatically set the thresholds or you can manually set them.

For information about the color encoding supported by Composer, see [*Specifying Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4402552732823-Specifying-Colors).
