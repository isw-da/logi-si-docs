---
title: "Aggregating Grouped Data"
id: 4419707551127
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707551127-Aggregating-Grouped-Data
updated_at: 2022-07-17T01:50:39Z
---

# Aggregating Grouped Data

# Aggregating Grouped Data

A very common requirement when grouping data is to perform some kind of *aggregation*, such as summing or counting, of the grouped values. The **DsAggregate Column** element, when used as a child of DsGroup, gives you the ability to generate this summary data for the grouped columns in the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699697431/dsgroup_06.png)

In the example above, the DsGroup element's Group Column has been set to ShipCity. A DsAggregate Column element has been added as a child element and configured to Sum the values found in the grouped Freight columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699697687/dsgroup_07.png)

And the results are shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) When grouping is applied and aggregation is used, only values from the columns named in the
Group Column and the Aggregate Column attributes are
returned to the datalayer.
