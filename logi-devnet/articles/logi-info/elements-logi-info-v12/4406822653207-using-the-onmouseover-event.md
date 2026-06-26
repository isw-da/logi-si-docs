---
title: "Using the onMouseOver Event"
id: 4406822653207
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822653207-Using-the-onMouseOver-Event
updated_at: 2022-04-06T06:10:24Z
---

# Using the onMouseOver Event

# Using the onMouseOver Event

You can make the pop-up menu appear when the mouse is hovered over the main menu link or image, which saves a mouse click:  
![](https://devnet.logianalytics.com/hc/article_attachments/4417575418135/popmenu_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583599767/popmenu_02a.png)

By introducing an **Event Handler** element *between* the main menu Label and the Action.Popup elements, as shown above, and setting its DHTML Event attribute to *onMouseOver*, you can cause the pop-up to appear when the mouse passes over the label, so clicking the link is not necessary.
