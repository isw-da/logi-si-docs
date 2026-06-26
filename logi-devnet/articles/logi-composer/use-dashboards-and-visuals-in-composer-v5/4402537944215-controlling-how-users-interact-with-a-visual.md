---
title: "Controlling How Users Interact With a Visual"
id: 4402537944215
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual
updated_at: 2021-09-15T02:23:14Z
---

# Controlling How Users Interact With a Visual

# Controlling How Users Interact With a Visual

You can control how users can interact with a visual. You can control their ability to:

* Change metrics, rulers, colors, visual styles, or otherwise modify a visual
* Group, filter, or sort visual data
* Use radial menu options
* Copy, export, or delete the visual
* Create keysets from visual data
* Export visual data
* Integrate a visual into external applications
* Change the defaults set for a visual in the data source configuration visual defaults.

This is useful in embedded use cases where the analytic on the parent application page needs to behave in a consistent manner with the rest of the application. These controls are managed on the interactivity sidebar for the visual.

To control user interactions with a visual:

1. Select the visual on the dashboard or in the Visual Gallery.
2. Select the interactivity option (![](https://devnet.logianalytics.com/hc/article_attachments/4406753439895/sidebar-interactive.png)) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual. The interactivity sidebar opens.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763903255/sidebar-interactivity_192x566.png)

   By default, all interactions are activated (on) for a visual. Each interaction is controlled by a toggle switch. Slide the toggle switches to the right to turn an interaction on; slide them to the left to turn the interaction off.

   Each interaction setting is described in the following table.

   | Visual Feature Group | Setting | Controls the ability to... |
   | --- | --- | --- |
   | **Data Interactivity** | Metrics | Change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. |
   | Group | Change the **Group** field on the x-axis of the visual. |
   | Filter | Filter data using the **Filter** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) and to the left of the visual title. (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** toggle in the Radial Menu settings on the interactivity sidebar too.) |
   | Sort | Sort and limit the data in a visual. The sort and limit () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) option is disabled when this toggle is off and you cannot access the Sort & Limit sidebar. |
   | **Radial Menu** | Zoom | Zoom into a selected data point on a visual using the **Zoom** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). |
   | Filter | Filter data using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** toggle in the Data Interactivity settings on the interactivity sidebar too.) |
   | Details | Display additional information about a specific visual data element using the **Details** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). |
   | Trend | View a trends for a selected data point using the **Trend** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). |
   | Keyset | Create a keyset from a selected data point using the **Keyset** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** toggle in the Visualization settings on the interactivity sidebar too.) |
   | Actions | Invoke an action using the **Actions** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** toggle in the Visualization settings on the interactivity sidebar too.) |
   | Link | Link to another dashboard using the **Link** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). |
   | **Visualization** | Settings | Specify settings for the visual. The visual settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) option is disabled when this toggle is off and you cannot access the visual settings sidebar. |
   | Rulers | Add visual reference lines and customize the markers used on the metric axis. The ruler settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) option is disabled when this toggle is off and you cannot access the ruler sidebar. |
   | Colors | Change the color palette used by the visual. The color settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) option is disabled when this toggle is off and you cannot access the color sidebar. |
   | Create Keyset | Create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Keyset** toggle in the Radial Menu settings on the interactivity sidebar too.) |
   | Copy | Copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). |
   | Export | Export a visual using the **Export** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). |
   | Actions | Invoke an action using the **Actions** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** toggle in the Radial Menu settings on the interactivity sidebar too.) |
   | Defaults | Specify defaults for a visual at the data source level using the **Defaults** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). |
   | Remove | Remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). |
   | Visual Style | Change the style of a visual. The visual style settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) option is disabled when this toggle is off and you cannot access the visual type sidebar. |
   | Select Time Bar Field | Change the time field on the [time bar](https://devnet.logianalytics.com/hc/en-us/articles/4402537901591-Use-the-Time-Bar). |
3. Slide the toggle switches on or off for the interactions you want to change. The visual is immediately updated.
