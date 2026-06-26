---
title: "Compare Filter Attributes"
id: 4419722754455
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722754455-Compare-Filter-Attributes
updated_at: 2022-07-17T02:08:43Z
---

# Compare Filter Attributes

# Compare Filter Attributes

The **CompareFilter** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Compare Type | (Required) Specifies the comparison operator to be used. See the table of operators below. |
| Data Column | (Required) Specifies the name of the data column whose data will be compared against the Compare Value attribute value. |
| ID | (Required) Specifies an unique element ID. |
| Case Sensitive | Specifies whether or not the comparisons of text values will be case-sensitive. Default value: *False* When used with DataLayer.ActiveSQL, this attribute may be set to *DataSourceCollation*. Case-sensitivity will then be defined by the database column's "collation" setting, which may or may not be case-sensitive. This option can provide better performance for case-insensitive filters. |
| Compare Value | Specifies the value that data will be compared against. Tokens may be used, but not @Data tokens for values from the parent datalayer. Leave this value blank to compare against *null*. |
| Data Type | Specifies the type of data being compared. Options include *Boolean*, *Date*, *DateTime*, *Number*, and *Text* and can be used to ensure unambiguous comparisons. |
| Include Condition | Specifies whether or not this element will be processed when the report runs. If left blank or if it contains an expression that evaluates to *True*, the element is processed and the new column is added to the datalayer. If it evaluates to *False*, the element is ignored and does not affect the datalayer. |
