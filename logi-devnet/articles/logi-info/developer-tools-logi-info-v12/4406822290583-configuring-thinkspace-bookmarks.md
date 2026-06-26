---
title: "Configuring Thinkspace Bookmarks"
id: 4406822290583
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822290583-Configuring-Thinkspace-Bookmarks
updated_at: 2022-04-06T06:05:41Z
---

# Configuring Thinkspace Bookmarks

# Configuring Thinkspace Bookmarks

Users may want to save the Thinkspace visualizations they've created, for re-use in later sessions. This can be done using *Bookmarks*.

A bookmark is a mechanism for storing and re-using request parameters, user input data, and configuration choices made at runtime. More information about them is available in [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822405143-Bookmarks).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575732887/devdm31_11.png)

When properly configured, Thinkspace charts will display a **Save** button, as shown above. When users click it, a "snapshot" of their runtime settings is saved in a bookmark. The snapshot can be retrieved in a later session to reproduce their settings and visualization.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583974167/devdm31_12.png)

To enable the button, in the \_Settings definition's **General** element, shown above, set the **Bookmark Collection Default** and **Bookmark Folder Location** attributes. Bookmark collections are often user-specific and the @Function.UserName~ token can be used here to achieve this. The location attribute requires a fully-qualified path to a specific folder within the application folder.
