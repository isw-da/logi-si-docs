---
title: "Applying the RegEx Filter"
id: 4406817808791
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817808791-Applying-the-RegEx-Filter
updated_at: 2022-04-06T06:08:21Z
---

# Applying the RegEx Filter

# Applying the RegEx Filter

The following example illustrates how the **RegEx Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563110807/regexfilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575558679/regexfilter_01a.png)

1. As shown above, a **RegEx Filter** element is added as a child to a datalayer element.
2. Its **Data Column** attribute value is set to the column in that datalayer whose value will be examined.
3. The **Regular Expression** attribute is set to define the desired regular expression code.

Using the example above, the sequence of events is that the datalayer reads in all the data from the datasource, then the RegEx Filter **removes** all rows whose Freight column values don't match the regular expression pattern (unlimited digits before the decimal point, two digits after it, and no dollar signs, commas, text, or symbols). All that remains in the datalayer for use in the report are rows whose Freight values match the pattern.
