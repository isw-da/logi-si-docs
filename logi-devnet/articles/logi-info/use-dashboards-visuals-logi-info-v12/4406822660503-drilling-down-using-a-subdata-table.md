---
title: "\"Drilling Down\" using a Subdata Table"
id: 4406822660503
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822660503--Drilling-Down-using-a-Subdata-Table
updated_at: 2022-04-06T06:10:27Z
---

# "Drilling Down" using a Subdata Table

# "Drilling Down" using a Subdata Table

When presenting summarized data in table, there's often a need to "drill-down"; to display the supporting data. Sometimes this means displaying an entirely **different** detail report, but frequently the detail data can be shown right **within** the original data table. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575414551/worksubdata_01.png)

Shown above is a **data table** that presents customer information, including their order totals. If more detailed information about a customer's orders is desired, the **Customer ID** value has been configured as a drill-down link.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575414807/worksubdata_02.png)

When the Customer ID link is clicked, the main table **expands** downward, as shown above, and a second or "sub" data table, with order information for the selected customer, is displayed within it. Clicking the link again will hide the subdata table. A More Info Row element provides the expansion capability, see [Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822236823-Data-Table-Rows).

To generate this report, **hierarchical data** is required. This kind of data can be created with complicated SQL queries, however, Logi Studio offers an alternate, easier approach. The **Subdata Layer**, and **Subdata Layer Relation Column** elements can be used to create hierarchical data without the need for complicated SQL queries.
