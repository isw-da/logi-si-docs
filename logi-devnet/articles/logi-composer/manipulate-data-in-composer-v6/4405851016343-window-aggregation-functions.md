---
title: "Window Aggregation Functions"
id: 4405851016343
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851016343-Window-Aggregation-Functions
updated_at: 2021-09-21T01:28:07Z
---

# Window Aggregation Functions

# Window Aggregation Functions

Window aggregation functions are a middle case between [column](https://devnet.logianalytics.com/hc/en-us/articles/4405859301911-Column-Aggregation-Functions) and [table](https://devnet.logianalytics.com/hc/en-us/articles/4405859303319-Table-Aggregation-Functions) aggregation functions. They provide a snapshot or window into a subset of data, depending on the groupings used by the visual. Each window function such as `WindowSUM` or `WindowAVG` requires a numeric field to aggregate followed by a list of one or more attributes. The function aggregates the data and groups the results based on these attributes *if the attributes are present in the visual*. Attributes absent from the visual are ignored from the aggregation.

Derived fields can be used in window aggregation functions.

For example, an aggregation `WindowAVG( profits, gender, city )` returns the average profits in the data, grouped by gender and city *if gender and city are represented in the visual*. If gender happens to be absent from the visual, then it is dropped from the aggregation. Effectively, the average profits would then be grouped only by city.

The following table describes the supported window aggregation functions.

| Function | Type | Description |
| --- | --- | --- |
| ``` WindowAVG(<field>,<attr1>[,<attr2>]...) ``` | numeric | Returns the average of a column (field), grouped by the specified attributes. |
| ``` WindowCOUNT(<field>,<attr1>[,<attr2>]... ) ``` | any | Returns the numeric count of values in a column (field), grouped by the specified attributes.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wild card character (\*) for `<field>` to include null values for the field in the count. |
| ``` WindowCOUNTD(<field>,<attr1>[,<attr2>]...) ``` | any | Returns the numeric count of unique values in a column (field), grouped by the specified attributes.  This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wild card character (\*) for `<field>` to include null values for the field in the count. |
| ``` WindowMAX(<field>,<attr1>[,<attr2>]...) ``` | numeric | Returns the maximum value of a column (field), grouped by the specified attributes. |
| ``` WindowMIN(<field>,<attr1>[,<attr2>]...) ``` | numeric | Returns the minimum value of a column (field), grouped by the specified attributes. |
| ``` WindowSUM(<field>,<attr1>[,<attr2>]...) ``` | numeric | Returns the sum of a column (field), grouped by the specified attributes. |

### Example

Suppose you have the following fields and data:

| name | gender | city | earned | spent |
| --- | --- | --- | --- | --- |
| Alan | M | Rockville | $10 | $2 |
| Bob | M | Rockville | $8 | $3 |
| Carol | F | Rockville | $5 | $5 |
| Darlene | F | Reston | $4 | $6 |
| Ed | M | Reston | $2 | $8 |

To create a custom metric containing a group's contribution to just gender, rather than to the whole, use the following formula.

```
SUM(earned)/WindowSUM(earned,gender) * 100
```

Using this custom metric in a pivot table with the example data set shown above produces results similar to the ones shown below.

| City | Gender | Volume | % of Each Gender's Earnings |
| --- | --- | --- | --- |
| Reston | F | 1 | 44.44 |
| M | 1 | 10 |
| Rockville | F | 1 | 55.56 |
| M | 2 | 90 |
| Total |  | 5 | 100 |

In this pivot table, each city's total earnings (`SUM(earned)`) is shown as a percentage of each gender's total earnings. If gender had been absent from the visual, the cities' total earnings would have been shown as totals of the whole, rather than of each gender.
