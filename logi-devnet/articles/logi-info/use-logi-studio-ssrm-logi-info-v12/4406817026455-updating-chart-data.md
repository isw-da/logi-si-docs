---
title: "Updating Chart Data"
id: 4406817026455
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817026455-Updating-Chart-Data
updated_at: 2022-04-06T06:03:27Z
---

# Updating Chart Data

# Updating Chart Data

To request new data from the Info application server and replace the data, if any, in the chart, use this chart object method:

rdUpdateChartData(*[requestParams]*)
where requestParams is:

* An optional JavaScript object,
* Provided to the report definition as Request variables when the function is called,
* Where the property name is the Request variable name and the property value is Request variable value.

Here's an example using the chart object from [Getting the Chart Object](https://devnet.logianalytics.com/hc/en-us/articles/4406822111255-Getting-the-Chart-Object):

var requestParams = {};   
requestParams.OrderDate = "01/01/2015";  
requestParams.ProductCategory = "Seafood";  
myChartObject.rdUpdateChartData(requestParams);

In a hypothetical report definition using this script, the Chart Canvas Chart element would have a child datalayer that made use of the request variables by using tokens. For example, using DataLayer.SQL, they might be used in a query like this:

SELECT \* FROM Orders WHERE OrderDate = '@Request.OrderDate~' AND Category = '@Request.ProductCategory~'

The query would return a result set in which the OrderDate column value = "01/01/2015" and the Category column value = "Seafood". The chart series would be updated with that result set.
The same behavior applies whether the datalayer is a child of the Chart Canvas Chart element or a child of one of the Series elements.
