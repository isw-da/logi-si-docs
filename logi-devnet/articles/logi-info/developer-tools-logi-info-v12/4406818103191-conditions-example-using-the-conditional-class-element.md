---
title: "Conditions Example: Using the Conditional Class Element"
id: 4406818103191
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818103191-Conditions-Example-Using-the-Conditional-Class-Element
updated_at: 2022-04-06T06:10:11Z
---

# Conditions Example: Using the Conditional Class Element

# Conditions Example: Using the Conditional Class Element

The **Conditional Class** element allows you to dynamically apply
different style sheet **classes**, based on the Condition attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562961175/usingcond_04.png)

Suppose product managers want to be *visually alerted* if product
stock levels fall below 100 units. In fact, when an item falls below that
threshold, they'd like to see its "in stock" count displayed in
the table in red, as in the example above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583612695/usingcond_05.png)

In the example shown above, the **Label** in the last data table column
displays the number of units in stock. Its font color may be explicitly
set in its own Class attribute, or it may be inherited from a parent
element or a theme.

To give the product managers what they want, a
**Conditional Class** element is added beneath the Label, and its
attributes set as shown above. The expression in the Conditional Class
element's **Condition** attribute sets the threshold and its
**Class** attribute specifies which class to apply if the Condition
expression evaluates to *True*.

Multiple Conditional Class elements can be used beneath a parent element
(the maximum is nine Conditional Class elements). In this case, the class
from the *first* one of these elements that has a Condition attribute
that evaluates to *True* will be applied; any remaining Conditional
Class elements below it will *not* be evaluated.
