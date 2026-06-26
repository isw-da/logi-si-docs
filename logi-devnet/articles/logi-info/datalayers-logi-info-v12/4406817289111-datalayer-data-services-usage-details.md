---
title: "DataLayer.Data Services - Usage Details"
id: 4406817289111
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817289111-DataLayer-Data-Services-Usage-Details
updated_at: 2022-04-06T06:05:11Z
---

# DataLayer.Data Services - Usage Details

# DataLayer.Data Services - Usage Details

Here are some important details about using this datalayer:

* DataLayer.Data Services uses the special **Connection.Logi Application Service** element, which connects it to the built-in web service installed with the Discovery Module 3.0, *not* directly to a datasource. The Dataviews executed by the datalayer specify the required datasource connection details themselves. Connection configuration details are available in [Connecting to the Logi Application Service](https://devnet.logianalytics.com/hc/en-us/articles/4406817373591-Connecting-to-the-Logi-Application-Service).
* DataLayer.Data Services provides data for numerous parent elements, including Local Data, Data Table, certain Input, and all Series elements. The data is available using @Local or @Data tokens, as usual.
* DataLayer.Data Services has optional, specialized "Ds" child elements which can be used to introduce additions to a Dataview at execution. These include custom filtering, grouping, and sorting, and creation of calculated and aggregation columns. See [DataLayer.Data Services - Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406822247575-DataLayer-Data-Services-Attributes) for details. A small set of standard child elements, e.g. Crosstab Filter and Time Period Column, which act on the returned data in the standard fashion are also available for use with this
  datalayer.
