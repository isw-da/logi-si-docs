---
title: "Changing Color Schemes"
id: 4402537921943
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537921943-Changing-Color-Schemes
updated_at: 2021-09-15T02:22:56Z
---

# Changing Color Schemes

# Changing Color Schemes

Color schemes provide ways to identify and highlight metrics and attributes on a visual using color. Color schemes are specified for visuals in different ways, based on the visual type.

* For [histograms](https://devnet.logianalytics.com/hc/en-us/articles/4402552919063-Bars-Histograms) and [line and bar trend charts](https://devnet.logianalytics.com/hc/en-us/articles/4402552924183-Edit-Line-Bar-Trend-Charts), the colors are specified on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) of a data source configuration and cannot be changed using the Color sidebar.
* The colors on [standard bar charts](https://devnet.logianalytics.com/hc/en-us/articles/4402552919959-Standard-Bar-Charts), [heat maps](https://devnet.logianalytics.com/hc/en-us/articles/4402552921495-Heat-Maps), [KPI charts](https://devnet.logianalytics.com/hc/en-us/articles/4402552923287-KPI-Charts), [U.S. region maps](https://devnet.logianalytics.com/hc/en-us/articles/4402537927959-US-Region-Maps), [world country maps](https://devnet.logianalytics.com/hc/en-us/articles/4402537928599-World-Maps), [packed bubble charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537929239-Packed-Bubble-Charts), [tree maps](https://devnet.logianalytics.com/hc/en-us/articles/4402552934423-Tree-Maps), and [word cloud charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537949591-Word-Clouds) are based on the color metric selected for the visual. Colors can be changed using the Color sidebar and on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) of a data source configuration.
* The color of [multiple metric bar](https://devnet.logianalytics.com/hc/en-us/articles/4402537919383-Bars-Multiple-Metric-Charts) and [multiple-metric line](https://devnet.logianalytics.com/hc/en-us/articles/4402537926039-Line-Trend-Multiple-Metric-Charts) charts are based on the y-axis metric you have selected. Colors can be changed using the Color sidebar and on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) of a data source configuration.
* Visual colors are not available for [map marker charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537927319-Marker-Maps), [pivot tables](https://devnet.logianalytics.com/hc/en-us/articles/4402537933719-Pivot-Tables), and [raw data tables](https://devnet.logianalytics.com/hc/en-us/articles/4402537935639-Raw-Data-Tables-RDT-).
* For all other visuals ([box plots](https://devnet.logianalytics.com/hc/en-us/articles/4402537920023-Box-Plots), [donut charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537922583-Donut-Charts), [floating bubble charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537923223-Floating-Bubble-Charts), [line-trend attribute charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537925399-Line-Trend-Attribute-Value-Charts), [pie charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537929879-Pie-Charts), and [scatter plot charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537936279-Scatter-Plots)), the visual colors are based on an x-axis Group field you have selected. Colors can be changed using the Color sidebar and on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) of a data source configuration.

Color palettes for your Composer environment are defined using themes. In addition, the default color palette used for visuals and for specific visual styles is defined using themes. See [*Manage UI Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402537896343-Manage-UI-Themes).

To access the Color sidebar for a visual:

1. Select the visual in the Visual Gallery or on a dashboard.
2. Select **Edit Visual** on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) to access the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763899159/sidebar-color.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).

   The **Color** sidebar for the selected visual opens.
3. Make changes as needed. For details about the color options, refer to the description of the specific [visual style](https://devnet.logianalytics.com/hc/en-us/articles/4402537848855-Visual-Metrics-and-Attributes-Reference) used by the visual.
4. If you want to use the palette specified by the theme defined for the environment, select the **Inherit from theme** checkbox. The colors specified in the theme activated for the Composer environment and for this visual style will be used and will override other palette settings you might have specified on the Color sidebar. For more information about themes, see [*Manage UI Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402537896343-Manage-UI-Themes).

The ability to control colors on a visual is provided using the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).
