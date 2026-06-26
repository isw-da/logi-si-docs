---
title: "The Group Filter"
id: 4419722944407
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722944407-The-Group-Filter
updated_at: 2022-07-17T01:47:46Z
---

# The Group Filter

# The Group Filter

The **Group Filter** groups the data rows in a datalayer and gives youthe ability to create aggregate values from the grouped rows.

The following topics discuss the Group Filter element:

* [Grouping Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707616279-Grouping-Data#Grouping)
* [Grouping for Unique Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419715318935-Grouping-for-Unique-Rows#Unique)
* [Grouping on Multiple Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419722941975-Grouping-on-Multiple-Columns#Multiple)
* [Conditional Grouping](https://devnet.logianalytics.com/hc/en-us/articles/4419707615255-Conditional-Grouping#Conditional)
* [Aggregating Grouped Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707614359-Aggregating-Grouped-Data#Aggregating)
* [Using Group DrillThrough](https://devnet.logianalytics.com/hc/en-us/articles/4419715320087-Using-Group-DrillThrough#Drillthrough)

## About the Group Filter

The behavior of the Group Filter element is similar to that of the GROUP BY clause in a SQL query. However, unlike a query, the element applies its grouping to data *after* it's been retrieved into the datalayer. This is very useful as it allows grouping to be applied to *all* kinds of data, including data from sources that lack SQL-like features, such as XML files and web services.
