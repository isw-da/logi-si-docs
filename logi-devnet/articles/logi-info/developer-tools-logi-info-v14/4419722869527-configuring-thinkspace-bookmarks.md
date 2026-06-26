---
title: "Configuring Thinkspace Bookmarks"
id: 4419722869527
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722869527-Configuring-Thinkspace-Bookmarks
updated_at: 2022-07-17T01:51:27Z
---

# Configuring Thinkspace Bookmarks

# Configuring Thinkspace Bookmarks

Users may want to save the Thinkspace visualizations they've created, for re-use in later sessions. This can be done using *Bookmarks*.

A bookmark is a mechanism for storing and re-using request parameters, user input data, and configuration choices made at runtime. More information about bookmarks are available in [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706787991/devdm31_11.png)

When properly configured, Thinkspace charts will display a **Save** button, as shown above. When users click it, a "snapshot" of their runtime settings is saved in a bookmark. The snapshot can be retrieved in a later session to reproduce their settings and visualization.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706788247/devdm31_12.png)

To enable the button, in the \_Settings definition's **General** element, shown above, set the **Bookmark Collection Default** and **Bookmark Folder Location** attributes. Bookmark collections are often user-specific and the @Function.UserName~ token can be used here to achieve this. The location attribute requires a fully-qualified path to a specific folder within the application folder.
