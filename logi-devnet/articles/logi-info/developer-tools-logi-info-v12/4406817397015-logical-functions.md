---
title: "Logical Functions"
id: 4406817397015
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817397015-Logical-Functions
updated_at: 2022-04-06T06:05:50Z
---

# Logical Functions

# Logical Functions

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The functions listed in the table below are for SQL queries and should not be used with inline scripts.

The following table lists the logical functions used in Logi Info:

| Attribute | Description |
| --- | --- |
| CONTAINS(string, substring) | Returns *true* if the string contains the specified substring. e.g. CONTAINS('Hello World','World') returns true if filter or 1 for calculated column. |
| ENDSWITH(string, substring) | Returns *true* if the string ends with the specified substring. E.g. ENDSWITH('Hello World', 'ld') returns true for filters or 1 for calculated columns. |
| IFNULL(value, default\_value) | Returns the value if it is not null, otherwise the default\_value is returned. Argument types for value and default\_value must match. e.g. IFNULL([ShipVia],2) -if ShipVia is null then 2 is returned otherwise the value of ShipVia is returned. |
| IIF(expression, true\_part, false\_part) | Returns the true\_part if the boolean expression is true, otherwise the false\_part is returned. E.g. IIF(45 > 40, 'big', 'small') returns 'big'. |
| INLIST(test\_value, value1, ... valueN) | Returns *true* if the specified value matches any in the list. e.g. INLIST(4, 3, 5, 6, 4) returns *true* for a filter or 1 for a calculated column. Sample: INLIST([ShipVIA],1,2,3). |
| ISNULL(value) | Returns *true* if the value is null, false if it contains any value. e.g. ISNULL([ShipRegion]) returns *true* or *false* for filters and *0* or *1* for calculated columns. |
| STARTSWITH(string, substring) | Returns *true* if the string begins with the specified substring. E.g. STARTSWITH('Hello World', 'He') returns *true* for filters or 1 for calculated columns. |
