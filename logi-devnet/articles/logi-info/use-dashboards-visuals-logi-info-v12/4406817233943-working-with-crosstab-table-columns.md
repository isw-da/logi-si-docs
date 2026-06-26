---
title: "Working with Crosstab Table Columns"
id: 4406817233943
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817233943-Working-with-Crosstab-Table-Columns
updated_at: 2022-04-06T06:04:51Z
---

# Working with Crosstab Table Columns

# Working with Crosstab Table Columns

Instead of using the wizard, developers can manually build crosstab tables using two types of crosstab table columns: Label Columns and Value Columns. Crosstab tables have one Label Column by default; the number of Value Column cells is determined by the number of Crosstab Column values.

Here's how to add a Crosstab Table Label column:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563421207/xtabtable_06.png)

1. As shown above, in Logi Studio, select the parent Crosstab Table element and add a **Crosstab Table Label Column** element beneath it. Configure any of its optional attributes.
2. Then, add a **Label** element beneath the new column and use a regular @Data token to reference values from a column returned by the datalayer.

Next, we want to add **Crosstab Table Value Columns** elements to create the Value columns for the crosstab table. Value columns contain the results of the aggregations of the data from the specified column.

But the results of the aggregations do not appear in the datalayer under any of its column names, so how is it referenced? Special @Data tokens allow you to access Crosstab column and Value data. Here are the tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575802263/xtabtable_07.png)

These special tokens are:

* **@Data.rdCrosstabColumn~** - Returns the values in the specified Crosstab Column
* **@Data.rdCrosstabValue~** - Returns the aggregated values in the specified Value Column
* **@Data.rdCrosstabValCount~** - Returns the number of corresponding records from the Value Column used to calculate the current aggregate value if the aggregation is *Sum*, *Count*, or *Average*.

Let's add a Value Column and set its attributes using the special tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584059543/xtabtable_08.png)

1. Beneath the Crosstab Table element, add a **Crosstab Table Value Columns** element, as shown above.
2. We want to use data in the column headers, so set the element's **Column Header** attribute to one of the special tokens: *@Data.rdCrosstabColumn~.*   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563421591/xtabtable_09.png)

3. Add a **Label** element beneath the Crosstab Table Value Columns element and set its **Caption** attribute to *@Data.rdCrosstabValue~*, as shown above, to display the aggregated crosstab values.
