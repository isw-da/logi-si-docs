---
title: "Date and Time Filter Aggregation Functions"
id: 4405851015447
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851015447-Date-and-Time-Filter-Aggregation-Functions
updated_at: 2021-09-21T01:28:07Z
---

# Date and Time Filter Aggregation Functions

# Date and Time Filter Aggregation Functions

To filter a custom metric using dates or times, you must already have a time attribute configured in your data source. The following date and time functions can only be used after WHERE in your custom metric.

Date field options use common time formats such as YTD, MMDDYYYY, and YoY.

The following date and time filter aggregation functions are supported.

| Supported Date and Time Functions | |
| --- | --- |
| Function | Description |
| `DATE()` | **Deprecated.** Use `NOW()` instead. |
| `DateADD('<time_period>',<interval>,'<date>')` | **Deprecated.** Use `TIME_ADD` instead.  For example, consider this `DateADD` specification:   ``` DateADD('YEAR', 1, '2021-01-01') ```   Use this `TIME_ADD` specification instead:   ``` TIME_ADD('YEAR', 1, '2021-01-01') ```   In a second example, consider this `DateADD` specification:   ``` DateADD('MONTH', 1, DATE()) ```   Use this `TIME_ADD` specification instead:   ``` TIME_ADD('YEAR', 1, NOW()) ``` |
| `DateSUB('<time_period>',<interval>,'<date>')` | **Deprecated.** Use `TIME_ADD` instead, specifying a negative number for `interval`.  For example, consider this `DateADD` specification:   ``` DateSUB('YEAR', 1, '2021-01-01') ```   Use this `TIME_ADD` specification instead:   ``` TIME_ADD('YEAR', -1, '2021-01-01' ```   TIME\_ADD supports negative interval numbers for subtraction. |
| `NOW()` | Obtains the current date and time for the derived field. However, `NOW()` functionality is not enabled by default. To enable this functionality, you must set the `calculations.rle.now.function` property in the `query-engine.properties` file to `true` and [restart the query engine microservice](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices). See [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties). |
| `PreviousPeriod(<offset>,<numPeriods>)` | This function is supported only within a TRANSFORM clause used for [filtering the custom metric](https://devnet.logianalytics.com/hc/en-us/articles/4405851003543-Apply-Filters-to-Custom-Metrics).  The period returned is of the same length as the currently represented period, but not immediately prior to it. Instead, it counts back in `<numPeriods>` periods of time, measured in units named by `<offset>`.  The following time `<offset>` values are supported: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`.  See [*PreviousPeriod Function*](#Previous). |
| `TIME()` | **Deprecated.** Use `NOW()` instead. |
| `TIME_ADD('<time_period>',<interval>, <date-time-field>)` | Adds an interval value to the `<timepart>` of the date-time field:  In the following example, 7 is added to the hour in the field called `date_time_field`:   ``` TIME_ADD ('HOUR', +7, date_time_field) ``` |

## Date Filter Functions

Specific parameters are needed for the `DateADD` and `DateSub` functions. The following table describes them.

| Parameter | Value |
| --- | --- |
| `time_period` | Supported time periods (with corresponding interval range): `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND` |
| `interval` | Whole number integer. Negative numbers are supported for subtraction. |
| `date` | * Current day operator: date() * Standard date and time formats supported by Composer, including:    + `yyyy-MM-dd HH:mm:ss`   + `MM/dd/yy hh:mm aa`   + `yyyy` For all supported formats, see [*Supported Date and Time Formats*](https://devnet.logianalytics.com/hc/en-us/articles/4405851010711-Supported-Date-and-Time-Formats). |

## PreviousPeriod Function

The `PreviousPeriod` function is used for comparing data values between different time periods. This function can be used when you need to compare one time period to another of equivalent size for variance custom metrics. For example, comparing results from the current month to the previous month or the current week to the same week one year ago.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Note that this function only works when the date field used in the formula is selected on the time bar.

To use this function, the `TRANSFORM`[SQL-like expression](https://devnet.logianalytics.com/hc/en-us/articles/4405859312535-Supported-SQL-Like-Expressions) must be used in the custom metric to convert the date range for a specified time attribute. For example:

```
SUM(Sales) TRANSFORM saledate = PreviousPeriod('month',1)
```

If the `saledate` time period is March 2015, the custom metric returns `SUM(Sales)` where the `saledate` is February 2015.​

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the data is grouped by the same field for which a `PreviousPeriod` transformation is performed and it is grouped by days but transformed by units of months, quarters, or years, null values are returned when the previous period does not have matching days for the current period. For example, if the current period is the month of March and `PreviousPeriod('month',1)` is used for the transformation, null values are produced for February 29-31, 2015 because those days are not valid days (although they are valid days for March 2015). Composer attempts to preserve the day-of-month correspondence between the two periods.

Specific parameters must be specified in `PreviousPeriod` functions. The following table describes them.

| Parameter | Value |
| --- | --- |
| `offset` | The time granularity for the previous period (includes `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`). |
| `numPeriods` | The argument specifying the number of periods to go back in time. |
