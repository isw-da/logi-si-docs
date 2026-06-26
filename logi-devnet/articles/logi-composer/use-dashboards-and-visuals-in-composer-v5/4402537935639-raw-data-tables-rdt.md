---
title: "Raw Data Tables (RDT)"
id: 4402537935639
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537935639-Raw-Data-Tables-RDT
updated_at: 2021-09-15T02:23:05Z
---

# Raw Data Tables (RDT)

# Raw Data Tables (RDT)

Raw data tables (RDT) are based on at least one metric and one attribute. They contain a table of the raw data from the data source selected for the visual. Raw data tables are supported by all Composer [data connectors](https://devnet.logianalytics.com/hc/en-us/articles/4402537840279-Composer-Data-Connector-Reference).

Data from Fusion data sources can be used in raw data tables. However, Composer recommends that you initially use a subset of fields from Fusion data sources on raw data tables to limit the load on Composer's query engine and improve its performance. You can change the subset in data source configurations and add additional fields, later, as needed while working on a dashboard.

Number field formatting in raw data tables is based on the formatting specified for the numeric field in a data source configuration. Time field formatting in aggregated raw data tables is based on the granularity specified for the time field in the data source configuration.

If you want raw data tables for a data source to support live mode and data playback, be sure that the data source includes a time field and that it meets the requirements for live mode and playback. See [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4402552905879-Live-Mode-and-Historical-Playback).

When you first create a raw data table, the [default settings](https://devnet.logianalytics.com/hc/en-us/articles/4402552929687-Configuring-Default-Raw-Data-Table-Settings) specified in the data source configuration are used to create the table. You can modify the table fields, enlarge or decrease the size of the columns, rearrange the table columns, and sort the data by the column headings. See the following topics:

* [*Configuring Default Raw Data Table Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4402552929687-Configuring-Default-Raw-Data-Table-Settings)
* [*Configuring Settings for a Specific Raw Data Table*](https://devnet.logianalytics.com/hc/en-us/articles/4402552930711-Configuring-Settings-for-a-Specific-Raw-Data-Table)
* [*Modifying Raw Data Table Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402537934999-Modifying-Raw-Data-Table-Fields)
* [*Rearranging Raw Data Table Columns and Changing Column Widths*](https://devnet.logianalytics.com/hc/en-us/articles/4402552928919-Rearranging-Raw-Data-Table-Columns-and-Changing-Column-Widths)
* [*Sorting Data in a Raw Data Table*](https://devnet.logianalytics.com/hc/en-us/articles/4402552931479-Sorting-Data-in-a-Raw-Data-Table)

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) You can use [*Keyboard Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4402537923991-Keyboard-Controls) on the Raw Data Table Settings sidebar instead of a mouse.
