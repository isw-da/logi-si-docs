---
title: "Shared Elements"
id: 4419715558423
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715558423-Shared-Elements
updated_at: 2022-07-17T02:05:36Z
---

# Shared Elements

# Shared Elements

Shared
elements provide an opportunity to create "reusable code", with its traditional
benefits of greater efficiency and single instance maintenance, in Logi reports.

The following topics discuss shared elements:

* [Creating a Shared Element Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723266327-Creating-a-Shared-Element-Definition#Creating)
* [Using Shared Elements in a Report Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723268247-Using-Shared-Elements-in-a-Report-Definition#Using)
* [Passing Parameters to Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707937815-Passing-Parameters-to-Shared-Elements#PassParameters)
* [Passing Elements to Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707936919-Passing-Elements-to-Shared-Elements#PassElements)
* [Shared Element Usage Tips](https://devnet.logianalytics.com/hc/en-us/articles/4419723267351-Shared-Element-Usage-Tips#Tips)

## About Shared Elements

Developers often find that they're using the same elements, or groups of elements, repeatedly in *multiple* report definitions. Report headers and footers are good examples. However, rather than adding these elements or groups of elements repeatedly into numerous report definitions, and being faced with the challenge of maintaining them, developers can instead use **shared elements**.

A "shared element" is a *container* for one or more elements, identified by the shared element ID. It's referenced with a kind of placeholder element in a definition. At runtime, the Logi Server Engine replaces the placeholder with the actual elements from the shared element container, before the report HTML is generated.

Any changes made to a shared element "ripples through" to every definition that uses it, which makes maintenance easy. For example, you may wish to add a copyright message in your pages; by making it a shared element, you'll only have to change the year in one location each January.

A shared element also provides a level of abstraction similar to that found in object-oriented programming: a shared element can produce different results in different report definitions based on the data or variables fed to it. So it's not only reusable but its results and behavior can be dynamic based on external factors, including tokens, definition modifiers, stylesheets, etc. that reside in the definition that uses the shared element. This is a powerful feature that developers can leverage to make themselves
more efficient and their reports more reliable.

The examples below are from the Template Modifier Files sample application. Please read this topic carefully as the words "shared" and "element" appear many times in many ways and can be confusing.

A **Master Report** is a special report definition that includes
elements that are to be included in other reports. It's frequently used
to provide a template-like frame, often defined with a header, a menu,
and a footer, for integration with other reports. You may find this to be an useful alternative to building the same thing using shared elements. For more information, see [Master Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419707763991-Master-Reports).

The **Shared Element Params** element allows you to pass values into a shared element. These values are applied before the shared element is inserted into the calling report definition, making the shared element itself dynamic. The **Passed Shared Element** element even allows you to pass and include groups of elements, from the calling definition, into a shared element. These elements are
discussed in more detail
in later sections.

The **Include Shared Element** element has a **Condition** attribute, allowing you to dynamically employ shared elements.
![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The Condition attribute of shared elements does not support Default Request Parameter values, as the Default values are initiated after the shared elements have been processed. Request tokens can be used (as long as they are provided explicitly; however, default values won't be available when the conditions are evaluated.
