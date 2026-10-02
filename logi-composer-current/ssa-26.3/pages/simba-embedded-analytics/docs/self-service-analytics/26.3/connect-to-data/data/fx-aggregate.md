> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Aggregation Functions

Use aggregate functions in [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics). Custom metrics can also include the use of [row-level functions](#supported-row-level-functions), conditional CASE expressions, statistical functions, an expansive list of arithmetic functions, as well as FIRST and LAST values. In addition, they can be [filtered](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#apply-filters-to-custom-metrics) (using [date and time filter functions](#date-and-time-filter-aggregation-functions) and [SQL-like expressions](#supported-sql-like-expressions)).

Data can be aggregated using column, table, or window aggregation functions. Each is explained in the links below. Aggregation functionality is explained in the links below.

* [Conditional CASE Expressions](#conditional-case-expressions)
* [Supported Statistical Functions](#supported-statistical-functions)
* [Arithmetic Functions](#arithmetic-functions)
* [Column Aggregation Functions](#column-aggregation-functions)
* [Table Aggregation Functions](#table-aggregation-functions)
* [Window Aggregation Functions](#window-aggregation-functions)
* [Date and Time Filter Aggregation Functions](#date-and-time-filter-aggregation-functions)
* [Metric Aggregation Functions](#metric-aggregation-functions)

<h2 id="column-aggregation-functions">
  Column Aggregation Functions
</h2>

Column aggregation functions aggregate data using all the data displayed on a visual. They group results in the same way that the visual itself groups its data. For example, if your visual shows data grouped by gender (male and female), then column aggregation functions return two results, one for males and one for females. Only data included in the visual by any filters that have been applied are included in the results.

The following table describes the supported column aggregation functions.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th>Parameter Type</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`AVG(<field>)`</td>
      <td>numeric</td>
      <td>Returns the average of a column (field), grouped in the same manner as the visual data.</td>
    </tr>

    <tr>
      <td>`COUNT(<field>)`</td>
      <td>any</td>

      <td>
        Returns the numeric count of values in a column (field), grouped in the same manner as the visual data.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.

        <br />

        Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`COUNTD(<field>)`</td>
      <td>any</td>

      <td>
        Returns the numeric count of unique values in a column (field), grouped in the same manner as the visual data.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.

        <br />

        Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`MAX(<field>)`</td>
      <td>numeric</td>
      <td>Returns the maximum value of a column (field), grouped in the same manner as the visual data.</td>
    </tr>

    <tr>
      <td>`MIN(<field>)`</td>
      <td>numeric</td>
      <td>Returns the minimum value of a column (field), grouped in the same manner as the visual data.</td>
    </tr>

    <tr>
      <td>`SUM(<field>)`</td>
      <td>numeric</td>
      <td>Returns the sum of a column (field), grouped in the same manner as the visual data.</td>
    </tr>

    <tr>
      <td>`FIRST_VALUE(<field>)`</td>
      <td>any</td>
      <td>Returns the first value of a given expression in the group, as when the expression is sorted in the ascending order.</td>
    </tr>

    <tr>
      <td>`LAST_VALUE(<field>)`</td>
      <td>any</td>
      <td>Returns the last value of a given expression in the group, as when the expression is sorted in the ascending order.</td>
    </tr>

    <tr>
      <td>`STDDEV_POP(<field>)`</td>
      <td>numeric</td>
      <td>Computes the population standard deviation and returns the square root of the population variance.</td>
    </tr>

    <tr>
      <td>`STDDEV_SAMP(<field>)`</td>
      <td>numeric</td>
      <td>Computes the cumulative sample standard deviation and returns the square root of the sample variance.</td>
    </tr>

    <tr>
      <td>`VAR_POP(<field>)`</td>
      <td>numeric</td>
      <td>Returns the population standard variance of a given expression.</td>
    </tr>

    <tr>
      <td>`VAR_SAMP(<field>)`</td>
      <td>numeric</td>
      <td>Returns the sample variance of a given expression.</td>
    </tr>

    <tr>
      <td>`MEDIAN(<field>)`</td>
      <td>numeric</td>
      <td>Computes the median value across the group.</td>
    </tr>
  </tbody>
</table>

<h4 id="column-aggregation-functions-example">
  Example
</h4>

Suppose you have the following fields and data in a data source:

| name | gender | city | earned | spent |
| - | - | - | - | - |
| Alan | M | Rockville | \$10 | \$2 |
| Bob | M | Rockville | \$8 | \$3 |
| Carol | F | Rockville | \$5 | \$5 |
| Darlene | F | Reston | \$4 | \$6 |
| Ed | M | Reston | \$2 | \$8 |

To use this data set to create a custom metric called `Leftover` (a group's leftover money), use the following formula.

```
SUM( earned ) - SUM( spent )
```

If you used the `Leftover` custom metric in a visual grouping by gender using the data above, you would get the results shown below.

| Gender | Leftover |
| - | - |
| F | -2 |
| M | 7 |
| Total | 5 |

Males have \$7, derived from (10+8+2) - (2+3+8). Females have -\$2 left over, derived from (5+4) - (5+6). If you used the same custom metric in a visual grouping by city, you would see Rockville having \$13, from (10+8+5) - (2+3+5), and Reston having -\$8, from (4+2) - (6+8).

<h2 id="date-and-time-filter-aggregation-functions">
  Date and Time Filter Aggregation Functions
</h2>

To filter a custom metric using dates or times, you must already have a time attribute configured in your data source. The following date and time functions can only be used after WHERE in your custom metric.

Date field options use common time formats such as YTD, MMDDYYYY, and YoY.

The following date and time filter aggregation functions are supported.

<table>
  <thead>
    <tr>
      <th colSpan={2} scope="col">Supported Date and Time Functions</th>
    </tr>

    <tr>
      <th scope="col">Function</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`DATE()`</td>
      <td>**Deprecated.** Use `NOW()` instead.</td>
    </tr>

    <tr>
      <td>`DateADD('<time_period>',<interval>,'<date>')`</td>

      <td>
        **Deprecated.** Use `TIME_ADD` instead.

        <br />

        For example, consider this `DateADD` specification:

        <br />

        ```
        DateADD('YEAR', 1, '2021-01-01')
        ```

        <br />

        Use this `TIME_ADD` specification instead:

        <br />

        ```
        TIME_ADD('YEAR', 1, '2021-01-01')
        ```

        <br />

        In a second example, consider this `DateADD` specification:

        <br />

        ```
        DateADD('MONTH', 1, DATE())
        ```

        <br />

        Use this `TIME_ADD` specification instead:

        <br />

        ```
        TIME_ADD('YEAR', 1, NOW())
        ```
      </td>
    </tr>

    <tr>
      <td>`DateSUB('<time_period>',<interval>,'<date>')`</td>

      <td>
        **Deprecated.** Use `TIME_ADD` instead, specifying a negative number for `interval`.

        <br />

        For example, consider this `DateADD` specification:

        <br />

        ```
        DateSUB('YEAR', 1, '2021-01-01')
        ```

        <br />

        Use this `TIME_ADD` specification instead:

        <br />

        ```
        TIME_ADD('YEAR', -1, '2021-01-01'
        ```

        <br />

        TIME\_ADD supports negative `interval` numbers for subtraction.
      </td>
    </tr>

    <tr>
      <td>`NOW()`</td>

      <td>
        Obtains the current date and time for the derived field. `NOW()` functionality is available when you use a supported connector.

        <br />

        Set the `calculations.rle.now.function` property in the `query-engine.properties` file to `true` and [restart the query engine microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

        <br />

        See [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties).
      </td>
    </tr>

    <tr>
      <td>`PreviousPeriod(<offset>,<numPeriods>)`</td>

      <td>
        This function is supported only within a TRANSFORM clause used for [filtering the custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#apply-filters-to-custom-metrics).

        <br />

        The period returned is of the same length as the currently represented period, but not immediately prior to it. Instead, it counts back in `<numPeriods>` periods of time, measured in units named by `<offset>`.

        <br />

        The following time `<offset>` values are supported: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`.

        <br />

        See [PreviousPeriod Function](#previousperiod-function).
      </td>
    </tr>

    <tr>
      <td>`TIME()`</td>
      <td>**Deprecated.** Use `NOW()` instead.</td>
    </tr>

    <tr>
      <td>`TIME_ADD('<time-period>',<interval>, <date-time-field>)`</td>

      <td>
        Adds an interval value to the `<timepart>` of the date-time field:

        <br />

        In the following example, 7 is added to the hour in the field called `date_time_field`:

        <br />

        ```
        TIME_ADD ('HOUR', +7, date_time_field)
        ```
      </td>
    </tr>
  </tbody>
</table>

### Date Filter Functions

Specific parameters are needed for the `DateADD` and `DateSub` functions. The following table describes them.

<table>
  <thead>
    <tr>
      <th scope="col">Parameter</th>
      <th scope="col">Value</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`time_period`</td>
      <td>Supported time periods (with corresponding interval range): `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`</td>
    </tr>

    <tr>
      <td>`interval`</td>
      <td>Whole number integer. Negative numbers are supported for subtraction.</td>
    </tr>

    <tr>
      <td>`date`</td>

      <td>
        * Current day operator: date()

        <br />

        * Standard date and time formats supported include:

        <br />

        * `yyyy-MM-dd HH:mm:ss`
        * `MM/dd/yy hh:mm aa`
        * `yyyy`

        <br />

        For all supported formats, see [Convert Attributes to Time Fields in Data Source Field Specifications](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#convert-attributes-to-time-fields-in-data-source-field).
      </td>
    </tr>
  </tbody>
</table>

<h3 id="previousperiod-function">
  PreviousPeriod Function
</h3>

The `PreviousPeriod` function is used for comparing data values between different time periods. This function can be used when you need to compare one time period to another of equivalent size for variance custom metrics. For example, comparing results from the current month to the previous month or the current week to the same week one year ago.

<Note>
  Note that this function only works when the date field used in the formula is selected on the time bar.
</Note>

To use this function, the `TRANSFORM` [SQL-like expression](#supported-sql-like-expressions) must be used in the custom metric to convert the date range for a specified time attribute. For example:

```
SUM(Sales) TRANSFORM saledate = PreviousPeriod('month',1)
```

If the `saledate` time period is March 2015, the custom metric returns `SUM(Sales)` where the `saledate` is February 2015.

<Note>
  If the data is grouped by the same field for which a `PreviousPeriod` transformation is performed and it is grouped by days but transformed by units of months, quarters, or years, null values are returned when the previous period does not have matching days for the current period. For example, if the current period is the month of March and `PreviousPeriod('month',1)` is used for the transformation, null values are produced for February 29-31, 2015 because those days are not valid days (although they are valid days for March 2015). Self-Service Analytics attempts to preserve the day-of-month correspondence between the two periods.
</Note>

Specific parameters must be specified in `PreviousPeriod` functions. The following table describes them.

| Parameter | Value |
| - | - |
| `offset` | The time granularity for the previous period (includes `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`). |
| `numPeriods` | The argument specifying the number of periods to go back in time. |

<h2 id="table-aggregation-functions">
  Table Aggregation Functions
</h2>

Table aggregation functions are broader in scope than column aggregation functions. Table aggregation functions use all data from a field and produce a single, ungrouped value. You typically do not use the result directly in a visual, since it is ungrouped.

For example, if you have sales records grouped by gender, a `TableSUM` custom metric returns the total sales of all records as one value, regardless of the group in consideration. The `TableSUM` result would include both the male and female data values. Consequently, males and females would appear to have the same sales if the `TableSUM` result was included in the visual.

Table aggregation functions are typically used to calculate percentages of a whole or average values.

The following table describes the supported table aggregation functions.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`TableAVG(<field>)`</td>
      <td>numeric</td>
      <td>Returns the average of a column (field), regardless of how the visual is grouped.</td>
    </tr>

    <tr>
      <td>`TableCOUNT(<field>)`</td>
      <td>any</td>

      <td>
        Returns the numeric count of values in a column (field), regardless of how the visual is grouped.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`TableCOUNTD(<field>)`</td>
      <td>any</td>

      <td>
        Returns the numeric count of unique values in a column (field), regardless of how the visual is grouped.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data. Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`TableMAX(<field>)`</td>
      <td>numeric</td>
      <td>Returns the maximum value of a column (field), regardless of how the visual is grouped.</td>
    </tr>

    <tr>
      <td>`TableMIN(<field>)`</td>
      <td>numeric</td>
      <td>TableMIN returns the minimum value of a column (field), regardless of how the visual is grouped.</td>
    </tr>

    <tr>
      <td>`TableSUM(<field>)`</td>
      <td>numeric</td>
      <td>TableSUM returns the sum of a column (field), regardless of how the visual is grouped.</td>
    </tr>
  </tbody>
</table>

<h4 id="table-aggregation-functions-example">
  Example
</h4>

Suppose you have the following fields and data:

| name | gender | city | earned | spent |
| - | - | - | - | - |
| Alan | M | Rockville | \$10 | \$2 |
| Bob | M | Rockville | \$8 | \$3 |
| Carol | F | Rockville | \$5 | \$5 |
| Darlene | F | Reston | \$4 | \$6 |
| Ed | M | Reston | \$2 | \$8 |

Using this data, you can create a custom metric containing individual earnings as a percentage of total earnings with the following formula:

```
SUM(earned) / TableSUM(earned) * 100
```

in which:

* `SUM(earned)` calculates the sum earnings for each individual.
* `TableSUM(earned)` calculates the total earnings of all records in the data.
* The quotient of `SUM(earned) / TableSUM(earned)` is multiplied by 100 to convert the result into a percentage.

Shown on a table using the example data above, the results would look like this:

| Name | % of Whole |
| - | - |
| Alan | 34.48 |
| Bob | 27.59 |
| Carol | 17.24 |
| Darlene | 13.79 |
| Ed | 6.90 |
| Total | 100 |

<h2 id="window-aggregation-functions">
  Window Aggregation Functions
</h2>

Window aggregation functions are a middle case between [column](#column-aggregation-functions) and [table](#table-aggregation-functions) aggregation functions. They provide a snapshot or window into a subset of data, depending on the groupings used by the visual. Each window function such as `WindowSUM` or `WindowAVG` requires a numeric field to aggregate followed by a list of one or more attributes. The function aggregates the data and groups the results based on these attributes *if the attributes are present in the visual*. Attributes absent from the visual are ignored from the aggregation.

Derived fields can be used in window aggregation functions.

For example, an aggregation `WindowAVG( profits, gender, city )` returns the average profits in the data, grouped by gender and city *if gender and city are represented in the visual*. If gender happens to be absent from the visual, then it is dropped from the aggregation. Effectively, the average profits would then be grouped only by city.

The following table describes the supported window aggregation functions.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`WindowAVG(<field>,<attr1>[,<attr2>]...)`</td>
      <td>numeric</td>
      <td>Returns the average of a column (field), grouped by the specified attributes.</td>
    </tr>

    <tr>
      <td>`WindowCOUNT(<field>,<attr1>[,<attr2>]... )`</td>
      <td>any</td>

      <td>
        Returns the numeric count of values in a column (field), grouped by the specified attributes.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.

        <br />

        Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`WindowCOUNTD(<field>,<attr1>[,<attr2>]...)`</td>
      <td>any</td>

      <td>
        Returns the numeric count of unique values in a column (field), grouped by the specified attributes.

        <br />

        This aggregate function normally ignores null values for the specified field. Consequently, the result of this aggregate function may not be the same as the actual number of records in the data.

        <br />

        Use the wildcard character (\*) for `<field>` to include null values for the field in the count.
      </td>
    </tr>

    <tr>
      <td>`WindowMAX(<field>,<attr1>[,<attr2>]...)`</td>
      <td>numeric</td>
      <td>Returns the maximum value of a column (field), grouped by the specified attributes.</td>
    </tr>

    <tr>
      <td>`WindowMIN(<field>,<attr1>[,<attr2>]...)`</td>
      <td>numeric</td>
      <td>Returns the minimum value of a column (field), grouped by the specified attributes.</td>
    </tr>

    <tr>
      <td>`WindowSUM(<field>,<attr1>[,<attr2>]...)`</td>
      <td>numeric</td>
      <td>Returns the sum of a column (field), grouped by the specified attributes.</td>
    </tr>
  </tbody>
</table>

<h4 id="window-aggregation-functions-example">
  Example
</h4>

Suppose you have the following fields and data:

| name | gender | city | earned | spent |
| - | - | - | - | - |
| Alan | M | Rockville | \$10 | \$2 |
| Bob | M | Rockville | \$8 | \$3 |
| Carol | F | Rockville | \$5 | \$5 |
| Darlene | F | Reston | \$4 | \$6 |
| Ed | M | Reston | \$2 | \$8 |

To create a custom metric containing a group's contribution to just gender, rather than to the whole, use the following formula.

```
SUM(earned)/WindowSUM(earned,gender) * 100
```

Using this custom metric in a pivot table with the example data set shown above produces results similar to the ones shown below.

<table>
  <thead>
    <tr>
      <th>City</th>
      <th>Gender</th>
      <th>Volume</th>
      <th>% of Each Gender's Earnings</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td rowSpan={2}>Reston</td>
      <td>F</td>
      <td>1</td>
      <td>44.44</td>
    </tr>

    <tr>
      <td>M</td>
      <td>1</td>
      <td>10</td>
    </tr>

    <tr>
      <td rowSpan={2}>Rockville</td>
      <td>F</td>
      <td>1</td>
      <td>55.56</td>
    </tr>

    <tr>
      <td>M</td>
      <td>2</td>
      <td>90</td>
    </tr>

    <tr>
      <td>Total</td>

      <td />

      <td>5</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

In this pivot table, each city's total earnings (`SUM(earned)`) is shown as a percentage of each gender's total earnings. If gender had been absent from the visual, the cities' total earnings would have been shown as totals of the whole, rather than of each gender.

<h2 id="arithmetic-functions">
  Arithmetic Functions
</h2>

Custom metrics support the following arithmetic functions in your aggregate functions.

The following table describes the supported arithmetic functions.

| Function | Type | Description |
| - | - | - |
| `POWER(numeric1, numeric2)` | numeric | Returns numeric1 raised to the power of numeric2. |
| `MOD(numeric1, numeric2)` | numeric | Returns the remainder (modulus) of numeric1 divided by numeric2. The result is negative only if numeric1 is negative. |
| `SQRT(numeric)` | numeric | Returns the square root of numeric. |
| `LN(numeric)` | numeric | Returns the natural logarithm (base e) of numeric. |
| `LOG10(numeric)` | numeric | Returns the base 10 logarithm of numeric. |
| `EXP(numeric)` | numeric | Returns e raised to the power of numeric. |
| `CEIL(numeric)` | numeric | Rounds numeric up, returning the smallest integer that is greater than or equal to numeric. |
| `FLOOR(numeric)` | numeric | Rounds numeric down, returning the largest integer that is less than or equal to numeric. |
| `ROUND(numeric1, numeric2)` | numeric | Rounds numeric1 to optionally numeric2 (if not specified 0) places right to the decimal point. |
| `RAND(seed)` | numeric | Generates a random double between 0 and 1 inclusive, optionally initializing the random number generator with *seed*. |
| `SIGN(numeric)` | numeric | Returns the signum of *numeric*. |
| `SIN(numeric)` | numeric | Returns the sine of numeric. |
| `COS(numeric)` | numeric | Returns the cosine of numeric. |
| `TAN(numeric)` | numeric | Returns the tangent of numeric. |
| `COT(numeric)` | numeric | Returns the cotangent of numeric. |
| `ASIN(numeric)` | numeric | Returns the arcsine of numeric. |
| `ACOS(numeric)` | numeric | Returns the arc cosine of numeric. |
| `ATAN(numeric)` | numeric | Returns the arctangent of numeric. |
| `PI()` | numeric | Returns a value that is closer than any other value to pi. |
| `DEGREES(numeric)` | numeric | Converts numeric from radians to degrees. |
| `RADIANS(numeric) >` | numeric | Converts numeric from degrees to radians. |

<h2 id="conditional-case-expressions">
  Conditional CASE Expressions
</h2>

You can include the use of CASE expressions (singular or nested) in your custom metrics, much as you would row-level case and SQL case expressions. These capabilities include:

Conditions in `when` :

* Condition must be an aggregate-level expression.
* Can compare both metrics and groups. Group values, or any other non-numeric values can be used through `FIRST_VALUE` / `LAST_VALUE` functions.
* Use existing metrics from the request or add new metrics.
* Row-level expressions can be used inside aggregation functions.
* Use `AND` / `OR` operators to build complex conditions.
* `where` and `transform` clauses can be used in conditions to modify aggregate expressions.

To return results in `then`that include custom metric expressions, including calculated sub-queries.

* Must be an aggregate-level expression.
* All result values must be of the same type.
* Can be a numeric or non-numeric value.
* `where` and `transform` clauses can be used in conditions to modify aggregate expressions.

Additionally, you can nest case functions if needed, both for conditions and results. If you use case expressions as part of an arithmetic expression, it must be enclosed in parentheses.

<Note>
  Only one result branch is returned from the expression, but all branches will be evaluated simultaneously, regardless of which condition is met first.
</Note>

<h2 id="supported-statistical-functions">
  Supported Statistical Functions
</h2>

| Type | Parameter Type | Description |
| - | - | - |
| `STDDEV_POP` | numeric | Computes the population standard deviation and returns the square root of the population variance. |
| `STDDEV_SAMP` | numeric | Computes the cumulative sample standard deviation and returns the square root of the sample variance. |
| `VAR_POP` | numeric | Returns the population standard variance of a given expression. |
| `VAR_SAMP` | numeric | Returns the sample variance of a given expression. |
| `MEDIAN` | numeric | Computes the median value across the group. |

<h2 id="supported-row-level-functions">
  Supported Row-Level Functions
</h2>

Use row-level functions in the row-level expressions you use to create the following calculation types:

* [derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields)
* [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics)
* [admin-defined functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov)

The row-level functions described in this section are fully supported by all three types. For information about the aggregate functions and SQL-like expressions you can use in custom metrics, see Supported Aggregation Functions and [Supported SQL-Like Expressions](#supported-sql-like-expressions).

Row-level functions are divided into the following categories:

* [Arithmetic Functions](#arithmetic-functions-2)
* [Conditional Functions](#conditional-functions)
* [Logical Functions](#logical-functions)
* [Numerical Functions](#numerical-functions)
* [Relational Functions](#relational-functions)
* [Text Functions](#text-functions)
* [Time Functions](#time-functions)

<h2 id="arithmetic-functions-2">
  Arithmetic Functions
</h2>

| Operator | Description |
| - | - |
| - (SUBTRACT) | Subtracts one numeric value from another |
| \* (MULTIPLY) | Multiply one number by another |
| / (DIVIDE) | Divide one number by another |
| + (ADD) | Addition: adds two numbers |

<h2 id="conditional-functions">
  Conditional Functions
</h2>

<table>
  <thead>
    <tr>
      <th>Operator</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>CASE</td>
      <td>Use the CASE function is the same manner as standard SQL CASE functions. CASE can be used to list a series of conditions and return an appropriate value for the first condition that is met.</td>
    </tr>

    <tr>
      <td>COALESCE</td>

      <td>
        Use the COALESCE function in the same manner as standard SQL COALESCE functions. COALESCE can be used to return the first non-null value in a list of values.

        <br />

        The COALESCE function also supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned.
      </td>
    </tr>
  </tbody>
</table>

<h2 id="logical-functions">
  Logical Functions
</h2>

| Operator | Description |
| - | - |
| AND | Evaluates to TRUE if both boolean expressions are TRUE. |
| BETWEEN | Evaluates to TRUE if the operand is within a range. |
| IN | Evaluates to TRUE if the operand is equal to one of a list of expressions. |
| NOT | Reverses the value of any other Boolean operator. |
| OR | Evaluates to TRUE if either boolean expression is TRUE. |

<h2 id="numerical-functions">
  Numerical Functions
</h2>

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>CEIL</td>
      <td>Returns the smallest integer value that is not less than the passed Value</td>

      <td>
        CEIL(value : Numeric) : Numeric

        <br />

        `CEIL(Field_A)`
      </td>
    </tr>

    <tr>
      <td>FLOOR</td>
      <td>Returns the largest integer value that is not greater than the passed value</td>

      <td>
        FLOOR(value : Numeric) : Numeric

        <br />

        `FLOOR(Field_A)`
      </td>
    </tr>

    <tr>
      <td>NUM\_TO\_TEXT</td>
      <td>Converts the numeric expression to text</td>

      <td>
        NUM\_TO\_TEXT(value : Numeric)

        <br />

        `NUM_TO_TEXT(Field_A)`
      </td>
    </tr>

    <tr>
      <td>ROUND</td>
      <td>Rounds a numeric value to the number of decimals specified</td>
      <td>ROUND(Field\_A, 0)</td>
    </tr>

    <tr>
      <td>UNIX\_TIME\_TO\_TIME</td>
      <td>Converts the numeric expression to time</td>
      <td>UNIX\_TIME\_TO\_TIME(Field\_Milliseconds /1000)</td>
    </tr>
  </tbody>
</table>

<h2 id="relational-functions">
  Relational Functions
</h2>

| Operator | Description |
| - | - |
| != | Checks whether the values of two operands are not equal. If the values are not equal, then the condition is true. |
| \< | Checks whether the value of the left operand is less than the value of the right operand. If it is, then the condition is true. |
| \<= | Checks whether the value of the left operand is less than or equal to the value of the right operand. If it is, then the condition is true. |
| = | Checks whether the values of two operands are equal. If the values are equal, then the condition is true. |
| > | Checks whether the value of the left operand is greater than the value of the right operand. If it is, then the condition is true. |
| >= | Checks whether the value of the left operand is greater than or equal to the value of right operand. If it is, then condition is true. |

You can also combine less than (\<) and greater than (>) functions using logical AND processing in the same statement. For example, the following are valid statements:

```
saledate > 2020-10-28 AND saledate < 2020-10-30
saledate > 2020-10-28 AND saledate < 2020-10-30 AND state = 'CA'
```

In each of these examples, the individual relational functions must all be true for the full statement to be true. In the second example, the sale date must be greater than October 28, 2020 and less than October 30, 2020 and the sale must take place in the state of California.

<h2 id="text-functions">
  Text Functions
</h2>

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>CONCAT</td>
      <td>Returns a text that is the result of concatenating two or more text values.</td>
      <td>`CONCAT(Field_FirstName, ' ,', Field_LastName)`</td>
    </tr>

    <tr>
      <td>LENGTH</td>
      <td>Returns the number of characters of the specified string.</td>
      <td>`LENGTH(SUBSTRING('$12456.00', 2, 10))`</td>
    </tr>

    <tr>
      <td>LOCATE</td>
      <td>Finds the first occurrence of substring in a string, starting at position.</td>
      <td>`LOCATE('Mr.', CONCAT(Field_FirstName, ' ,', Field_LastName), 0)`</td>
    </tr>

    <tr>
      <td>LOWER</td>
      <td>Returns the argument in lowercase.</td>
      <td>`LOWER(SUBSTRING(Field_A, 0, 3 ))`</td>
    </tr>

    <tr>
      <td>LPAD</td>
      <td>Returns the text argument, left-padded with the text specified by *padString* to a length of Length characters.</td>
      <td>`LPAD(SUBSTRING(Field_A, 0, 15), 3, 'abc')`</td>
    </tr>

    <tr>
      <td>LTRIM</td>
      <td>Returns a text value after removing leading blanks.</td>
      <td>`LTRIM(SUBSTRING(Field_A, 0, 5))`</td>
    </tr>

    <tr>
      <td>RPAD</td>
      <td>Returns the Text argument, right-padded with the text specified by *padString* to a length of Length characters.</td>
      <td>`RPAD(SUBSTRING(Field_A, 0, 15), 3, 'abc')`</td>
    </tr>

    <tr>
      <td>RTRIM</td>
      <td>Returns a text value after removing trailing blanks.</td>
      <td>`RTRIM(SUBSTRING(Field_A, 0, 5))`</td>
    </tr>

    <tr>
      <td>SUBSTRING</td>
      <td>Returns the substring of String value which begins at position defined by Start and is Length characters long.</td>
      <td>`SUBSTRING(Field_A, 4, 3)`</td>
    </tr>

    <tr>
      <td>TEXT\_TO\_NUM</td>
      <td>Converts the text string to numeric.</td>
      <td>`TEXT_TO_NUM(LTRIM(Field_A))`</td>
    </tr>

    <tr>
      <td>TEXT\_TO\_TIME</td>

      <td>
        Converts the text expression to time according to the specified format.

        <br />

        This function requires input in the form of an attribute or string field containing data that could be parsed as a time field and the format for the time field.

        <br />

        Valid formats must be enclosed in single quotation marks and can only use the following syntax elements: `YYYY` (for years), `MM` (for months), `DD` (for days), `HH24` (for hours), `MI` (for minutes), `SS` (for seconds), and `MS` (for milliseconds).

        <br />

        Separators in the syntax that are allowed are `-` (dashes), `:` (colons), `.` (periods), `/` (backslashes), and spaces.
      </td>

      <td>`TEXT_TO_TIME(Field_A,'YYYY-MM-DD HH24:MI:SS')`</td>
    </tr>

    <tr>
      <td>UPPER</td>
      <td>Returns the argument in uppercase.</td>
      <td>`UPPER(SUBSTRING(Field_A, 0, 3))`</td>
    </tr>
  </tbody>
</table>

<h2 id="time-functions">
  Time Functions
</h2>

The following time functions are supported. Valid values for `<timepart>` vary, based on the Self-Service Analytics connector selected, but can include YEAR, QUARTER, MONTH, WEEK, WEEK\_OF\_YEAR, WEEK\_OF\_MONTH, DAY, DAY\_OF\_YEAR, DAY\_OF\_MONTH, DAY\_OF\_WEEK, HOUR, MINUTE, SECOND, or MILLISECOND. Review the documentation for the Self-Service Analytics connector for any deviations from this list. Note that the WEEK\_OF\_YEAR function calculates the week from January 1, not from the week containing January 1.

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>EXTRACT</td>

      <td>
        Extracts the `<timepart>` of the `<datetime>` field:

        <br />

        ```
        extract(<timepart>,<datetime>)
        ```
      </td>
    </tr>

    <tr>
      <td>NOW</td>

      <td>
        Obtains the current date and time for the derived field. `NOW()` functionality is available when you use a supported connector. Set the `calculations.rle.now.function` property in the `query-engine.properties` file to `true` and [restart the query engine microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices). See [Query Engine Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#query-engine-properties).

        <br />

        ```
        CASE WHEN [date column] = ''
        NOW()
        ELSE [date column]
        END
        ```
      </td>
    </tr>

    <tr>
      <td>TIME\_ADD</td>

      <td>
        Adds an interval value to the `<timepart>` of the `<datetime>` field:

        <br />

        ```
        time_add(<timepart>, <interval>, <datetime>)
        ```

        <br />

        In the following example, 7 is added to the hour in the field called `date_time_field`:

        <br />

        ```
        TIME_ADD (hour, +7, date_time_field)
        ```
      </td>
    </tr>

    <tr>
      <td>TIME\_DIFF</td>

      <td>
        Returns the time difference between two time fields in the unit you request:

        <br />

        ```
        time_diff('<timepart>', <end_date_field>, <start_date_field>)
        ```

        <br />

        In the following example, the difference between the values of the ENDDATE and STARTDATE fields is returned in days:

        <br />

        ```
        time_diff('DAY', ENDDATE, STARTDATE)
        ```
      </td>
    </tr>

    <tr>
      <td>TIME\_TO\_UNIX\_TIME</td>

      <td>
        Returns the value of a `<datetime>` field as a Unix time stamp:

        <br />

        ```
        time_to_unix_time(<datetime>)
        ```
      </td>
    </tr>

    <tr>
      <td>TRUNCATE\_TIME</td>

      <td>
        Rounds (Truncates) the `<datetime>` field value down to the granularity specified by `<timepart>`:

        <br />

        ```
        truncate_time(<timepart>,<datetime>)
        ```
      </td>
    </tr>
  </tbody>
</table>

<h2 id="metric-aggregation-functions">
  Metric Aggregation Functions
</h2>

provides a set of metric functions that are used to group (aggregate) data. The following aggregation methods can be selected for metrics in your visuals. See also [Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#metrics).

<table>
  <thead>
    <tr>
      <th>Aggregation Function</th>
      <th>What Is Returned</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>AVG</td>
      <td>The average of the data values for the field. This function is available only for numeric fields.</td>
    </tr>

    <tr>
      <td>DISTINCT COUNT</td>
      <td>The total number of unique values for the field. This function is available only for attribute and numeric fields.</td>
    </tr>

    <tr>
      <td>COUNT</td>
      <td>The total number of values for the field. This function is available only for attribute and numeric fields.</td>
    </tr>

    <tr>
      <td>MIN</td>
      <td>The lowest value in all the data values for the field. This function is available only for numeric fields.</td>
    </tr>

    <tr>
      <td>MAX</td>
      <td>The highest value in all the data values for the field. This function is available only for numeric fields.</td>
    </tr>

    <tr>
      <td>SUM</td>
      <td>The total of all the data values for the field. This function is available only for numeric fields.</td>
    </tr>

    <tr>
      <td>LAST VALUE</td>
      <td>The last value in all the data values for the field, sorted by the time attribute selected for the time bar. If the latest date and time for the time attribute is exactly the same in multiple records, the last value for the field is the maximum value of the field in the records with the latest date and time. See [LAST VALUE Examples](#last-value-examples). This function is available only for numeric fields.</td>
    </tr>

    <tr>
      <td>NO AGGREGATION</td>
      <td>No Aggregation is available if you group and sort by the same field. When you use No Aggregation, you can select the sort Order of as Alphabetical (A-Z) or Reverse Alphabetical (Z-A).</td>
    </tr>

    <tr>
      <td>LISTAGG</td>

      <td>
        Use to transform row-level data into a string of consolidated data, comma-separated data, or other custom-delimited string. For example, use `Listagg(fieldname, 'delimiter')` to concatenate the fields values, separated by the defined delimiter.

        <br />

        Pushdown is supported for multiple connectors:

        <br />

        BigQuery, Impala, MySQL, MemSQL, Oracle, PostgreSQL, Redshift, Snowflake, and SparkSQL.
      </td>
    </tr>
  </tbody>
</table>

Suppose you have the following raw data:

| Name | Gender | Age |
| - | - | - |
| Johnny | Male | 10 |
| Adam | Male | 12 |
| Mina | Female | 11 |
| Jenny | Female | 13 |
| Ann | Female | 15 |

When this data is aggregated by gender, only two records (one for males and one for females) are returned and the aggregation must somehow determine what value to return for the age of the different genders. To do this, the aggregation requires input (using a metric function) about how the age should be returned. For example, if you elected to aggregate the data by gender and return the average age using the AVG metric function, the resulting data would be:

| Gender | Age Returned | Aggregation Calculation | Aggregation Logic |
| - | - | - | - |
| Male | 11 | 10 + 12 = 22 /2 = 11 | Johnny's and Adam's ages are summed and divided by 2 (two males). |
| Female | 13 | 11 + 13 + 15 = 39 /3 = 13 | Mina's, Jenny's, and Ann's ages are summed and divided by 3 (three females). |

If you elected to aggregate the data by gender and return the minimum age using the MIN metric function, the resulting data would be:

| Gender | Age Returned | Aggregation Logic |
| - | - | - |
| Male | 10 | Johnny's and Adam's ages are evaluated and the lower of the two ages is returned. |
| Female | 11 | Mina's, Jenny's, and Ann's ages are evaluated and the lower of the three ages is returned. |

<h3 id="last-value-examples">
  LAST VALUE Examples
</h3>

The LAST VALUE examples in this section use the following data:

| Record # | Gender | Country | Price | Items | Sale\_Date |
| - | - | - | - | - | - |
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

<h4 id="examples-grouping-by-one-field">
  Examples: Grouping By One Field
</h4>

Suppose you aggregate this data by Gender and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Gender | Price Returned | Aggregation Logic |
| - | - | - |
| Male | 60 | In all the records for males, two records have the latest date (2019-01-03) - records #1 and #6. Therefore, the prices in both records are compared and the maximum price is returned. The result is 60 from record #6. |
| Female | 71 | In all the records for females, two records have the latest date (2019-01-04) - records #7 and #14. Therefore, the prices in both records are compared and the maximum price is returned. The result is 71 from record #14. |

Suppose you aggregate this data by Country and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Country | Price Returned | Aggregation Logic |
| - | - | - |
| US | 1 | In all the records for the US, the record with the latest date is for the female with a sale date of 2019-01-04 (record #7). The price in that record is 1. |
| UK | 41 | All the records for the UK are for 2019-01-01. Therefore, the prices in all records are compared and the maximum price is returned. The result is 41 from record #11. |
| UA | 71 | In all the records for the UA, the record with the latest date is for a female with a sale date of 2019-01-04 (record #14). The price in that record is 71. |

<h4 id="example-grouping-by-two-fields">
  Example: Grouping By Two Fields
</h4>

Suppose you aggregate this data by Gender and then by Country and request that the last value for Price be returned based on the Sale\_Date. The results would be:

| Gender | Country | Price Returned | Aggregation Logic |
| - | - | - | - |
| Male | US | 10 | The two records for US males are compared and the latest record has a sale date of 2019-01-03 (record #1). The price in that record is 10. |
| Male | UK | 40 | The two records for UK males have the same sale dates (2019-01-01). Therefore, the prices in all UK male records are compared and the maximum price is returned. The result is 40 from record #4. |
| Male | UA | 60 | The two records for UA males are compared and the latest record has a sale date of 2019-01-03 (record #6). The price in that record is 60. |
| Female | US | 1 | The three records for US females are compared and the latest record has a sale date of 2019-01-04 (record #1). The price in that record is 1. |
| Female | UK | 41 | The two records for UK females have the same sale dates (2019-01-01). Therefore, the prices in all UK female records are compared and the maximum price is returned. The result is 41 from record #11. |
| Female | UA | 71 | The three records for UA females are compared and the latest record has a sale date of 2019-01-03 (record #1). The price in that record is 10. |

<h4 id="example-grouping-by-two-last-value-metrics">
  Example: Grouping By Two LAST VALUE Metrics
</h4>

Suppose you aggregate this data by Gender and request that the last value for Price and the last value for Items be returned based on the Sale\_Date. The results would be:

| Gender | Price Returned | Items Returned | Aggregation Logic |
| - | - | - | - |
| Male | 60 | 6 | In all the records for males, two records have the latest date (2019-01-03) - records #1 and #6. The prices and item counts in both records are compared and the maximum price and item count are returned. The returned results are a price of 60 from record #6 and 6 items from record #1. |
| Female | 71 | 7 | In all the records for females, two records have the latest date (2019-01-04) - records #7 and #14. The prices and item counts in both records are compared and the maximum price and item count are returned. The returned results are a price of 71 from record #14 and 7 items from record #7. |

<h2 id="supported-sql-like-expressions">
  Supported SQL-Like Expressions
</h2>

Self-Service Analytics's custom metrics support the following SQL-like expressions:

<table>
  <thead>
    <tr>
      <th>Expression</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>WHERE</td>

      <td>
        Use WHERE to filter by a condition. Data will only be included in the custom metric if the condition that follows is true. For example:

        <br />

        ```
        COUNT(weatherdelay) WHERE airportcode IN ('LAX', 'ORD', 'IAD')
        ```

        <br />

        Row-level functions and expressions can be used in WHERE clauses in custom metrics. In a custom metric, WHERE clauses allow you to specify a formula without first creating a derived field. The WHERE clause must be in the leftmost part of the custom metric expression, but it can be expressed with a row-level function or any of the aggregate functions available for custom metrics. In the following example, the total planned sales is calculated for men.

        <br />

        ```
        SUM(plannedsales) WHERE UPPER(gender) = 'MALE'
        ```
      </td>
    </tr>

    <tr>
      <td>AND</td>

      <td>
        Use AND to form a conjunctive condition. Data is only included in the custom metric if it meets both of the conditions connected by AND. The following example calculates the sum of `deicing` only if the `broadphaseofflight` includes LANDING and the `airportcode` is YYZ.

        <br />

        ```
        SUM(deicing) WHERE broadphaseofflight IN 'LANDING' AND airportcode='YYZ'
        ```
      </td>
    </tr>

    <tr>
      <td>OR</td>

      <td>
        Use OR to for a disjunctive condition. Data is included in the custom metric if it meets either of the conditions connected by OR. The following example calculates the sum of `deicing` if the `broadphaseofflight` includes LANDING or the `airportcode` is YYZ.

        <br />

        ```
        SUM(deicing) WHERE broadphaseofflight IN 'LANDING' OR airportcode='YYZ'
        ```
      </td>
    </tr>

    <tr>
      <td>BETWEEN...AND</td>

      <td>
        Use BETWEEN to filter using a range of values. The following example counts the number of distinct records for `weatherdelay` that have `cancelledflight` counts between 2 and 10.

        <br />

        ```
        COUNTD(weatherdelay) WHERE cancelledflight BETWEEN 2 AND 10
        ```
      </td>
    </tr>

    <tr>
      <td>IN</td>

      <td>
        Use IN to filter using a set of values. Data is included in the custom metric only if a data field matches one of the listed values. The following example calculates the sum of `weatherdelay` only for records in which the `airportcode` field is LAX, ORD, or IAD.

        <br />

        ```
        SUM(weatherdelay) WHERE airportcode IN ('LAX','ORD','IAD')
        ```
      </td>
    </tr>

    <tr>
      <td>NOT IN</td>

      <td>
        Use NOT IN to filter using a set of values. Data is included in the aggregation only if a data field does not match one of the listed values. The following example calculates the sum of `weatherdelay` only for records in which the `airportcode` field is *not* LAX, ORD, or IAD.

        <br />

        ```
        SUM(weatherdelay) WHERE airportcode NOT IN ('LAX','ORD','IAD')
        ```
      </td>
    </tr>

    <tr>
      <td>TRANSFORM</td>

      <td>
        Use TRANSFORM to filter based on a derived date. To derive a date with TRANSFORM, you must already have a time attribute configured in your data source.

        <br />

        The following example calculates the sum of `weatherdelay` only for records in which the `eventdate` is for the previous period. In other words, if the visual is examining two weeks of data for `weatherdelay`, this calculation will provide data about the two weeks prior to that.

        <br />

        ```
        SUM(weatherdelay) TRANSFORM eventdate=PreviousPeriod()
        ```

        <br />

        To work correctly, data must be available for the periods of time considered.
      </td>
    </tr>
  </tbody>
</table>

<h2 id="row-level-expressions">
  Row-Level Expressions
</h2>

A row-level expression is a mathematical expression involving a single record (row) in the data. They are used to calculate [derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) but can also be used in [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics) and [admin-defined functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov).

Row-level expressions are created using attributes and metrics from the data and [row-level functions](#supported-row-level-functions).

<Note>
  Be careful not to create row-level expressions using fields in a data source that have had their field data type changed. Doing so may generate errors for the row-level expression. Instead, use the original field (with its original field type) to create a derived field of the field type you need and then use the new derived field in your row-level expressions.
</Note>

<h2 id="operators">
  Operators
</h2>

Valid operators used in Self-Service Analytics are described below.

| Operator | Applies to | Determines whether the data in the field you select... |
| - | - | - |
| Begins With | strings | Begins with the string you have specified. |
| Between | numbers | Falls numerically between the two numbers you specified. |
| Contains | strings | Contains the string you have specified. |
| Does Not Begin With | strings | Does **not** begin with the string you have specified. |
| Does Not Contain | strings | Does *not* contain the string you have specified. |
| Does Not End With | strings | Does **not** end with the string you have specified. |
| Ends With | strings | Ends with the string you have specified. |
| Equal | numbers | Is equal to the number you specified. |
| Exclude | numbers & strings | Includes the number or string you specify. If it does, the data is excluded from the output. |
| Greater Than | numbers | Is greater than the number you specified. |
| Greater Than or Equal | numbers | Is greater than or equal to the number you specified. |
| Include | numbers & strings | Includes the number or string you specify. If it does, the data is included in the output. |
| Less Than | numbers | Is less than the number you specified. |
| Less Than or Equal | numbers | Is less than or equal to the number you specified. |
| Not Between | numbers | Does **not** fall numerically between the two numbers you specified. |
| Not Equal | numbers | Is **not** equal to the number you specified. |

<h2 id="distinct-counts">
  Distinct Counts
</h2>

Distinct count functionality determines the number of unique values in a column or expression within a selected table by comparing all the records pulled from the data store by a data source configuration. When distinct counts are used, unique value results are returned when analyzing data. For example, distinct counts could return the number of:

* Unique customers in a sales database
* Unique UPC codes for a category of products
* The number of trucks in a company's fleet

For example, given a single collection and string field with the following three values:

1. Apple
2. Orange
3. Apple

The distinct count returns 2, since there are only two distinct values (“Apple” and “Orange”), while an ordinary count returns 3 to reflect the total number of records. SQL-based connectors might produce a query that looks like this:

```
select count(distinct myField) from myCollection
```

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>
      <td>Cloudera Impala connectors can receive only a single distinct count field in a query.</td>
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>
