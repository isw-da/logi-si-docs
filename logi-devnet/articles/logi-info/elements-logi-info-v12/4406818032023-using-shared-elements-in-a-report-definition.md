---
title: "Using Shared Elements in a Report Definition"
id: 4406818032023
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818032023-Using-Shared-Elements-in-a-Report-Definition
updated_at: 2022-04-06T06:09:45Z
---

# Using Shared Elements in a Report Definition

# Using Shared Elements in a Report Definition

Using your shared elements in a report definition is very easy. Here's how to use a shared report header:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562997015/shrelements_04.png)

1. Add an **Include Shared Element** element to your report definition, as shown above, in this case beneath the Report Header element.
2. Set its **Definition File** attribute value by selecting the *sharedElements* definition from the drop-down list of definitions.
3. Set its **Shared Element ID** attribute value by selecting the *SharedHeader* definition from the drop-down list of shared elements in the previously selected definition.

Include Shared Element elements can be added anywhere in your report definition, and the same shared element can even be used multiple times in the same definition, ifnecessary.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562997143/shrelements_05.png)

As soon as you select the shared element in the Attributes panel, its contents will be displayed, in read-only mode, in the Element Tree, as shown above. Any modifications to it must be made in the definition that contains the shared element.

Now you can copy the configured Include Shared Element element into the Report Header of every report definition in an application. This will result in the same header appearing on every report.

Shared elements can also be used to include common but *non-visual* code in definitions, such as shim scripts, meta tags, and more.
