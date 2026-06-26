---
title: "Passing Elements to Shared Elements"
id: 4406822601367
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822601367-Passing-Elements-to-Shared-Elements
updated_at: 2022-04-06T06:09:45Z
---

# Passing Elements to Shared Elements

# Passing Elements to Shared Elements

There may be situations where it's desirable to pass *entire elements* into a shared element. The passed element is then added to the shared element before it's applied to the calling report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575472407/shrelements_10.png)

Imagine that you provide a report with a footer that includes a logo image and standard menu links, like the one shown above. Depending on the consumer, you need to show a different logo and the images are different sizes and types. Passing a configured Image element to the shared element is a good solution.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575472791/shrelements_11.png)

This time we'll start our example, shown above, in the sharedElements report definition and construct our footer. Where the logo image will appear, we added an **Include Shared Element** element. When configuring it, we used the special identifier "PassedSharedElement" for the Definition File attribute (it appears at the very top of the pull-down list of options), and the ID that we'll give later to the Passed Shared Element element in the calling definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562999703/shrelements_12.png)

In our Default definition, shown above, we added an Include Shared Element element in the footer. Beneath it, we added a **Passed Shared Element** element and set it ID attribute to match the one we used in the sharedElement definition. Then we added child elements beneath it, including the Image element we're passing.

Using Division elements as containers for the image allows us to make the choice of image conditional, based on the Divs' Condition attributes.

This is a very powerful feature. Another interesting possible implementation would be to use a Passed Shared Element to pass a *datalayer* to a visualization, allowing it to work with data from different data sources.
