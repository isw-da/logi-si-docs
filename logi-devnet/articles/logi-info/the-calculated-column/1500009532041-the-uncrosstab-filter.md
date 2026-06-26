---
title: "The UnCrosstab Filter"
id: 1500009532041
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532041-The-UnCrosstab-Filter
updated_at: 2021-06-17T01:58:40Z
---

# The UnCrosstab Filter

# The UnCrosstab Filter

The **UnCrosstab Filter** element is used with datalayer elements to "un-pivot" or "reverse pivot" rows of data into columns of data. It converts one row of multi-column data into multiple rows, each with a single data
value. This topic discusses use of this element.

* About the UnCrosstab Filter
* [Apply the UnCrosstab Filter](#sec1)
* [Use Dynamic UnCrosstab Filters](#sec2)

*This element is not available in Logi Report.*

## About the UnCrosstab Filter

The **UnCrosstab Filter** element, introduced in v10.1.18, is available for use with all datalayer elements and is the functional opposite of the Crosstab Filter element.

In operation, the element basically converts each row in the datalayer, each of which has multiple columns, into multiple rows, each of which has one value column. 

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771598743/uncrosstab_01.png)

It's a little easier to understand the filter's actions when you can see the effect limited to one row, in a data table, as shown above.

This "un-pivot" action normalizes the data on the fly and, among other applications, can be really useful when having to work with data imported from spreadsheets.

## Apply the UnCrosstab Filter

The following example illustrates how the **UnCrosstab Filter** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771598999/uncrosstab_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778500119/uncrosstab_02a.png)

1. As shown above, an **UnCrosstab Filter** element is added as a child beneath a datalayer element.
2. Its **Column Heading ID** attribute value is set to the column used to provide the original pivoted column headings.
3. The **Value Column ID** attribute is set to name of a new column that will receive the data values.
4. The optional **Label Columns** attribute identifies one or more columns, in a comma-separated list, that are not pivoted.
5. The optional **Remove Columns** attribute identifies one or more columns, in a comma-separated list, that should not be included in the output.

In the complete example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the UnCrosstab Filter builds a substitute datalayer by examining each row in the source datalayer and adding rows to the substitute datalayer for each value column found.

## Use Dynamic UnCrosstab Filters

The UnCrosstab Filter element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771598999/uncrosstab_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778500375/uncrosstab_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be altered or not.
