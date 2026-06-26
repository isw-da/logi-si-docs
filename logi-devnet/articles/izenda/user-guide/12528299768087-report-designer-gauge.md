---
title: "Report Designer/Gauge"
id: 12528299768087
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528299768087-Report-Designer-Gauge
updated_at: 2023-02-23T15:07:12Z
---

# Report Designer/Gauge

# Report Designer/Gauge

Gauge is a built-in type of report part that displays data using a speedometer.

## Define a Linear Gauge

1. Select the chart in Report Body (See [Manage Report Parts](https://devnet.logianalytics.com/hc/en-us/articles/12528284369047-Report-Designer-Design#manage-report-parts) for how to add a chart).
2. Click the expand icon (<) on the right to open the Properties boxes if needed.
3. Select the vertical Report Part Properties box.
4. The properties are listed in Report Part Properties box in these sections.
   * General Info
   * Gauge
   * Grouping
   * View
   * Printing

![../_images/Gauge_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528204067735/gauge_properties_251x642.png)

User can configure the properties and see changes reflected in Preview pane:

* Select Linear Gauge in Gauge Type drop-down. (See below for Solid Gauge and Simple Gauge.)

  ![../_images/Gauge_Border_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528219899927/gauge_border_settings_458x421.png)
* Configure border settings:

  1. In Gauge group, click the gear icon (⚙) to open Gauge Border Settings pop-up.
  2. Choose the border to be visible or not.
  3. Select a border color.
  4. Select the border thickness (in pixels).
  5. Click OK to close the Border Settings pop-up.

  Note: The Preview section will not be shown if the **Show Preview section in Configuration Mode** checkbox is unchecked in Others tab in Advanced Settings.

  > [![../_images/Gauge_Border_Settings_No_Preview.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528204081303/gauge_border_settings_no_preview_458x290.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219905943/gauge_border_settings_no_preview.png)

  Please see [Update Others Settings](https://devnet.logianalytics.com/hc/en-us/articles/12528299314327-Advanced-Settings#advanced-settings-others) for more details.
* Customize the relative distance between the tick marks (in Intervals box for Linear Gauge only).

  ![../_images/Color_Theme_Selection.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528219912727/color_theme_selection_458x339.png)
* Configure color theme settings:

  1. In Gauge group, click the gear icon (⚙) after the Color Theme option to open Color Theme Selection pop-up.
  2. Choose a color theme.
  3. Click OK to close the Color Theme Selection pop-up.

  Note:When System Admin change the [Default Color Setting](https://devnet.logianalytics.com/hc/en-us/articles/12528299389591-System-Configuration-Report#set-default-color-theme), all report parts using the default color theme will update properly.
* Select to use Separator. (See [Define Separator](#define-separator))
* It looks better to invert the Linear Gauge (to horizontal direction).

  ![../_images/Gauge_Data_Refresh_Interval_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528204095383/gauge_data_refresh_interval_settings_460x237.png)
* Configure Data Refresh Interval if needed.
* Optionally display a long report in multiple pages.
* Optionally choose to print each grid in a new page by checking Page Break After Separator in Printing group.

[![../_images/NW_Orders_Linear_Gauge_Sum(Freight)_Group(ShipCity).png](https://devnet.logianalytics.com/hc/article_attachments/12528219934615/nw_orders_linear_gauge_sum_freight__group_shipcity__950x299.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204106519/nw_orders_linear_gauge_sum_freight__group_shipcity_.png)

To define the above sample gauge:

1. Select Northwind Orders table in Data Source.
2. Add a gauge report part and select Linear Gauge as the type.
3. Add [ShipCity] to Labels (X-axis) box, it will show up as Group(ShipCity).
4. Click Add Metrics to create Metrics 1.
5. Add [Freight] to Value box, it will show up as Sum(Freight).
6. Optionally set the threshold values like following:

[![../_images/NW_Orders_Linear_Gauge_Sum(Freight)_Group(ShipCity)_Threshold.png](https://devnet.logianalytics.com/hc/article_attachments/12528204122007/nw_orders_linear_gauge_sum_freight__group_shipcity__threshold_950x346.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219940247/nw_orders_linear_gauge_sum_freight__group_shipcity__threshold.png)

Screenshot for Dynamic Threshold to be updated.

## Define Separator

The Separator option displays multiple sections of gauges according to each unique value of the field(s) defined in Separators box.

For example: this report with multiple gauges, each one for each country in Northwind Orders table.

[![../_images/NW_Orders_Gauge_Separator_ShipCountry_Sum(Freight)_Group(ShipCity).png](https://devnet.logianalytics.com/hc/article_attachments/12528219960343/nw_orders_gauge_separator_shipcountry_sum_freight__group_shipcity__950x535.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204125847/nw_orders_gauge_separator_shipcountry_sum_freight__group_shipcity_.png)

1. Tick Use Separator check-box in Grouping in Report Part Properties to see Separators box inside the gauge configuration.
2. Add [ShipCity] to Labels (X-axis) box, it will show up as Group(ShipCity).
3. Click Add Metrics to create Metrics 1.
4. Add [Freight] to Value box, it will show up as Sum(Freight).
5. Add [ShipCountry] to Separators box, it will show up as Group(ShipCountry).

## Define a Solid Gauge

1. Select Solid Gauge in Gauge Type drop-down.
2. The rest of the properties are similar to Linear Gauge.

An example solid gauge with separator and threshold:

[![../_images/NW_Orders_Gauge_Separator_ShipCountry_Sum(Freight)_Group(ShipCity)_Threshold.png](https://devnet.logianalytics.com/hc/article_attachments/12528219965975/nw_orders_gauge_separator_shipcountry_sum_freight__group_shipcity__threshold_950x513.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219961879/nw_orders_gauge_separator_shipcountry_sum_freight__group_shipcity__threshold.png)

[![../_images/Report_Simple_Gauge.png](https://devnet.logianalytics.com/hc/article_attachments/12528219975959/report_simple_gauge_350x219.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204144535/report_simple_gauge.png)

## Others

* Grid view pop-up option. This option is available from version 2.10.0.

  Click ![gridViewIcon](https://devnet.logianalytics.com/hc/article_attachments/12528218934551/grid_view_icon.png) icon to see the grid view of the gauge data associated with the current metric.

  [![../_images/Gauge_Grid_View_Popup.png](https://devnet.logianalytics.com/hc/article_attachments/12528204157463/gauge_grid_view_popup_653x198.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219980439/gauge_grid_view_popup.png)

* Metric drop-down.

> [![../_images/Gauge_Metric_Dropdown.png](https://devnet.logianalytics.com/hc/article_attachments/12528219999127/gauge_metric_dropdown_308x176.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219988631/gauge_metric_dropdown.png)
