---
title: "Setting JSON Chart Data"
id: 4406817024279
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817024279-Setting-JSON-Chart-Data
updated_at: 2022-04-06T06:03:25Z
---

# Setting JSON Chart Data

# Setting JSON Chart Data

To get the chart data directly from a JSON data source, without going to the application server, use this chart object method:

rdSetChartData(chartOptions, *[updateType], [maxVisiblePoints]*)

where chartOptions is:

* A required JSON data object,
* Containing chart options, using the standard Logi Info server chart data structure.

and updateType is:

* An optional value,
* Either *'UpdateData'* (the default, which replaces the chart data) or *'AppendData'*, which appends the data.

and maxVisiblePoints is:

* A positive integer,
* Used only when updateType = *'AppendData',*
* The threshold of total chart data points. The chart will delete old data points if the number of total points is greater than this value.

Here's an example using the chart object from [Appending Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817020311-Appending-Chart-Data):

var chartOptions = {  
 chart: {},  
 series: [{  
id: 'mySeriesId',   
 data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]  
}]  
};   
myChartObject.rdSetChartData(chartOptions, 'UpdateData');
