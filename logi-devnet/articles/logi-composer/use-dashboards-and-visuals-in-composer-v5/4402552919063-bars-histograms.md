---
title: "Bars: Histograms"
id: 4402552919063
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552919063-Bars-Histograms
updated_at: 2021-09-15T02:22:50Z
---

# Bars: Histograms

# Bars: Histograms

Histograms require only one metric (number or integer). The metric data range is divided into intervals and the metric values that fall within each interval are counted. The histogram plots the value counts (Volume) against the metric intervals.

Histograms are supported only by data sources that use Composer [connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference) that support the Histogram feature. See [*Connector Feature Support*](https://devnet.logianalytics.com/hc/en-us/articles/4402537705623-Connector-Feature-Support).

Data from Fusion data sources can be used in histograms.

This topic describes:

* [*Configuring Default Histogram Settings for a Data Source*](#Configur)
* [*Configuring Settings for a Specific Histogram*](#Configur3)
* [*Configuring Colors for a Specific Histogram*](#Configur2)

## Configuring Default Histogram Settings for a Data Source

To configure default histogram settings for a data source configuration:

1. Edit the appropriate data source configuration. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration).
2. Select the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab in the data source configuration wizard.
3. On the **Standard** subtab of the [Visuals](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) tab, select **Bars: Histogram**.

   If you want to be able to display the data collected by this data source configuration as a histogram, make sure the **Bars:Histogram** checkbox is selected.

   Default histogram settings appear on the right side of the page.
4. Configure the default settings as follows:

   | Setting | Description |
   | --- | --- |
   | Group By | Select the attribute by which the data should be grouped. |
   | Number of bars | Specify the number of bars:  * **Auto** - if you select this option, the bins for all your data set will be built and corresponding bars will be displayed. * **Limit to** - specify the maximum number of bars to be displayed on your visual. * **Bar interval** - specify the bar interval for your visual. |
   | Axis values | Specify the types of values to be shown on the visual:  * **Absolute** - select this option if you want to see the exact values. * **Relative** - select this option if you want to see the values in %. |
   | Show Cumulative Line | Select this checkbox if you want the cumulative line to be displayed on your visual. |
   | Cumulative Line Color | Select the color for the cumulative line on your visual. |
   | Bins Color | Select the color for the bins on the visual. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763898903/save-white-btn_40x23.png).

## Configuring Settings for a Specific Histogram

To change the settings for a specific histogram:

1. Edit the histogram you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753439511/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Histogram Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763925015/bar-histogram-settings_192x312.png)
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Number of Bars | Specify the number of bars:  * **Auto** - if you select this option, the bins for all your data set will be built and corresponding bars will be displayed. * **Limit to** - specify the maximum number of bars to be displayed on your visual. * **Bar interval** - specify the bar interval for your visual. |
   | Labels | Slide the **Append Absolute Values**, and **Append Relative Values** sliders on (to the right) to enable these label options. |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.

## Configuring Colors for a Specific Histogram

To specify the color settings for a specific histogram using the Color sidebar:

1. Edit the visual you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763899159/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753447447/color-bar-hist2_288x193.png)
3. Configure the color settings as described below. Supported color specifications are described in [*Specifying Colors*](https://devnet.logianalytics.com/hc/en-us/articles/4402552732823-Specifying-Colors).

   | Setting | Description |
   | --- | --- |
   | Bins Color | Select the color for the bins on the visual. |
   | Cumulative Line Color | Select the color for the cumulative line on your visual. |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753438615/dash-save.png) to save the dashboard and the visual with its updated settings.
