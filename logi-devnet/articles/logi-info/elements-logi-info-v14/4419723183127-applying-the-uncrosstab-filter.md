---
title: "Applying the UnCrosstab Filter"
id: 4419723183127
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723183127-Applying-the-UnCrosstab-Filter
updated_at: 2022-12-18T18:47:01Z
---

# Applying the UnCrosstab Filter

# Applying the UnCrosstab Filter

The following example illustrates how the **UnCrosstab Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714903447/uncrosstab_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699911959/uncrosstab_02a.png)

1. As shown above, an **UnCrosstab Filter** element is added as a child beneatha datalayer element.
2. Its **Column Heading ID** attribute value is set to the column used to provide the original pivoted column headings.
3. The **Value Column ID** attribute is set to name of a new column that will receive the data values.
4. The optional **Label Columns** attribute identifies one or more columns, in a comma-separated list, that are not pivoted.
5. The optional **Remove Columns** attribute identifies one or more columns, in a comma-separated list, that should not be included in the output.

In the complete example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the UnCrosstab Filter builds a substitute datalayer by examining each row in the source datalayer and adding rows to the substitute datalayer for each value column found.
