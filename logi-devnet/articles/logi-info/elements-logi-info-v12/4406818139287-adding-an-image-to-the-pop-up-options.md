---
title: "Adding an Image to the Pop-up Options"
id: 4406818139287
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818139287-Adding-an-Image-to-the-Pop-up-Options
updated_at: 2022-04-06T06:10:24Z
---

# Adding an Image to the Pop-up Options

# Adding an Image to the Pop-up Options

The menu item text that appears in the pop-up menu can be accompanied by an image.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583600279/popmenu_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417562949015/popmenu_05a.png)

The examples above show a menu with and without the images. To include an image, you need to configure the Popup Option element differently:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575419799/popmenu_06.png)

Instead of using the Popup Options element's **Caption** attribute to set the text that will be displayed, leave it blank and then add an **Image** and a **Label** element, as shown above, as child elements. The Action element remains a child of the Popup Option element, rather than of the Image or Label.
