---
title: "Report Designer/Map"
id: 12528284448791
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528284448791-Report-Designer-Map
updated_at: 2023-02-23T15:01:58Z
---

# Report Designer/Map

# Report Designer/Map

Map is a built-in type of report part that displays data on geographic maps, ranging from world map to continent and country maps.

## Configure Report Part Properties for Map

1. Select the chart in Report Body (See [Manage Report Parts](https://devnet.logianalytics.com/hc/en-us/articles/12528284369047-Report-Designer-Design#_bm2) for how to add a chart).
2. Click the expand icon (<) on the right to open the Properties boxes if needed.
3. Select the vertical Report Part Properties box.
4. The properties are listed in Report Part Properties box in 6 sections
   * General Info
   * Map
   * Labels
   * Legends
   * Data
   * View

![../_images/Report_Part_Properties_for_Map.png](https://devnet.logianalytics.com/hc/article_attachments/12528204302999/report_part_properties_for_map_245x602.png)

User can configure the properties and see changes reflected in Preview pane:

* Select a type in Map Type drop-down.

  + World
  + Continent
  + Country

  ![../_images/Report_Map_Border_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528204307095/report_map_border_settings_454x404.png)

  Configure border settings:

  1. In Map group, click the gear icon (⚙) to open Border Settings pop-up.
  2. Choose the border to be visible or not.
  3. Select a border color.
  4. Select a dash style.
  5. Select the border thickness (in pixels).
  6. Click OK to close the Border Settings pop-up.

  ![../_images/Color_Theme_Selection.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528204311191/color_theme_selection_604x447.png)
* Configure color theme settings:

  1. In Map group, click the gear icon (⚙) next to the Color Theme option to open Color Theme Selection pop-up.
  2. Select a color theme and click OK to the pop-up.

  **Note:**When System Admin change the [Default Color Setting](https://devnet.logianalytics.com/hc/en-us/articles/12528299389591-System-Configuration-Report#set-default-color-theme), all report parts using the default color theme will update properly.

  ![../_images/Report_Map_Background_Color_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528204325271/report_map_background_color_settings_455x406.png)

  Set the background color.

  1. In Map group, click the gear icon (⚙) to open Map Background Color Settings pop-up.
  2. Select a background color.
  3. Choose to apply the color to the entire map (covering the legend Sum(Freight)) or to the plot area only (covering the map only).
  4. Click OK to close the Map Background Color Settings pop-up.

  ![../_images/Report_Map_Labels_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528220193815/report_map_labels_settings_246x166.png)
* Configure the text direction for the labels.
* To be updated: Hover Labels
* To be updated: Show Map Labels
* Configure the legends.

  [![../_images/Report_Map_Legend_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528220199447/report_map_legend_settings_684x424.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204340119/report_map_legend_settings.png)
* Choose to display values of data points or not.

  [![../_images/Report_Map_Data_Show_Value_Labels.png](https://devnet.logianalytics.com/hc/article_attachments/12528204351127/report_map_data_show_value_labels_635x284.png)](https://devnet.logianalytics.com/hc/article_attachments/12528220204055/report_map_data_show_value_labels.png)
* To be updated: Zoom into a region of the map.

  ![../_images/Report_Designer_Data_Refresh_Interval.png](https://devnet.logianalytics.com/hc/article_attachments/12528202610327/report_designer_data_refresh_interval_455x259.png)
* Configure how often data is refreshed when report is being viewed.

  1. Click the gear icon (⚙) to open Data Refresh Interval Settings pop-up.
  2. Choose to have data refreshed automatically or manually.
  3. Enter an interval between each refresh (in seconds).
  4. Choose to view all data or enter a number to view that specific number of latest records only.

Note: If the **Show Preview section in Configuration Mode** checkbox (In Others tab in Advanced Settings) is unticked then The Preview section will not be displayed for following pop-ups:

> - Map Border Settings   
> - Map Background Color Settings   
> - Legend Settings   
> - Zoom Settings
>
> [![../_images/Report_Map_Border_Settings_No_Preview.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528220218519/report_map_border_settings_no_preview_464x294.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204356631/report_map_border_settings_no_preview.png)

Please see [Update Others Settings](https://devnet.logianalytics.com/hc/en-us/articles/12528299314327-Advanced-Settings#advanced-settings-others) for more details.

## Others

* Grid view pop-up option. This option is available from version 2.10.0.

  Click ![gridViewIcon](https://devnet.logianalytics.com/hc/article_attachments/12528218934551/grid_view_icon.png) icon to see the grid view of the map data associated with the current metric.

  [![../_images/Map_Grid_View_Popup.png](https://devnet.logianalytics.com/hc/article_attachments/12528204376215/map_grid_view_popup_653x226.png)](https://devnet.logianalytics.com/hc/article_attachments/12528220224919/map_grid_view_popup.png)

* Metric drop-down.

> [![../_images/Map_Metric_Dropdown.png](https://devnet.logianalytics.com/hc/article_attachments/12528220234391/map_metric_dropdown_308x228.png)](https://devnet.logianalytics.com/hc/article_attachments/12528204378263/map_metric_dropdown.png)
