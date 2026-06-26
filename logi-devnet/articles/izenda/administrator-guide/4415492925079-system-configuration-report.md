---
title: "System Configuration/Report"
id: 4415492925079
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492925079-System-Configuration-Report
updated_at: 2021-12-10T03:10:23Z
---

# System Configuration/Report

# System Configuration/Report

The **System Configuration/Report** page allows users to:

* configure Report Version History feature.
* set a default background image for report header, for each tenant.
* customize the names for “Global Categories” and “Local Categories” in a multi-tenant system (see [Global Report Setup Guide](https://devnet.logianalytics.com/hc/en-us/articles/4415512097943-Global-Report-Setup-Guide)).

## Configure Report Version History

1. In browser, log in to Izenda as a user with System Configuration
   permission.
2. The Setting Level must be System.

* Uncheck the Enforce Version History check-box will disable Report Version and remove all version history.
* Change the maximum number of versions per report in “No. archived versions to keep” box.

  Note: The existing report versions that exceed this number are not removed. Setting this number only limits future report versions.
* Click the Clear Archived Versions Now button at the top will remove all current version history but still keep tracking versions.
* To use a schedule to remove all current version history, tick the Remove Archived Versions check-box then set up the time and recurrence.

[![../_images/System_Configuration_Report_Version.png](https://devnet.logianalytics.com/hc/article_attachments/4415504364439/system_configuration_report_version_792x269.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504364183/system_configuration_report_version.png)

## Set Default Header Image

1. In browser, log in to Izenda as a user with System Configuration
   permission.
2. Click Settings, then System Configuration then Report in the left
   menu.
3. Select the Setting Level: either System or a specific tenant.
4. In Default Header Image section, enter a relative path or the full url to the image.
   * Sample relative path in web server box: `/images/contoso.png`
   * Sample full url: `http://image.google.com/contoso.png`
5. Click Save button at the top.

## Customize the names for “Global Categories” and “Local Categories”

1. In browser, log in to Izenda as a user with System Configuration
   permission.
2. The Setting Level must be System.
3. Change the names in Global Name and Local Name boxes.
4. Click Save button at the top.

[![../_images/Customize_Global_And_Local_Names.png](https://devnet.logianalytics.com/hc/article_attachments/4415492460823/customize_global_and_local_names_792x379.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504364695/customize_global_and_local_names.png)

## Set Default Color Theme for Chart, Gauge, and Map

> [![../_images/Customize_Color_Pallete_Selection_Popup.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511729687/customize_color_pallete_selection_popup_604x438.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492461079/customize_color_pallete_selection_popup.png)
>
> 1. In browser, log in to Izenda as a System Admin.
> 2. Click Settings, then System Configuration then Report on the left
>    menu.
> 3. Select the Setting Level: either System or a specific tenant.
> 4. In Default Color Theme for Chart, Gauge, and Map section, click gear icon
> 5. Choose any theme then click OK to close Default Color Theme Selection popup.
> 6. **Once a default is set all existing reports and dashboards using charts will assume the new default color theme for that setting level. This can be configured at the report level by editing the report and selecting a new theme or no theme.**
> 7. When a default is set, all new charts, gauges and maps will use the default for that setting level unless the user selects a different theme or No Theme.
> 8. Global reports when set to use the System default, will show in the tenant level using the Tenant’s default. If no default is set for the tenant the System default will be used at the tenant level.
> 9. Report level settings are the highest priority for themes, so any theme other than the default set for a report will be the theme used.
> 10. Field level settings for color values will work with color themes, taking higher priority than the default or selected themes.

Note:

* The preview limitation for the number of colors in each theme is 12. In case [the color theme file](https://devnet.logianalytics.com/hc/en-us/articles/4415504605847-Color-theme-for-Chart-Gauge-and-Map#color-theme-file) exceeds this, system will load and populate the first 12 colors.
* When a theme has invalid color(s), the system will ignore and load the others.
* See Guide here for creating a custom [color theme file](https://devnet.logianalytics.com/hc/en-us/articles/4415504605847-Color-theme-for-Chart-Gauge-and-Map#color-theme-file).

## Global Reports and Default Themes

> * Please see the grid below to understand how themes work with Global Reports and Dashboards.

| Default Theme in System Level | Default Theme in Tenant Level | Theme Used in Global Report | Theme Seen in Tenant Level | Notes |
| --- | --- | --- | --- | --- |
| A | B | No Theme | No Theme | Theme A is set as system default and B is set as Tenant default but Global report creator **chose No Theme to override defaults** |
| A | B | A | B | Theme A is set as system default and B is as Tenant default and Global report creator **left default theme** so tenant user will see thier default |
| A | B | B | B | Theme A is set as system default and B is set as Tenant default but Global report creator **chose theme B to override defaults** |
| No Theme | B | No Theme | B | No Theme is set as system default and B is set as Tenant default and Global report creator **left No Theme default in report** as default so tenant will see their default |
| No Theme | B | A | A | No Theme is set as system default and B is set as Tenant default and Global report creator **chose theme A to override defaults** |
| A | No Theme | No Theme | No Theme | Theme A is set as system default and No Theme is set as Tenant default but Global report creator **chose No Theme to override defaults** |
| A | No Theme | A | A | Theme A is set as system default and No Theme is set as Tenant default and Global report creator **left report as default so tenant will see System Default** |
| A | No Theme | B | B | Theme A is set as system default and No Theme is set as Tenant default but Global report creator **chose Theme B to override defaults** |
