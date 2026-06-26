---
title: "Elements Using the Condition Attribute"
id: 4419707972759
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707972759-Elements-Using-the-Condition-Attribute
updated_at: 2022-07-17T02:22:53Z
---

# Elements Using the Condition Attribute

# Elements Using the Condition Attribute

The following elements have a **Condition** attribute. In the first
group, the Condition attribute simply determines whether or not the
element and its child elements are *rendered* on the page:

* Column Cell
* Crosstab Table Label Column
* Data Table Column
* Division
* Local Data
* More Info Row
* More Info Row Column
* Include Frame (also called Sub-Report)
* Row
* Security Filter
* Set Session Variables
* Tooltip Panel

These two elements use the **Condition** attribute slightly differently
to control other behaviors:

* Conditional Class - the Condition attribute determines whether the
  element's style sheet class is applied to all of its child elements that
  do not have a class specified.
* Condition Filter - the Condition attribute determines which data layer
  result rows are kept and which are filtered out.

Many elements also have an **Include Condition** attribute, which
determines if the element is included in processing. Typically, elements
with this attribute are filter and column elements used to manipulate
data.

Elements that have a value in their **Condition** or
**Include Condition** attributes are now indicated by a diamond
icon:

![](https://devnet.logianalytics.com/hc/article_attachments/7522742938007/usingcond_08.png)

The diamond icon, shown circled above, appears in both the Element Tree
(left) and in the Attributes Panel.
