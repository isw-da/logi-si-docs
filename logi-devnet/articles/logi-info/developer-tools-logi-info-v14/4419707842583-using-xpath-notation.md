---
title: "Using XPath Notation"
id: 4419707842583
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707842583-Using-XPath-Notation
updated_at: 2022-07-17T02:23:27Z
---

# Using XPath Notation

# Using XPath Notation

The TMF examples shown so far have used element **IDs** to identify elements whose attributes are to be changed. However, XPath notation can be used instead, if preferred.

<TemplateModifier>  
 <SetAttribute XPath="//Label[@ID='lblFilterDescription']" Caption="Filtrer par les valeurs des cellules." />  
 </TemplateModifier>

The example shown above uses an earlier TMF example with XPath notation, instead of an element ID. XPath can be very useful when you want to identify multiple elements with similar names or types.

In Studio, you can find the XPath of an element in a report or template by right-clicking on the element and selecting **Copy XPath**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522803649303/copy_xpath.png)

Selecting this option will copy the direct XPath of that element, the tag name, and ID attribute (if available) to the Clipboard, which can then be copied into a TMF.

See this external site for more information about [XPath syntax](https://www.w3schools.com/xml/xpath_intro.asp).
