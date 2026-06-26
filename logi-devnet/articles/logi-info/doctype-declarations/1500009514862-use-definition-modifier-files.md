---
title: "Use Definition Modifier Files"
id: 1500009514862
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514862-Use-Definition-Modifier-Files
updated_at: 2021-06-17T01:58:17Z
---

# Use Definition Modifier Files

# Use Definition Modifier Files

**Definition Modifier Files** (DMFs) allow Logi Info developers to modify any of the elements and attributes in a report definition, based on conditional criteria, at runtime. These powerful files are discussed in this topic.

* About Definition Modifier Files
* [The Definition Modifier File Element](#Element)
* [The Definition Modifier File](#File)
* [XPath or Element ID Notation](#XPath_or_Element_ID_Notation)
* [List of Special XML Tags](#Tags)
* [Using Tokens in the DMF](#Using_Tokens_in_the_DMF)

## About Definition Modifier Files

A DMF is an XML file that contains instructions to modify a
definition file's elements and their attributes at runtime. It's a separate file that's processed *before* the Logi Server Engine starts to render a report definition. At that time, elements may be conditionally inserted or removed, and attributes may be set or unset.

This makes it possible to set culture- or
customer-specific values based, for example, on locale or security roles, at run-time. This means that each user can potentially receive a different report because the definition used to generate their report has been customized for them, on the fly.

DMFs are similar to **Template Modifier Files** (which only affect super-elements and themes) and they're also conceptually similar to a plug-in that executes on the "LoadDefinition" event. In this context, you might think of them as the "poor man's plug-in": they can provide similar functionality but don't require additional development tools (Visual Studio, etc.) to write and compile a plug-in .dll or .jar file.

Here are two examples of how DMFs might be used.

* Language Translation: you can use **XPath** notation in a DMF to find and replace specific strings of text anywhere in a report definition, in order to translate them into another language on the fly. You could even have a different DMF for each language supported and tokenize the DMF name in your report definition so that you can support multiple languages on the fly.

* Insert Additional Elements: you can use a DMF to add custom
  reporting content (headers, footers, and data) based, for example, on the user type, company,
  or other criteria.

## The Definition Modifier File Element

The presence of a **Definition Modifier File** element tells the Logi Server Engine to process the file it identifies.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771828631/usingdmf_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778671383/usingdmf_01a.png)

As shown above, the element is a child of the report definition's root element. Its **Definition Modifier File** attribute value is the name of the actual XML file. The file can be in any folder accessible to the Logi application but when a fully-qualified file path is not specified, the assumed location is the \_SupportFiles folder. Tokens can be used here to provide
the DMF filename, which allows you to specify different DMFs (or no DMF)
for different situations, users, etc.

## The Definition Modifier File

Although the proper terminology for an XML object is "element", the term "tag" will be used in the following discussion in order to avoid confusion between Logi elements and XML elements.

A DMF is an XML file that contains special tags that temporarily customize a report definition, in memory, just as the Logi Server Engine begins to render it. This "virtual customization" does not alter the report definition saved in the file system. These XML files can be edited right in Studio's Workspace Panel. Here's an example of a DMF:

|  |  |
| --- | --- |
|  | <DefinitionModifier>     <!-- 1. setting attributes based on existing content -->    <SetAttribute XPath="//DataTableColumn[@Header='Order ID']" Header="Ordre" />    <SetAttribute XPath="//DataTableColumn[@Header='Order Date']" Header="Date d'Ordre" />    <SetAttribute XPath="//DataTableColumn[@Header='Customer ID']" Header="ID de Client" />    <SetAttribute XPath="//DataTableColumn[@Header='Freight']" Header="Fret" />     <!-- 2. adding additional elements into the report -->     <AppendChildElement XPath="/Report/ReportFooter">         <NewElement>             <Division ID="divExports">                  <LineBreak LineCount="1" />                 <Label ID="lblExportExcel" Caption="Export Excel">                     <Action Type="NativeExcel" ID="exportExcel">                         <Target Type="NativeExcel" />                     </Action>                 </Label>                 <Spaces Size="3" />                 <Label ID="lblExportPDF" Caption="Export PDF">                     <Action Type="PDF" ID="exportPDF">                         <Target Type="PDF" />                     </Action>                 </Label>                 <Spaces Size="3" />                 <Label ID="lblExportWord" Caption="Export Word">                     <Action Type="NativeWord" ID="exportWord">                         <Target Type="NativeWord" />                     </Action>                 </Label>             </Division>         </NewElement>     </AppendChildElement>  </DefinitionModifier> |

The example starts and ends with <DefinitionModifier> tags, but they're not strictly required; any tags that properly open and close the XML are acceptable. Also note that **comments** can be embedded into the XML using the HTML <!-- ... --> comment syntax.

## XPath or Element ID Notation

In the first section of the example, a special **<SetAttribute>** tag is used to find and replace the desired text. **XPath notation** is used here to identify the element and attribute values to be replaced. The result is that all of the English text in the table column headers will be replaced with French text.

See this site for more information about [XPath syntax](https://www.w3schools.com/xml/xpath_syntax.asp).

In the second section, the **<AppendChildElement>** tag is used to insert elements and set their attributes. One of the beauties of this tag is that you can list multiple elements beneath it as a group, rather than having to use a tag per element, as you might expect.

Also in this section, to illustrate an alternative method, the actual Logi **element ID** is used to identify the new elements and their attributes, rather than XPath. Either method, XPath or Element ID notation, can be used. The result of this second section is that a set of Export links are added to report footer.

## List of Special XML Tags

This table provides a complete list of the special XML tags available for use in DMFs:

| XML Tag | Description | In Release |
| --- | --- | --- |
| AppendChildElement | Appends new child element as the *last* element beneath the element identified in its XML "ID" attribute. | 10.0 |
| InsertAfterElement | Inserts new element *after* the element identified in its XML "ID" attribute. | 10.0 |
| InsertBeforeElement | Inserts new element *before* the element identified in its XML "ID" attribute. | 10.0 |
| PrependChildElement | Adds new child element as the *first* element beneath the element identified in its XML "ID" attribute. | 10.0 |
| Remark | "Comments" the XML tag it encloses, so it has no effect. | 10.0 |
| RemoveElement | Removes the element identified in its XML "ID" attribute. | 10.0 |
| SetAttribute | Sets the attribute value identified for the element identified in its XML "ID" attribute, overwriting any value already there. | 10.0 |
| SetAttributeWhenEmpty | Sets the attribute value identified for the element identified in its XML "ID" attribute, but only if that attribute does not have a value already. | 10.0 |
| SetAttributeWithInsert | Inserts an additional attribute value *before* any existing value identified for the element identified in its XML "ID" attribute. This order is important, as it allows existing values related to CSS to "win" any conflicts by being last in the order. | 10.0 |
| UpdateOrAppendChildElement | If the child element does not exist, appends it as the *last* element beneath the element identified in its XML "ID" attribute. If the child element exists, updates its attributes. | 10.0 |

Additional examples of these tags in use can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009531981-Template-Modifier-Files).

## Using Tokens in the DMF

DMFs can provide dynamic customizations through the use of tokens.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771828887/usingdmf_02.png)

First, the actual file name used in the Definition Modifier File attribute can be a **token**. You could, for example, have a different DMF for each language or culture and use the token that signifies the user's browser Culture setting, as shown above, to select the correct file. *(Note: the tokenized DMF file name will not be available until the end-of-May 2010 release.)*

   <SetAttribute XPath="//DataTableColumn[@Header='Freight']" Header="@Constant.myItalianWord~" />

Second, you can use tokens within the DMF file itself. For example, the line above replaces the word "Freight" with the value of a constant.
