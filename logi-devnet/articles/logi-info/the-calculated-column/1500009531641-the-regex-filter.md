---
title: "The RegEx Filter"
id: 1500009531641
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531641-The-RegEx-Filter
updated_at: 2021-06-17T01:58:34Z
---

# The RegEx Filter

# The RegEx Filter

The **RegEx Filter** element is used with datalayer elements to filter out data rows. It works by applying pattern matching using regular expressions, providing developers with a great deal of flexibility in making the comparison. This topic discusses use of this element.

* About the RegEx Filter
* [Applying the RegEx Filter](#sec1)
* [Using Multiple and Dynamic RegEx Filters](#sec2)

*This element is not available in Logi Report.*

## About the RegEx Filter

"RegEx" is an abbreviation of "regular expression", which provides a concise and flexible method for "matching" (specifying and recognizing) text strings, including particular characters, words, and/or patterns of characters.

The **RegEx Filter** element, introduced in v10.1.18, is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically attempts to match a specified data column value against a specified regular expression pattern and it removes all rows from the datalayer where there is no match (the match result is *False*).

The RegEx Filter's pattern matching can be very useful for finding and removing "bad" data; that is, data that's malformed or incomplete. Consider this example regular expression: ^3[47][0-9]{13}$ which was written to validate data that's supposed to be American Express credit card numbers. The expression indicates that each number should start with either 34 or 37 and has to have 15 digits.

For developers who may not be familiar with regular expressions, the following two external sites provide useful information:

<http://www.regular-expressions.info/examples.html>

<http://www.zytrax.com/tech/web/regex.htm#simple>

The RegEx Filter element is similar to [The Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009514302-The-Condition-Filter) element, however, it may provide *better performance* because it's implemented as a native part of the Logi Data Engine and so does not need to execute script like the Condition Filter.

## Applying the RegEx Filter

The following example illustrates how the **RegEx Filter** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771635607/RegExFilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778529047/regexfilter_01a.png)

1. As shown above, a **RegEx Filter** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be examined.
3. The **Regular Expression** attribute is set to define the desired regular expression code.

Using the example above, the sequence of events is that the datalayer reads in all the data from the datasource, then the RegEx Filter **removes** all rows whose Freight column values don't match the regular expression pattern (unlimited digits before the decimal point, two digits after it, and no dollar signs, commas, text, or symbols). All that remains in the datalayer for use in the report are rows whose Freight values match the pattern.

#### Using Multiple and Dynamic RegEx Filters

1. Developers can use two or more **consecutive** RegEx Filter elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771635863/regexfilter_02.png)

In this case, the matches will be evaluated **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first RegEx Filter is applied, only records that match its pattern will remain in the datalayer to be matched to the second RegEx Filter.

2. The RegEx Filter element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771636119/regexfilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778529303/regexfilter_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
