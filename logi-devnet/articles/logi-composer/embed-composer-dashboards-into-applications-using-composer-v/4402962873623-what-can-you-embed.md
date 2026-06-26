---
title: "What Can You Embed?"
id: 4402962873623
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402962873623-What-Can-You-Embed
updated_at: 2021-08-07T17:29:24Z
---

# What Can You Embed?

# What Can You Embed?

The Composer JavaScript application framework allows you to query data from the Composer server and embed Composer visuals in your own web application. The Composer client application provides a number of controls for interacting with these visuals. These controls are part of the Composer client application rather than the visual itself. When you embed the visual, these controls are not embedded with visuals.

For example the image below shows a bar chart in the Composer client application. The highlighted objects are not embedded with the visual when it is embedded in a custom application.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952919063/vis-embedding_576x308.png)

Objects not embedded include:

* Visual title and information
* Visual [drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955730967-Use-the-Visual-Menu)
* X and Y selectable axis labels
* Time bar and time controls
* Context menu
* Tool tips
* Legend
* Controls for saving, searching, selecting favorites, sharing, or adding additional visuals

The same visual, embedded in a custom app, looks like the following example.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952919319/embedded-vis_305x233.png)

While the SDK does not replicate controls found in the Composer client application, it does provide the data that you need to recreate many of them.
