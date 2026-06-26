---
title: "The DsCalculated Column"
id: 4419707543831
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707543831-The-DsCalculated-Column
updated_at: 2022-07-17T01:50:54Z
---

# The DsCalculated Column

# The DsCalculated Column

The **DsCalculated Column** element is used with DataLayer.Data Services to add a new column to a data containing a value that's the result of a expression. The expression can include data from other columns, tokens, and literals, and is evaluated for every row in the data.

The following topics discsus the DsCalculated Column element:

* [DsCalculated Column Attributes](#Attributes)
* [DsCalculated Column Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4419715265431-DsCalculated-Column-Usage-Examples#Simple)

For more information about Dataviews, see [Dataviews](https://devnet.logianalytics.com/hc/en-us/articles/4419707255831-Dataviews).

## About the DsCalculated Column

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The DsCalculated Column element discussed here is available in Logi Info v12.5 but has been deprecated in later Info versions; consult the [Release Notes](https://documentation.logianalytics.com/inf/content/release-notes.htm) for specific details.

The DsCalculated Column is similar to other elements designed to *extend* the data available in a datalayer. Like the **DsAggregate Column** element, it's added as a child element beneath DataLayer.Data Services and adds a **new column** to the data. This column value is derived data which is accessible using an @Data token.

The new column's value results from evaluating an expression, for each row in the datalayer. This calculated value is populated in the new column in every
row of the data and can be used in further calculations, Summary Rows, Link Params,
etc.
