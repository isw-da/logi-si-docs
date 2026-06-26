---
title: "Using an Icon with a Shape Element"
id: 4406818067991
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818067991-Using-an-Icon-with-a-Shape-Element
updated_at: 2022-04-06T06:09:59Z
---

# Using an Icon with a Shape Element

# Using an Icon with a Shape Element

Logi Info includes a few standard shape elements, such as **Rectangle**. Let's see how we can use an FA icon with that.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562977559/fa_10_640x178.png)

In the example above, we see a Rectangle element with a child **Label** element (the Label text will appear inside the Rectangle borders). The Rectangle's **Class** attribute is set to:

fa fa-motorcycle fa-3x pull-left pad10

The only class you won't recognize is *pad10*, which is in a separate style sheet added for this example app and provides some padding inside the rectangle borders.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562977687/fa_11.png)

And the results are shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The height of the rectangle and the size of the text is being controlled by the *height* of the icon + the padding.
