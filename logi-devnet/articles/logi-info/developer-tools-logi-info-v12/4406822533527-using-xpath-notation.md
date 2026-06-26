---
title: "Using XPath Notation"
id: 4406822533527
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822533527-Using-XPath-Notation
updated_at: 2022-04-06T06:08:49Z
---

# Using XPath Notation

# Using XPath Notation

The TMF examples shown so far have used element **IDs** to identify elements whose attributes are to be changed. However, XPath notation can be used instead, if preferred.

<TemplateModifier>  
 <SetAttribute XPath="//Label[@ID='lblFilterDescription']" Caption="Filtrer par les valeurs des cellules." />  
 </TemplateModifier>

The example shown above uses an earlier TMF example with XPath notation, instead of an element ID. XPath can be very useful when you want to identify multiple elements with similar names or types.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) In Studio, you can find the XPath of an element in a report or template by right-clicking on the element and selecting **Copy XPath**:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563085207/copy_xpath1_442x435.png)

Selecting this option will copy the direct XPath of that element, the tag name, and ID attribute (if available) to the Clipboard, which can then be copied into a TMF.

See this external site for more information about [XPath syntax](https://www.w3schools.com/xml/xpath_intro.asp).
