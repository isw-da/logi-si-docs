---
title: "DsCalculated Column Attributes"
id: 4419715264407
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715264407-DsCalculated-Column-Attributes
updated_at: 2022-07-17T02:08:01Z
---

# DsCalculated Column Attributes

# DsCalculated Column Attributes

The attributes for the DsCalculated Column element are described below:

| Attribute | Description |
| --- | --- |
| DsExpression | (Required) Specifies an expression that returns a string, numeric, or boolean value. Tokens, including data from other data columns, literals, and functions may be used here. The syntax you use to create expressions is discussed in detail in [Dsexpression Reference](https://devnet.logianalytics.com/hc/en-us/articles/4419715267991-Dsexpression-Reference). |
| ID | (Required) Specifies a unique ID for the element, and becomes the name of the column added to the data. |
| Include Condition | Specifies whether or not this element will be processed when the report runs. If left blank or if it contains an expression that evaluates to *True*, the element is processed and the new column is added to the data. If it evaluates to *False*, the element is ignored and does not affect the data. |
