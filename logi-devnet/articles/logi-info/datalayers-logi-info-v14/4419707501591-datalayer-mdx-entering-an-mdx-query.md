---
title: "DataLayer.MDX - Entering an MDX Query"
id: 4419707501591
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707501591-DataLayer-MDX-Entering-an-MDX-Query
updated_at: 2022-07-17T01:53:09Z
---

# DataLayer.MDX - Entering an MDX Query

# DataLayer.MDX - Entering an MDX Query

When working with an **OLAP Table** element, you can enter an MDX query directly into the DataLayer.MDX element's **MDX Source** attribute. This query is executed at runtime against the datasource associated with the element's Connection ID attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714720407/dlmdx_01.png)

The example above shows a query in the MDX Source attribute value. As you can see, this type of query is relatively complex and prone to typos during entry. In order to help you formulate a correct query, instead of typing in the query you can use the **MDX Query Builder** tool, which is accessed by clicking the Browse button at the end of the MDX Source attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699653015/dlmdx_02.png)

Based on the selected (1) Cube, the MDX Query Builder presents lists of (2) Dimensions and Members, **and** (3) Measures. These can be moved to an axis or added and removed by selecting and right-clicking them, as shown above. The (4) results of these actions can be seen in the Results panel, in tabular or (5) source code form.
Clicking (6) **OK** will cause the query constructed in the Results panel to be copied into the datalayer's **MDX Source** attribute, if the MDX Query Builder was called by clicking the attribute's browse button. Otherwise, the query text can be selected, copied, and pasted elsewhere as needed.

## When a Query Has Been Entered Manually

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) If you *have already entered a query manually* in the MDX Source attribute and you then open it in the MDX Query Builder, the tool will try to "reverse-engineer" the query. It succeeds at this most of the time but, if the query includes **tokens** or is created using a non-standard SQL language, the MDX Query Builder may fail and display an error message. This is especially likely when Logi tokens have been used outside of a SELECT statement.
