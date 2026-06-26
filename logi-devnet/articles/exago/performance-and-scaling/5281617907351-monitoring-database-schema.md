---
title: "Monitoring Database Schema"
id: 5281617907351
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281617907351-Monitoring-Database-Schema
updated_at: 2022-05-03T22:08:49Z
---

# Monitoring Database Schema

# Monitoring Database Schema

The monitoring database has three tables that can be used to build reports. This topic describes what data is stored, and how to interpret what you see.

![structure.png](https://devnet.logianalytics.com/hc/article_attachments/5432236898711/structure.png)

Entity-relationship diagram (ERD) for the monitoring database

## SystemStatistics Table

The SystemStatistics table logs the available CPU load and memory for the system on which each scheduler service is installed.

Data is polled at occasional intervals. You can specify the time between polls using the **StatisticsIntervalMinutes** setting in the `Monitoring.exe.config` file. For instructions, see [Monitoring: Setup](https://devnet.logianalytics.com/hc/en-us/articles/5281636945431-Monitoring-Setup)

The table contains the following data columns:

### id

An integer used to uniquely identify each row. This is the primary key for the table.

### transactionId v2017.2+

An integer used to associate rows with **type**: `CPU available` and **type**: `free memory` to common transactions, in order to facilitate a vertical table transformation and report off both CPU and Memory usage in the same report and chart.

### hostId

The scheduler which was polled for system data. Every scheduler is polled at the same time. Schedulers are identified by their host address, as specified in the Admin Console.

**Example.** `tcp://localhost:2010`

### type

One of:

* `CPU available`, which indicates that the **value** field in this row shows the CPU load percentage available at this time.
* `free memory`, which indicates that the **value** field in this row shows the amount of free memory at this time.

### value

One of:

* A value indicating the CPU load available at this time, as a percentage of 100%. This field indicates CPU available if the **type** field for this row shows `CPU available`. This value is “-1” if the scheduler could not be reached at this time.
* A value indicating the amount of free memory at this time, in megabytes (MB). This field indicates free memory if the **type** field for this row shows `free memory`. This value is “-1” if the scheduler could not be reached at this time.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This field should be formatted as a decimal, either in the metadata for this column, or in the report cell formatting.

### timestamp

A datetime value indicating when this scheduler was polled.

### Transform

The following **[Vertical Table Support](https://devnet.logianalytics.com/hc/en-us/articles/5281643770903-Vertical-Table-Support)** transform is recommended for the SystemStatistics table:

```
<?xml version="1.0" encoding="UTF-8"?>
<entity>
   <!--<entity_name></entity_name>-->
   <db_name>SystemStatistics</db_name>
   <!--<datasource_id></datasource_id>-->
   <object_type>table</object_type>
   <key>
      <col_name>transactionId</col_name>
   </key>
   <transform>
      <col_name>type</col_name>
      <val_name>value</val_name>
      <non_transform_col>
         <col_name>timestamp</col_name>
         <data_type>8</data_type>
      </non_transform_col>
      <non_transform_col>
         <col_name>hostId</col_name>
         <data_type>0</data_type>
      </non_transform_col>
      <non_transform_col>
         <col_name>transactionId</col_name>
         <data_type>0</data_type>
      </non_transform_col>
   </transform>
</entity>
```

## Audit Table

The Audit table records when certain events, which you specify, happen to reports. This table records data for the web application and the schedulers.

Data is logged at the time of each event, but the data is only collected in the core database at occasional intervals. You can specify the time between data collections using the **ExtractionIntervalMinutes** setting in the `Monitoring.exe.config` file. For instructions, see [Monitoring: Setup](https://devnet.logianalytics.com/hc/en-us/articles/5281636945431-Monitoring-Setup).

The table contains the following data columns:

### id

An integer used to uniquely identify each row. This is the primary key for the table.

### hostId

The application for which this action took place. The web application and schedulers are identified by their host address.

**Example.** `tcp://localhost:2010`  
**Example.**`http://localhost`

### transactionType

A string indicating which type of event has triggered this row to be created. One of:

* Execute Report
* Rename Report
* Duplicate Report
* Delete Report
* Design Report
* Save Report XML
* Chart Control
* Gauge Control
* Map Control
* Google Map Control

### userId

The userId parameter for this event.

### companyId

The companyId parameter for this event.

### timestamp

A DateTime value indicating when this event happened.

### auditId

For rows where the **transactionType**is `Execute Report`, this field joins up to two rows in the **ExecutionDetail** table that indicate when this execution started and, if successful, when it ended.

This field also joins rows in the **ReportDetail** table which give some information about the report in which the logged event happened.

## ExecutionDetail Table

This table records data for report execution events.

Up to two rows for each event are created:

* The first has **transactionType**`Report Execution Begins`, which logs when the report execution started.
* The second has **transactionType** `Report Execution Ends`, which logs when the report execution ends. If the report execution was not successful, this row will not be created.

The table contains the following data columns:

### auditId

An integer used to join up to two rows in this table with a row in the **Audit** table.

### transactionId

A globally unique identifier (GUID) for this execution. This GUID is used in several places throughout Exago. Notably, it is used as the file name for scheduled reports which have been saved to disk.

### transactionType

One of:

* `Report Execution Begins`, which indicates that the **timestamp** value for this row shows when this execution started.
* `Report Execution Ends`, which indicates that the **timestamp** value for this row shows when this execution ended.

### timestamp

A datetime value indicating when this execution started or finished, depending on the value of **transactionType**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This table uses columns (**transactionId** and **transactionType**) as a primary key.

### Transform

The following **vertical transformation** is recommended for the ExecutionDetail table:

```
<?xml version="1.0" encoding="UTF-8"?>
<entity>
   <!--<entity_name></entity_name>-->
   <db_name>ExecutionDetail</db_name>
   <!--<datasource_id></datasource_id>-->
   <object_type>table</object_type>
   <key>
      <col_name>transactionId</col_name>
   </key>
   <transform>
      <col_name>transactionType</col_name>
      <val_name>timestamp</val_name>
      <non_transform_col>
         <col_name>auditId</col_name>
         <data_type>2</data_type>
      </non_transform_col>
   </transform>
</entity>
```

## ReportDetail Table

This table records information about the reports which relate to events in the Audit table.

### auditId

An integer used to join a row in this table with a row in the **Audit** table.

### reportId

The file path and name of the report which the event affected.

### reportType

The type of report: advanced, express, expressview, chained, Dashboard
