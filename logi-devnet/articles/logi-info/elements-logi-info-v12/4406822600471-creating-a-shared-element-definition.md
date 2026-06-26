---
title: "Creating a Shared Element Definition"
id: 4406822600471
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822600471-Creating-a-Shared-Element-Definition
updated_at: 2022-04-06T06:09:44Z
---

# Creating a Shared Element Definition

# Creating a Shared Element Definition

Shared elements can be defined in any report definition but the recommended practice is to create one or more *separate* report definitions in Logi Studio just to hold shared elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575473047/shrelements_01.png)

In the example shown above, a separate definition named "sharedElements" has been created to hold the shared elements. This approach has several benefits, including the possibility of copying the definition file itself to other Logi applications, extending the reusability concept and enforcing consistency.

If you're creating a shared elements definition for a Mobile Reporting application, be sure to place the definition within the **Mobile Reports** folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583650071/shrelements_02.png)

In the **sharedElements** definition, as shown above, a shared element definition is started by adding a **Shared Element** element. This is the basic container for one or more elements that you want to share. Be sure to give this element the required unique ID. This definition doesn't need any of the standard elements usually found in a report definition, such as Style, Report Header, Body, and Report Footer.

A definition file can hold many Shared Element elements, each containing one or more elements to be shared.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575473431/shrelements_03.png)

As shown above, a variety of elements can be added beneath the Shared Element element. These can include any element available for report definitions. In the example, elements have been added to create a common header for several reports.

Your shared elements are now available to any report definition in your application.
