---
title: ".NET Plug-in - Example: Changing Data in a Datalayer"
id: 4406817213463
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817213463--NET-Plug-in-Example-Changing-Data-in-a-Datalayer
updated_at: 2022-04-06T06:04:39Z
---

# .NET Plug-in - Example: Changing Data in a Datalayer

# .NET Plug-in - Example: Changing Data in a Datalayer

The following are code examples for a plug-in that converts RTF text in a datalayer to plain text. It creates an in-memory RichTextBox control, then iterates through all records in the datalayer, processing and replacing the contents of a data column.

[Visual Basic]  
 Imports System.Xml.Linq  
Imports System.Windows.Forms.RichTextBox  
  
 Public Class Plugin  
  
 Public Sub RTF2Text(ByRef rdObjects As rdPlugin.rdServerObjects)  
Dim objRTB As New System.Windows.Forms.RichTextBox()  
Dim objDoc As New XmlDocument()  
Dim objNodeList As XmlNodeList  
Dim objNode As XmlNode' load the XML from the datalayer  
objDoc = rdObjects.CurrentData  
  
' get a nodelist for all nodes (records) in XML doc  
' in XPath syntax "dtTest" equals the name of the data table,   
 ' and is the node name in the XML document  
objNodeList = objDoc.SelectNodes("//dtTest")' loop thru each node, processing the "colText" attribute value,   
 ' which is name of column with RTF text.  
' put each value into RichTextBox as RTF, then reassign it as plain text  
For Each objNode In objNodeList  
 objRTB.Rtf = objNode.Attributes.ItemOf("colText").Value  
objNode.Attributes.ItemOf("colText").Value = objRTB.Text  
Next' clean up  
objNode = Nothing  
objNodeList = Nothing  
objDoc = Nothing  
objRTB = Nothing End Sub  
  
 End Class  
 [C#}  
using System;  
 using System.Xml.Linq;  
 using rdPlugin;  
using System.Windows.Forms;  
  
 namespace RTFPlugin  
 {  
 public class Plugin  
 {  
public void RTF2Text(ref rdServerObjects rdObjects)  
{  
RichTextBox objRTB;  
XmlDocument objDoc;  
XmlNodeList objNodeList;  
// create RichTextBox  
objRTB = new RichTextBox();// load the XML from the datalayer  
objDoc = new XmlDocument();  
objDoc = rdObjects.CurrentData;// get a nodelist for all nodes (records) in XML doc  
// in XPath syntax "dtTest" equals the name of the data table,   
// and is the node name in the XML document  
objNodeList = objDoc.SelectNodes("//dtTest");// loop thru each node, processing the "colText" attribute value,   
// which is name of column with RTF text.  
// put each value into RichTextBox as RTF, then reassign it as plain text  
foreach (XmlNode objNode in objNodeList)  
 {  
objRTB.Rtf = objNode.Attributes.GetNamedItem("colText").Value;  
objNode.Attributes.GetNamedItem("colText").Value = objRTB.Text;  
}  
}  
 }  
 }
