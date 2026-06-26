---
title: "Procedure.XML Modifier - Usage Example: Set Element Text"
id: 4419707787031
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707787031-Procedure-XML-Modifier-Usage-Example-Set-Element-Text
updated_at: 2023-04-12T13:54:59Z
---

# Procedure.XML Modifier - Usage Example: Set Element Text

# Procedure.XML Modifier - Usage Example: Set Element Text

This example demonstrates how to set the text for HTML tags that support text.

<p>Now is time for all good men to come to the aid of their country</p>  
<p ID="CopyrightMsg">Copyright (c) 2018 Good Works, Inc.</p>
  
Assume we have an HTML page with the code shown above in it, and we'd like to programmatically change the year in the copyright declaration.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707025175/xmlmod_12.png)

In our Process Task, shown above, the Procedure.XML Modifier element's Filename attribute (not shown) has been set to the path and filename for the XML data file:

@Function.AppPhysicalPath~\\_SupportFiles\PageFragment.html

The **Set Element Text** element's Xml Modifier ID attribute is set to the target node's ID and its value is set to the new text to be inserted or that will replace any existing text. Color highlighting shows the relationship between the data and the attribute values.

<p>Now is time for all good men to come to the aid of their country</p>  
<p ID="CopyrightMsg">Copyright (c) 2020 Good Works, Inc.</p>
  
After the task runs, we can look at the HTML file once again and see that the text has been changed, as shown above.
