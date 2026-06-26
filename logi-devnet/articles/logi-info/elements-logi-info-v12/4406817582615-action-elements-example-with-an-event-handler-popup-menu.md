---
title: "Action Elements Example: With an Event Handler Popup Menu"
id: 4406817582615
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817582615-Action-Elements-Example-With-an-Event-Handler-Popup-Menu
updated_at: 2022-06-20T11:55:32Z
---

# Action Elements Example: With an Event Handler Popup Menu

# Action Elements Example: With an Event Handler Popup Menu

The **Action.Popup Menu** element can be used with event handlers to cause a "pop-up" menu to appear when the mouse passes over a link or image.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563215895/introacts_13.png)

The example shown above shows the elements used to produce the Documents popup menu (sometimes called a "pull-down" menu) on an early version of DevNet:

* The Event Handler element is set to fire on the *onMouseOver* event. When it fires, it executes the **Action.Popup Menu** element beneath it.
* A **Popup Option** element is included for each pop-up menu item to be displayed.
* Each Popup Option element needs, at least, a **Label** element and an **Action** element beneath it to cause something to happen when the pop-up menu item is clicked. If an **Image** element is included, it will also be displayed.

The Action.Popup Menu element has a **Popup Location** attribute that controls where the pop-up menu appears in relation to the Image or Label clicked to call it. The popup menu can be beneath it, as shown above, or beside it to the right.
