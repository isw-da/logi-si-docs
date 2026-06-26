---
title: "Control How Users Interact With a Visual"
id: 34933282294029
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933282294029-Control-How-Users-Interact-With-a-Visual
updated_at: 2026-05-26T22:08:50Z
---

# Control How Users Interact With a Visual

# Control How Users Interact With a Visual

You can control how users can interact with a visual. You can control their ability to:

* Change metrics, rulers, colors, visual styles, or otherwise modify a visual
* Group, filter, or sort visual data
* Use context menu options
* Copy, export, or delete the visual
* Create keysets from visual data
* Export visual data
* Integrate a visual into external applications
* Change the defaults set for a visual in the data source configuration visual defaults

**Important:** 
User attributes are not resolved when previewing interactivity settings, and default fallbacks will be used in the Preview mode.

You can control user interactivity using the interactivity sidebar of a visual from the Visual Gallery.

**Note:** 
Individual visual interactivity settings can be overridden by [dashboard interactivity](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814650893-Control-How-Users-Interact-With-a-Dashboard) settings. When a dashboard overrides the interactivity settings specified for an individual visual, the visual's interactivity settings are not changed, but they are ignored, and the visual interactivity settings specified by the dashboard are used.

**Note:** 
You can include several controls for embedded visuals, allowing users to select and deselect favorite visuals, as well as filter the list of visuals in the embedded Visual Gallery by favorite status. See [Use the Visual Gallery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933265735565-Use-the-Visual-Gallery).

Control user interactions with a visual

1. Select the visual in the Visual Gallery.
2. Select the interactivity option (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167804826893)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual. The interactivity sidebar opens.

   ![use to define interactive options for your visuals](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166916730381 "Interactivity sidebar menu, visuals")

   By default, all interactivity settings are activated (on) for a visual. Each interaction is controlled by a switch. Slide the switches to the right to turn a setting on; slide them to the left to turn the setting off.

   In addition, you can use the **Preview Interactivity Settings** option to test the visual interactivity settings. When this switch is turned on, the visual behaves as it will when it is embedded. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the visual. It is not saved with the visual; so if you turn it on and save the visual, it will still be off the next time you edit the visual.

   Each visual interactivity setting is described in the following table.

   | Visual Feature Group | UI Setting | JavaScript Setting | Controls the ability to... |
   | --- | --- | --- | --- |
   | **Data Interactivity** | Metrics | `METRICS` | Change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932886385037-Metrics) in a table. |
   | Group | `GROUPING` | Change the **Group** field on the x-axis of the visual. This setting also controls whether a user can group tables. |
   | Filter | `FILTER` | Filter data using the **Filter** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) and to the left of the visual name on a visual, or a display name if viewed in a dashboard. (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Context Menu settings on the interactivity sidebar too.) |
   | Sort | `SORT` | Sort and limit the data in a visual. The sort and limit () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar. |
   | Format | `FORMAT` | [Format specific data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933268999949-Format-Numeric-Table-Data-Using-the-Table-Context-Menu) in a visual. These formatting options are disabled when the switch is off. |
   | **Context Menu** | Zoom | `ZOOM_ACTION` | Zoom into a selected data point on a visual using the **Zoom** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). |
   | Filter | `FILTER_ACTION` | Filter data using the **Filter** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Data Interactivity settings on the interactivity sidebar too.) |
   | Details | `DETAILS_ACTION` | Display additional information about a specific visual data element using the **Details** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). |
   | Trend | `TREND_ACTION` | View trends for a selected data point using the **Trend** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). |
   | Keyset | `KEYSET_ACTION` | Create a keyset from a selected data point using the **Keyset** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** switch in the Visualization settings on the interactivity sidebar too.) |
   | Actions | `ACTIONS_ACTION` | Invoke an action using the **Actions** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Visualization settings on the interactivity sidebar too.) |
   | Link | `LINK_ACTION` | Link to another dashboard using the **Link** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). |
   | **Visualization** | Settings | `SETTINGS` | Specify settings for the visual. The visual settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual settings sidebar. |
   | Rulers | `RULERS` | Add visual reference lines and customize the markers used on the metric axis. The ruler settings () [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the ruler sidebar. |
   | Colors | `COLORS` | Change the color palette used by the visual. The color settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the color sidebar. |
   | Conditional Formatting | `CONDITIONAL_FORMATTING` | Apply conditional formatting to data in the visual. The conditional formatting () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when disabled. |
   | Create Keyset | `KEYSET` | Create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Keyset** switch in the Context Menu settings on the interactivity sidebar too.) |
   | Save | `SAVE` | Save the visual. |
   | Save As | `SAVE_AS` | Save the visual using a new name. |
   | Copy | `COPY` | Copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). |
   | Actions | `ACTIONS` | Invoke an action using the **Actions** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Context Menu settings on the interactivity sidebar too.) |
   | Remove | `REMOVE` | Remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). |
   | Visual Style | `VISUAL_STYLE` | Change the style of a visual. The visual style settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual type sidebar. |
   | Select Time Bar Field | `TIMEBAR_FIELD` | Change the time field on the [time bar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933204115725-Use-the-Time-Bar). |
   | Maximize | `MAXIMIZE` | Maximize a visual for optimal viewing. |
   | Rename | `RENAME` | Rename a visual. |
   | Show Time Bar Panel | `TIMEBAR_PANEL` | Show the [time bar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933204115725-Use-the-Time-Bar) for the visual. |
   | Info | `INFO` | Allow users to edit information in the Info sidebar menu. |
   | **Exporting** | Export to PNG/PDF | `EXPORT_PNG_PDF` | Export a visual to PNG/PDF using the **Export** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). |
   | Export to CSV | `EXPORT_CSV` | Export a visual to a CSV file using the **Export** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). |
   | Export to XLSX | `EXPORT_XLSX` | Export a visual to an XLSX file using the **Export** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). |
3. Slide the switches on or off for the interactivity settings you want to change.
4. Optionally, preview the behavior with the interactivity settings applied. Slide the **Preview Interactivity Settings** switch on (to the right).
5. Select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167815862413) to save the visual.
