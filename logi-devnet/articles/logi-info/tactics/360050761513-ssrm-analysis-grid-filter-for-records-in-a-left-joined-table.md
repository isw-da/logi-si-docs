---
title: "SSRM Analysis Grid: Filter for Records in a Left Joined Table"
id: 360050761513
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050761513-SSRM-Analysis-Grid-Filter-for-Records-in-a-Left-Joined-Table
updated_at: 2020-07-27T22:32:40Z
---

# SSRM Analysis Grid: Filter for Records in a Left Joined Table

**Description**

An SSRM user may want to filter for all records from the first table selected that don't have a matching records from a second table that is left-joined to it.  This is somewhat tricky to achieve in the SSRM Analysis Grid.  Applying a filter looking for a null or empty-string value in a column from the second table will not work for this purpose.  ActiveSQL has been designed so that filters against a column from a left-joined table are applied to the subquery just for that table, then the left-join is converted to an inner-join in the table, so the filter is restrictive on the whole data set, as users who do not understand SQL expect the filters to work this way.  This makes answering the original question somwhat tricky, as you need to filter on the result set after the first table is left-joined to the second table.

**Implementation:**

The tactic used here is to create a calculated column that uses columns from both tables, so it must be generated off of the joined result set.  Then you can filter off this calculated column.

A quick sample formula column / calculated column in SQL Server syntax generated against the Northwind test database is below.

```
Left( isNull([Customer.Full Name],'abcdefg')+[Orders.Customer Id], 7)
```

* In this example both fields are text fields, you could use non-text fields, but the syntax would be different or you'd at least have to cast / convert them to strings first
* [Orders.Customer Id] is from the first table
* [Customer.Full Name] is from the left-joined table, it is assumed there is always a value in this column
* isNull is used to identify Null records in the column from the left-joined column, then replace it with a unique string that can be filtered against.
* The Left function trims the whole resulting string so the records you are looking for should have the value 'abcdefg'

Then a filter has to be added where you filter against this new formula column for records = 'abcdefg'

**Further Reading**

ActiveSQL

<https://documentation.logianalytics.com/logiinfov12/content/datalayer.active-sql-12.7.htm>

Developing with the Analysis Grid

<https://documentation.logianalytics.com/logiinfov12/content/analysis-grid-devs-12.7.htm>

Configuring InfoGo (SSRM) for developers

<https://documentation.logianalytics.com/logiinfov12/content/config-infogo-devs.htm>
