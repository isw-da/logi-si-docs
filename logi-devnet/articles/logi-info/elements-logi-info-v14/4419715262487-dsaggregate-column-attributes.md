---
title: "DsAggregate Column Attributes"
id: 4419715262487
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715262487-DsAggregate-Column-Attributes
updated_at: 2022-07-17T02:08:02Z
---

# DsAggregate Column Attributes

# DsAggregate Column Attributes

The attributes for the DsAggregate Column element are described below:

| Attribute | Description |
| --- | --- |
| Aggregate Column | (Required) Specifies the name of the column in the datalayer that contains the values to be aggregated. |
| Aggregate Function | (Required) Specifies the aggregating function to be applied to the column named in the previous attribute. The available functions include:  * Avg * Count * Distinct * Max * Min * Sum |
| ID | (Required) Specifies a unique ID for the element. |
| Include Condition | Specifies if the aggregation will be applied. If left blank or contains a formula that evaluates to *True*, the element is applied to the data. If the value evaluates to *False*, the element is ignored and does not affect the data. |
