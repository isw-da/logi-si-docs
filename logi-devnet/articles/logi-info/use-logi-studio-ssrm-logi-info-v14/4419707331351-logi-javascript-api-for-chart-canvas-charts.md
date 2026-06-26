---
title: "Logi JavaScript API for Chart Canvas Charts"
id: 4419707331351
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707331351-Logi-JavaScript-API-for-Chart-Canvas-Charts
updated_at: 2022-07-17T02:09:13Z
---

# Logi JavaScript API for Chart Canvas Charts

# Logi JavaScript API for Chart Canvas Charts

The Logi JavaScript API for Chart Canvas Charts is a library that developers can use to work with Chart Canvas Charts.

The following topics provide information needed to work with the API:

* [Getting the Chart Object](https://devnet.logianalytics.com/hc/en-us/articles/4419707334167-Getting-the-Chart-Object#Object)
* [Updating Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707337111-Updating-Chart-Data#Updating)
* [Appending Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715101591-Appending-Chart-Data#Appending)
* [Setting JSON Chart Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707335319-Setting-JSON-Chart-Data#JSON)
* [Using a Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419715106199-Using-a-Timer#Timers)
* [Using "Pushed" Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707338135-Using-Pushed-Data-#Pushed)
* [Events: *beforeCreateChart*  and *afterCreateChart*](https://devnet.logianalytics.com/hc/en-us/articles/4419715103511-Events-beforeCreateChart-and-afterCreateChart#afterCreateChart)

## About the API

The **Logi JavaScript API** allows you to interact with Chart Canvas Charts using JavaScript in order to customize them and/or refresh them periodically as needed. Data can be retrieved from the Info application server or directly from JSON sources and the visualization updated without redrawing the entire report page.

Scripts including the API functions can be executed by user interface actions, by using a timer, or by "listening" for data broadcast from an outside source. These are all discussed in the topics mentioned above.

### Showing Initial Data

To show some initial data in a chart that will be updated automatically, use a datalayer under the chart or series as you normally would. This datalayer will run and provide data for the chart when the page is first loaded, or when its refreshed, but will not interfere with data delivered using this API.

### Restrictions

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Logi Info licenses the underlying code for Chart Canvas Charts from a 3rd-party. However, we only license the part of their code library that we need, not the entire library, and our license does not include the right to allow developers to independently access the library. Developers who access the library directly in their Logi Info applications using the Logi API do so at their own risk,
as we
cannot guarantee that the
library and/or our implementation of it will not change in future Logi Info releases.
