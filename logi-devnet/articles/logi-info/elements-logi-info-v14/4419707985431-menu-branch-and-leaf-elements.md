---
title: "Menu Branch and Leaf Elements"
id: 4419707985431
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707985431-Menu-Branch-and-Leaf-Elements
updated_at: 2022-07-17T02:05:20Z
---

# Menu Branch and Leaf Elements

# Menu Branch and Leaf Elements

The menu "options" are created using **Menu Branch** and **Menu Leaf** elements. A branch is an option that will have sub-options (leaves), while a leaf is an option that has no sub-options. A menu can have any number of branches and leaves, and many levels of nesting.

These two elements have the same attributes:

| Attribute | Description |
| --- | --- |
| Caption | (Required) Specifies the visible text of the menu option. |
| Class | Specifies one or more CSS classes to be used by the element. When set, this class will also be used by all child elements that don't have their own class. May be used with or without a theme. |
| Condition | Specifies an expression that evaluates to a value of True or False. If True, then the option is displayed, otherwise it's removed. Expressions should be in JavaScript or intrinsic functionsyntax. Typically, expressions compare values using a token, such as @Data.value~ < 0. Enclose both sides of the expression in quotes when working with strings: "@Data.myColumn~" == "SomeValue". |
| Expanded | (Menu Branch only) Specifies whether a branch is expanded when the menu is initially displayed. The default value is *False*. |
| ID | Specifies a unique element ID. |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to see the option, users without them will not. |
| Tooltip | Specifies the text that will appear when the user hovers the cursor over the menu option. |
