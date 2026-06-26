---
title: "The Compare Filter"
id: 1500009529901
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009529901-The-Compare-Filter
updated_at: 2021-06-17T01:58:05Z
---

# The Compare Filter

# The Compare Filter

The **Compare Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer. This topic discusses use of this element.

* About the Compare Filter
* [Applying the Compare Filter](#Applying)
* [Using Multiple and Dynamic Compare Filters](#Dynamic)
* [Use with a Condition Filter](#Condition)

*This element is not available in Logi Report.*

## About the Compare Filter

The Compare Filter element, introduced in v10.1.18, is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically compares a specified data column value against a specified literal or tokenized value and removes all rows from the datalayer where the comparison returns *False*. A variety of comparisons, such as *Equal*, *Greater Than*, *Less Than*, etc., are supported.

This element is quite similar to [The Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009514302-The-Condition-Filter) element, however, it may provide *better performance* because it's implemented as a native part of the Logi Data Engine and so does not need to execute script like the Condition Filter.

## Apply the Compare Filter

The following example illustrates how the **Compare Filter** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890711/compfilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890967/compfilter_01a.png)

1. As shown above, a **Compare Filter** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be compared.
3. The **Compare Type** attribute is set to define the comparison operator.
4. Finally, the **Compare Value** attribute is set to the value the data column values will be compared against.

Using the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the Compare Filter **removes** all rows that don't match the criteria (CategoryID column value is greater than 4). All that remains in the datalayer for use in the report are rows whose CategoryID values are greater than 4.

## Comparison Operator Options

The Compare Type attribute value provides a number of operators in a pull-down list. The provided operators include:

| Operator | Description |
| --- | --- |
| =, <, >, <=, >=, < > | Basic standard comparison operations. String types evaluated are culture-sensitive. |
| Between | The Compare Value attribute must include two comma-separated values. Datalayer rows with values in the specified Data Column that are equal to, or within the range, are retained. |
| Contains | Datalayer rows with values in the specified Data Column that contain the Compare Value string value are retained. |
| ContainsAll | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, all values from both arrays must be the same, in any order. |
| ContainsAllInOrder | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, all values from both arrays must be the same, and in the same order. |
| ContainsAny | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, just one values from either array must be the same. |
| ContainsNone | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, none of the values from the Compare Value attribute can be present in the specified Data Column. |
| EndsWith | For the row to be retained, the value in the specified Data Column must end with the Compare Value. |
| FuzzyMatch | Performs a "fuzzy" string match. For the row to be retained, the value in the specified Data Column must "closely" match that in the Compare Value. |
| IsDateTime | For the row to be retained, the specified Data Column must contain a valid date/time value. |
| IsDecimal | For the row to be retained, the specified Data Column must contain a valid decimal value. |
| IsEven | For the row to be retained, the specified Data Column must contain an even number. |
| IsInteger | For the row to be retained, the specified Data Column must contain a valid integer value. |
| IsNotDateTime | For the row to be retained, the specified Data Column must *not* contain a valid date/time value. |
| IsNotDecimal | For the row to be retained, the specified Data Column must *not* contain a valid decimal value. |
| IsNotInteger | For the row to be retained, the specified Data Column must *not* contain a valid integer value. |
| IsOdd | For the row to be retained, the specified Data Column must contain an odd number. |
| LengthEquals | For the row to be retained, the length of the specified Data Column value must equal the Compare Value. |
| LengthGreaterThan | For the row to be retained, the length of the specified Data Column value must be greater than the Compare Value. |
| LengthGreaterThanOrEqualTo | For the row to be retained, the length of the specified Data Column value must be equal to or greater than the Compare Value. |
| LengthLessThan | For the row to be retained, the length of the specified Data Column value must be less than the Compare Value. |
| LengthLessThanOrEqualTo | For the row to be retained, the length of the specified Data Column value must be less than or equal to the Compare Value. |
| LengthNotEqualTo | For the row to be retained, the length of the specified Data Column value must *not* equal the Compare Value. |
| NotBetween | The Compare Value attribute must include two comma-separated values. Datalayer rows with values in the specified Data Column that are *outside* the range, are retained. |
| NotContains | Datalayer rows with values in the specified Data Column that *do not* contain the Compare Value string value are retained. |
| NotEndsWith | For the row to be retained, the value in the specified Data Column must *not* end with the Compare Value. |
| NotFuzzyMatch | Performs a "fuzzy" string match. For the row to be retained, the value in the specified Data Column must *not* "closely" match that in the Compare Value. |
| NotRegEx | For the row to be retained, the value in the specified Data Column must *not* match the Regular Expression in the Compare Value. |
| NotStartsWith | For the row to be retained, the value in the specified Data Column must *not* start with the Compare Value. |
| RegEx | For the row to be retained, the value in the specified Data Column must match the Regular Expression in the Compare Value. |
| StartsWith | For the row to be retained, the value in the specified Data Column must start with the Compare Value. |

You may also type in your own operators, such as *!=* (not equal).

## Use Multiple and Dynamic Compare Filters

1. Developers can use two or more **consecutive** Compare Filter elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778719255/compfilter_02.png)

In this case, the comparisons will be evaluated **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Compare Filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated for the second Compare Filter.

2. Developers can make Compare Filter elements **dynamic** by using tokens:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890711/compfilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771891223/compfilter_03.png)

As shown above, Compare Value attribute can contain tokens such as @Request, so that comparison values are dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

3. The Compare Filter element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771890711/compfilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771891607/compfilter_04.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.

## Use with a Condition Filter

Beginning with v11.0.127, Compare Filters can also be used with the Condition Filters to create complex expressions that include ANDs and ORs and levels of parentheses. For more information on Condition Filters, see [The Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009514302-The-Condition-Filter).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778719511/compfilter_05.png)

For example, consider the element arrangement shown above. For each row of the datalayer, the three **Compare Filters** will be evaluated first. Each of them will produce a *True* or *False* value as a result of their comparison operations. Those values will be assigned to @Compare tokens which include the element ID, for example: @Compare.CompareFilter1~. The scope of these tokens is
limited to the parent Condition Filter.

After all of the Compare Filters are evaluated, the **Condition Filter** will be evaluated and its **Condition** attribute value can include expressions that use the @Compare tokens. For example, the Condition attribute value above might be:

@Compare.CompareFilter1~ AND (@Compare.CompareFilter2~ OR @Compare.CompareFilter3~)

And, of course, you can also use other types of tokens and literal values in the Condition attribute to get the expression you need, such as:

@Data.UnitPrice~ <= 100 AND (@Compare.CompareFilter1~ OR @Compare.CompareFilter2~)

You may be able achieve the same results with complicated scripting for the Condition attribute value, however, in most cases use of multiple Compare Filters as shown in this example will produce better performance than scripting.
