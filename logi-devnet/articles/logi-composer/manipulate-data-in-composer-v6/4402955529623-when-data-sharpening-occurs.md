---
title: "When Data Sharpening Occurs"
id: 4402955529623
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955529623-When-Data-Sharpening-Occurs
updated_at: 2021-08-07T17:30:29Z
---

# When Data Sharpening Occurs

# When Data Sharpening Occurs

When Composer connects to your data source for the first time, it runs an initial query to return a sample of the data set—approximately 100 rows of data—to provide an initial time range. Meanwhile, it continues to run a comprehensive query to obtain the actual MIN/MAX range based on the entire data set. In this instance, based on the results of the sample query, Data Sharpening may not activate because the time range and time granularity results fall short of the criteria for sharpening to execute. However, after Composer completes the full query, Data Sharpening works as expected as long as the correct parameters have been applied and the time criteria are met. Depending on the size of your data set, the comprehensive query process may take a few minutes to complete its execution (additional constraints include the size and type of the data source and other factors such as competing resources on the database and resource and performance limitations).

Bear in mind that Composer connects to and runs queries in your original data source and can be resource intensive. The full query runs in the background at the same time as a series of microqueries that sample data across partitions and refine estimates.

When you create a visual, Composer determines whether Data Sharpening is necessary based on the visual style selected and the time attribute parameters that are set for it.

* For non-trend visuals (such as [bars](https://devnet.logianalytics.com/hc/en-us/articles/4402955700887-Bar-Chart-Styles), [donut charts](https://devnet.logianalytics.com/hc/en-us/articles/4402955704855-Donut-Charts), and [heat maps](https://devnet.logianalytics.com/hc/en-us/articles/4402963079575-Heat-Maps)), the granularity of the driving time field must be less than 10% of the range that is set in the time bar (determined by the MIN/MAX range set in the data source). The minimum granularity used by Composer will *always* be **minutes**. Thus, even if your driving time field granularity (DTFG) is **seconds**, Composer will use **minutes** when performing this 10% rule calculation.
* For trend visuals (such as [line and bars trend](https://devnet.logianalytics.com/hc/en-us/articles/4402963082007-Edit-Line-Bar-Trend-Charts) and [line trend attribute value](https://devnet.logianalytics.com/hc/en-us/articles/4402963083543-Line-Trend-Attribute-Value-Charts) charts), Composer runs an internal check to determine whether Data Sharpening should execute. Similar to the non-trend visuals, a 10% criteria is used, but it is slightly modified for the trend visual scenario. If the granularity of the driving time field for the source is less than 10% of the time granularity used in the particular trend visual, then Data Sharpening executes.

The bottom line is that Composer tries to perform Data Sharpening when warranted based on the size of the data set, the time attributes available, and the time granularity that is set. If Composer determines that results can be rendered in the visual quickly without Data Sharpening, it does so. Otherwise, it attempts to use Data Sharpening to return near instantaneous result sets that are refined over time until the query completes.
