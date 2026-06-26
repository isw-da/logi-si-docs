---
title: "Adding an Image to the Pop-up Options"
id: 4419707988631
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707988631-Adding-an-Image-to-the-Pop-up-Options
updated_at: 2022-07-17T01:26:36Z
---

# Adding an Image to the Pop-up Options

# Adding an Image to the Pop-up Options

The menu item text that appears in the pop-up menu can be accompanied by an image.

![](https://devnet.logianalytics.com/hc/article_attachments/4419715006231/popmenu_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419707211159/popmenu_05a.png)

The examples above show a menu with and without the images. To include an image, you need to configure the Popup Option element differently:

![](https://devnet.logianalytics.com/hc/article_attachments/4419715006615/popmenu_06.png)

Instead of using the Popup Options element's **Caption** attribute to set the text that will be displayed, leave it blank and then add an **Image** and a **Label** element, as shown above, as child elements. The Action element remains a child of the Popup Option element, rather than of the Image or Label.
