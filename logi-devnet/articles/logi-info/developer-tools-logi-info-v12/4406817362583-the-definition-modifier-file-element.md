---
title: "The Definition Modifier File Element"
id: 4406817362583
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817362583-The-Definition-Modifier-File-Element
updated_at: 2022-04-06T06:05:36Z
---

# The Definition Modifier File Element

# The Definition Modifier File Element

The presence of a **Definition Modifier File** element tells the Logi
Server Engine to process the file it identifies.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563342231/usingdmf_01.png)

As shown above, the element is a child of the report definition's root
element. Its **Definition Modifier File** attribute value is the name
of the actual XML file, with .xml extension. The file can be in any folder
accessible to the Logi application but when a fully-qualified file path is
not specified, the assumed location is the \_SupportFiles folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Tokens can be used here to provide the DMF filename, which allows
you to specify different DMFs (or no DMF) for different situations, users,
etc.
