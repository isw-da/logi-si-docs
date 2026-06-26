---
title: "Grouping on Multiple Columns"
id: 4406822354583
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822354583-Grouping-on-Multiple-Columns
updated_at: 2022-04-06T06:06:29Z
---

# Grouping on Multiple Columns

# Grouping on Multiple Columns

Grouping can be accomplished on more than one column in the datalayer at the same time. This example shows the effects of grouping multiple columns:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583912343/groupfilter_05.png)

1. As shown above, a **Group Filter** element is added as a child to the datalayer element.
2. Its **Group Column** attribute is set to the names of columns in the datalayer, in a comma-separated list. The data will be grouped based on the values in these columns, in the order of the column names in the list.
3. Its **Data Type** column is set to the data type of the column named in the Group Column attribute. This ensures unambiguous ordering of the data and, though optional, setting it is recommended. If the columns listed in Group Column are of different data types, individual data types can also be entered here in a comma-separated list as well.
4. Its **Keep Grouped Rows** attribute is set to *True* to ensure that all rows are retained in the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563262743/groupfilter_06.png)

The resulting output is shown above. The rows are grouped first by LastName and then by CustomerID.
The optional **Sort Sequence** attribute allows you to control the way in which grouped rows are sorted. The default (blank) value causes *Ascending* order to be used, but you can change the value to *Descending* if desired. When grouping on multiple columns, you can control the sort sequence for each grouping by entering multiple sort order values here, in a comma-separated list that corresponds to the column list.
