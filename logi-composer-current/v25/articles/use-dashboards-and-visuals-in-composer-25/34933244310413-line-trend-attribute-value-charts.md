---
title: "Line Trend: Attribute Value Charts"
id: 34933244310413
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933244310413-Line-Trend-Attribute-Value-Charts
updated_at: 2026-05-26T22:09:07Z
---

# Line Trend: Attribute Value Charts

# Line Trend: Attribute Value Charts

Attribute value line charts are based on one metric, one attribute and one time attribute. Attribute value line charts are supported by all Composer [data connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference) except Cloudera Search. They are supported by Composer Apache Solr connectors for version 5.2 or later.

This topic describes:

* [Configure Settings for a Specific Attribute Value Line Chart](#Configur3)
* [Configure Colors for a Specific Attribute Value Line Chart](#Configur2)

For information on setting even time intervals, see [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals).

## Configure Settings for a Specific Attribute Value Line Chart

**Change the settings for a specific attribute value line chart**

1. Edit the attribute value line chart you want to modify. See [Edit Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933280606989-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select the settings icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167846253965)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Line Chart Settings sidebar for the visual appears.

   ![define the settings for your line chart](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166969093005 "Line chart settings work area")
4. Alter the settings as needed:

   | Setting | Description |
   | --- | --- |
   | Display Style | Select **Line Chart** or **Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default.  The **Area Chart** setting turns on the fill option for the line chart (fills the visual with appropriate colors between the lines).  The **Line Chart** setting turns off the fill option (so only lines appear). |
   | Display as stacked | Slide this switch on (to the right) to display the visual as a stacked area chart. When turned on, the Stacking Style options become available. |
   | Stacking Style | Select one of the stacking styles: **Stacked** or **100% Stacked**. These options are only available if the **Display as stacked** switch is on.  * The **Stacked** setting is the default and displays the plotted lines in a stacked format. Stacked charts are best used to show how individual values in the data relate to all of the other values for the same data. * The **100% Stacked** option displays the plotted lines in a stacked format but as they relate to a cumulative whole. The y-axis cumulative total is always represented as 100% in a 100% stacked format and all individual values are presented as percentages of the whole. |
   | Horizontal Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Line Thickness | Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box. |
5. Optionally, edit the number or date and time format for this visual. See [Configure Number Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933278713485-Configure-Number-Formatting-for-Visuals) and [Configure Date and Time Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263048077-Configure-Date-and-Time-Formatting-for-Visuals).
6. Select the save icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167846255885)) to save the dashboard and the visual with its updated settings.

## Configure Colors for a Specific Attribute Value Line Chart

**Specify the color settings for a specific attribute value line chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933280606989-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167840745741)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Color sidebar for the visual appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167846257677)
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932703126541-Specify-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.  * For distinct color styles, select a data point in the legend to turn it off and on in the visual. * Use the color selector to manually assign colors for legend items. If available, enable or disable a static legend for this visual. |
   | Color Attribute | Select the attribute that affects the segment color in the visual. |
   | Group By Color Palette | Select a color palette for this specific visual.  Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933172226573-Manage-UI-Themes). |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select the save icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167846255885)) to save the dashboard and the visual with its updated settings.
