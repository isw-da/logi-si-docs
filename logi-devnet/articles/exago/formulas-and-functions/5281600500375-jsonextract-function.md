---
title: "JSONExtract Function"
id: 5281600500375
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281600500375-JSONExtract-Function
updated_at: 2022-05-03T22:08:04Z
---

# JSONExtract Function

# JSONExtract Function

|  |  |
| --- | --- |
| Description | Pick out one or more portions of a JSON input string as a single value, an array of values, a JSON object, or list of items, via a standard JSONPath expression. |
| Remark | Takes two arguments:  * *JSONtoParse*: The input JSON to parse and return the value(s) from * *JSONPath*: A JSONPath expression that describes what value(s) to return from JSONtoParse   By default, JSONExtract is done in-memory unless the system administrator explicitly sets a hidden system configuration flag to translate JSONExtract to SQL for processing in the Data Source. JSONPath is a standardized format for accessing elements of a JSON structure. |
| Examples | ``` "JSONtoParse ="{    "products":[       {          "name":"Côte de Blaye",          "price":263.50       },       {          "name":"Ipoh Coffee",          "price":46.0       },       {          "name":"Vegie-spread",          "price":43.9       },       {          "name":"Northwoods Cranberry Sauce",          "price":40       }    ] } ```   `JSONExtract(JSONtoParse, "$..price")` returns *[263.5,46.0,43.9,40]* `JSONExtract(JSONtoParse, "$..products[3].name")`returns *[“Northwoods Cranberry Sauce”]*   ---  ``` JSONtoParse = {"color": "green", "code": "123"} ```   `JSONExtract(JSONtoParse, "$.color")` returns *green* `JSONExtract(JSONtoParse, "$.code")` returns *123* |

## JSONExtract in the Data Source

By default, the application will extract JSON in-memory. The system administrator can enable JSON extraction in the database, for those Data Sources that support it, by changing a system configuration setting. Each Data Source implements this function differently, so care should be taken when enabling this feature.

Table A below lists the supported JSONPath expressions for in-memory processing and processing in the supported Data Source types.

Table A — Supported JSONPath Expressions in Data Sources

| JSONPath Feature | In-Memory | MySQL | Oracle | SQL Server 2016+ |
| --- | --- | --- | --- | --- |
| `$` | Yes | Yes | No | No |
| `$.prop` | Yes | Yes | Yes | Yes |
| `$.prop[0]` | Yes | Yes | Yes | Yes |
| `$[1,2]` | Yes | No | No | No |
| `$..recursive` | Yes | No | No | No |
| `$.prop.*` | Yes | Yes | No | No |
| `$[*]` | Yes | Yes | No | No |
| `$[3:5]` | Yes | No | No | No |
| `$[6:]` | Yes | No | No | No |
| `$[:3]` | Yes | No | No | No |
| `$[-2:]` | Yes | No | No | No |
| `$[?(@.prop == val)]` | No | No | No | No |
| `$[?(@.prop != val)]` | No | No | No | No |
| `$[?(@.prop > val)]` | No | No | No | No |
| `$[?(@.prop < val)]` | No | No | No | No |
| `$[?(@.prop >= val)]` | No | No | No | No |
| `$[?(@.prop <= val)]` | No | No | No | No |
| `$[?(@.prop =~ val)]` | No | No | No | No |
| `$[?(!@.prop =~ val)]` | No | No | No | No |
| `$[?(@.prop == val && @.prop == val)]` | No | No | No | No |
| `$[?(@.prop == val || @.prop == val)]` | No | No | No | No |
| `$[?(@.prop in ['1', '2', '3'])]` | No | No | No | No |
| `$[?(@.prop nin ['1', '2', '3'])]` | No | No | No | No |

### Notes and Exceptions

* IBM DB2 — testing has shown this data source does not support JSONExtract although its documentation says that it does
* PostgreSQL — no support for JSONPath syntax, so JSONExtract can only be done in-memory
* Oracle — if the JSONPath expression selects a JSON object from within the main JSON object, the return value will be null
