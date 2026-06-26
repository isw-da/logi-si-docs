---
title: "Positive and Negative Number Formatting"
id: 4419722931223
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722931223-Positive-and-Negative-Number-Formatting
updated_at: 2022-07-17T01:48:26Z
---

# Positive and Negative Number Formatting

# Positive and Negative Number Formatting

To construct a custom format for currency or numbers that treats positive and negative numbers differently, use a semi-colon and a space in the Format attribute to delineate two formats:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714761751/formatdata_02.png)

For example, the Format value shown above will show positive numbers with a comma as a thousands separator. It will show negative numbers in the same way but also enclose them in parenthesis. Note the semi-colon *and* space which separate the positive and negative formats.

You can also use the **Conditional Class** element, beneath any Label element that displays numeric data, to display negative numbers in a different color than positive numbers.
