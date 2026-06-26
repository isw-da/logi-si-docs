---
title: "Filter Datalayers"
id: 4419707593111
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707593111-Filter-Datalayers
updated_at: 2022-07-17T02:07:44Z
---

# Filter Datalayers

# Filter Datalayers

Datalayer elements retrieve data from datasources and developers frequently need to apply conditioning to them to exclude data that is unnecessary or unwanted. This filtering is analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer. This topic discusses use of datalayer filtering elements.

The following topics provide additional information about filtering datalayers:

* [Applying a Static Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707592215-Applying-a-Static-Filter#Static)
* [Applying a Dynamic Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707591319-Applying-a-Dynamic-Filter#Dynamic)

## About Filtering Elements

Filtering elements are added to Logi definitions as children of datalayer elements. Their purpose is to *remove rows* from the datalayer based on some criteria. These elements include:

| Element | Description |
| --- | --- |
| Analysis Filter | This super-element adds a complete user interface, configurable from simple to complex, for creating and managing real-time datalayer filtering. It's consistent with the filtering interface now found in other super-elements like the Analysis Grid. For more information, see [The Analysis Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707274007-The-Analysis-Filter). |
| Compare Filter | Analogous to the *WHERE* clause in a SQL query, this element removes rows from the datalayer that do not meet specified criteria. Uses native data engine code for fastest performance. |
| Condition Filter | Similar to the Compare Filter, this element uses scripting to remove rows from the datalayer that do not meet specified criteria. |
| Contain Filter | Analogous to using a *WHERE**x CONTAINS y* clause in a SQL query, this element removes rows from the datalayer that do not return results in a text search of specified columns. |
| DeDuplicate Filter | Analogous to using a *DISTINCT* clause in a SQL query, this element removes rows from the datalayer that have duplicated values in specified columns. |
| RegEx Filter | Removes rows from the datalayer by applying pattern matching using regular expressions. |
| Relevance Filter | Removes rows (*irrelevant* data) from the datalayer that do not meet a threshold; optionally, irrelevant rows can be retained, grouped together, and handled as an individual entity. |
| Security Filter | Removes rows from the datalayer, like a Condition Filter, but is applied based on a user's security rights. |

It's possible to use multiple filters, of the same type or in mixed combinations, to achieve the desired filtering effect.
