---
title: "Applying the Compare Filter"
id: 4406817185943
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817185943-Applying-the-Compare-Filter
updated_at: 2022-04-06T06:04:30Z
---

# Applying the Compare Filter

# Applying the Compare Filter

The following example illustrates how the **Compare Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575830807/compfilter_01.png)

1. As shown above, a **Compare Filter** element is added as a child to a datalayer element.
2. Its **Compare Type** attribute is set to define the comparison operator.
3. Its **Data Column** attribute value is set to the column in that datalayer whose value will be compared.
4. Finally, the **Compare Value** attribute is set to the value the data column values will be compared against.

Using the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the Compare Filter **removes** all rows that don't match the criteria (CategoryID column value is greater than 4). All that remains in the datalayer for use in the report are rows whose CategoryID values are greater than 4.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) To compare against Null values, leave the **Compare Value** attribute *blank*.

## Comparison Operator Options

The **Compare Type** attribute value provides a number of operators in a pull-down list.

The provided operators include:

| Attribute | Description |
| --- | --- |
| =, <, >, <=, >=, < > | Basic standard comparison operations. String types evaluated are culture-sensitive. |
| Between | The Compare Value attribute must include two comma- or pipe character-separated values. Datalayer rows with values in the specified Data Column that are equal to, or within the range, are retained. See examples below for usage. |
| Contains | Datalayer rows with values in the specified Data Column that contain the Compare Value string value are retained. |
| ContainsAll | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, all values from both arrays must be the same, in any order. |
| ContainsAllInOrder | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, all values from both arrays must be the same, and in the same order. |
| ContainsAny | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, just one values from either array must be the same. |
| ContainsNone | Compares two comma-delimited arrays, one in the specified Data Column, the other in the Compare Value attribute. For the row to be retained, none of the values from the Compare Value attribute can be present in the specified Data Column. |
| EndsWith | For the row to be retained, the value in the specified Data Column mustend with the Compare Value. |
| FuzzyMatch | Performs a "fuzzy" string match. For the row to be retained, the value in the specified Data Column must "closely" match that in the Compare Value. |
| InDay | For the row to be retained, the date value in the specified Data Column must be within the same day as the Compare Value. |
| InList | For the row to be retained, the value in the specified Data Column *must* be one of the values specified in a comma-separated list in the Compare Value. |
| InWeek | For the row to be retained, the date value in the specified Data Column must be within the same week as the Compare Value. |
| InMonth | For the row to be retained, the date value in the specified Data Column must be within the same month as the Compare Value. |
| InQuarter | For the row to be retained, the date value in the specified Data Column must be within the same quarter as the Compare Value. |
| InYear | For the row to be retained, the date value in the specified Data Column must be within the same year as the Compare Value. |
| IsDateTime | For the row to be retained, the specified Data Column must contain a valid date/time value. |
| IsDecimal | For the row to be retained, the specified Data Column must contain a valid decimal value. |
| IsEven | For the row to be retained, the specified Data Column must contain an even number. |
| IsInteger | For the row to be retained, the specified Data Column must contain a valid integer value. |
| IsNotDateTime | For the row to be retained, the specified Data Column must *not* contain a valid date/time value. |
| IsNotDecimal | For the row to be retained, the specified Data Column must *not* contain a valid decimal value. |
| IsNotInteger | For the row to be retained, the specified Data Column must *not* contain a valid integer value. |
| IsOdd | For the row to be retained, the specified Data Column must contain an odd number. |
| LengthEquals | For the row to be retained, the length of the specified Data Column value must equal the Compare Value. |
| LengthGreaterThan | For the row to be retained, the length of the specified Data Column value must be greater than the Compare Value. |
| LengthGreaterThanOrEqualTo | For the row to be retained, the length of the specified Data Column value must be equal to or greater than the Compare Value. |
| LengthLessThan | For the row to be retained, the length of the specified Data Column value must be less than the Compare Value. |
| LengthLessThanOrEqualTo | For the row to be retained, the length of the specified Data Column value must be less than or equal to the Compare Value. |
| LengthNotEqualTo | For the row to be retained, the length of the specified Data Column value must *not* equal the Compare Value. |
| Like | For the row to be retained, the Data Column Value must match the Compare Value. |
| NotBetween | The Compare Value attribute must include two comma-separated values. Datalayer rows with values in the specified Data Column that are *outside* the range, are retained. |
| NotContains | Datalayer rows with values in the specified Data Column that *do not* contain the Compare Value string value are retained. |
| NotEndsWith | For the row to be retained, the value in the specified Data Column must *not* end with the Compare Value. |
| NotFuzzyMatch | Performs a "fuzzy" string match. For the row to be retained, the value in the specified Data Column must *not* "closely" match that in the Compare Value. |
| NotInList | For the row to be retained, the value in the specified Data Column must *not* be one of the values specified in a comma-separated list in the Compare Value. |
| NotLike | For the row to be retained, the Data Column Value must *not* match the Compare Value. |
| NotRegEx | For the row to be retained, the value in the specified Data Column must *not* match the Regular Expression in the Compare Value. |
| NotStartsWith | For the row to be retained, the value in the specified Data Column must *not* start with the Compare Value. |
| RegEx | For the row to be retained, the value in the specified Data Column must match the Regular Expression in the Compare Value. |
| StartsWith | For the row to be retained, the value in the specified Data Column must start with the Compare Value. |

You may also type in your own operators, such as *!=* (not equal).
