---
title: "Aggregating Grouped Data"
id: 4406817399191
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817399191-Aggregating-Grouped-Data
updated_at: 2022-04-06T06:05:52Z
---

# Aggregating Grouped Data

# Aggregating Grouped Data

A very common requirement when grouping data is to perform some kind of *aggregation*, such as summing or counting, of the grouped values. The **DsAggregate Column** element, when used as a child of DsGroup, gives you the ability to generate this summary data for the grouped columns in the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563320087/dsgroup_06.png)

In the example above, the DsGroup element's Group Column has been set to ShipCity. A DsAggregate Column element has been added as a child element and configured to Sum the values found in the grouped Freight columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575725335/dsgroup_07.png)

And the results are shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) When grouping is applied and aggregation is used, only values from the columns named in the
Group Column and the Aggregate Column attributes are
returned to the datalayer.
