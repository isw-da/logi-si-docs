---
title: "Row-Level Expressions"
id: 34932904405901
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932904405901-Row-Level-Expressions
updated_at: 2026-05-26T22:07:05Z
---

# Row-Level Expressions

# Row-Level Expressions

A row-level expression is a mathematical expression involving a single record (row) in the data. They are used to calculate [derived fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) but can also be used in [custom metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836147341--Maintain-Custom-Metrics) and [admin-defined functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions).

Row-level expressions are created using attributes and metrics from the data and [row-level functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions).

**Note:** 
Be careful not to create row-level expressions using fields in a data source that have had their field data type changed. Doing so may generate errors for the row-level expression. Instead, use the original field (with its original field type) to create a derived field of the field type you need and then use the new derived field in your row-level expressions.
