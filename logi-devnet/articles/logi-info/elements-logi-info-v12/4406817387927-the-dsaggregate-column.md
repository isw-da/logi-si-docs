---
title: "The DsAggregate Column"
id: 4406817387927
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817387927-The-DsAggregate-Column
updated_at: 2022-04-06T06:05:48Z
---

# The DsAggregate Column

# The DsAggregate Column

The **DsAggregate Column** element is used with DataLayer.Data Services to add a new column to the data containing an aggregated value of the data in one of the other columns.

The following topics discuss the DsAggregate Column elements:

* [DsAggregate Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817386775-DsAggregate-Column-Attributes)
* [DsAggregate Column Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4406822303127-DsAggregate-Column-Usage-Example)

For more information about Dataviews, see [Dataviews](https://devnet.logianalytics.com/hc/en-us/articles/4406822071191-Dataviews).

## About the DsAggregate Column

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The DsAggregate Column element discussed here is available in Logi Info v12.5 but has been deprecated in later Info versions; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.

The **DsAggregate Column** is similar to other elements designed to *extend* the available data. Like the DsCalculated Column element, it's added as a child element beneath DataLayer.Data Services and adds a **new column** to the data. This column contains derived data which is accessible using an @Data token.

The new column's value is the result of aggregating the value of the data in one column, for all rows, in the data. The aggregated value is populated in the new column in every
row of the data so that it can be used in further calculations and displays.

Similar aggregations can be performed in a Dataview definition but this element allows dynamic aggregations based on variable conditions at runtime.
