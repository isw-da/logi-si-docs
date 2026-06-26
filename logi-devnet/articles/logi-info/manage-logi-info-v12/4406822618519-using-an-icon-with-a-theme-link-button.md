---
title: "Using an Icon with a Theme Link Button"
id: 4406822618519
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822618519-Using-an-Icon-with-a-Theme-Link-Button
updated_at: 2022-04-06T06:10:00Z
---

# Using an Icon with a Theme Link Button

# Using an Icon with a Theme Link Button

In [Combining Icon and Text in a Label](https://devnet.logianalytics.com/hc/en-us/articles/4406822616215-Combining-Icon-and-Text-in-a-Label), when an icon was used in a Label with a caption, we couldn't add more classes to style the text. That remains true but we *can* add other classes to style the text *container*. In this example, we'll add the ThemeLinkButton class.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575449879/fa_08_638x178.png)

As shown above, we've used a Label element, with a caption, and we've set the Class attribute value to:

fa fa-flag fa-lg pull-left ThemeLinkButton

The *pull-left* class is an FA class that left-justifies the icon and the *ThemeLinkButton* class has also been added.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583628695/fa_09.png)

And we can see the resulting Theme-based button shape and coloring above. In a live application, the button shading will change when the mouse cursor hovers over it.
