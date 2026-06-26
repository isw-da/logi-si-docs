---
title: "Master Report Elements"
id: 4406817762839
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817762839-Master-Report-Elements
updated_at: 2022-04-06T06:08:03Z
---

# Master Report Elements

# Master Report Elements

A **Master Report** is a regular Report definition that can
includeany elements you feel are required.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563133079/masterrpt_03.png)

The only element it *must* have is the
**Master Report Content** element, as shown in the example above. This
is the "placeholder" for the content from other report
definitions. It tells the Logi Server Engine where to insert the other
definitions at runtime. This element has no attributes and only one of
them is allowed in a Master Report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575579543/masterrpt_04.png)

In the other report definitions in your application, add a
**Master Report** element, as shown above. Set its
**Report Definition File** attribute value to the name of your Master
Report definition (tokens may *not* be used here). This will cause
the integration of the definitions at runtime.
