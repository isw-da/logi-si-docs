---
title: "Grouping for Unique Rows"
id: 4419715318935
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715318935-Grouping-for-Unique-Rows
updated_at: 2022-07-17T01:47:49Z
---

# Grouping for Unique Rows

# Grouping for Unique Rows

There are many situations in which you may need to use only *unique* rows, for instance, to populate an **Input Select List** element. This can be done with grouping, as the following example illustrates:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706862231/groupfilter_03.png)

1. As shown above, a **Group Filter** element is added as a child to the datalayer element.
2. Its **Group Column** attribute is set to the name of a column in the datalayer. The data will be grouped based on the values in this column.
3. Its **Data Type** column is set to the data type of the column named in the Group Column attribute. This ensures unambiguous ordering of the data and, though optional, setting it is recommended.
4. The **Keep Grouped Rows** attribute is left *blank*; its default value is *False*. This causes all rows after the first one in each group to be *removed* from the datalayer, creating a list of unique values.
![](https://devnet.logianalytics.com/hc/article_attachments/4419714778903/groupfilter_04.png)

The resulting output is shown above. The rows are grouped by CategoryID and only one row exists for each category.
