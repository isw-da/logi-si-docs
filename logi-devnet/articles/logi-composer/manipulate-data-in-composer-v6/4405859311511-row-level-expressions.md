---
title: "Row-Level Expressions"
id: 4405859311511
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859311511-Row-Level-Expressions
updated_at: 2021-09-21T01:28:12Z
---

# Row-Level Expressions

# Row-Level Expressions

A row-level expression is a mathematical expression involving a single record (row) in the data. They are used to calculate [derived fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) but can also be used in [custom metrics](https://devnet.logianalytics.com/hc/en-us/articles/4405859285399-Maintain-Custom-Metrics) and [admin-defined functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions).

Row-level expressions are created using attributes and metrics from the data and [row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Be careful not to create row-level expressions using fields in a data source that have had their field data type changed. Doing so may generate errors for the row-level expression. Instead, use the original field (with its original field type) to create a derived field of the field type you need and then use the new derived field in your row-level expressions.
