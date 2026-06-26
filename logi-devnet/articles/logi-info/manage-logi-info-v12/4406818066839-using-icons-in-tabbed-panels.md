---
title: "Using Icons in Tabbed Panels"
id: 4406818066839
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818066839-Using-Icons-in-Tabbed-Panels
updated_at: 2022-04-06T06:09:58Z
---

# Using Icons in Tabbed Panels

# Using Icons in Tabbed Panels

Finally, let's see how we can use multiple icons in tabbed panels.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575450007/fa_12_625x189.png)

In the example above, a **Tab**  element and several **Tab Panel** elements have been added. Each panel is supposed to contain information about different credit cards, so let's place their names and an icon for each card in their respective tabs. We can do this with a Class attribute value of:

fa fa-cc-amex fa-2x pull-left padTB10

The *fa-cc-xxxx* class will be different for each type of credit card. The only class you won't recognize is *padTB10*, which is in a separate style sheet added for this example app and provides some top and bottom padding inside the tabs.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562977943/fa_13_466x125.png)

And the results are shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The height of the tabs and the size of the text is being controlled by the *height* of the icon + the padding.
