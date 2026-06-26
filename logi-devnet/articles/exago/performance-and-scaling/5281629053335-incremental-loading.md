---
title: "Incremental Loading"
id: 5281629053335
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281629053335-Incremental-Loading
updated_at: 2022-05-03T22:08:51Z
---

# Incremental Loading

# Incremental Loading

**Incremental loading** limits the amount of data that is returned for each database query. This allows users to load reports incrementally, starting with a small set of rows and adding more in steps as desired.

Incremental loading can shorten the amount of time it takes a report to load and be usable. It can also help reduce continuous load on a database which may improve load balancing performance.

To enable it, set **Admin Console** > **General** > **Database Settings** > **Row Limit Step Size** to a value *greater than 0*. This value sets the initial number of rows returned when the report is first executed, as well as the number of rows returned for each subsequent query.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For the best user experience, keep the number of items in the Report Tree less than 1000.

The step size can be overridden for with a smaller value at the report-level with the Advanced Report Designer’s **[Report Viewer option](https://devnet.logianalytics.com/hc/en-us/articles/5281541782039-Advanced-Reports-Report-Options#Report)****Report Row Step Limit**.

Choosing a **Row Limit Step Size** that allows most reports to avoid reaching the limit entirely is ideal since truncated results can affect report accuracy. Summary data may not be accurate if not all of the pertinent rows are available for aggregation. Another consideration is performance. If there are a lot of slow running reports due to the amount of data being returned, then the need to balance between report completeness in the first execution vs performance by limiting the number of rows returned will need to be considered. Each environment is unique, so the *1000 row* recommendation can be used as a starting point and then fine tuning applied.

## Usage

With incremental loading enabled, when an ExpressView is run or a report is run in the Report Viewer (the interactive toolbar must be enabled), the report will only query the first number of rows specified in the configuration setting.

If there are fewer rows than the full data set:

* (*v2021.1+*) a link displays on the toolbar with the message **Showing *X* Results**. Click the link to load more data:
  + **Load X more Records** — get the next number of data rows and add them to the existing report
  + **Load All Data** — get the remainder of the data set
* (*pre-v2021.1*) an alert icon displays on the toolbar with the message “**Truncated results displayed**” unless the report qualifies for [Infinite Scrolling](#Infinite).  
  ![xI4CXqtDPI.png](https://devnet.logianalytics.com/hc/article_attachments/5432236933783/xi4cxqtdpi.png)

  Alert icon in Report Viewer, *pre-v2021.1*

  ![BsOp5IeTx5.png](https://devnet.logianalytics.com/hc/article_attachments/5432183800343/bsop5ietx5.png)

  Alert icon in ExpressView, *pre-v2021.1*

  Click the icon to retrieve more data. Choose from:

  + **Generate +*number*** to retrieve the next *number* of rows and add them to the report. (The number is determined by the *Row Limit Step Size* setting).
  + **Generate All** to get the full data set.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Exporting a truncated report from the Report Viewer generates a file with only the existing rows.

Incremental loading has no effect for Dashboards, Chained Reports, or Scheduled Reports. Exporting from the Report Tree and Advanced Report Designer is not affected by incremental loading.

## Infinite Scrolling v2018.1+

With **Incremental Loading** enabled, in [certain conditions](#Conditio), scrolling or paging through the Report Viewer will cause additional rows to be loaded automatically instead of needing to click the **Truncated Results Displayed** alert icon each time.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When a report qualifies for infinite scrolling, the **Truncated Results Displayed** alert icon and the Report Viewer’s interactive sorts and filters dock are hidden.

### Conditions for Infinite Scrolling

Infinite Scrolling requires reports to be designed in a certain manner. If the conditions are not met, users will need to manually step through the rows instead by clicking the icon.

To qualify for infinite scrolling, reports must have:

* a visible Detail section,
* at least one Sort,
* utilize a data source that supports range selection, such as Oracle, MySQL, DB2, Informix, Microsoft SQL Server, or PostgreSQL.

A report that contains any of the following will be disqualified from infinite scrolling:

* interactive sorts or filters (sorts and filters in the Report Viewer’s interactive dock)
* Top N filters
* a CrossTab
* collapsible groups
* cross-source or Cartesian joins
* in-memory aggregate functions (for example [RunningSum](https://devnet.logianalytics.com/hc/en-us/articles/5281614243735-Aggregate-Functions#RunningS)), custom functions, or server events that use the full data set (for example [OnDataCombined](https://devnet.logianalytics.com/hc/en-us/articles/5281613493399-Global-Event-OnDataCombined)).
* a **Row Limit Step Size** setting that returns less than one full page of data

### Range Method

The method used to construct the range limiting SQL statement depends on the Data Source, and can be customized by editing the [dbconfigs.json](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File) and setting the `"RowRangeMethodString"` property for each source. See [wrRowRangeSqlMethod](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrRowRan).
