---
title: "Shared Elements"
id: 1500009531821
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531821-Shared-Elements
updated_at: 2021-06-17T01:58:37Z
---

# Shared Elements

# Shared Elements

Shared
elements provide an opportunity to create "reusable code", with its traditional
benefits of greater efficiency and single instance maintenance, in Logi reports. This topic discusses shared elements.

* About Shared Elements
* [Create a Shared Element Definition](#Creating)
* [Add Shared Elements to a Report](#Adding)
* [Shared Element Usage Tips](#Tips)

## About Shared Elements

Developers often find that they're using the same elements, or groups of elements, repeatedly in **multiple** report definitions. Report headers and footers are good examples. However, rather than adding these elements or groups of elements repeatedly into numerous report definitions, and being faced with the challenge of maintaining them, developers can instead use **shared elements**.

A "shared element" is a **container** for one or more elements, identified by the shared element ID. It's referenced with a kind of **placeholder** element in a definition. At runtime, the Logi Server Engine replaces the placeholder with the actual elements from the shared element container, before the report HTML is generated.

As "reusable code", any changes made to a shared element ripples through to every report that uses it, which makes maintenance very easy.

A shared element also provides a level of abstraction similar to that found in object-oriented programming: a shared element can produce different results in different report definitions based on the data or variables fed to it. So it's not only reusable but its results and behavior can be dynamic based on external factors, including tokens, definition modifiers, stylesheets, etc. that reside in the definition that uses the shared element. This is a powerful feature that developers can leverage to make themselves
more efficient and their reports more reliable.

Many of the Sample Applications available on DevNet use shared elements and you can refer to them for implementation examples. Look for a sample app that has a "menu" of links across the top of the page, just below the banner image, such as the Animated Charts sample. The menu links are created using shared elements.

The examples below are from the Template Modifier Files sample application. Please read this topic carefully as the words "shared" and "element" appear many times in many ways and can be confusing.

## Create a Shared Element Definition

Using shared elements begins by creating a **definition**. Shared elements can be defined in any report definition but the recommended practice is to create a *separate* report definition just to hold shared elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778512407/shrelements_01.png)

In the example shown above, a separate definition named "sharedElements" has been created to hold the shared elements. This approach has several benefits, including the possibility of copying the definition file itself to other Logi applications, extending the reusability concept and enforcing consistency.

If you're creating a shared elements definition for a Mobile Reporting application, be sure to place the definition within the **Mobile Reports** folder.

**sharedElements**![](https://logianalytics.zendesk.com/hc/article_attachments/4402778512663/shrelements_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771613591/shrelements_02a.png)

In the definition, as shown above, a shared element definition is started by adding a **Shared Element** element. This is the basic container for one or more elements that you want to share. Be sure to give this element the required unique ID.

A definition file can hold many Shared Element elements, each containing one or more elements to be shared.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771613847/shrelements_03.png)

As shown above, a variety of elements can be added beneath the Shared Element element. These can include any element available for report definitions. In the example, elements have been added to create a common header for several reports.

Your shared elements are now available to any report definition in your application.

## Add Shared Elements to a Report

Adding your shared elements to a report definition is very simple:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778512919/shrelements_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778513303/shrelements_04a.png)

1. Add an **Include Shared Element** element to your report definition, as shown above, beneath the Report Header element.
2. Set its **Definition File** attribute value by selecting the sharedElements definition from the drop-down list of definitions.
3. Set its **Shared Element ID** attribute value by selecting the sharedHeader definition from the drop-down list of shared elements in the previously selected definition.
4. Set its **ID** attribute to an arbitrary unique value.

Include Shared Element elements can be added anywhere in your report definition, and the same shared element can be used multiple times in the same definition if necessary.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771614103/shrelements_04b.png)

Beginning with v10.0.269, once you've added an Include Shared Element element to your definition, you can click the "+" box next to it to **expand it** and see the elements it's associated with, and their attributes, in read-only mode. Any modifications to the element being shared must occur in the definition that contains the shared element.

Repeating steps 1-4 above for every report definition in an application will result in the same header appearing on every report.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778513559/shrelements_05.png)

The resulting report is shown above. The highlighted area at the top is the content created by the shared element.

## Shared Element Usage Tips

* The insertion of the shared XML source code in a shared element into a report at runtime is done *without* dynamic review of the "parent-child" element relationship rules, so it's possible to include shared elements where they don't belong. Therefore, it's the **developer's responsibility** to ensure that the "element rules" are being followed. To do this, we recommend that you create shared elements by first, using all the elements to be shared right where they belong,
  directly in a report, then successfully testing them, then copying them out to the shared element definition, and finally replacing them with the Include Shared Element element.
* Multiple Shared Element elements can be placed in the same definition:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771614359/shrelements_06.png)

The example shown above is from the definition file for the DevNet web site and shows multiple Shared Element elements in a single definition file.

* Stylesheets apply to shared elements in several ways. If the shared elements do not include a style sheet of their own then the style sheet of the definition using the shared elements is applied. If the a style sheet is included as one of the shared elements, then any style classes with the same name in both it and the report definition's style sheet will cascade.
* Both the **Definition File** and **Shared Element ID** attribute values of the
  Include Shared Element element can be specified using tokens.
* If a shared element definition file becomes very large, it may be useful and may improve performance to create multiple shared element definition files. Some developers group their shared elements into different definition files based on their function or purpose.
* **Action.ShowElement** cannot be used to show/hide an Include Shared Element element, although use of Division elements can achieve conditional inclusion of shared elements.
* Shared elements are embedded into a report definition when the report runs, so any Request parameters that are passed to the report can be used in the shared elements. Similarly, shared elements can work with **data** from a datalayer in a parent report definition, but they must be in scope; i.e. beneath the chart or table that's the parent of the datalayer. The exception to this is data from LocalData, which can be used throughout the report and shared elements.
* Logi Info developers can also use shared elements in Process definitions.
