---
title: "Table Aggregation Functions"
id: 34932868847245
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868847245-Table-Aggregation-Functions
updated_at: 2026-05-26T22:07:09Z
---

# Table Aggregation Functions

# Table Aggregation Functions

Table aggregation functions are broader in scope than column aggregation functions. Table aggregation functions use all data from a field and produce a single, ungrouped value. You typically do not use the result directly in a visual, since it is ungrouped.

For example, if you have sales records grouped by gender, a `TableSUM` custom metric returns the total sales of all records as one value, regardless of the group in consideration. The `TableSUM` result would include both the male and female data values. Consequently, males and females would appear to have the same sales if the `TableSUM` result was included in the visual.

Table aggregation functions are typically used to calculate percentages of a whole or average values.

The following table describes the supported table aggregation functions.

| Function | Type | Description |
| --- | --- | --- |
| `TableAVG(<field>)` | numeric | Returns the average of a column (field), regardless of how the visual is grouped. |
| `TableCOUNT(<field>)` | any | Returns the numeric count of values in a column (field), regardless of how the visual is grouped.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wildcard character (\*) for `<field>` to include null values for the field in the count. |
| `TableCOUNTD(<field>)` | any | Returns the numeric count of unique values in a column (field), regardless of how the visual is grouped.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wildcard character (\*) for `<field>` to include null values for the field in the count. |
| `TableMAX(<field>)` | numeric | Returns the maximum value of a column (field), regardless of how the visual is grouped. |
| `TableMIN(<field>)` | numeric | TableMIN returns the minimum value of a column (field), regardless of how the visual is grouped. |
| `TableSUM(<field>)` | numeric | TableSUM returns the sum of a column (field), regardless of how the visual is grouped. |

### Example

Suppose you have the following fields and data:

| name | gender | city | earned | spent |
| --- | --- | --- | --- | --- |
| Alan | M | Rockville | $10 | $2 |
| Bob | M | Rockville | $8 | $3 |
| Carol | F | Rockville | $5 | $5 |
| Darlene | F | Reston | $4 | $6 |
| Ed | M | Reston | $2 | $8 |

Using this data, you can create a custom metric containing individual earnings as a percentage of total earnings with the following formula:

SUM(earned) / TableSUM(earned) \* 100

in which:

* `SUM(earned)` calculates the sum earnings for each individual.
* `TableSUM(earned)` calculates the total earnings of all records in the data.
* The quotient of `SUM(earned) / TableSUM(earned)` is multiplied by 100 to convert the result into a percentage.

Shown on a table using the example data above, the results would look like this:

| Name | % of Whole |
| --- | --- |
| Alan | 34.48 |
| Bob | 27.59 |
| Carol | 17.24 |
| Darlene | 13.79 |
| Ed | 6.90 |
| Total | 100 |
