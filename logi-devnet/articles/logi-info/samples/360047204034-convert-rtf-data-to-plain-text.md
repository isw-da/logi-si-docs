---
title: "Convert RTF Data to Plain Text"
id: 360047204034
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047204034-Convert-RTF-Data-to-Plain-Text
updated_at: 2022-02-07T21:53:58Z
---

# Convert RTF Data to Plain Text

## **Plugin Description**

This plug-in converts Rich Text Formatted text, in data retrieved into a datalayer, into plain text. The RTF text in a datalayer column is replaced with plain text, in the same column. This is achieved by creating an in-memory instance of a RichTextBox control and passing the data through it, and this sample uses Windows components to do that. Developers working on non-Windows platforms will need to find a Java component with similar functionality.

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Xml
Imports System.Windows.Forms.RichTextBox


Public Class Plugin

    Public Sub RTF2Text(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim objRTB As New System.Windows.Forms.RichTextBox()
        Dim objDoc As New XmlDocument()
        Dim objNodeList As XmlNodeList
        Dim objNode As XmlNode

        ' load the XML from the datalayer
        objDoc = rdObjects.CurrentData

        ' get a nodelist for all nodes (records) in XML doc
        ' in XPath syntax "dtTest" equals the name of the data table, and is the node name in the XML document
        objNodeList = objDoc.SelectNodes("//dtTest")

        ' loop thru each node, processing the "colText" attribute value, which is name of column with RTF text
        ' put each value into RichTextBox as RTF, then reassign it as plain text
        For Each objNode In objNodeList
            objRTB.Rtf = objNode.Attributes.ItemOf("colText").Value
            objNode.Attributes.ItemOf("colText").Value = objRTB.Text
        Next

        ' clean up
        objNode = Nothing
        objNodeList = Nothing
        objDoc = Nothing
        objRTB = Nothing

    End Sub

End Class
```

## 

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
