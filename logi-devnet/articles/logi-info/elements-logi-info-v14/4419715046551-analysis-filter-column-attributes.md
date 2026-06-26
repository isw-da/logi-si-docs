---
title: "Analysis Filter - Column Attributes"
id: 4419715046551
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715046551-Analysis-Filter-Column-Attributes
updated_at: 2022-07-17T02:09:29Z
---

# Analysis Filter - Column Attributes

# Analysis Filter - Column Attributes

The Analysis Filter Column element has the following attributes:

| Attribute | Description |
| --- | --- |
| Column Header | (Required) Specifies the text describing the column that will appear in the list of columns that can be selected when defining a filter in Design view. This text also appears in the filter description, between square brackets, in Simple view. Allows you to specify a "user-friendly" name for the column. |
| Data Column | (Required) Specifies the name of a column in the datalayer. |
| Data Type | (Required) Specifies the data type of the column specified in the previous attribute. |
| ID | (Required) Specifies a unique identifier for this element. |
| Format | Specifies a format for values or percentages displayed. More information can be found in [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data). |
| Popup Values for Filter | Specifies text to be displayed in Simple view when no filters have been defined.  Default value: *(No filters)* |
| Security Right ID | If specified, access to this element is controlled via Logi security. Specify the ID of a Right defined in the application's settings/security section. Only users that Right will be able to see the element. Multiple Right IDs may be entered in a comma-separated list. In that case, the element will be visible to users with any one of the Rights specified. |
