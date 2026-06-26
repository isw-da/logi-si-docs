---
title: "Shared Element Usage Tips"
id: 4406818030743
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818030743-Shared-Element-Usage-Tips
updated_at: 2022-04-06T06:09:45Z
---

# Shared Element Usage Tips

# Shared Element Usage Tips

The following is a list of helpful tips when using Shared Elements:

* The insertion of the shared XML source code in a shared element into a report at runtime is done *without* dynamic review of the "parent-child" element relationship rules, so it's possible to include shared elements where they don't belong. Therefore, as the developer it's your responsibility to ensure that the "element rules" are being followed. To do this, we recommend that you create shared elements by first, using all the elements to be shared right where they belong,
  directly in a report, then successfully testing them, then copying them out to the shared element definition, and finally replacing them with the Include Shared Element element.
* Multiple Shared Element elements can be placed in the same definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562997271/shrelements_06.png)

* **Stylesheets** apply to shared elements in several ways. If the shared elements do not include a style sheet of their own then the style sheet of the definition using the shared elements is applied. If a style sheet *is* included in one of the shared elements, then any style classes with the same name in both it and the report definition's style sheet will cascade.

* Both the **Definition File** and **Shared Element ID** attribute values of the
  Include Shared Element element can be specified using tokens.

* If a shared element definition file becomes very large, it may be useful and may improve performance to create multiple shared element definition files. Some developers group their shared elements into different definition files based on their function or purpose.
* **Action.ShowElement** cannot be used to show/hide an Include Shared Element element, although use of Division elements can achieve conditional inclusion of shared elements.
* Shared elements are inserted into a report definition when the report runs, so any Request parameters that are passed to the report can be used in the shared elements. Similarly, shared elements can work with *data* from a datalayer in a parent report definition, but they must be in scope; i.e. inserted beneath the chart or table that's the parent of the datalayer. The exception to this is data from LocalData, which can be used throughout the report and shared elements.
* You may also include shared elements in Process definitions.
