---
title: "ReportFunction"
id: 4415504765847
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504765847-ReportFunction
updated_at: 2021-12-10T03:09:23Z
---

# ReportFunction

# ReportFunction

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) | Y | The id of the function |  |
| **name**  string |  | The function/operator |  |
| **expression**  string |  | The expression |  |
| **dataType**  string |  | The data type |  |
| **formatDataType**  string |  | The output data type |  |
| **syntax**  string |  | The syntax displayed to user | For example:  `expression+expression` |
| **expressionSyntax**  string |  | The syntax of the function/operator | For example:  `+` |
| **isOperator**  boolean |  | Is this an operator (or a function) |  |
| **userDefined**  boolean |  | Is this a user-defined function |  |
| **extendedProperties**  object |  | A dynamic object to store the extended properties |  |

**Sample**:

```
{"id":null,"name":"*","expression":null,"dataType":null,"formatDataType":null,"syntax":"expression * expression","expressionSyntax":"*","isOperator":false}
```
