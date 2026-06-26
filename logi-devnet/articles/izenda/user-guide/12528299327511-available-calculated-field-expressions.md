---
title: "Available Calculated Field Expressions"
id: 12528299327511
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528299327511-Available-Calculated-Field-Expressions
updated_at: 2023-02-23T15:04:54Z
---

# Available Calculated Field Expressions

# Available Calculated Field Expressions

| Function Name | Syntax |
| --- | --- |
| expression | expression |
| + | expression + expression |
| - | expression - expression |
| / | expression / expression |
| < | expression < expression |
| <= | expression <= expression |
| <> | expression <> expression |
| = | expression = expression |
| > | expression > expression |
| >= | expression >= expression |
| AND | boolean\_expression AND boolean\_expression |
| AVG | AVG (expression) |
| BETWEEN | BETWEEN (test\_expression, begin\_expression, end\_expression) |
| CASE WHEN…THEN…ELSE…END | CASE WHEN (boolean\_expression) THEN (result\_expression) […n] [ELSE (else\_result\_expression)] END |
| CASE…WHEN…THEN…ELSE…END | CASE (input\_expression) WHEN (when\_expression) THEN (result\_expression) […n] [ELSE (else\_result\_expression)] END |
| CAST…AS | CAST (expression AS data\_type) |
| CONCAT | CONCAT (expression, expression[,expression…]) |
| CONVERT | CONVERT (data\_type [( length)], expression[, style]) |
| COUNT | COUNT (expression) |
| DATEADD | DATEADD (datepart, number, expression) |
| DATEDIFF | DATEDIFF (datepart, startdate, enddate) |
| DATEPART | DATEPART (datepart, date) |
| DISTINCT | DISTINCT (column) or DISTINCT column |
| GETDATE | GETDATE () |
| IF…THEN…ELSE…END | IF (boolean\_expression) THEN (true\_expression) [ELSE (false\_expression)] END |
| IIF | IIF (boolean\_expression, true\_expression, [false\_expression]) |
| ISNULL | ISNULL (check\_expression, replacement\_value) |
| LEN | LEN (expression) |
| MAX | MAX (expression) |
| MIN | MIN (expression) |
| OR | boolean\_expression OR boolean\_expression |
| ROUND | ROUND (expression, length[, function]) |
| RUNNING AVG | RUNNINGAVG (column) |
| RUNNING COUNT | RUNNINGCOUNT (column) |
| RUNNING SUM | RUNNINGSUM (column) |
| SUM | SUM (expression) |
