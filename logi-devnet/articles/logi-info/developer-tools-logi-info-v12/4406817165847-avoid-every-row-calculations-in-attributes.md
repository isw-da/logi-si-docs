---
title: "Avoid \"Every Row\" Calculations in Attributes"
id: 4406817165847
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817165847-Avoid-Every-Row-Calculations-in-Attributes
updated_at: 2022-04-06T06:04:27Z
---

# Avoid "Every Row" Calculations in Attributes

# Avoid "Every Row" Calculations in Attributes

Attributes that can evaluate expressions are very useful. However, for
best performance and especially when the evaluation will run for every
datalayer row, try doing the evaluation *outside* of the application.
For example, the **Condition** attribute expects a *True* or
*False* value and you'll get better performance if you can calculate
that value outside of the application, for example, inside a SQL query.

Suppose you want to use a time-difference calculation to apply a
**Conditional Class** element to data: if a date is 10 days overdue,
set the data value color to Red.   
![](https://devnet.logianalytics.com/hc/article_attachments/4417563461655/performance_03.png)

You could put a complete DateDiff( ) expression into its
**Condition** attribute, as shown in the image above. After the data is
retrieved, this calculation will run repeatedly, once for every single row
in the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575834775/performance_04.png)

However, for best performance when using a SQL datasource, do your
DateDiff( ) calculation in your SQL query and create a data column
containing *True* or *False* based on the results. Then use that
data column value in the Condition attribute, as shown above. Once again,
this is especially significant when the comparison has to be run for
*every row* of data.
