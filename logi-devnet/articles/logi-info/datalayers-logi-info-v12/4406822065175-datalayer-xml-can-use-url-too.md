---
title: "DataLayer.XML Can Use URL, Too"
id: 4406822065175
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822065175-DataLayer-XML-Can-Use-URL-Too
updated_at: 2022-04-06T06:02:49Z
---

# DataLayer.XML Can Use URL, Too

# DataLayer.XML Can Use URL, Too

The **DataLayer.XML File** element is very useful for getting data
from an XML file into tables or input select lists. However, instead of
specifying a filename, you can specify a **URL** instead and retrieve
data from sources other than the local file system. Here's how it
works:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584237847/xmlfile_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417584238103/xmlfile_01a.png)

Usually, when using a DataLayer.XML File element, for the
**XML File** attribute you provide (1) the name of a file in the file
system. If you enter just the filename, the application will look for it
first in the \_SupportFiles folder.
However, you can instead provide (2) a URL to a file on another server.
This could be useful in centralizing look-up information or getting data
from another server.
