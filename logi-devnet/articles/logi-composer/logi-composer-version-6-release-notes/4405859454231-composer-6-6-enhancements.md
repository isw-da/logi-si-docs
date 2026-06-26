---
title: "Composer 6.6 Enhancements"
id: 4405859454231
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.6 Enhancements

# Composer 6.6 Enhancements

This topic describes the significant enhancements in Composer 6.6.

* [*Authorization Changes*](#Authoriz)
* [*Connector Updates*](#Connecto)
* [*COALESCE Function Changes*](#COALESCE)
* [*Performance Improvements*](#Performa)
* [*User Interface Changes*](#User)

## Authorization Changes

The group privilege **Can Manage Visuals** was renamed to **Can Administer Visuals** in this release. The corresponding API privilege **ROLE\_MANAGE\_VISUALS** was also renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used; if you use the Composer user interface (UI) to manage groups, the change will happen automatically.

In addition, to alter and save an individual visual in a dashboard now, you must either be assigned to a group with the **Can Administer Visuals** (**ROLE\_ADMINISTER\_VISUALS**) privilege or be the creator of the visual.

See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

## Connector Updates

The maximum version of Spark SQL data stores supported by the Composer Spark SQL connector is now version 3.0. See [*Manage the Spark SQL Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector).

## COALESCE Function Changes

The [COALESCE function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. See [*Conditional Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions).

## Performance Improvements

In this release, server start times improved by up to 15 percent.

## User Interface Changes

The following changes were made to the user interface in this release:

* Labels on bar charts have been upgraded so they are easier to read. They now take into account the bar color as well as the background color of the UI.
* Table data can now be aggregated by group field if:

  + The group field is not the first group field for the table
  + The data source indicates that the group field can be aggregated.

  If a group field meets these criteria, you can specify the [column aggregation function](https://devnet.logianalytics.com/hc/en-us/articles/4405859301911-Column-Aggregation-Functions) used for its data in the table. Column aggregation functions can be selected from the table column [context menus](https://devnet.logianalytics.com/hc/en-us/articles/4405851236759-Group-Table-Data-Using-the-Table-Context-Menu) or from the [table settings sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4405851237655-Group-Table-Data-Using-the-Table-Settings-Sidebar). See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851238551-Group-and-Ungroup-Table-Data).
