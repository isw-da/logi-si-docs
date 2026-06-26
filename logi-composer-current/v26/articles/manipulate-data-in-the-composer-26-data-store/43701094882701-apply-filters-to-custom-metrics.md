---
title: "Apply Filters to Custom Metrics"
id: 43701094882701
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701094882701-Apply-Filters-to-Custom-Metrics
updated_at: 2026-05-29T14:08:12Z
---

# Apply Filters to Custom Metrics

# Apply Filters to Custom Metrics

You can apply filters to your custom metrics. This means that attributes from the data can be applied as filter parameters to further refine and narrow your results. Specifying a filter lets you perform a calculation within a predefined range, for example, determining sales results within a certain period of time or within a certain demographic.

This topic covers the application of filters to custom metrics and provides instructions covering the operators and syntax for integrating a filter into your custom metrics.

## Filter Syntax

To create a custom metric that includes filters, operators or expressions are required.

When integrating a filter within a custom metric, keep in mind that Composer supports certain operators and follows a logical structure. In general, creating a filtered custom metric entails selecting the appropriate function variable, integrating the desired attribute or metric, using the appropriate filter operators and Date function, and entering a date in the correct format. Composer custom metrics use one of the following general structures:

<agg-function> WHERE <field> <operator> <values>
<agg-function> TRANSFORM <field> PreviousPeriod([offset,numPeriods])

where:

* `<agg-function>` is any of the aggregate functions described in [Supported Aggregation Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701096111373-Supported-Aggregation-Functions).
* WHERE or TRANSFORM is the appropriate [SQL-like expression](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116252685-Supported-SQL-Like-Expressions) used for custom metric filtering. TRANSFORM is used specifically with the `PreviousPeriod`[date and time filter aggregation function](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701083818509-Date-and-Time-Filter-Aggregation-Functions). WHERE and TRANSFORM filters are always applied to the broadest possible expression. For example, the following two expressions are both valid, but the first applies the filters to both SUMs, while the second expression applies the filter only to `SUM(Sales)`.

  SUM(Profit)/SUM(Sales) WHERE zipcode IN (90210,94107,92101)

  SUM(Profit)/(SUM(Sales) WHERE zipcode IN (90210,94107,92101))

  WHERE clauses can include row-level functions and expressions.
* `<field>` is a field (metric or attribute) in the data.
* `<operator>` is one of the operators shown in the following table:

  | Filters | | |
  | --- | --- | --- |
  | Capability | Operators | Notes |
  | Filtering on attribute options | NULL check: IS NULL, IS NOT NULL  Single value: =, !=, STARTS WITH, ENDS WITH, CONTAINS  Multiple values: IN(), NOT IN() | + Non-numeric fields such as Name, Address and State can be used as a filter. + References to an attribute in a field must be enclosed in single quotation marks. For example:  SUM(Sales) WHERE State = ‘Florida’ + Values specified for STARTS WITH, ENDS WITH, and CONTAINS are case-sensitive. The following example would show sales for states that include the lowercase letters `ia`, such as California and Louisiana (and others):  SUM(Sales) WHERE State CONTAINS 'ia' |
  | Filtering on date field options | Date range operator: BETWEEN | + Standard date formats (see [Convert Attributes to Time Fields in Data Source Field Specifications](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078376461-Convert-Attributes-to-Time-Fields-in-Data-Source-Field-Specifications)) are supported (such as 'yyyy-mm-dd', 'dd/mm/yyyy' including 'hh-mm-ss')   . + Date (‘01-01-2015’) must be enclosed in single quotation marks. + Supported time periods are YEAR, MONTH, WEEK, or DAY |
  | Filtering on numeric fields and custom metric options | >, <, =, != | + References to a numeric field must be enclosed in single quotation marks + References can be made to other custom metrics (using the custom metric label) |
* `<value>` is an appropriate value, based on the requirements of the [SQL-like expression](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116252685-Supported-SQL-Like-Expressions). Values can be specific numbers or dates, or one of the [date and time filter aggregation functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701083818509-Date-and-Time-Filter-Aggregation-Functions).

## Examples

The following table provides examples of filtered custom metrics.



| Filtered Custom Metric Examples | |
| --- | --- |
| Capability | Example |
| Filtering on Attribute options | SUM(Sales) WHERE State = ‘California’  SUM(Profit)/SUM(Sales) WHERE zipcode IN (90210,94107,92101) |
| Filtering on Date field options | MIN(Margin) WHERE Sale\_Date BETWEEN ‘2013-01-01’ AND DateADD(MONTH, 6, ‘01-01-2014’)) |
| Filtering on numeric fields and custom metric options | SUM(Sales)/(SUM(Sales) WHERE User\_Income = ‘0 to $25000’)  To calculate year over year growth:  ((SUM(price) WHERE sale\_date BETWEEN '2014-01-01' AND '2015-01-01') - (SUM(price) WHERE sale\_date BETWEEN '2013-01-01' AND '2014-01-01')) / (SUM(price) WHERE sale\_date BETWEEN '2012-01-01' AND '2013-01-01') \* 100 |
| Comparing the difference between the current period to last period | Compare this period's deliveries to last period's deliveries:  SUM(deliveries) TRANSFORM delivery\_date = PreviousPeriod() |
| Using a row-level expression or function in a filter | SUM(plannedsales) WHERE maxage - age > 30 SUM(plannedsales) WHERE UPPER(gender) = 'MALE' |
