---
title: "Building a Report"
id: 4415492632215
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492632215-Building-a-Report
updated_at: 2021-12-10T15:40:07Z
---

# Building a Report

# Building a Report

This topic provides information about how to create different reports in the Izenda BI.

* [Build a Generic Report](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report)
  + [Prepare an Empty Report Object](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#_bm)
  + [Populate Report Name and Categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#_bm2)
  + [Populate selected data sources](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#Populate_selected_data_sources)
  + [Call Save report as draft API](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#_bm4)
  + [Populate the report parts](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#_bm5)
  + [Call Save report API](https://devnet.logianalytics.com/hc/en-us/articles/4415492651031-Build-a-Generic-Report#_bm6)
* [Build a simple Grid](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid)
  + [Prepare an empty ReportPartGrid object](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid#_bm)
  + [Populate selected data sources fields](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid#Populate_selected_data_sources_fields)
  + [Update the properties of each field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid#_bm3)
  + [Update the properties of the grid in “properties” field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid#_bm4)
  + [Back to the step in `BuildaGenericReport`](https://devnet.logianalytics.com/hc/en-us/articles/4415504585495-Build-a-Simple-Grid#Build)
* [Build a simple Chart](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart)
  + [Prepare an empty ReportPartChart object](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart#_bm)
  + [Populate selected data sources fields](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart#_bm2)
  + [Update the properties of each field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart#_bm3)
  + [Update the properties of the Chart in “properties” field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart#_bm4)
  + [Back to the Save step in `BuildaGenericReport`](https://devnet.logianalytics.com/hc/en-us/articles/4415492652183-Build-a-Simple-Chart#Build)
* [Build a simple Gauge](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge)
  + [Prepare an empty ReportPartGauge object](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge#_bm)
  + [Populate selected data sources fields](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge#Populate_selected_data_sources_fields)
  + [Update the properties of each field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge#_bm3)
  + [Update the properties of the Gauge in “properties” field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge#_bm4)
  + [Back to the Save step in `BuildaGenericReport`](https://devnet.logianalytics.com/hc/en-us/articles/4415492655767-Build-a-Simple-Gauge#Build)
* [Build a simple Map](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map)
  + [Prepare an empty ReportPartMap object](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map#_bm)
  + [Populate selected data sources fields](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map#_bm2)
  + [Update the properties of each field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map#_bm3)
  + [Update the properties of the Map in “properties” field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map#_bm4)
  + [Back to the Save step in `BuildaGenericReport`](https://devnet.logianalytics.com/hc/en-us/articles/4415492657687-Build-a-Simple-Map#Build)
* [Build a simple Form](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form)
  + [Prepare an empty ReportPartForm object](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form#_bm)
  + [Populate selected data sources fields](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form#_bm2)
  + [Update the properties of each field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form#_bm3)
  + [Update the properties of the Form in “properties” field per user selection](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form#_bm4)
  + [Back to the Save step in `BuildaGenericReport`](https://devnet.logianalytics.com/hc/en-us/articles/4415492654487-Build-a-Simple-Form#Build)
* [Sample Properties for a ReportPartElement](https://devnet.logianalytics.com/hc/en-us/articles/4415492658583-Sample-Properties-for-a-ReportPartElement)
