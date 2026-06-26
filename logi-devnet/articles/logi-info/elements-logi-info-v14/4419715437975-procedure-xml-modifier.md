---
title: "Procedure.XML Modifier"
id: 4419715437975
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715437975-Procedure-XML-Modifier
updated_at: 2022-07-17T01:40:08Z
---

# Procedure.XML Modifier

# Procedure.XML Modifier

The **Procedure.XML Modifier** family of elements allows you to use a Process Task to modify an XML file at runtime.

The following topics discuss the elements and their usage:

* [Child Modifier Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707781015-Procedure-XML-Modifier-Child-Modifier-Elements#ChildMod)
* [Usage Example: Set Attribute](https://devnet.logianalytics.com/hc/en-us/articles/4419707786007-Procedure-XML-Modifier-Usage-Example-Set-Attribute#SetAttribute)
* [Usage Example: Append Child Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707782935-Procedure-XML-Modifier-Usage-Example-Append-Child-Element#AppendChildElement)
* [Usage Example: Prepend Child Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707784087-Procedure-XML-Modifier-Usage-Example-Prepend-Child-Element#PrependChildElement)
* [Usage Example: Set Element Text](https://devnet.logianalytics.com/hc/en-us/articles/4419707787031-Procedure-XML-Modifier-Usage-Example-Set-Element-Text#SetText)

## About Procedure.XML Modifier

This topic discusses a Logi Info feature that allows you to update an XML file from a Process Task. Basic information about using tasks is available in [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4419715442583-Process-Tasks).
The techniques and syntax used to do this are similar to those used with a [Definition Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419722864279-Definition-Modifier-Files) (DMF) and reading about them may be helpful. A DMF applies a separate file containing special coded directives to a report definition in order to modify it at runtime. Procedure.XML Modifier operates in a similar manner but the "directives" are created by adding special elements to the Process Task,
rather than coding them in a separate file.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The proper terminology for an XML object is "element", which may cause confusion between the Logi Info *visual**elements* in Logi Studio and XML document *elements*. We've attempted to clearly distinguish them in this topic, but please read carefully.
With Procedure.XML Modifier, XML elements and attributes in a file can be added, changed, or removed. "Target" elements can be identified by their ID attribute or by using XPath notation to locate them (learn more about [XPath syntax](https://www.w3schools.com/xml/xpath_intro.asp)).
What kinds of XML files can this procedure element be used to modify? DMFs can modify Logi Info report definitions, which are XML documents, and Procedure.XML Modifier can do so, too, but in a much more programmable fashion. Other XML files, including data files, can also be modified. For example, you might export data to a file using Procedure.Export XML and then want to modify the file in
some way based on subsequent task operations.
If you're inserting a new Logi Info element into a definition, you'll need to supply its XML source code. You can get that code by temporarily adding it to a definition, selecting it, configuring it, and copying it. Its XML source code (including that for any child elements) will be copied to your Clipboard and then you can paste it where needed. Don't forget to delete the element if it is indeed temporary.
Through the use of Logi Info features such as [Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715558423-Shared-Elements), Procedure.XML Modifier and its child elements can be reused and even parameterized, if desired.
