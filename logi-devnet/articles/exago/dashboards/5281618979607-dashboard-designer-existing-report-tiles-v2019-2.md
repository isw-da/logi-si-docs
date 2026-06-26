---
title: "Dashboard Designer: Existing Report Tiles (v2019.2+)"
id: 5281618979607
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281618979607-Dashboard-Designer-Existing-Report-Tiles-v2019-2
updated_at: 2022-05-03T22:09:12Z
---

# Dashboard Designer: Existing Report Tiles (v2019.2+)

# Dashboard Designer: Existing Report Tiles (*v2019.2+*)

Existing **ExpressViews**, **Advanced Reports**, or**CrossTab Reports** can be added to a **Dashboard**. Existing **filters** and **parameters** can be accessed and modified from the **Dashboard Designer**. Reports on Dashboards have most of the same interactivity as in the **[Report Viewer](https://devnet.logianalytics.com/hc/en-us/articles/5281541805591-Report-Viewer)**, with the exception of the interactive sorts/filters dock.

To add an existing report to a Dashboard, review [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-). Tiles can be added from the ![NewTileButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432328391575/newtilebutton.png)**New Tile** menu, or by dragging the report directly to the canvas from the ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)**Report Tree**.

In *v2021.1+:*

![F0GZnxsosm.png](https://devnet.logianalytics.com/hc/article_attachments/5432300185879/f0gznxsosm.png)

By default when the Refresh Reminder feature is enabled, a placeholder image is displayed in the tile until it is manually refreshed by clicking the Refresh icon

If the report has **prompting filters** or **parameters** on it, these items can be modified in the corresponding **Filters**![FilterMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432253309335/filtermenu.png)and **Parameters ![ParametersMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432356157463/parametersmenu.png)**menus in the top toolbar. Review [Dashboard Designer: Filters (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281602706327-Dashboard-Designer-Filters-v2019-2-) and [Dashboard Designer: Parameters (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281588292887-Dashboard-Designer-Parameters-v2019-2-).

## Tile Properties Pane

Controls for building and interacting with the **Existing Report** tile are contained in the **Tile Properties Pane** on the right side of the screen. Click on the tile to select it and the Tile Properties Pane will fill with the properties for the selected tile.

### Content

The **Content** tab for existing reports allows the report in the tile to be changed. Select the report from the list, and then click **Apply**. Only reports of the same type as the existing tile can be selected. For example, a tile which shows an ExpressView can only be changed to another ExpressView.

If an ExpressView is selected, the **Suppress Tabular Detail Rows** (*pre-v2021.1*) checkbox will be displayed at the bottom of the pane. Check this checkbox to hide all of the data detail rows when the ExpressView is in tabular view mode.

![suppressrows.png](https://devnet.logianalytics.com/hc/article_attachments/5432371023255/suppressrows.png)

**ExpressView** in tabular view mode, showing suppressed tabular detail on the left, and unsuppressed tabular detail on the right

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Adding an existing report tile or changing the name of the report contained in the tile will require a **Refresh** of the tile’s contents if the Refresh Reminder feature is enabled in *v2021.1*.

### Style

#### ExpressView

The Style tab for ExpressViews contains the **Tile** and **Fit**sections. This is how this tile appears on the canvas is changed. The settings here override the **Canvas Format** defaults.

* v2021.1.6+ Setting a **Minimum Column Width** prevents columns of the ExpressView from shrinking below a set number of pixels wide. A column that starts off less than this value (in the report design itself, for example) won’t expand to this value. Instead, originally narrow columns will use their own starting width as the minimum column width. If all of the columns are wider than the space available in the tile, a horizontal scroll bar appears. The default value is *100*.
* Check **Background** to set a background color for the tile. Click **Color** to open the color selector and choose a background color. Unchecking the **Background** checkbox makes the tile transparent.
* Check **Tile Header** to set a background color for the tile’s header. Click **Color** to open the color selector and choose a background color. Unchecking the **Tile Header** checkbox makes the header background transparent.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > The Tile Header options are only shown if the Tile Header is visible on the canvas.
* Check **Shadow** to show a slight shadow effect around the tile.
* Check **Border** to apply a border to the tile.
  + Check **Customize Border** to set the properties of each of the four tile borders individually. Leave unchecked to have the border properties applied equally to the four sides.
  + Click **Color** to open the color selector and choose a border color.
  + **Width** sets the border width in pixels.
  + **Round** sets the roundness of the corners.

#### Other Report Types

The **Style** tab is broken down into two areas for other kinds of reports: **Fit** and **Tile**.

The **Fit** section determines how contents of the report are presented in the tile.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Changing this setting will require a **Refresh** of the tile’s contents.

* *Responsive Report Height* will change the height of rows based on the size of the tile so that when the tile is expanded, the rows will fill the available space.
* *Keep Original* *Report Cell Heights* will not change the row height when the tile size is changed.
* v2021.1.6+ Setting a **Minimum Column Width** prevents columns of the report from shrinking below a set number of pixels wide. A column that starts off less than this value (in the report design itself, for example) won’t expand to this value. Instead, originally narrow columns will use their own starting width as the minimum column width. If all of the columns are wider than the space available in the tile, a horizontal scroll bar appears. The default value is *100*.

The **Tile** section is where tile appearance can be changed. The settings here override the **Canvas Format** defaults.

* Check **Tile Header** to set a background color for the tile’s header. Click **Color** to open the color selector and choose a background color. Unchecking the **Tile Header** checkbox makes the header background transparent.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > The Tile Header options are only shown if the Tile Header is visible on the canvas.
* Check **Shadow** to show a slight shadow effect around the tile.
* Check **Border** to apply a border to the tile.
  + Check **Customize Border** to set the properties of each of the four tile borders individually. Leave unchecked to have the border properties applied equally.
  + Click **Color** to open the color selector and choose a border color.
  + **Width** sets the width in pixels of the border.
  + **Round** sets the roundness of the border corners.

### Advanced

The **Advanced Tab** for **Existing Reports** is further broken down into two areas: **Refresh** and **Navigation**.

**Refresh** contains:

* **Designer**pre-v2021.1
  + **Refresh report when changes are made**: check the checkbox to reload the data on the report whenever changes are made to the tile in the Designer. The report will always refresh when the Dashboard Designer is opened and when the tile is manually refreshed with the Tile Menu or the **Refresh ![DashboardRefresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432239300119/dashboardrefresh.png)** icon on the toolbar. Not available if the tile contains an **ExpressView**.
* **Viewer** — check the box to enable automatic refreshing of the data in the [Dashboard Viewer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281602922903-Dashboard-Viewer-v2019-2-). Check the box and then set the number of seconds in between report refreshes. Uncheck the box to disable automatic report refreshing.

**Navigation** contains additional options for controls which will be displayed in the tile when the report is run.

* **Allow searching**: check the checkbox to add a search box at the bottom of the tile that can search the report for data.
* **Allow scrolling**: will only be shown if the tile contains an **Advanced Report**. Check the checkbox to add scroll bars to the tile if the report contents extend beyond the bounds of the tile.
* **Table/chart toggle button**: will only be shown if the tile contains an **ExpressView**. Check the checkbox to include toggle buttons that allow switching between the visualization display mode and the tabular display mode. When unchecked, the toggle buttons are hidden.
