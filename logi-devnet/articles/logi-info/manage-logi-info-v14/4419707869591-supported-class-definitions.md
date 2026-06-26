---
title: "Supported Class Definitions"
id: 4419707869591
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707869591-Supported-Class-Definitions
updated_at: 2022-07-17T01:36:03Z
---

# Supported Class Definitions

# Supported Class Definitions

There are several ways in which classes can be defined within style sheets and all of them can be used in style sheets for Logi applications.

Logi elements work with CSS classes that are defined using these selectors:

| Selector | Example | How Applied |
| --- | --- | --- |
| 1. An HTML tag | BODY {  color: white;  } | Applied automatically to the HTML tag. No assignment in an element's Class attribute is necessary. |
| 2. An HTML tag and a Class name, separated by a period (.) | TD.left {  text-align: left;  } | Applied automatically to the HTML tag. For example, if a table element has the class *.left* applied to it, its cells (which use <TD> tags) will have *TD.left* applied to them. |
| 3. A Class name only, preceded by a period (.) | .textLeft {  text-align: left; } | Applied to an element by entering the class name, *without* the leading period, in the element's Class attribute. |
| 4. An Element ID, preceded by the hash mark (#) | #myLabel {  color:Red; } | Automatically applied to elements with an element ID matching the class name. It's not available to any element with a different ID. No assignment in the Class attribute is necessary. |

The last example, which uses the Element ID, is very useful for applying style to elements which seem to have no mechanism for controlling their appearance. For example, by default, Data Table Column header text is centered and its data is left-aligned, but this technique can be used to right-align them instead.
