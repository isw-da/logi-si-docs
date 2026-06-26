---
title: "Conditions Example: Using the Division Element "
id: 4419723313687
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723313687-Conditions-Example-Using-the-Division-Element
updated_at: 2022-07-17T02:22:52Z
---

# Conditions Example: Using the Division Element 

# Conditions Example: Using the Division Element

A **Division** element is very useful as a *container* for other
elements and, through use of its Condition attribute, allows you to
selectively control whether it and its child elements, possibly entire
areas of application pages, are rendered.

![](https://devnet.logianalytics.com/hc/article_attachments/7522731541143/usingcond_02.png)

In the example shown above, three **Division** elements have been used
to contain responses to specific potential errors.

If the Request variable and value ;"ErrorCode=3" is passed to
this page when it's called, then the "divErrorMsg3" element will
be displayed, along with its child elements, causing an error message to
appear on the page. The other two Divisions, which have a similar
expression in their Condition expressions but with a comparison to values
*1* and *2*, will not be displayed.

As mentioned earlier, the effect of displaying or hiding a Division
element extends beyond just visibility; for example, datalayers within
divisions *will not run* if the division is not displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Division elements include "HTML Attribute Params", enabling you to apply your application to work with other frameworks or libraries easier. With the HTML Attribute Params, you have the option to include "style" parameters:

![](https://devnet.logianalytics.com/hc/article_attachments/7522742777623/divisions_attributes_844x349.png)

After the HTML Attribute Params are applied:

![](https://devnet.logianalytics.com/hc/article_attachments/7522726273303/division_attributes_working_ex_894x425.png)

If an attribute was set in both Element and HTML attribute params, the one set in the HTML attribute params will be ignored.
