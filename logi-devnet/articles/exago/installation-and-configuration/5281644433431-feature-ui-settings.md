---
title: "Feature/UI Settings"
id: 5281644433431
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281644433431-Feature-UI-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Feature/UI Settings

# Feature/UI Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Feature/UI Settings**.

---

## Introduction

The **Feature/UI settings** allow administrators to hide various features in the user interface. As each heading indicates, settings may apply to specific report types or the entire application.

## Settings

The parameters are broken up into several sub-sections:

* Available Report Types
* ExpressView Settings
* Express Report Designer Settings pre-v2019.2
* Advanced Report Designer Settings
* Dashboard Report Designer Settings
* Common Settings

### Available Report Types

These settings enable/disable report types.

#### Allow Creation/Editing of Express Reports pre-v2019.2

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

Enables/Disables the Express Report wizard.

#### Allow Creation/Editing of Advanced Reports

Enables/Disables the Advanced Report Wizard and Report Designer

#### Allow Creation/Editing of CrossTabs

Enables/disables the creation of new CrossTab reports from the main menu.

When *False*, the **Show CrossTab Wizard** setting will appear under Advanced Report Designer Settings, permitting CrossTabs to be enabled/disabled separately in the Advanced Report Designer.

#### Allow Creation/Editing of Dashboards

Enables/Disables the Dashboard Designer.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Both **Allow Creation/Editing of Dashboards** and **General** > **Main Settings** > **Allow Execution in Viewer** must be *True* to enable the Dashboard Designer.

#### Allow Creation/Editing of Chained Reports

Enables/Disables the Chained Report wizard.

#### Allow Creation/Editing of ExpressViews

Enables/Disables the ExpressView designer.

### ExpressView Settings

These settings only apply to the ExpressView designer.

#### Allow Editing ExpressView with Live Data

When *True*, users are allowed to make changes to an ExpressView when the in Live Data (**Run**) mode. When *False*, users must click the **Stop** button on the toolbar before changes may be made.

The default value is*false* for *pre-v2021.1.1* or*true* for *v2021.1.1+*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Prior to *v2021.1.1* we recommend setting this to *False*. Editing live ExpressViews will cause an increase in Data Source requests, and may reduce performance.

#### Fields Enabled in Data Fields Tree v2017.1.2+

This setting controls whether users are allowed to add fields to an ExpressView that are not directly joinable to another field on the report.

* **All joinable fields** (*default*): Users can add any fields with a join path to existing report fields.
* **Direct joins only**: Users can only add fields with a direct join to an existing report field.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> As of *v2018.1.23+*, the join algorithm has been modified for ExpressViews with **Direct joins only** enabled. The **Disable Non-Joined Data Objects**database setting is now taken into consideration when generating a join path, allowing these ExpressViews to properly analyze join weight and encompass constructed SQL.

#### Join Path Algorithm

Select the join path algorithm to use when running ExpressViews with multiple data objects.

* **Standard** (*default*): More performant in most cases.
* **Legacy**: Select if you are experiencing issues with ExpressViews created in an older version.

#### ExpressView Tutorial v2018.2–v2020.1

Enables an instructive tutorial guide using ExpressViews to guide new users through the process of building an ExpressView report. The user can opt out during the course of the tutorial.

#### ExpressView Hints v2018.2–v2020.1

Enable context-sensitive hints when using different features in ExpressViews.

### Express Report Designer Settings pre-v2019.2

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was removed from the [Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console) in *v2019.2* but remains available here in the config file. No other functionality was removed.

These settings only apply to the Express Report wizard.

#### Show Styling Toolbar

Enables/Disables the styling tools in the Layout tab of the Express Report wizard.

#### Show Themes

Enables/Disables the Theme dropdown in the Layout tab of the Express Report wizard.

#### Show Grouping

Enables/Disables the grouping tools in the Layout tab of the Express Report wizard.

#### Show Formula Button

Enables/Disables the formula editor button in the Layout tab of the Express Report wizard.

### Advanced Report Designer Settings

These settings only apply to the Advanced Report designer.

#### Show CrossTab Wizard

If Allow Creation/Editing of CrossTabs in Available Report Types is *False*, this option becomes available. When Allow Creation/Editing of CrossTabs is *True*, this option is hidden from view in the Admin Console.

Set to *True* to allow CrossTab widgets to be added to Advanced Reports in the Designer, or *False* to completely disable the creation of CrossTabs in the application.

#### Show Chart Wizard

Enables/disables the **Chart Wizard**![Chart.png](https://devnet.logianalytics.com/hc/article_attachments/5432233083031/chart.png) icon in the toolbar (*pre-v2021.1*) or from the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu (*v2021.1+*). Set to *False* to disable users from creating or editing charts.

#### Chart Colors

Lists the values used for default chart colors, except for heatmap charts. Hexadecimal values should be separated by commas or semicolons.

#### Heatmap Chart Colors v2020.1.3+

Lists the values used for default heatmap chart colors, either as CSS color names or hexadecimal color codes with a leading # sign. Values must be separated by commas or semicolons. This list of colors will be applied to a heatmap when selecting *Default* from the **Theme** dropdown in the chart wizard.

#### Maximum Number of Chart Data Points

Upper limit on the number of data points visible on a chart. If the limit is exceeded, a warning will be displayed to the user. Charts with large numbers of data points could cause browser performance issues.

#### Default Chart Font

Specifies a default font for charts created in the Advanced Report Designer. This setting can be overridden on a per-Report basis. Does not apply to ExpressView charts or Dashboard visualization tiles.

#### Show Geochart Map Wizard

Enables/Disables the**GeoCharts**  ![Map.png](https://devnet.logianalytics.com/hc/article_attachments/5432233146519/map.png) icon in the toolbar (*pre-v2021.1*) or from the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu (*v2021.1+*). Set to *False* to disable users from creating or editing GeoCharts.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The first time Show Geochart Map Wizard is set to true a dialog appears prompting you to accept the terms of using the Google Charts API. Type “I accept” in the first box and your full name in the second to accept the terms and enable mapping.

#### GeoChart Map Key

Optional Google Maps license key for GeoCharts permissions. License must contain the **Google Maps JavaScript API** service. See **Legacy Maps (GeoCharts)** for more information.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Due to a change in Google’s Maps API Terms of Service, if geocharting was enabled after June 2016, or if geocharting had been enabled before, but changed your host domain name after June 2016, you need a license key to use this feature.

#### Geochart Map Colors

List the values used for default Geochart map colors. Hexadecimal values or CSS color names should be separated by commas (or semicolons).

#### Show Google Map Wizard

Enables/Disables the**Google Maps**  ![GoogleMaps.png](https://devnet.logianalytics.com/hc/article_attachments/5432124975895/googlemaps.png) icon in the toolbar (*pre-v2021.1*) or from the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu (*v2021.1+*). Set to *False* to disable users from creating or editing Google Maps.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> In order to use Google Maps, a license key must be obtained from Google, a polygon file must be downloaded from our [support site](https://support.exagoinc.com/hc/en-us/categories/202053837). and the Exago server must have an Internet connection. See [Installing Optional Features](https://devnet.logianalytics.com/hc/en-us/articles/5281627357079-Installing-Optional-Features)

#### Google Map Key

License key for Google Maps permissions. This is required to use the new Google Mapping feature. License must contain the **Google Maps JavaScript API** and **Geocoding API** services. See **Google Maps** for more information.

#### Google Map Key (unlimited or JS API restricted)

License key for Google Maps permissions. Must contain either:

* Google Maps **JavaScript API** and **Geocoding API** services, unlimited key.
* Google Maps **JavaScript API** service, limited key with referrer URLs. If this is the case, supply a limited **Geocoding API** service key in the following field.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When upgrading from a version prior to *v2018.1*, the value previously supplied for the Google Map Key will appear here.

#### Google Map Key (optional Geocode API restricted)

License key for Google Maps permissions. If the previous field contains a key limited to the **JavaScript API** service, supply a limited **Geocoding API** service key in this field, given server IP addresses. Otherwise leave this blank.

#### Google Map Colors

List the values used for default Google map colors. Hexadecimal values or CSS color names should be separated by commas or semicolons.

#### Show Gauge Wizard

Enables/Disables the **Gauge Wizard**  ![Gauge.png](https://devnet.logianalytics.com/hc/article_attachments/5432233271959/gauge.png) icon in the toolbar (*pre-v2021.1*) or from the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu (*v2021.1+*). Set to *False* to disable users from creating or editing gauges.

#### Gauge Colors

List the values used for default gauge colors. Hexadecimal values or CSS color names should be separated by commas (or semicolons).

#### Show Document Template

Enables/Disables working with document templates. Set to *False* to disable users from using the Document Template menu.

#### Show Document Template Upload Button

Set to *True* to allow users to upload document template files from their local computer. Set to *False* to prevent users from uploading Document Templates.

#### Show Linked Report

Enables/Disables the **Linked Report**![LinkedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432125018135/linkedreport.png)icon in the toolbar. Set to *False* to disable users from linking reports.

#### Show Linked Report Fields

Enables/Disables the Fields tab in the Linked Report dialog.

#### Show Linked Report Formula

Enables/Disables the Formula tab in the Linked Report dialog.

#### Show Linked Action

Enables/Disables the **Linked Action Event**![LinkedAction.png](https://devnet.logianalytics.com/hc/article_attachments/5432185689239/linkedaction.png) icon. When *True*, users will be able to add **Action Events** to reports.

#### Show Auto Sum Button v2021.1+

Enable/disable the **AutoSum**![Sum.png](https://devnet.logianalytics.com/hc/article_attachments/5432230783511/sum.png)icon in the Advanced Report Designer’s toolbar. The default value is *False*.

#### Show Insert Image

Enables/Disables the**Image**  ![InsertPicture.png](https://devnet.logianalytics.com/hc/article_attachments/5432244444695/insertpicture.png) icon in the toolbar (*pre-v2021.1*) or from the **Insert**![Insert.png](https://devnet.logianalytics.com/hc/article_attachments/5432182571543/insert.png)![DropDownArrow2.png](https://devnet.logianalytics.com/hc/article_attachments/5432176827159/dropdownarrow2.png) menu (*v2021.1+*). Set to *False* to disable users from inserting images.

#### Show Joins Window

Enables/Disables the Joins menu under **Advanced Options**. Set to *False* to disable users from modifying joins.

#### Show Advanced Joins

Enables/Disables additional options in the Joins menu. Set to *True* to enable advanced users to create, delete, and modify joins.

#### Advanced Joins Display v2017.3.1+

Select whether to show complex join options in the report Joins menu.

* *Complex* — allow users to modify join operators and expressions, and allow conjoining clauses.
* *Standard* — only permit joining data columns on equality.

#### Allow Category Aliasing v2017.3.1—2020.1

#### Allow Data Object Aliasing v2021.1+

Category renamed Data Object aliasing allows users to add categories multiple times on the same report. This may be necessary for some advanced join operations.

#### Show Events Window

Enables/Disables the Events item under **Advanced Options**. Set to *True* to allow users to apply Server Event Handlers in the report. See **Server Events** for more information.

#### Show Report-Level Parameters Window v2019.1.3+

Enables/Disables the Parameters item under **Advanced Options**. Set to *True* to allow users to view system-parameters and define their own report-level parameters for use within reports. See [Advanced Options](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options).

#### Show SQL Window

Enables/Disables the Show Generated SQL menu under **Advanced Options**. Set to *True* to allow users to view the SQL that will be sent to the data sources upon execution. See [Advanced Options](https://devnet.logianalytics.com/hc/en-us/articles/5281548966167-Advanced-Options).

#### Show Linked Reports in New Tab pre-v2017.3

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **Show Linked Reports in New Tab** flag has been replaced with the Linked Report Display setting as of *v2017.3*.

Specify how to display Linked Reports. Set to *True* to open Linked Reports in a new tab. Set to *False* to display Linked Reports in a floating window above the parent report.

#### Linked Report Display v2017.3+

Specify where to display drilldowns for linked reports.

* *Cursor —* a popup window appears at the mouse cursor
* *New Tab —* the linked report opens in a new user interface tab
* *Center of screen —* a popup window appears at the center of the screen

#### Allow Grouping on Non-Sorts

Enables/disables users to create groups on non-sort formulas.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Grouping on non-sort formulas is deprecated and unsupported.

#### Allow Creation of Custom SQL Objects v2018.1+

Allow end-users to write custom SQL objects at the report level.

#### Data Sources to Exclude from Custom SQL Creation v2018.1+

When Allow Creation of Custom SQL Objects is enabled, enter the data sources to exclude from Report-Level SQL. Write each data source in double quotation marks (“), and separate sources by a comma (,). Example: `"Northwind","AdventureWorks"`.

### Dashboard Report Designer Settings

These settings only apply to the Dashboard designer. If Allow Creation/Editing of Dashboards is *false* these settings will be ignored.

#### Prompt user for Parameters/Filters on Execution

Default setting indicating whether to prompt the user for filter and/or parameter values when executing a Dashboard. The option can be overridden on an individual Dashboard in the Options menu.

#### Automatically Refresh Reports v2021.1+

In the Dashboard Designer, enable/disable automatically loading data into the tiles, requiring the end user to manually refresh the tile in order to see any data in it.

When *True*, reports and visualization tiles will automatically load data when the Dashboard Designer is first opened, and whenever changes are made to the Dashboard or the tiles on the canvas. This is the *pre-v2021.1* behavior.

When *False*, reports and visualization tiles will display placeholder data until either the **Refresh**![DashboardRefresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432239300119/dashboardrefresh.png) icon on the tile, or the **Refresh**![DashboardRefresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432239300119/dashboardrefresh.png) icon on the Designer’s toolbar is explicitly clicked. If changes are made to the Dashboard or the tile, a notification icon will appear in the tile and toolbar. By limiting the frequency of calls to the Data Sources and execution engine, responsiveness of the Dashboard Designer can increase especially for very complex and data intensive Dashboards.
This functionality is referred to as the **Refresh Reminder** feature in the Dashboards documentation. When *False*, the default value, tiles do not automatically load and therefore the Refresh Reminder feature is enabled.

#### Show URL Item Button

Display/Hide the URL item in the New Tile Menu of the Dashboard Designer. When *False*, users will not be able to add URL tiles to the Dashboard canvas.

#### Allow Creation/Editing of Dashboard Visualizations

Display/Hide the Visualization item in the New Tile Menu and Tile Properties Pane of the Dashboard Designer.

#### Use Sample Data for Dashboard Visualization Design pre-v2019.2

Set to *True* to use sample data while creating and editing Dashboard Visualizations. This will reduce the number of calls to the database. Set to *False* to query the Data Source for each change made while editing Dashboard Visualizations.

#### Visualization Database Row Limit pre-2017.2

Maximum number of rows returned on a queries made by Data Visualizations. This only applies to Tables, Views and Functions. Set to 0 to return all rows.

#### Refresh Reports/Visualizations on Dashboards Silently

Set to *True* to disable the refresh hourglass animation for timed automatic Dashboard reloads.

#### Minimum Tile Width for Dashboard Reflow v2019.1+

Specifies the minimum width a tile will be drawn when Dashboard Reflow is enabled. Please see the **Canvas** section of the **Dashboard Designer** topic for more information.

#### Minimum Window Width for Dashboard Reflow v2019.1+

Specifies the minimum window size where Dashboard Reflow will begin to take effect. Please see the **Canvas** section of the **Dashboard Designer** topic for more information.

### Common Settings

#### Default Designer Font

Specifies a default font for reports created in the Advanced Report Wizard, Express Report Wizard, Advanced Report Designer and Dashboard Designer. This setting can be overridden on a per-report basis.

End-users must have the selected font installed locally in order to display. Otherwise, Exago will default to Sans Serif.

#### Default Designer Font Size

Specifies a default font size for reports created in the Advanced Report Wizard, Express Report Wizard, Advanced Report Designer, and Dashboard Designer. This setting can be overridden on a per-report basis. Does not apply to CrossTabs.

#### Show Help Button

Enables/Disables the **Help**![Help.png](https://devnet.logianalytics.com/hc/article_attachments/5432233043223/help.png) icon in the top right corner of the user interface. Set to *False* to disable users from accessing the context-sensitive help system.

#### Custom Help Source

Specifies the URL that contains custom context-sensitive help content. See [Custom Context Sensitive Help](https://devnet.logianalytics.com/hc/en-us/articles/5281597846295-Custom-Context-Sensitive-Help).

#### Show Exports in Tab

Set to *True* to open PDF reports in an Exago tab. Set to *False* to prompt the user to download the PDF.

#### Show IE Download Button

Set to *True* if Internet Explorer is not automatically prompting users to download PDF, XLS, RTF or CSV export files.

#### Show Join Fields

Enables/Disables any **Data Fields** that are used as Unique Keys or Joins. Set to *False* to hide all unique key and join Data Fields from users. To hide specific Data Fields, see [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column).

#### Show Grid Lines in Report Viewer

Sets the default output to show grid lines or not. This can be overridden on a per-report basis.

#### Show Enhanced Tooltips

Sets the style of tooltips to display. If *True*, enhanced tooltips which support HTML will be displayed. If *False*, standard browser tooltips will be shown.

#### Save on Report Execution

Set to *False* to disable automatic saving of reports when executing from the Report Designer.

#### Save on Finish Press

Set to *False* to disable automatic saving of reports when finish button is pressed in a wizard.

#### Enable Right-Click Menus

Set to *False* to disable right click menus.

#### Enable Reports Tree Drag and Drop

Set to *False* to disable the dragging of reports and folders in the Report Tree.

#### Show Report Upload/Download Options

Set to *True* to enable users to upload and download report files by right clicking on folders and reports. Default value is *False*.

#### Allow interactivity in Report Viewer

Set to *False* to disable Interactive Report Viewer capabilities, including: changing column width, styling output, and interactive filters.

#### Show Toolbar in Report Viewer

Specify if Report Viewer should display paging, search, and export options.

* *Auto* — Exago will detect if the report only displays a single page of content from the Report Footer Section. If so the HTML Toolbar will be hidden, otherwise it will show.
* *Show* —the toolbar will always show.
* *Hide* — the toolbar will never show.

#### Default interactive report viewer dock is open

Set to *True* to have the Interactive Dock opened by default when a report is executed in the Report Viewer.

#### Interactive report viewer default dock placement

Specify if the Interactive Dock should appear on the left or right of the Report Viewer. The default value is *Left**pre-v2021.1.5* or*Right**v2021.1.5+*

#### Allow save to report design for report viewer

Set to *False* to prevent users from saving changes to a report made in the Report Viewer back to the original report design. This effectively removes the **Save Changes To This Report** and **Save Changes to New Report** options in the Report Viewer.

#### Maximum number of fields in a CrossTab header or tabulation source

Specify the maximum allowed fields in a CrossTab header or tabulation source. Note that adding a large number of data fields to a CrossTab will significantly increase the execution time of the report.

#### Use SVG for Application Icons v2016.3+

Set to *True* to se SVG icons instead of the default PNG icons in user interface elements. SVG icons look nicer on high-pixel density screens, but they may not be compatible with some web browsers.

When using a custom application theme, this setting should be set to *True*.

#### Application Theme Selection v2016.3+

Choose from a selection of available user interface themes, or choose *Create New Application Theme…* to create a new theme. See [Application Themes Overview](https://devnet.logianalytics.com/hc/en-us/articles/5281620572951-Application-Themes-Overview).

After choosing a theme, users should clear their browser cache and refresh the user interface in order for the theme change to take effect.

#### Update All Application Themes v2020.1.3+

Click the ![Refresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432258806679/refresh.png)**Update** button to update all custom application themes with the newest copy of the image and CSS files available in the Basic theme. It is recommended to click this button after updating Exago from one major version to another (for example *v2020.1*–*v2021.1*).

Depending on the number of the themes available and the number of changes made between versions, this operation may take a minute or so to complete.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The context-sensitive help is not affected by the theme selection.

#### Show Data Fields Search Box v2017.2+

#### Data Fields Search Mode

Enables/Disables the data field search tools in the Data Fields Pane of the ExpressView, Advanced Report and Dashboard Designers.

* *Disabled* — there is no search box
* *As You Type* — search results display as the user types
* *On Submit* — search results display after hitting the Enter key

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> We highly recommend setting **Column Metadata**, and setting **Schema Access Type** to *Metadata* for all available objects, before enabling this feature.
