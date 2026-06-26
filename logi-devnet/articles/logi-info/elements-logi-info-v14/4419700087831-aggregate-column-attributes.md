---
title: "Aggregate Column Attributes"
id: 4419700087831
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700087831-Aggregate-Column-Attributes
updated_at: 2022-07-17T02:25:29Z
---

# Aggregate Column Attributes

# Aggregate Column Attributes

The attributes for the Aggregate Column element are described below:

| Attribute | Description |
| --- | --- |
| Aggregate Column | (Required) The name of the column in the datalayer that contains the values to be aggregated. |
| Aggregate Function | (Required) The aggregating function to be applied to the column named in the previous attribute. The available functions include:  * Average * Concat (see section below) * Count * Distinct Count * Max * Median * Min * Mode * Std Deviation * Sum    Columns with Null values are *excluded* by default. If you want them to be included, create the constant rdCalculationsIncludeNulls and set it to *True.* |
| ID | (Required) The unique element ID for the Aggregate Column element. |
| Concat Separator | The character used to separate concatenated text values, if any. Default: *comma* |
| Data Type | The data type of the column named in the Aggregate Column attribute value. |
| Include Condition | Determines if the aggregation will be applied. If left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. |

## The Concat Function

The Concat function builds a string of concatenated values by taking all the text in the specified data column and concatenating it together using the default (a comma) or specified separator character.

![](https://devnet.logianalytics.com/hc/article_attachments/7522882076951/aggrcol_04.png)

This can be useful for a variety of purposes, including creating default values for select lists.
