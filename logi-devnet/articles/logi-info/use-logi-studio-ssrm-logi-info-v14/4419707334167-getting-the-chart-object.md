---
title: "Getting the Chart Object"
id: 4419707334167
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707334167-Getting-the-Chart-Object
updated_at: 2022-07-17T02:09:13Z
---

# Getting the Chart Object

# Getting the Chart Object

The API library is automatically included in your Logi Info v12+ application when you use Chart Canvas Charts; you do not need to take any special steps to include it in your definition.
The first thing you need to do is get the chart object, using this function:

rdGetChartCanvasObject(*chartId*) 

Here's an example that assumes you have a Chart Canvas Chart element with the ID "myChartCanvas1":

```
var myChartObject = rdGetChartCanvasObject('myChartCanvas1');
```

With the chart object in hand, you can proceed to manipulate the chart data.
