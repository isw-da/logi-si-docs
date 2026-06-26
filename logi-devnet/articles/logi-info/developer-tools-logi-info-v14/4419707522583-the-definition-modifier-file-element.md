---
title: "The Definition Modifier File Element"
id: 4419707522583
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707522583-The-Definition-Modifier-File-Element
updated_at: 2022-07-17T02:24:35Z
---

# The Definition Modifier File Element

# The Definition Modifier File Element

The Definition Modifier File element is a child of the report definition's root element. The presence of a DMF element tells the Logi
Server Engine to process the file it identifies. Its **Definition Modifier File** attribute value is the name
of the actual XML file, with .xml extension. The file can be in any folder
accessible to the Logi application but when a fully-qualified file path is
not specified, the assumed location is the \_SupportFiles folder.

The Definition Modifier File (DMF) element now includes a **Condition** attribute that enables loading of the DMF. By default, this attribute it set to "True".

![](https://devnet.logianalytics.com/hc/article_attachments/7522826046871/dmf_824x186.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)

* If this attribute is not set, set to an empty string, or set to "1", it is considered "True".

* You can use tokens to provide the DMF filename (as shown above), enabling you to specify different DMFs (or no DMF) for different situations, users,
  etc.
