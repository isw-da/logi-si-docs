---
title: "Summarizing Column Data"
id: 4419722795671
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722795671-Summarizing-Column-Data
updated_at: 2022-07-17T01:54:36Z
---

# Summarizing Column Data

# Summarizing Column Data

You can perform typical *aggregations* of column data to create summary information for Data Tables. The following aggregations are available when summarizing column data:

* Average
* AverageOfAllRows
* Count
* CountOfAllRows
* DistinctCount
* Max
* Median
* Min
* Mode
* StdDev
* Sum

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)By default, aggregations *exclude* columns with Null values. Create the constant rdCalculationsIncludeNulls in your \_Settings definition and set it to *True* if you want to include them.

You can display the summary information at the bottom of a Data Table in a dedicated row, on every page or just the last page (if the data spans multiple pages).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706734999/dtcols_09_621x150.png)

To summarize a data column:

1. Add a **Data Column Summary** element beneath a Data Table Column element, as shown above.
2. Set its **Data Column** attribute value to the name of the column to be summarized.
3. Select an aggregating function in the **Function** attribute value.
4. Give the element an **ID** - this is *important* as the ID may be used later in order to reference the summarized value.
5. Set the **Data Type** attribute value to the proper data type (optional but recommended).

You can add a Data Column Summary element to every Data Table column that you want to summarize.
As mentioned above, the summarized value is available using an @Data token. So, the data in the example above would be available as @Data.sumFreight~. However, you do not need to use this token if you use a **Summary Row** element to display your summarized data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699635223/dtcols_10_541x145.png)

As shown above, the **Summary Row** element is added as a child of the Data Table (its position in the element tree does not matter) and its attributes are set as shown. This will cause a separate row to appear at the end of the report and its **Caption** will appear in the first column; the summarized values for each column that has a child Summary element will automatically appear in this row.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706735255/dtcols_11.png)

The example above shows the summary row and summarized Freight column value.   
![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The summary row will inherit the *format* of its data column.
An alternative to using data column summaries is to use datalayer aggregate columns. An aggregate column behaves like any other column in the datalayer, and developers can perform additional calculations using more datalayer column elements.
