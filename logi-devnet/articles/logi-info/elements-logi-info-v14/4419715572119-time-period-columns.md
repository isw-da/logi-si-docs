---
title: "Time Period Columns"
id: 4419715572119
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715572119-Time-Period-Columns
updated_at: 2022-07-17T01:30:39Z
---

# Time Period Columns

# Time Period Columns

Developers frequently need to work with parts of **dates** and **timestamps** and often employ various string parsing techniques to do so. The **Time Period Column** element, described in this topic, allows you to directly access the date and time parts of data without resorting to JavaScript functions and complicated parsing.

The following topics discuss the Time Period Columns element:

* [Time Period Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715570199-Time-Period-Columns-Attributes)
* [Time Period Column Simple Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4419715571095-Time-Period-Columns-Simple-Usage-Example#Simple)
* [Time Period Column Advanced Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4419723276055-Time-Period-Columns-Advanced-Usage-Example#Advanced)

## About the Time Period Column

The Time Period Column is similar to other elements designed to extend the data available in a datalayer. Like the **Calculated Column** element, the Time Period Column is added as a child element beneath a datalayer and **adds a new column** to the datalayer. This column contains derived data which is accessible using an @Data token. In this case, the derived data can be any of the parts of a DateTime value.

Time Period Columns can also be configured to be *culture-aware* so that the values derived will agree with the culture settings of the user's browser.

### Dynamic Application

The Time Period Column element has an **Include Condition** attribute:   

![](https://devnet.logianalytics.com/hc/article_attachments/4419699976599/timeperiod_01.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Time Period Column will be added to the datalayer or not.
