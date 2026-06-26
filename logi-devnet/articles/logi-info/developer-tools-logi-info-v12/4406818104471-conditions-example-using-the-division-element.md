---
title: "Conditions Example: Using the Division Element"
id: 4406818104471
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818104471-Conditions-Example-Using-the-Division-Element
updated_at: 2022-04-06T06:10:13Z
---

# Conditions Example: Using the Division Element

# Conditions Example: Using the Division Element

A **Division** element is very useful as a *container* for other
elements and, through use of its Condition attribute, allows you to
selectively control whether it and its child elements, possibly entire
areas of application pages, are rendered.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575434903/usingcond_02.png)

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

##
