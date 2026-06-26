---
title: "Creating Hierarchies by Hiding Duplicate Values"
id: 4419722948759
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722948759-Creating-Hierarchies-by-Hiding-Duplicate-Values
updated_at: 2022-07-17T01:47:38Z
---

# Creating Hierarchies by Hiding Duplicate Values

# Creating Hierarchies by Hiding Duplicate Values

Use the **Hide Duplicates** element to create a hierarchical layout
within a Data Table from one or more data groups.

The Hide Duplicates element can be added beneath any Data Table Column to
suppress output when the record in the current row is equal to the record
from the previous row. By utilizing the Hide Duplicates element in several
columns, developers can achieve the effect of a hierarchical table.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714780055/hierarchdata_13.png)

This example starts with the same datalayer used in the previous example,
and uses one **Data Table Column** element for each report column, as
shown above. Each Data Table Column has a child **Label** element to
display the data. No **Group Header Row** or
**Group Summary Row** elements, or their child elements, will be
used.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706865687/hierarchdata_14.png)

Beneath *each* of the first six Data Table Column elements, add a
**Hide Duplicates** element. This element has one attribute,
**Data Column**, which is the name of the column to check for duplicate
values.

In the first three columns (the "Customer" columns), set this
value to "CustomerID", as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714780311/hierarchdata_15.png)

In the second set of three columns (the "Order" columns), set
Hide Duplicates elements' Data Column attribute to a comma-separated list
of "CustomerID,OrderID", as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699750679/hierarchdata_16.png)

and the resulting report shows how the data is grouped and indented by
virtue of suppressing duplicate data.
