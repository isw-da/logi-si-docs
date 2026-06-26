---
title: "Using Forecast.Current Time Period"
id: 4406817466007
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817466007-Using-Forecast-Current-Time-Period
updated_at: 2022-04-06T06:06:16Z
---

# Using Forecast.Current Time Period

# Using Forecast.Current Time Period

The **Forecast.Current Time Period** element produces its forecast by analyzing a value from the last row in the datalayer and "prorating" it into the future, through completion of a specific time period. Its calculations *do not* take working hours per day, holidays, or weekends into consideration.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563289111/forecast_02.png)

The Forecast.Current Time Period element is a child of any datalayer, as shown above, and its attributes include:

| Attribute | Description |
| --- | --- |
| Data Column | (Required) Specifies the name of a column in the datalayer that contains the values which will be "prorated" across the time period. |
| DateTime Data Column | (Required) Specifies the name of a column in the datalayer that contains date values (and, optionally, a time) that are the starting point in time from which to prorate the Data Column value. |
| ID | (Required) A unique element ID. |
| Time Period | (Required) Specifies the time period through which values should be forecast. Options include: Hour, Day, Week, Month, Quarter, Year. |
| Forecast Difference Column ID | Specifies the name of a new column that will be created in the datalayer to hold the value of the difference between the starting data value and each prorated forecast value. |
| Forecast Indicator Column ID | Specifies the name of a new column to be added to the datalayer, with value set to "True", for each row used in the forecast analysis. If left blank, the column will automatically be named "{ElementId}" + "ForecastIndicator" |
| Forecast Value Column ID | Specifies the name of a new column that will be created in the datalayer to hold each forecast value. |
