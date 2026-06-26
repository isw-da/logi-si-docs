---
title: "Applying a Static Filter"
id: 4419707592215
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707592215-Applying-a-Static-Filter
updated_at: 2022-07-17T01:48:55Z
---

# Applying a Static Filter

# Applying a Static Filter

The following example illustrates use of the **Compare Filter**, with static filtering criteria:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706831255/filteringdls_01.png)

1. As shown above, a **Compare Filter** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be compared.
3. The **Compare Type** attribute is set to define the comparison operator. A number of standard operators are provided in a pull-down list and you may also type-in your own operators, such as *!=* (not equal).
4. Finally, the **Compare Value** attribute is set to the *static*, or literal, value the data column values will be compared against. Tokens may be used here. Ensure that date values used here are specified in the *yyyy-mm-dd* format.

Using the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the Compare Filter **removes** all rows that don't match the criteria (CategoryID column value is greater than 4). All that remains in the datalayer for use in the report are rows whose CategoryID values are greater than 4.
