---
title: "Connection String From External File"
id: 360047151234
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047151234-Connection-String-From-External-File
updated_at: 2022-02-07T21:56:06Z
---

# Connection String From External File

## Plugin Description

This plug-in sets a Connection element's Connection String attribute dynamically, using data from a text file. It was created to provide a specific security behavior requested by a customer: the ability to manage datasource connections without modifying the \_settings file directly. The download includes the plug-in .dll, the VB.NET source code for it, an example \_settings.lgx file showing how the plug-in is called, and an example text file (context.txt) which contains the connection string. (.NET)

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## View Code Snippet

```
Imports System.Xml
Imports System.Web
Imports System.IO



Public Class LogiPlugin

    Public Sub setConnectionString(ByRef rdObjects As rdPlugin.rdServerObjects)
        'get the variables
        Dim sConnID As String = rdObjects.PluginParameters("ConnID")
        Dim sFilePath As String = rdObjects.PluginParameters("ConnFilePath")
        'load in XML _settings file
        Dim xmlSettings As New XmlDocument()
        xmlSettings.LoadXml(rdObjects.CurrentDefinition)
        'locate your connection element from it's ID (this is passed in from the variable)
        Dim eleConn As XmlElement = xmlSettings.SelectSingleNode("//*[@ID='" & sConnID & "']")
        'read the connection string from a text file on the system
        Dim sConnection As String = GetFileContents(sFilePath)
        eleConn.SetAttribute("ConnectionString", sConnection)
        rdObjects.CurrentDefinition = xmlSettings.OuterXml
    End Sub


    Public Function GetFileContents(ByVal FullPath As String, _
       Optional ByRef ErrInfo As String = "") As String

        Dim strContents As String
        Dim objReader As StreamReader
        Try

            objReader = New StreamReader(FullPath)
            strContents = objReader.ReadToEnd()
            objReader.Close()
            Return strContents
        Catch Ex As Exception
            Return ErrInfo = Ex.Message
        End Try
    End Function

End Class
```

## Further Reading

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
