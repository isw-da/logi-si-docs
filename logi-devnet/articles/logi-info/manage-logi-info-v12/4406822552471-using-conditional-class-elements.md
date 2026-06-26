---
title: "Using Conditional Class Elements"
id: 4406822552471
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822552471-Using-Conditional-Class-Elements
updated_at: 2022-04-06T06:09:08Z
---

# Using Conditional Class Elements

# Using Conditional Class Elements

The **Conditional Class** element allows you to dynamically apply different style sheet classes, based on the Condition attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435287/usingcond_03.png)  

Suppose product managers want to be *visually alerted* if product stock levels fall below 100 units. In fact, when an item falls below that threshold, they'd like to see its "in stock" count displayed in the table in red, as in the example above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575527703/usingcss_04.png)

In the example shown above, the **Label** in the last data table column displays the number of units in stock. Its font color may be explicitly set in its own Class attribute, or it may be inherited from a parent element or a theme.

To give the product managers what they want, a **Conditional Class** element is added beneath the Label, and its attributes set as shown above. The expression in the Conditional Class element's **Condition** attribute sets the threshold and its **Class** attribute specifies which class to apply if the Condition expression
evaluates to *True*.

Multiple Conditional Class elements can be used beneath a parent element. In this case, the class from the *first* one of these elements that has a Condition attribute that evaluates to *True* will be applied; however, any remaining Conditional Class elements below it will *not* be evaluated.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)If you're using a stock Logi Theme (see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4406818168855-Themes)) and use a Conditional Class element with a complex element structure, like a Data Table, application of the conditional class may override the Theme styling for the *entire* structure, causing undesired results. Be sure, especially when using a Theme, to apply conditional
classes at the right level of the element structure. For example, if you want to affect data table rows, make a Conditional Class element the child of each Data Table Column element, rather than making it a child of the Data Table element itself.
