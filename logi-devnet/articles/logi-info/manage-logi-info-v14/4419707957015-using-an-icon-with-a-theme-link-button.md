---
title: "Using an Icon with a Theme Link Button"
id: 4419707957015
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707957015-Using-an-Icon-with-a-Theme-Link-Button
updated_at: 2022-07-17T01:30:02Z
---

# Using an Icon with a Theme Link Button

# Using an Icon with a Theme Link Button

In [Combining Icon and Text in a Label](https://devnet.logianalytics.com/hc/en-us/articles/4419715579543-Combining-Icon-and-Text-in-a-Label), when an icon was used in a Label with a caption, we couldn't add more classes to style the text. That remains true but we *can* add other classes to style the text *container*. In this example, we'll add the ThemeLinkButton class.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699991575/fa_08_638x178.png)

As shown above, we've used a Label element, with a caption, and we've set the Class attribute value to:

fa fa-flag fa-lg pull-left ThemeLinkButton

The *pull-left* class is an FA class that left-justifies the icon and the *ThemeLinkButton* class has also been added.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707173143/fa_09.png)

And we can see the resulting Theme-based button shape and coloring above. In a live application, the button shading will change when the mouse cursor hovers over it.
