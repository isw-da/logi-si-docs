---
title: "Dashboard Designer: Adding Reports (pre-v2019.2)"
id: 5281595992855
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281595992855-Dashboard-Designer-Adding-Reports-pre-v2019-2
updated_at: 2022-05-03T22:09:12Z
---

# Dashboard Designer: Adding Reports (pre-v2019.2)

# Dashboard Designer: Adding Reports (*pre-v2019.2*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to *pre-v2019.2* of the application. For current Dashboard documentation, see [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-).

Any **Advanced Report**, **Express Report**, **ExpressView**, and **CrossTab Report** can be added to a **Dashboard**. Existing filters and prompting parameters can be accessed and modified from the **Dashboard Designer**. Reports have most of the same interactability as in the **Report Viewer**, with the exception of the interactive sidebar.

To add a report to a **Dashboard**, simply drag it from the report tree onto the **Dashboard**.

For information about managing report filters and parameters, see [Filters and Parameters](#Filters).

For information about what report settings are available, see [Report Settings](#Report).

## Filters and Parameters

When you add a report with prompting filters or parameters to a **Dashboard**, you have several choices for how these filters can be accessed on the **Dashboard**, as well as which reports they can apply to. Select the report tile, then click the Filters or Parameters tabs to edit the filter settings.

For each filter or parameter you can do the following:

**Apply to**

Choose whether this filter or parameter applies to the **Report**, or to all reports on the **Dashboard**. If you select **Dashboard**, then the filter or parameter must be edited in the **Dashboard** Filters or Parameters panes. Deselect the report, then click the ![icon.filterstab.png](https://devnet.logianalytics.com/hc/article_attachments/5432359533591/icon.filterstab.png)

**Filters****![icon.parameters.png](https://devnet.logianalytics.com/hc/article_attachments/5432226071191/icon.parameters.png)Parameters**

**Prompt for value**

Select this option to prompt users to enter a value when running the **Dashboard**.

**Interactive**

Interactive filters and parameters can be edited in the **Dashboard Viewer** filters and parameters panes.

**Operator**

Change the filter operator. Click the lock ![TreeReportLock.png](https://devnet.logianalytics.com/hc/article_attachments/5432176031767/treereportlock.png)

**Dashboard**

**Value**

Set the value or values for the filter or parameter. If the filter or parameter is interactive or prompting, then other users can select different values when running the **Dashboard**.

## Report Settings

You can edit some additional settings for reports on a **Dashboard**. The following settings are available:

**Reload Interval**

Select how often, in seconds, the report will automatically refresh in the Dashboard viewer. The default ‘0’ seconds disables automatic refresh.

**Allow Searching**

Show a search and paging bar to allow users to browse the report.

**Allow Scrolling**

Show horizontal and vertical scroll bars if the report cannot fit in its tile.

**Only run report in design screen when report is manually refreshed**

Do not run the report immediately in the **Dashboard Designer**. Choose this option for large reports which may take a while to load.

[![Concept Link Icon](https://devnet.logianalytics.com/hc/article_attachments/5432159914263/transparent.gif)See Also](javascript:void(0);)
