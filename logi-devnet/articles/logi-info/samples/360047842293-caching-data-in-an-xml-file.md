---
title: "Caching Data in an XML File"
id: 360047842293
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047842293-Caching-Data-in-an-XML-File
updated_at: 2022-02-07T21:55:04Z
---

# Caching Data in an XML File

## **Plugin Description**

This plug-in can be used to create a "cached" XML data file from any datalayer within a report. This is particularly useful if you're integrating with 3rd party tools that must read data from a file or if you need to cache the data across multiple reports, users, sessions, etc. This download includes the plug-in .dll, the VB.NET source code for it, and a demo report definition that illustrates how to use it. (.NET)

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Xml
Imports System.Web
Imports System.IO



Public Class LogiPlugin

    Public Sub CreateXMLDataFile(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim sFileName As String = rdObjects.PluginParameters("XmlFileName")
        Dim sFilePath As String = rdObjects.PluginParameters("XmlFilePath")
        Dim xmlDataFile As System.Xml.XmlDocument = rdObjects.CurrentData
        xmlDataFile.Save(sFilePath & sFileName)
    End Sub

End Class
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
