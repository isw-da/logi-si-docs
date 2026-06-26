---
title: "Dashboard Designer"
id: 4415492926487
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492926487-Dashboard-Designer
updated_at: 2021-12-10T03:10:26Z
---

# Dashboard Designer

# Dashboard Designer

The **Dashboard Designer** page allows users to:

|  |  |
| --- | --- |
| * select a preset layout * add report parts to a dashboard * customize dashboard layout * edit dashboard description and background * copy and move dashboard * switch to presentation mode | * configure sharing access * add subscriptions and scheduled delivery * print dashboard * email dashboard * dashboard filters |

## Create a New Dashboard

1. Click the plus icon (+) next to Dashboards to create a new one.
2. Select a preset layout from the pop-up.

   > User can always add and remove tiles in the preset layout
   > afterwards.
   >
   > [![../_images/Dashboard_Add_Icon_and_Preset_Layout.png](https://devnet.logianalytics.com/hc/article_attachments/4415504384919/dashboard_add_icon_and_preset_layout_635x344.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492479639/dashboard_add_icon_and_preset_layout.png)
3. Select to either create a “text” dashboard tile or include an existing report part in each one.

   [![../_images/Dashboard_Tiles_Report_Part_or_Text.png](https://devnet.logianalytics.com/hc/article_attachments/4415504385431/dashboard_tiles_report_part_or_text_600x200.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504385175/dashboard_tiles_report_part_or_text.png)
4. For a “text” dashboard tile, click the Configuration mode (page flip)
   icon to input the content.

   [![../_images/Text_Dashboard_Tile.png](https://devnet.logianalytics.com/hc/article_attachments/4415511743127/text_dashboard_tile_600x228.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504385815/text_dashboard_tile.png)

   1. Optionally enter a title and description.
   2. Click the gear icons (⚙) to format the title and description.
   3. The title and description are limited to one paragraph of text and
      simple formatting:
      * font face and font size.
      * text effects bold, italic, underlined.
      * font color and background color.
      * text alignment.
   4. Enter the content into Body Text.
   5. This section supports unlimited amount of text and more formatting
      options:
      * Bullet List and Numbering List.
      * Indented text.
5. For existing report part option, use the Report Part Selection pop-up to search and use an existing report part:

   1. Optionally specify a report category or sub-category.
   2. Type a partial text in Report Name to search for the containing
      report first.
   3. Other search options include Created By, Created Date, Last Edited
      By and Last Edited Date.
   4. Click Search to see the list of matching reports.
   5. Select a report to display the list of child report parts.
   6. Select the right report part and click OK to use it.

   [![../_images/Dashboard_Report_Part_Selection.png](https://devnet.logianalytics.com/hc/article_attachments/4415511743511/dashboard_report_part_selection_600x220.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504386199/dashboard_report_part_selection.png)
6. Repeat for other tiles then click Save at the top to save the dashboard.

Following is a sample dashboard with 3 tiles: a comparison column chart, detail grid and a text part for the summary:

[![../_images/Dashboard_Sample.png](https://devnet.logianalytics.com/hc/article_attachments/4415504386839/dashboard_sample_767x332.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504386455/dashboard_sample.png)

## Customize Dashboard Layout

The dashboard tiles can be added, copied, resized, moved around, swapped
in position and deleted.

1. Move the cursor over the title bar to see Copy, Configuration/View mode, Fullscreen and Delete buttons.
2. Switch the tiles back to View mode to be able to change the layout.
3. Place the cursor over the edges of dashboard tiles then click and drag to resize them.
4. Move the cursor over the title bar then drag to move the tiles.
5. Drag a tile onto another to swap them.
6. Click the Add Dashboard Tile button at the top to insert a new tile
   at the end.

![../_images/Dashboard_Tile_Title_Bar.png](https://devnet.logianalytics.com/hc/article_attachments/4415492480151/dashboard_tile_title_bar_405x43.png)

## Edit Dashboard

[![../_images/Dashboard_Edit_Menu.png](https://devnet.logianalytics.com/hc/article_attachments/4415504387351/dashboard_edit_menu_182x157.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492480407/dashboard_edit_menu.png)

The Edit menu allows user to:

* Set a description for the dashboard.
* Set background color.
* Set background image:
  1. Select Set Background Image to open Background Image Settings
     pop-up.
  2. Enter the url of the image.
  3. Choose to stretch or center the image.
  4. Click OK to close the pop-up.
* Copy or Move dashboard, this is similar to Report ([Copy a Report](https://devnet.logianalytics.com/hc/en-us/articles/4415504850839-Report-List#copy-a-report) and [Move a Report](https://devnet.logianalytics.com/hc/en-us/articles/4415504850839-Report-List#move-a-report)).
* Hide or show report part filter descriptions in dashboard.

## Switch to Presentation Mode

Click the Presentation button at the top to switch to Presentation mode.

> [![../_images/Dashboard_Presentation_Mode.png](https://devnet.logianalytics.com/hc/article_attachments/4415492483223/dashboard_presentation_mode_600x377.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504387607/dashboard_presentation_mode.png)

* In this mode, each dashboard tile takes turn being displayed for a
  configurable time.
* The sub toolbar allows user to configure the slide transition time
  and switch to fullscreen.

Note: Using report parts with short data refresh intervals together with presentation mode in fullscreen can effectively make up a live slide show dashboard.

## Configure Sharing Access

1. Click the Access button at the top to open Access screen.
2. Click the Add Sharing button to add a new sharing.
3. Select either Everyone, Role, or User from the Share With drop-down.
4. For Role or User, select a specific one from the drop-down.
5. Select a permission from Acces Right drop-down (See details in List
   of Access Rights table below).
6. Click Save button at the top to save the list.

[![../_images/Dashboard_Sharing_Access.png](https://devnet.logianalytics.com/hc/article_attachments/4415504388503/dashboard_sharing_access_600x166.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504387863/dashboard_sharing_access.png)

Table 7 List of Access Rights








| Interact with shared report | Full Access | Save As | Locked | View Only | No Access |
| --- | --- | --- | --- | --- | --- |
| **View the dashboard with filter interaction** | ✔ | ✔ | ✖ | ✔ | ✖ |
| **View the dashboard with NO filter interaction** | ✖ | ✖ | ✔ | ✖ | ✖ |
| **Save changes in the dashboard** | ✔ | ✖ | ✖ | ✖ | ✖ |
| **Save As changes in the dashboard** | ✔ | ✔ | ✖ | ✖ | ✖ |

Table 8 Access Rights Precendence (Higher Right covers lower ones)

| **Access Right** |
| --- |
| Full Access |
| Save As |
| Locked |
| View Only |
| No Access |

Another function of this screen is to change the Dashboard Owner (next
to the dashboard name):

1. Click the plus icon to open All Users pop-up.
2. Select either User Name, Email Address or Role to search for. Select All to search for all fields.
3. Type a partial name into the search box and click the search icon (🔍).
4. Only matching users will be displayed.
5. Select the user then click OK to close the pop-up.
6. Click Save button at the top to save the dashboard together with the owner.

## Add Subscriptions

1. Click the Subscribe button at the top to open Subscription screen.
2. Dashboard Subscription is similar to [Report
   List](https://devnet.logianalytics.com/hc/en-us/articles/4415504850839-Report-List#add-report-subscriptions-for-current-user).
3. Click the Subscribe button again to close Subscription screen.

## Add Scheduled Delivery

1. Click the Schedule button at the top to open Schedule screen.
2. Dashboard Schedule is similar to [Report
   Schedule](https://devnet.logianalytics.com/hc/en-us/articles/4415512103447-Report-Designer-Schedule).
3. Click the Schedule button again to close Schedule screen.

## Print Dashboard

1. Click the Print button at the top and select either HTML or PDF format to open Print pop-up.
2. Select print options in the left menu while the print preview is
   reflected on the right:

   * Select a target printer using Change button.
   * Select specific pages to print.
   * Increase the number of copies, then tick the Collate check-box to
     have the pages of each copy printed separately, instead of being
     mixed together.
   * Select a page layout Portrait or Landscape.
   * Select a paper size.

     ![../_images/Dashboard_Print_Options.png](https://devnet.logianalytics.com/hc/article_attachments/4415511744151/dashboard_print_options_233x608.png)
   * Select a margin option. In Custom mode, the margins in preview
     pane can be resized interactively.

     ![../_images/Dashboard_Print_Custom_Margins.png](https://devnet.logianalytics.com/hc/article_attachments/4415504389015/dashboard_print_custom_margins_500x211.png)
   * Select a print resolution in Quality drop-down: the higher the
     number of dpi, the clearer and more detailed output.
   * Select to print headers and footers or not.
   * Select to print background images or not.
3. For more advanced options, click the link Print using system
   dialog… to use the system Print dialog.

## Email Dashboard

The dashboard can be delivered via email on-demand (instead of Scheduled
Delivery) using the Email button:

1. Choose a delivery method Link or Embedded HTML to open Compose Email pop-up with the email template already populated.
2. Fill in the To, Subject and optionally CC boxes.
3. Optionally select the delivery method Link, Attachment or Embedded HTML.
4. Click OK to close the pop-up and send the email.

## Dashboard Filters

1. The filter section on the dashboard will only show common filters between all report parts used in the dashboard.
2. By default, common filters are defined as the same field from the same table in the same schema of the database utilizing the same filter operator.
3. Common filter definitions can be altered in Settings > Data Setup > Advanced Settings > Others > Determine common filter for the same field based on. The following options are available:

   * Same field of the same data object from the same database schema (Default)
   * Same field name regardless of database schema or connection string
   * Same alias name regardless of database schema or connection string

   **Notes:** From version 2.15.0, the Use Lookup checkbox states are also considered when determining dashboard common filter.
4. Stored procedures used in reports follow the same logic as above.
5. Any filters which are not common between all report parts are available on the back of the report part tile. The user can flip the tile and update results to change the filters for the specific report part.
6. Common filters query only one instance of a common filter (the first one in the dashboard), for data driven filters (checkbox, selection, tree, popup style filters where the user is presented data for selection). This means when Field A is common, based on rules set above, only the first instance of the field which is common will be queried to pull results for common filter data.
7. Common filter order in the dashboard is set by the top most left dashboard tile. The filters associated with this report will be used to set the order. This order will update when a new tile is added, a tile is removed, and on saving the dashboard. The order is not recalcualted as tiles are moved around on the dashboard.
