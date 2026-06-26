---
title: "Column Aggregation Functions"
id: 43701095977229
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095977229-Column-Aggregation-Functions
updated_at: 2026-05-29T14:08:17Z
---

# Column Aggregation Functions

# Column Aggregation Functions

Column aggregation functions aggregate data using all the data displayed on a visual. They group results in the same way that the visual itself groups its data. For example, if your visual shows data grouped by gender (male and female), then column aggregation functions return two results, one for males and one for females. Only data included in the visual by any filters that have been applied are included in the results.

The following table describes the supported column aggregation functions.

| Function | Parameter Type | Description |
| --- | --- | --- |
| `AVG(<field>)` | numeric | Returns the average of a column (field), grouped in the same manner as the visual data. |
| `COUNT(<field>)` | any | Returns the numeric count of values in a column (field), grouped in the same manner as the visual data.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.  Use the wildcard character (\*) for `<field>` to include null values for the field in the count. |
| `COUNTD(<field>)` | any | Returns the numeric count of unique values in a column (field), grouped in the same manner as the visual data.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.  Use the wildcard character (\*) for `<field>` to include null values for the field in the count. |
| `MAX(<field>)` | numeric | Returns the maximum value of a column (field), grouped in the same manner as the visual data. |
| `MIN(<field>)` | numeric | Returns the minimum value of a column (field), grouped in the same manner as the visual data. |
| `SUM(<field>)` | numeric | Returns the sum of a column (field), grouped in the same manner as the visual data. |
| `FIRST_VALUE(<field>)` | any | Returns the first value of a given expression in the group, as when the expression is sorted in the ascending order. |
| `LAST_VALUE(<field>)` | any | Returns the last value of a given expression in the group, as when the expression is sorted in the ascending order. |
| `STDDEV_POP(<field>)` | numeric | Computes the population standard deviation and returns the square root of the population variance. |
| `STDDEV_SAMP(<field>)` | numeric | Computes the cumulative sample standard deviation and returns the square root of the sample variance. |
| `VAR_POP(<field>)` | numeric | Returns the population standard variance of a given expression. |
| `VAR_SAMP(<field>)` | numeric | Returns the sample variance of a given expression. |
| `MEDIAN(<field>)` | numeric | Computes the median value across the group. |

### Example

Suppose you have the following fields and data in a data source:

| name | gender | city | earned | spent |
| --- | --- | --- | --- | --- |
| Alan | M | Rockville | $10 | $2 |
| Bob | M | Rockville | $8 | $3 |
| Carol | F | Rockville | $5 | $5 |
| Darlene | F | Reston | $4 | $6 |
| Ed | M | Reston | $2 | $8 |

To use this data set to create a custom metric called `Leftover` (a group's leftover money), use the following formula.

SUM( earned ) - SUM( spent )

If you used the `Leftover` custom metric in a visual grouping by gender using the data above, you would get the results shown below.

| Gender | Leftover |
| --- | --- |
| F | -2 |
| M | 7 |
| Total | 5 |

Males have $7, derived from (10+8+2) - (2+3+8). Females have -$2 left over, derived from (5+4) - (5+6). If you used the same custom metric in a visual grouping by city, you would see Rockville having $13, from (10+8+5) - (2+3+5), and Reston having -$8, from (4+2) - (6+8).
