---
title: "Appending Chart Data"
id: 4406817020311
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817020311-Appending-Chart-Data
updated_at: 2022-04-06T06:03:24Z
---

# Appending Chart Data

# Appending Chart Data

To request new data from the Info application server and append it to existing data, if any, in the chart, use this chart object method:

rdAppendChartData(*[requestParams], maxVisiblePoints*)

where requestParams is:

* An optional JavaScript object,
* Provided to the report definition as Request variables when the function is called,
* Where the property name is the Request variable name and the property value is Request variable value.

and maxVisiblePoints is:

* A positive integer,
* The threshold of total chart data points. The chart will delete old data points if the number of total points is greater than this value.

Here's an example using the chart object from *[Updating Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817026455-Updating-Chart-Data)*:

var requestParams = {};   
requestParams.OrderDate = "01/01/2015";  
requestParams.ProductCategory = "Seafood";  
myChartObject.rdUpdateChartData(requestParams, 100);

See [Updating Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817026455-Updating-Chart-Data) for an explanation of how the requestParams can be used as Request tokens in retrieving data.
