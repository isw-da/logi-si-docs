---
title: "Using Forecast.Time Series Decomp"
id: 4419707595415
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707595415-Using-Forecast-Time-Series-Decomp
updated_at: 2022-07-17T01:48:45Z
---

# Using Forecast.Time Series Decomp

# Using Forecast.Time Series Decomp

The **Forecast.Time Series Decomp** element uses a technique that's optimized for analyzing data across daily, weekly, or other time periods. The data to be analyzed should be grouped and detail rows discarded, so there is one data row for each time period. If possible, time intervals should be consistent, such as 12 months in a year, not 5 months spread across one year.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714761239/forecast_04.png)

The Forecast.Time Series Decomp element is a child of any datalayer, as shown above, and its attributes include:

| Attribute | Description |
| --- | --- |
| Dependent Data Column | (Required) Specifies the name of a column returned into the datalayer. It represents data values for the Y-axis. |
| ID | (Required) A unique element ID. |
| Independent Data Column | (Required) Specifies the name of a column returned into the datalayer. It represents data values for the X-axis. |
| Cycle Time Span | Specifies the periodic variation or cycle to be used in the analysis of the data. Options include:  * Hour: 1 day (a 24-hour cycle) * Daily: 1 week (a 7-day cycle) * Week: 1 month (a 4-week cycle) * Month: 1 year (a 12-month cycle) * Quarter: 1 year (a 4-quarter cycle) * Year: 1 year (a 1-year cycle) |
| Forecast Indicator Column ID | Specifies the name of a new column to be added to the datalayer, with value set to *True*, for each row used in the forecast analysis. If left blank, the column will automatically be named "{ElementId}" + "ForecastIndicator". |
| Forecast Length | Specifies the actual number of rows to analyze. A value entered that is greater than the total number of rows will be reduced to the total number of rows minus one. If left blank, 20% of the total number of rows will be used. |
| Forecast Value Column ID | Specifies the name of a new column that will be created in the datalayer to hold each forecast value. If this value is left blank, the forecast value will be *added* to the value of the Dependent Data Column. |
