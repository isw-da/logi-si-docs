---
title: "Overriding Element Style Classes"
id: 4406822551575
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822551575-Overriding-Element-Style-Classes
updated_at: 2022-04-06T06:09:06Z
---

# Overriding Element Style Classes

# Overriding Element Style Classes

The acronym "CSS" stands for Cascading Style Sheet, which means that the effects of style sheets, like water, flow "down hill". Classes assigned to elements that are "containers" or parents for other elements, such as divisions, tables, or rows, affect all the elements they contain. The style "flows" down into all the child elements within the container. However, if a style class is individually assigned to one of the child elements, it can *override*
the style set in the parent container element.

For example, you could assign to a **Table** element a style class that includes text-align: left, causing all text in the table columns to be aligned to the left. However, for a numeric column, you could assign a class that includes text-align: right to one of the
**Data Table Column** elements (a child element of the Table element). The alignment specified by
the Table element's class will be overridden by the Data Table Column element's class.

Similarly, classes from a global style sheet are applied before classes from a local style sheet, so the local style sheet will be the winner (will override) if there are any class duplications in both style sheets.

This inheritance and overriding of style classes doesn't always work the way you expect it to, though, and it can be frustrating. If style assigned to a parent isn't working on the child elements as you expect, ensure that they don't have their own class assignments or try moving the class assignment "up" a level, to the parent container element's parent container.

Some complicated elements, such as the **Dashboard**, **Analysis Grid**, and **Tabs** elements, have their own "internal style sheets" which govern their general appearance. It is possible to affect their appearance by including appropriate classes in your own report-level style sheet that override the default classes used with the elements. By looking around in your application folder, under the rdTemplate folder, you can find these element style sheets and determine which
classes to include and thereby override in your own style sheet.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)*Never change the default style sheet distributed with your Logi product! Always work from a copy.*

There's a caveat, however: future releases of Logi products may include class name changes that could cause your overrides to stop working and require you to update them.

## Style Sheets vs Themes

Logi **Themes** apply a specific appearance to a report page. A Theme includes its own style sheet and it's possible to assign *both* a theme *and* an individual style sheet to a report definition. In this case, if the theme's style sheet conflicts with your individual style sheet, then the classes in your individual style sheet will "win".

## How Did They Do That?

Not sure how to *recreate* the styles you see on the web? There are developer tools built into most modern browsers that let you to look "into" web pages to see how style is applied in them. These tools can be very helpful in learning both commonly-used and more esoteric techniques, and also in understanding how classes are "cascading" through the web page. They're are usually invoked using the F12 key while viewing a page in the browser.

In addition, unless a style sheet has been "minified" or compacted to an almost unreadable state, you can view it to see its classes. This is a great way to learn CSS tricks and advanced techniques. Look for its URL near the top of an HTML page, copy it, and paste it into your browser's address bar (relative references may require a little extra work), then browse to see the classes.
