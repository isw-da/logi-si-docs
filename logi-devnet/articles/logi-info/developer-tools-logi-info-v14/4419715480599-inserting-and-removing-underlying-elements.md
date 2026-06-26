---
title: "Inserting and Removing Underlying Elements"
id: 4419715480599
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715480599-Inserting-and-Removing-Underlying-Elements
updated_at: 2022-07-17T02:23:28Z
---

# Inserting and Removing Underlying Elements

# Inserting and Removing Underlying Elements

You can also use TMFs to insert, remove, and remark the internal elements that make up a super-element. This is accomplished using these XML tags:

* <PrependChildElement>
* <AppendChildElement >
* <InsertBeforeElement >
* <InsertAfterElement >
* <Remark >
* <RemoveElement >

The first four tags use a child tag, <NewElement>, to delimit the new element to be affected. The <Prepend- and <Append- tags make the new element the first or last child element in a group. See the section below about using the <NewElement> tag.

TMFs can insert [Definition Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419722864279-Definition-Modifier-Files).

If elements affected by these operations have their Security Right ID attributes set, those attribute values will be evaluated *before* the modification is executed. This allows security rights to control which modifications are applied.

Here's a practical example of some of these elements in action:

![](https://devnet.logianalytics.com/hc/article_attachments/7522757728919/usingtmf_06.png)

An Analysis Grid can display three **Export** buttons, as shown above, and its **Hide Exports** attribute can be used to hide all three of them from users. However, if you use the attribute to hide the buttons, it's an "All-or-None" situation: developers can't choose to show a subset of the export buttons.
A solution for those who wish to show a subset is to use a TMF. In the following example, we'll remove the **CSV** export button and add a **Print** button that mimics the PDF export functionality.
One important thing to know when looking at the Analysis Grid's definition file to get the appropriate element IDs is that the export "buttons" are really **Label** elements made to look like buttons using CSS.
Assuming the elements have been found and identified, the TMF can be written as follows:

<TemplateModifier>  
<RemoveElement ID="lblExportCsv" />  
<InsertAfterElement ID="lblExportPdf">  
<NewElement>  
<Label Caption="Print" ID="lblPrintBtn" Class="rdAgCommand" />  
</NewElement>  
</InsertAfterElement>  
<AppendChildElement ID="lblPrintBtn">  
<NewElement>  
<Action Type="PDF" ID="actExportPrint" />  
</NewElement>  
</AppendChildElement>  
<AppendChildElement ID="actExportPrint">  
<NewElement>  
<Target Type="PDF" Report="CurrentReport" ID="tgtExportPrint"/>  
</NewElement>  
</AppendChildElement>  
<InsertAfterElement ID="tgtExportPrint">  
<NewElement>  
<LinkParams rdAgNoDefCache="True" rdExportTableID="dtAnalysisGrid"/>  
</NewElement>  
</InsertAfterElement>  
</TemplateModifier>

The first thing this TMF does is remove the CSV button ("lblExportCsv") using the <RemoveElement> tag.

Then three elements are appended, using the <InsertAfterElement> and <AppendChildElement> tags, creating the new Print button, its child **Action** element, and that element's child **Target** element. Where they are appended is specified in the tag's ID attribute. Note the use of the <NewElement>
tag to delimit each element being added.

Finally, <InsertAfterElement> is used to add a LinkParams element at the same element hierarchy level as the Target element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522757741335/usingtmf_07.png)

The resulting interface change is shown above.
![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) It's possible to write the first part of the TMF in a more compact way, taking advantage of tag nesting:

<TemplateModifier>  
<RemoveElement ID="lblExportCsv" />  
  
<InsertAfterElement ID="lblExportPdf">  
<NewElement>  
<Label Caption="Print" ID="lblPrintBtn" Class="rdAgCommand">  
 <Action Type="PDF" ID="actExportPrint" >  
 <Target Type="PDF" Report="CurrentReport" ID="tgtExportPrint"/>  
 </Action>  
</Label>  
</NewElement>  
</InsertAfterElement>  
</TemplateModifier>

As shown above, only one <InsertAfterElement> tag is necessary, as long as the opening and closing tags for the nested elements are arranged correctly.

<TemplateModifier>  
<Remark>  
<RemoveElement ID="lblExportCsv" />  
</Remark>  
  
<InsertAfterElement ID="lblExportPdf">  
<NewElement>  
<Label Caption="Print" ID="lblPrintBtn" Class="rdAgCommand">  
 <Action Type="PDF" ID="actExportPrint" >  
 <Target Type="PDF" Report="CurrentReport" ID="tgtExportPrint"/>  
 </Action>  
</Label>  
</NewElement>  
</InsertAfterElement>  
  
<InsertAfterElement ID="tgtExportPrint">  
<NewElement>  
<LinkParams rdAgNoDefCache="True" rdExportTableID="dtAnalysisGrid"/>  
</NewElement>  
</InsertAfterElement>  
</TemplateModifier>

And, in the last variation, shown above, rather than removing tags, the <Remark> tag allows you to temporarily "comment out" portions of the TMFs, as shown above.

## Using the <NewElement> Tag

Tags that insert or add a new element use the <NewElement> child tag set to enclose the element to be inserted:

<InsertAfterElement>  
 <NewElement>  
<Division></Division>  
</NewElement>  
</InsertAfterElement>

You may only insert one element per <NewElement> tag set, as shown above.

<InsertAfterElement>  
 <NewElement>  
<Division></Division>  
<Division></Division> <--- will be ignored  
</NewElement>  
</InsertAfterElement>

You may *not* insert multiple elements per <NewElement> tag, as shown above.  
Instead use multiple <InsertAfterElement> (or similar) tags,

<InsertAfterElement>  
 <NewElement>  
<Division>  
<Division></Division>  
<Division></Division>  
</Division>  
</NewElement>  
</InsertAfterElement>

or wrap the multiple elements in a single top-level container element, as shown above.
