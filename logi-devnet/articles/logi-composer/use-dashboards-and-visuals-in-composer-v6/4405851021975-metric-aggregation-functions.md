---
title: "Metric Aggregation Functions"
id: 4405851021975
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851021975-Metric-Aggregation-Functions
updated_at: 2021-09-21T01:28:12Z
---

# Metric Aggregation Functions

# Metric Aggregation Functions

Composer provides a set of metric functions that are used to group (aggregate) data. The following aggregation methods can be selected for metrics in your visuals. See also [*Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics).

| Aggregation Function | What Is Returned |
| --- | --- |
| AVG | The average of the data values for the field. This function is available only for numeric fields. |
| DISTINCT COUNT | The total number of unique values for the field. This function is available only for attribute fields. |
| MIN | The lowest value in all the data values for the field. This function is available only for numeric fields. |
| MAX | The highest value in all the data values for the field. This function is available only for numeric fields. |
| SUM | The total of all the data values for the field. This function is available only for numeric fields. |
| LAST VALUE | The last value in all the data values for the field, sorted by the time attribute selected for the time bar. If the latest date and time for the time attribute is exactly the same in multiple records, the last value for the field is the maximum value of the field in the records with the latest date and time. See [*LAST VALUE Examples*](#LAST). This function is available only for numeric fields. |

Suppose you have the following raw data:

| Name | Gender | Age |
| --- | --- | --- |
| Johnny | Male | 10 |
| Adam | Male | 12 |
| Sarah | Female | 11 |
| Jenny | Female | 13 |
| Ann | Female | 15 |

When this data is aggregated by gender, only two records (one for males and one for females) are returned and the aggregation must somehow determine what value to return for the age of the different genders. To do this, the aggregation requires input (using a metric function) about how the age should be returned. For example, if you elected to aggregate the data by gender and return the average age using the AVG metric function, the resulting data would be:

| Gender | Age Returned | Aggregation Calculation | Aggregation Logic |
| --- | --- | --- | --- |
| Male | 11 | 10 + 12 = 22 /2 = 11 | Johnny's and Adam's ages are summed and divided by 2 (two males). |
| Female | 13 | 11 + 13 + 15 = 39 /3 = 13 | Sarah's, Jenny's, and Ann's ages are summed and divided by 3 (three females). |

If you elected to aggregate the data by gender and return the minimum age using the MIN metric function, the resulting data would be:

| Gender | Age Returned | Aggregation Logic |
| --- | --- | --- |
| Male | 10 | Johnny's and Adam's ages are evaluated and the lower of the two ages is returned. |
| Female | 11 | Sarah's, Jenny's, and Ann's ages are evaluated and the lower of the three ages is returned. |

## LAST VALUE Examples

The LAST VALUE examples in this section use the following data:

| Record # | Gender | Country | Price | Items | Sale\_Date |
| --- | --- | --- | --- | --- | --- |
| 1 | Male | US | 10 | 6 | 2019-01-03 |
| 2 | Male | US | 20 | 5 | 2019-01-02 |
| 3 | Male | UK | 30 | 4 | 2019-01-01 |
| 4 | Male | UK | 40 | 3 | 2019-01-01 |
| 5 | Male | UA | 50 | 2 | 2019-01-02 |
| 6 | Male | UA | 60 | 1 | 2019-01-03 |
| 7 | Female | US | 1 | 7 | 2019-01-04 |
| 8 | Female | US | 11 | 6 | 2019-01-03 |
| 9 | Female | US | 21 | 5 | 2019-01-02 |
| 10 | Female | UK | 31 | 4 | 2019-01-01 |
| 11 | Female | UK | 41 | 3 | 2019-01-01 |
| 12 | Female | UA | 51 | 2 | 2019-01-02 |
| 13 | Female | UA | 61 | 1 | 2019-01-03 |
| 14 | Female | UA | 71 | 0 | 2019-01-04 |

### Examples: Grouping By One Field

Suppose you aggregate this data by Gender and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Gender | Price Returned | Aggregation Logic |
| --- | --- | --- |
| Male | 60 | In all the records for males, two records have the latest date (2019-01-03) - records #1 and #6. Therefore, the prices in both records are compared and the maximum price is returned. The result is 60 from record #6. |
| Female | 71 | In all the records for females, two records have the latest date (2019-01-04) - records #7 and #14. Therefore, the prices in both records are compared and the maximum price is returned. The result is 71 from record #14. |

Suppose you aggregate this data by Country and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Country | Price Returned | Aggregation Logic |
| --- | --- | --- |
| US | 1 | In all the records for the US, the record with the latest date is for the female with a sale date of 2019-01-04 (record #7). The price in that record is 1. |
| UK | 41 | All the records for the UK are for 2019-01-01. Therefore, the prices in all records are compared and the maximum price is returned. The result is 41 from record #11. |
| UA | 71 | In all the records for the UA, the record with the latest date is for a female with a sale date of 2019-01-04 (record #14). The price in that record is 71. |

### Example: Grouping By Two Fields

Suppose you aggregate this data by Gender and then by Country and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Gender | Country | Price Returned | Aggregation Logic |
| --- | --- | --- | --- |
| Male | US | 10 | The two records for US males are compared and the latest record has a sale date of 2019-01-03 (record #1). The price in that record is 10. |
| Male | UK | 40 | The two records for UK males have the same sale dates (2019-01-01). Therefore, the prices in all UK male records are compared and the maximum price is returned. The result is 40 from record #4. |
| Male | UA | 60 | The two records for UA males are compared and the latest record has a sale date of 2019-01-03 (record #6). The price in that record is 60. |
| Female | US | 1 | The three records for US females are compared and the latest record has a sale date of 2019-01-04 (record #1). The price in that record is 1. |
| Female | UK | 41 | The two records for UK females have the same sale dates (2019-01-01). Therefore, the prices in all UK female records are compared and the maximum price is returned. The result is 41 from record #11. |
| Female | UA | 71 | The three records for UA females are compared and the latest record has a sale date of 2019-01-03 (record #1). The price in that record is 10. |

### Example: Grouping By Two LAST VALUE Metrics

Suppose you aggregate this data by Gender and request that the last value for Price and the last value for Items be returned based on the Sale\_Date. The results would be:

| Gender | Price Returned | Items Returned | Aggregation Logic |
| --- | --- | --- | --- |
| Male | 60 | 6 | In all the records for males, two records have the latest date (2019-01-03) - records #1 and #6. The prices and item counts in both records are compared and the maximum price and item count are returned. The returned results are a price of 60 from record #6 and 6 items from record #1. |
| Female | 71 | 7 | In all the records for females, two records have the latest date (2019-01-04) - records #7 and #14. The prices and item counts in both records are compared and the maximum price and item count are returned. The returned results are a price of 71 from record #14 and 7 items from record #7. |
