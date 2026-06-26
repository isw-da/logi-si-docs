---
title: "Line Trend: Multiple Metric Charts"
id: 43701212528525
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212528525-Line-Trend-Multiple-Metric-Charts
updated_at: 2026-05-29T14:10:15Z
---

# Line Trend: Multiple Metric Charts

# Line Trend: Multiple Metric Charts

Multiple metric line charts are based on multiple metrics and one time attribute. Multiple metric line charts are supported by all Composer [data connectors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference) except Cloudera Search. They are supported by Composer Apache Solr connectors for version 5.2 or later.

This topic describes:

* [Configure Settings for a Specific Multiple Metric Line Chart](#Configur3)
* [Configure Colors for a Specific Multiple Metric Line Chart](#Configur2)

For information on setting even time intervals, see [Even Time Intervals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077393293-Even-Time-Intervals).

## Configure Settings for a Specific Multiple Metric Line Chart

**Change the settings for a specific multiple metric line chart**

1. Edit the multiple metric line chart you want to modify. See [Edit Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214480525-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select the settings icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243135988109)) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). The Line Chart Settings sidebar for the visual appears.

   ![define the settings for your visual here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242320330637 "Settings sidebar menu, line chart multiple metrics")
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Style | Select **Line Chart** or **Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default.  The **Area Chart** setting turns on the fill option for the line chart (fills the visual with appropriate colors between the lines). The **Line Chart** setting turns off the fill option (so only lines appear). |
   | Cumulative Sum | When enabled, Composer updates the visual to add the previous value to the next value, and both the original and cumulative value for selected items are displayed as a tool tip. |
   | Horizontal Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Line Thickness | Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box. |
5. Optionally, edit the number or date and time format for this visual. See [Configure Number Formatting for Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184419213-Configure-Number-Formatting-for-Visuals) and [Configure Date and Time Formatting for Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179815949-Configure-Date-and-Time-Formatting-for-Visuals).
6. Select the save icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243135990157)) to save the dashboard and the visual with its updated settings.

## Configure Colors for a Specific Multiple Metric Line Chart

**Specify the color settings for a specific multiple metric line chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214480525-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243135998733)) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). The Color sidebar for the visual appears.
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990058381-Specify-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.  For distinct color styles, select a data point in the legend to turn it off and on in the visual. |
   | Color | Manually select the color for each metric using the color selector. |
   | <type> Color Palette | Select a color palette for this specific visual.  Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-UI-Themes). |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select the save icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243135990157)) to save the dashboard and the visual with its updated settings.
