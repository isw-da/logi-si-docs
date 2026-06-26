---
title: "Procedure.XML Modifier - Child Modifier Elements"
id: 4406817788311
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817788311-Procedure-XML-Modifier-Child-Modifier-Elements
updated_at: 2022-04-06T06:08:13Z
---

# Procedure.XML Modifier - Child Modifier Elements

# Procedure.XML Modifier - Child Modifier Elements

Procedure.XML Modifier uses a number of child elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563120663/xmlmod_01.png)

All of the elements are shown above and they're described in the following table:

| Element | Description |
| --- | --- |
| Procedure.XML Modifier | (Required) The parent element for all other related elements. Specifies the fully-qualified path and file name, with extension, of the XML file to be modified. The application must have Full Control or equivalent file access permissions to file. The @Function.AppPhysicalPath~ token can be used here. |
| Append Child Element | Specifies a target XML element by ID or XPath. Appends a new child XML element as the *last* child of the target element. |
| * Cut Element | Specifies a target XML element by ID or XPath. Used with any Logi element that appends or inserts a new child XML element, this element deletes the target element first, *before* the append or insert, then makes it available for insertion. This is used primarily to "move" an XML element from one place to another in the file, an operation similar to "Cut and Paste"in a file system. For more information, see [this usage example](#PrependChildElement). |
| * New Element | Used with any Logi element that appends or inserts a new child XML element, this is the "container" for the XML source code that you want to insert. Use Logi Studio's Source tab to directly edit this element, adding the source code for the XML element(s) to be inserted. Not needed when Cut Element is used. For more information, see [this usage example](#AppendChildElement). |
| Insert After Element | Specifies a target XML element by ID or XPath and inserts a new XML element *after* the target element. |
| Insert Before Element | Specifies a target XML element by ID or XPath and inserts a new XML element *before* the target element. |
| Prepend Child Element | Specifies a target XML element by ID or XPath and adds new child XML element as the *first* element beneath the target element. |
| Remove Attribute | Specifies a target XML element by ID or XPath and removes the XML attribute specified by name (required) in the target element. |
| Remove Element | Specifies a target XML element by ID or XPath and removes it. |
| Rename Attribute | Specifies a target XML element by ID or XPath and renames its specified XML attribute with the specified new name. |
| Set Attribute | Specifies a target XML element by ID or XPath and replaces its specified XML attribute with the specified value. If the attribute doesn't exist, it's created and set to the value. |
| Set Element Text | Specifies a target XML element by ID or XPath and specifies its Inner Text value. |
| Update or Append Child Element | Specifies a target XML element by ID or XPath. If the specified child XML element *doesn*'t exist, it's appended as the *last* element beneath the target element. If the child element *does* exist, the specified attribute values replace the existing values. |
