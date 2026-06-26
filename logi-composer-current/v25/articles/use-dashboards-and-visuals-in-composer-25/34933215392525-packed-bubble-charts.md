---
title: "Packed Bubble Charts"
id: 34933215392525
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933215392525-Packed-Bubble-Charts
updated_at: 2026-05-26T22:08:59Z
---

# Packed Bubble Charts

# Packed Bubble Charts

Packed bubble charts are based on two metrics and one attribute. They are supported by all Composer [data connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

**Note:** 
To edit the number or date and time format for this visual, see [Configure Number Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933278713485-Configure-Number-Formatting-for-Visuals) and [Configure Date and Time Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263048077-Configure-Date-and-Time-Formatting-for-Visuals).

This topic describes:

* [Configure Colors for a Specific Packed Bubble Chart](#Configur2)

## Configure Colors for a Specific Packed Bubble Chart

**Specify the color settings for a specific packed bubble chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933280606989-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167807886221)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Color sidebar for the visual appears.
3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932703126541-Specify-Colors).

   | Setting | Description |
   | --- | --- |
   | Legend | Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.  * For distinct color styles, select a data point in the legend to turn it off and on in the visual. * For gradient color styles, use the legend’s gradient slider to show and hide your data. If available, enable or disable a static legend for this visual. |
   | Color Metric | Select the metric that affects the segment color in the visual. |
   | <type> Color Palette | If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Composer UI.  To override the palette selected by the theme, clear the **Inherit from Theme** checkbox and select a different color palette. |
   | Color Mode | Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen.  Either specific distinct colors will be used or a gradient of colors will be used. |
   | Threshold Mode | If you selected the **Gradient** color mode, this setting cannot be changed. If you selected the Distinct Colors color mode, select either **Auto** or **Manual** from the drop-down list.  **Auto** will automatically assign thresholds and colors for the visual.  **Manual** enables you to change the thresholds and colors used on the visual. |
   | Number of colors | Specify the number of colors to use for the visual. |
   | Color Rules | Color rules allow you to change the colors for each color used for the visual.  In addition, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual. |
4. Close the Color sidebar and the color settings are dynamically applied to the visual.
5. Select the save icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167818927373)) to save the dashboard and the visual with its updated settings.

### Understand Visual Color Condition Thresholds

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.
* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.
* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Composer automatically set the thresholds or you can manually set them.

For information about the color encoding supported by Composer, see [Specify Colors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932703126541-Specify-Colors).
