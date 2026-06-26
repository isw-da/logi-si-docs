---
title: "Composer 6.4 Enhancements"
id: 4405851162903
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851162903-Composer-6-4-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.4 Enhancements

# Composer 6.4 Enhancements

This topic describes the significant enhancements in Composer 6.4.

* [*Raw Data Table Changes*](#Raw)
* [*Data Source Configuration Changes*](#Data)
* [*Caching Changes*](#Caching)

## Raw Data Table Changes

The following changes were made to raw data tables in this release.

* All UI references to "raw data tables" or "raw data table" have been changed to simply "tables" or "table." Pivot tables are still referred to as "pivot tables."
* The column headings of a table now include a context menu you can use to perform various functions on the table, as described below. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743722135/three-dots-menu.png) next to the column heading name to access the menu.

  | Menu Option | Description |
  | --- | --- |
  | Aggregation | Shown only for numeric fields or metrics, this option allows you to change the aggregation method for the field. Valid options are AVG, MIN, MAX, SUM, NONE, or LAST VALUE. See [*Change Metric Aggregation in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405851233431-Change-Metric-Aggregation-in-Tables). |
  | Autosize all columns | This option causes Composer to autosize all the column widths in the table. See [*Change Column Widths*](https://devnet.logianalytics.com/hc/en-us/articles/4405859538455-Change-Column-Widths). |
  | Group by <field> | This option allows you to group the table by the field represented by the table column. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851238551-Group-and-Ungroup-Table-Data). |
  | Granularity | Shown only for time fields used to group the table, this option allows you to change the granularity of the grouped time field. Valid options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, and **Year**. See [*Change Time Field Granularity in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405851240599-Change-Time-Field-Granularity-in-Tables). |
  | Include Blanks | Shown only for time fields used to group the table, this option allows you apply even time intervals for the grouped time field. Select this option once to apply even time intervals. Select it a second time to remove even time intervals. See [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals). |
  | Ungroup <field> | This option removes grouping by the table column. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851238551-Group-and-Ungroup-Table-Data). |

  You can also select and hide a column from a table using the column heading context menu. See [*Select Columns Using the Table Context Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859545879-Select-Columns-Using-the-Table-Context-Menu) and [Hide Columns Using the Table Context Menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859543319-Hide-Columns-Using-the-Table-Context-Menu).
* You can now group tables by one or more fields in the raw data. Summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table. Grouping can be set on the table itself using the column heading context menus, on the Table Settings sidebar (a new Group area has been added), and in the default settings for a data source. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851238551-Group-and-Ungroup-Table-Data).

  In addition, the ability to group table data is now controlled by the **Group** interactivity setting. If the **Group** interactivity setting is switched off, the end user cannot group table data. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).
* You can change the aggregation of metrics in a table using the new table context menu. See [*Change Metric Aggregation in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405851233431-Change-Metric-Aggregation-in-Tables).

  In addition, the ability to change the aggregation of table metrics is now controlled by the **Metrics** interactivity setting. If the **Metrics** interactivity setting is switched off, the end user cannot change the aggregation of metrics in tables. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).
* You can now set [even time intervals](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals) for a time field (**Include Blanks** setting) dynamically in a table using the column heading context menus if the table is grouped by the time field. See [*Apply Even Time Intervals on Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992023-Apply-Even-Time-Intervals-on-Tables) and [Even Time Intervals](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals).
* You can now alter the granularity of a time field dynamically in a table using the column heading context menus if the table is grouped by the time field. See [*Change Time Field Granularity in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4405851240599-Change-Time-Field-Granularity-in-Tables).

## Data Source Configuration Changes

The following changes have been made to data source configurations:

* A new "Data Unavailable" message now appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a new "No search results" message appears. See [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).
* The default settings available for tables in a data source configuration have changed in this release. You can now specify default:

  + Aggregation methods for numbers and metrics in the table data
  + Columns to display in tables produced for the data source
  + Grouping for the table data.

  See [*Configure Default Table Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405859542295-Configure-Default-Table-Settings).

## Caching Changes

This release introduces a new metadata cache to cache field statistics and improve overall metadata caching performance. In past releases, both visual data and field statistics were stored in the same cache. This new metadata cache is largely controlled by the API at this time. However, the clear cache button (![](https://devnet.logianalytics.com/hc/article_attachments/4406743755287/clear-cache-btn_24x24.png)) on the [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page still clears all caches for the data source and the Caching switch at the bottom of the [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) of the data source configuration wizard still enables or disables all caching for a data source.

New API endpoints have been introduced to support cache clearing.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/sources/<source_id>/cache/visdata` | DELETE | Clears the visual data cache. |
| `/api/sources/<source_id>/cache/metadata` | DELETE | Clears the metadata cache. |
| `/api/sources/<source_id>/cache` | DELETE | Clears both the visual and metadata caches. |

In addition, several new properties have been introduced for source definitions using the API:

* A new boolean `cacheableMetadata` property indicates whether metadata caching is enabled for a data source. The existing `cacheable` property indicates whether caching, in general, is enabled for the data source.
* A new `statsCached` property allows you to control metadata (field statistics) caching on a per-field basis. This property can be used to configure the field statistics look-up via materialized views (ignoring internal caches and redirecting the requests from the original source) and to improve the performance of statistics requests when precreated statistics data exists. Please contact your Technical Support representative to get guidance on how to configure this.

See [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).
