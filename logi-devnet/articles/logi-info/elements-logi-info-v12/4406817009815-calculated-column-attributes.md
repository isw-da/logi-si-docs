---
title: "Calculated Column Attributes"
id: 4406817009815
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817009815-Calculated-Column-Attributes
updated_at: 2022-04-06T06:03:20Z
---

# Calculated Column Attributes

# Calculated Column Attributes

The attributes for the Calculated Column element are described below:

| Attribute | Description |
| --- | --- |
| Formula | (Required) Specifies a JavaScript expression that returns a string, numeric, or boolean value. Tokens, including data from other datalayer columns, literals, intrinsic functions, and functions in script files may be used here. *Do not* start the expression with an equals sign (=). Usage examples are provided below. Select the scripting type using the General element's Scripting Language attribute, in the \_Settings definition (JavaScript if the default and recommended language; VBScript is available for legacy application compatibility only). |
| ID | (Required) Specifies a unique ID for the Calculated Column element, andbecomes the name of the column added to the datalayer. |
| Error Limit | Specifies the maximum number of times (datalayer rows) evaluating an expressionwill be allowed to produce an error before the value specified in the Error Result attribute will be used instead. |
| Error Result | Specifies the value to be returned when the Error Limit is reached during evaluation. Default: *blank* |
| Include Condition | Specifies whether or not this element will be processed when the report runs. If left blank or if it contains an expression that evaluates to *True*, the element is processed and the new column is added to the datalayer. If it evaluates to *False*, the element is ignored and does not affect the datalayer. |
| Script File | Specifies the name of an optional script file containing functions or routines called in the Formula expression. If the script file is in the \_SupportFiles folder, no path is necessary. Otherwise, specify a fully-qualified file system path and filename (tokens such as @Function.AppPhysicalPath~ may be used). |
