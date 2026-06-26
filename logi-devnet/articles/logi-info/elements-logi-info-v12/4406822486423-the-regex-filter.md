---
title: "The RegEx Filter"
id: 4406822486423
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822486423-The-RegEx-Filter
updated_at: 2022-04-06T06:08:22Z
---

# The RegEx Filter

# The RegEx Filter

The **RegEx Filter** element is used with datalayer elements to filter out data rows. It works by applying pattern matching using regular expressions, providing developers with a great deal of flexibility in making the comparison.

The following topics discuss the RegEx Filter:

* [Applying the RegEx Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406817808791-Applying-the-RegEx-Filter#sec1)
* [Using Multiple and Dynamic RegEx Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406822487319-Using-Multiple-and-Dynamic-RegEx-Filters#sec2)

## About the RegEx Filter

"RegEx" is an abbreviation of "regular expression", which provides a concise and flexible method for "matching" (specifying and recognizing) text strings, including particular characters, words, and/or patterns of characters.

The **RegEx Filter** element is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities,such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically attempts to match a specified data column value against a specified regular expression pattern and it removes all rows from the datalayer where there is no match (the match result is *False*).

The RegEx Filter's pattern matching can be very useful for finding and removing "bad" data; that is, data that's malformed or incomplete. Consider this example regular expression: ^3[47][0-9]{13}$ which was written to validate data that's supposed to be American Express credit card numbers. The expression indicates that each number should start with either 34 or 37 and has to have 15 digits.

For developers who may not be familiar with regular expressions, the following external site provides useful information:

<http://www.regular-expressions.info/examples.html>

The RegEx Filter element is similar to the [The Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406822191255-The-Condition-Filter) element, however, it frequently provides *better performance* because it's implemented as a native part of the Logi Data Engine and so does not need to execute script, as the Condition Filter does.
