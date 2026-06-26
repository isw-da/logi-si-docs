---
title: "Time Period Columns"
id: 4406818047511
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818047511-Time-Period-Columns
updated_at: 2022-04-06T06:09:51Z
---

# Time Period Columns

# Time Period Columns

Developers frequently need to work with parts of **dates** and **timestamps** and often employ various string parsing techniques to do so. The **Time Period Column** element, described in this topic, allows you to directly access the date and time parts of data without resorting to JavaScript functions and complicated parsing.

The following topics discuss the Time Period Columns element:

* [Time Period Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406818045079-Time-Period-Columns-Attributes)
* [Time Period Column Simple Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4406818046103-Time-Period-Columns-Simple-Usage-Example#Simple)
* [Time Period Column Advanced Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4406822608151-Time-Period-Columns-Advanced-Usage-Example#Advanced)

## About the Time Period Column

The Time Period Column is similar to other elements designed to extend the data available in a datalayer. Like the **Calculated Column** element, the Time Period Column is added as a child element beneath a datalayer and **adds a new column** to the datalayer. This column contains derived data which is accessible using an @Data token. In this case, the derived data can be any of the parts of a DateTime value.

Time Period Columns can also be configured to be *culture-aware* so that the values derived will agree with the culture settings of the user's browser.

### Dynamic Application

The Time Period Column element has an **Include Condition** attribute:   

![](https://devnet.logianalytics.com/hc/article_attachments/4417583641239/timeperiod_01.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Time Period Column will be added to the datalayer or not.
