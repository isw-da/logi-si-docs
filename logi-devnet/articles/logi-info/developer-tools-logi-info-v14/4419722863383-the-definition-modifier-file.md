---
title: "The Definition Modifier File"
id: 4419722863383
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722863383-The-Definition-Modifier-File
updated_at: 2022-07-17T02:24:35Z
---

# The Definition Modifier File

# The Definition Modifier File

Although the proper terminology for an XML object is "element",
the term "tag" will be used in the following discussion in order
to avoid confusion between Logi elements and XML elements.

A DMF is an XML file that contains special tags that temporarily customize
a report definition, in memory, just as the Logi Server Engine begins to
render it. This "virtual customization" does not alter the
report definition saved in the file system. These XML files can be edited
right in Studio's Workspace Panel. Here's an example of a DMF:

<DefinitionModifier>  
  
 <!-- 1. setting attributes based on existing
content -->  
 <SetAttribute
XPath="//DataTableColumn[@Header='Order ID']"
Header="Ordre" />  
 <SetAttribute
XPath="//DataTableColumn[@Header='Order Date']"
Header="Date d'Ordre" />  
 <SetAttribute
XPath="//DataTableColumn[@Header='Customer ID']"
Header="ID de Client" />  
 <SetAttribute
XPath="//DataTableColumn[@Header='Freight']"
Header="Fret" />  
  
 <!-- 2. adding additional elements into the report
-->  
 <AppendChildElement
XPath="/Report/ReportFooter">  
 <NewElement>  
 <Division
ID="divExports">  
 <LineBreak
LineCount="1" />  
 <Label
ID="lblExportExcel" Caption="Export Excel">  
 <Action
Type="NativeExcel" ID="exportExcel">  
 <Target
Type="NativeExcel" />  
 </Action>  
 </Label>  
 <Spaces
Size="3" />  
 <Label
ID="lblExportPDF" Caption="Export PDF">  
 <Action
Type="PDF" ID="exportPDF">  
 <Target
Type="PDF" />  
 </Action>  
 </Label>  
 <Spaces
Size="3" />  
 <Label
ID="lblExportWord" Caption="Export Word">  
 <Action
Type="NativeWord" ID="exportWord">  
 <Target
Type="NativeWord" />  
 </Action>  
 </Label>  
 </Division>  
 </NewElement>  
 </AppendChildElement>  
 </DefinitionModifier>

The example starts and ends with <DefinitionModifier> tags, but
they're not strictly required; any tags that properly open and close the
XML are acceptable.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Comments can be embedded into
the XML using the HTML <!-- ... --> comment syntax.

If a Security Right ID attribute is being set, the element is
re-evaluated after the operation for security purposes.

## XPath or Element ID Notation

In the first section of the example, a special
**<SetAttribute>** tag is used to find and replace the desired
text. **XPath notation** is used here to identify the element and
attribute values to be replaced. The result is that all of the English
text in the table column headers will be replaced with French text.

In Studio, you can find the XPath of an element in a report or template by right-clicking on the element and selecting **Copy XPath**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522800986263/copy_xpath1_442x435.png)

Selecting this option will copy the direct XPath of that element, the tag name, and ID attribute (if available) to the Clipboard, which can then be copied into a TMF.

See this site for more information about
[XPath syntax](https://www.w3schools.com/xml/xpath_intro.asp).

In the second section, the **<AppendChildElement>** tag is used
to insert elements and set their attributes. One of the beauties of this
tag is that you can list multiple elements beneath it as a group, rather
than having to use a tag per element, as you might expect.

Also in this section, to illustrate an alternative method, the actual Logi
**element ID** is used to identify the new elements and their
attributes, rather than XPath. Either method, XPath or Element ID
notation, can be used. The result of this second section is that a set of
Export links are added to report footer.

## List of Special XML Tags

This table provides a complete list of the special XML tags available for
use in DMFs:

| XML Tag | Description |
| --- | --- |
| AppendChildElement | Appends new child element as the *last* element beneath the element identified in its XML "ID" attribute. See section below about use of NewElement tag. |
| InsertAfterElement | Inserts new element *after* the element identified in its XML "ID" attribute. See section below about use of NewElement tag. |
| InsertBeforeElement | Inserts new element *before* the element identified in its XML "ID" attribute. See section below about use of NewElement tag. |
| PrependChildElement | Adds new child element as the *first* element beneath the element identified in its XML "ID" attribute. See section below about use of NewElement tag. |
| Remark | "Comments" the XML tag it encloses, so it has no effect. |
| RemoveElement | Removes the element identified in its XML "ID" attribute. |
| SetAttribute | Sets the attribute value identified for the element identified in its XML "ID" attribute, overwriting any value already there. |
| SetAttributeWhenEmpty | Sets the attribute value identified for the element identified in its XML "ID" attribute, but only if that attribute does not have a value already. |
| SetAttributeWithInsert | Inserts an additional attribute value *before* any existing value identified for the element identified in its XML "ID" attribute. This order is important, as it allows existing values related to CSS to "win" any conflicts by being last in the order. |
| UpdateOrAppendChildElement | If the child element does not exist, appends it as the *last* element beneath the element identified in its XML "ID" attribute. If the child element exists, updates its attributes. *See section below about use of NewElement tag.* |

  

If elements affected by these operations have their Security Right ID
attributes set, those attribute values will be evaluated *before* the
modification is executed. This allows security rights to control which
modifications are applied.
Additional examples of these tags in use can be found in
[Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files).

## Using the <NewElement> Tag

Tags that insert or add a new element use the <NewElement> child tag
set to enclose the element to be inserted:

<InsertAfterElement>  
 <NewElement>  
 <Division></Division>  
 </NewElement>  
 </InsertAfterElement>

You may only insert one element per <NewElement> tag set, as shown
above.

<InsertAfterElement>  
 <NewElement>  
 <Division></Division>  
<Division></Division> <--- will be
ignored  
 </NewElement>  
 </InsertAfterElement>

You may *not* insert multiple elements per <NewElement> tag, as
shown above.

Instead use multiple <InsertAfterElement> (or similar) tags,

<InsertAfterElement>  
 <NewElement>  
 <Division>  
 <Division></Division>  
 <Division></Division>  
 </Division>  
 </NewElement>  
 </InsertAfterElement>

or wrap the multiple elements in a single top-level container element, as
shown above.

## Using Tokens in the DMF

DMFs can provide dynamic customizations through the use of tokens.

![](https://devnet.logianalytics.com/hc/article_attachments/7522845356567/usingdmf_02.png)

First, the actual file name used in the Definition Modifier File attribute
can be a **token**. You could, for example, have a different DMF for
each language or culture and use the token that signifies the user's
browser Culture setting, as shown above, to select the correct file.

<SetAttribute
XPath="//DataTableColumn[@Header='Freight']"
Header="@Constant.myItalianWord~" />

Second, you can use tokens within the DMF file itself. For example, the
line above replaces the word "Freight" with the value of a
constant.
