---
title: "Filter Settings"
id: 5281628457495
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281628457495-Filter-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Filter Settings

# Filter Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Filter Settings**.

---

## Introduction

The **Filter Settings** provide control over what filter options are exposed to users and how the dropdowns within filters behave.

## Settings

### Show Group (Min/Max) Filters

Enables/Disables the **Min/Max Filter** menu. Set to *False* to disable users from using Min/Max filters.

### Show Top N Filters v2017.1+

Enables/Disables the **Top/Bottom Filters** menu in the **ExpressView** and **Advanced Report** designer. Top N filters allow users to see the highest or lowest values for a data set. Set to *False* to disable users from using Top N filters.

### Allow New Filters at Execution

Controls the creation of new filters when a user is prompted for a filter value at the time of report execution. Set to *False* to disable new filters from being created at execution.

### Read Database for Filter Values

Enables/Disables filter dropdowns to contain values from the filter field’s data object.

Set to *False* only if retrieving the values for the dropdown will take more than a few seconds.

![Ok5zKkB47p.png](https://devnet.logianalytics.com/hc/article_attachments/5432124911639/ok5zkkb47p.png)

The Filters tab of the ExpressView Properties Pane with **Read Database for Filter Values** set to *True*

![OrAMOHG6UU.png](https://devnet.logianalytics.com/hc/article_attachments/5432124919959/oramohg6uu.png)

The Filters tab of the ExpressView Properties Pane with **Read Database for Filter Values** set to *False*. Note the lack of the filter dropdown arrow in the bottom figure.

### Allow Filter Dependencies

Causes filter drop downs to retrieve values dependent on the filters above them in the menu. Set to *True* to enable. Default value is *False*.

For a full description of how this feature works, see [Filter Dependency](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters#Filter).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting only works for Data Objects from databases and will not change drop downs from Web Services, .NET Assemblies and stored procedures.

### Show Filter Description

Enables/Disables reports to have description text for the filters menu. The filter description is set in the Description tab of the **New Report Wizard**, the **Description** item on the Report Designer’s Settings menu or the Report Designer's Save dialog.

A **Help**![Help.png](https://devnet.logianalytics.com/hc/article_attachments/5432233043223/help.png)icon appears in the Filters dialog. Clicking this icon displays the filter description.

### Default Filter Execution Window

Determines the default type of window that appears when prompting users for filter execution input:

* *Standard* — New reports display the standard filter execution window, allowing filters to be modified and new filters to be created.
* *Simple with Operator* — New reports display a simplified filter execution window that only allows the operator and value to be changed.
* *Simple without Operator* — New reports display a simplified filter window that only allows the value to be changed.
* *Custom* — New reports use a custom built filter execution window. When this option is chosen, [Allow User to Change Filter Window](#Allow) should be set to *False* and a value be provided for [Custom Filter Execution Window](#Custom). This is a deprecated feature and should not be used in new installations.

### Allow User to Change Filter Window

Enables/Disables reports to change the type of filter execution window that is displayed.

### Include Null Values for ‘NOT’ Filters

Indicates to include NULL values for filters with using the operators ‘not equal’ or ‘not one of’.

### Custom Filter Execution Window

Specifies a control or URL that contains Custom Filter Execution Window. This is a deprecated feature and should not be used in new installations.

### Restore All Default Date Filter Functions v2016.3+

Restores the default **[Filter Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281644078487-Custom-Filter-Functions)** to the **Extensions** menu.

### Restore All Default Formula Functions v2017.2+

Restores the default **[Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions)** to the **Extensions** menu.
