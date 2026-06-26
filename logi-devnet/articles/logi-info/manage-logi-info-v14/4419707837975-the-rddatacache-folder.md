---
title: "The rdDataCache Folder"
id: 4419707837975
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707837975-The-rdDataCache-Folder
updated_at: 2022-07-17T01:37:39Z
---

# The rdDataCache Folder

# The rdDataCache Folder

When data is returned from a data source, the Logi Server Engine may cache
it in server memory or in temporary XML files or in both. When certain
charts are used, temporary code fragment files are generated. These and
other temporary files are created by the system in the rdDataCache folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) When data is cached in this folder it makes easier to
"page" through the data and to retrieve it quickly. However, if
a new data query is executed, then the data cached here is replaced. The
two exceptions to this are when **DataLayer.Cached** is used and when a
super-element such as the **Analysis Grid**, which is designed to work
with cached data, are used. Both of these exceptions have specific
mechanisms for refreshing their data.

The default name and location of the rdDataCache folder works very well
for most implementations but they can be changed in
[The \_Settings Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723151767-The-Settings-Definition). This might be helpful when very large data sets and large numbers of
user raise concerns about temporary files consuming all of the free disk
space, or in clustered server environments where sharing is required.
These are unusual situations, however, and the default is appropriate for
most use-cases.
