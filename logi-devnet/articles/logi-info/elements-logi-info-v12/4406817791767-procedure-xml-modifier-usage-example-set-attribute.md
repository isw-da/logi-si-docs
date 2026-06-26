---
title: "Procedure.XML Modifier - Usage Example: Set Attribute"
id: 4406817791767
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817791767-Procedure-XML-Modifier-Usage-Example-Set-Attribute
updated_at: 2022-04-06T06:08:13Z
---

# Procedure.XML Modifier - Usage Example: Set Attribute

# Procedure.XML Modifier - Usage Example: Set Attribute

This example demonstrates one of the simplest operations: updating a report definition by changing an element's Class attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563119895/xmlmod_02.png)

In the image above, we see a report definition on the left, the attributes for its **Label** element in the center (note that there is no Class attribute value), and the resulting output on the right.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575566871/xmlmod_03.png)

And now we see the Process Task with **Procedure.XML Modifier** and **Set Attribute** elements above on the left. The Procedure.XML Modifier element's Filename attribute (not shown) has been set to:

@Function.AppPhysicalPath~\\_Definitions\\_Reports\newReport.lgx

The Set Attribute element attributes are shown above in the center (note that the Label element's ID is used for the Xml Modifier ID value), and the resulting output is on the right.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583768727/xmlmod_04.png)

If we refresh the report definition in Studio, we can see that it's been updated with the new Class attribute value, shown highlighted above.
To change multiple attributes for the same element, use multiple child Set Attribute elements in the Process Task.
