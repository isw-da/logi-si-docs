---
title: "The MDX Query Builder"
id: 4406818010775
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818010775-The-MDX-Query-Builder
updated_at: 2022-04-06T06:09:38Z
---

# The MDX Query Builder

# The MDX Query Builder

The **MDX Query Builder** provides an easy way to construct MDX queries, which are essentially two-dimensional queries against three-dimensional (cube) data. The notation used to select cube data has strict formatting requirements and the MDX Query Builder helps you build valid queries.

You can invoke the MDX Query Builder from two datalayer elements: **DataLayer.MDX** and **DataLayer.SQL**.

DataLayer.MDX is used to retrieve data for the OLAP Grid and OLAP Table elements, exclusively, and DataLayer.SQL is used to retrieve data for a variety of other elements, including standard data tables and charts. The datalayers must reference a valid **Connection.OLAP** element to access the server.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563016599/usingstudio_56a.png)

As shown above, the MDX Query Builder is invoked by clicking the browse button at the end of the datalayer's **MDX Source** or **Source** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575491735/usingstudio_56b.png)

When the MDX Query Builder is displayed, as shown above, you must first select a (1) Cube. Based on that selection, the MDX Query Builder presents lists of (2) Dimensions and Members, and (3) Measures. These can be moved to an axis or added and removed by selecting and right-clicking them, as shown above. The (4) results of these actions can be seen in the Results panel, in tabular or (5) source code form.

Clicking (6) **OK** will cause the query constructed in the Results panel to be copied into the datalayer's MDX Source or Source attribute, if the MDX Query Builder was called by clicking the attribute's browse button. Otherwise, the query text can be selected, copied, and pasted elsewhere as needed.

### When a Query Has Been Entered Manually

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If you *have already entered a query manually* in the MDX Source or Source attributes and you then open it in the MDX Query Builder, the tool will try to "reverse-engineer" the query. It succeeds at this most of the time but, if the query includes **tokens** or is created using a non-standard SQL language, the MDX Query Builder may fail and display an error message. This is especially likely when Logi tokens have been used outside of a SELECT statement.
