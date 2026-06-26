---
title: "Replace Characters in String (.NET)"
id: 360047205454
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047205454-Replace-Characters-in-String-NET
updated_at: 2022-02-07T21:50:57Z
---

# Replace Characters in String (.NET)

## **Plugin Description**

This .NET plug-in is designed to provide a generic means to modify/replace sections of the resultant HTML using regular expressions and the FinishHTML event.

It was created to enable to the modification of Google Maps calls to support v3 of the Google Maps API in the current release of the Logi Info engine. However, its generic implementation will allow any string to be replaced within the resultant HTML. The download includes the .dll, VB source code, and an example report definition.

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Text.RegularExpressions

Public Class Plugin

    Public Sub StrReplace(ByRef rdObjects As rdPlugin.rdServerObjects)
        'Get Plugin Parameters for Regex
        Dim currText As String = rdObjects.PluginParameters("current")
        Dim replaceText As String = rdObjects.PluginParameters("replace")

        'Get the HTML (run from FinishHTML event)
        Dim sHtml As String = rdObjects.ResponseHtml
        Dim sRepHtml As String

        Try
            'Use RegEx to replace the text
            sRepHtml = Regex.Replace(sHtml, currText, replaceText, RegexOptions.IgnoreCase)
        Catch
            'Don't throw an error, just respond with the original HTML.
            sRepHtml = rdObjects.ResponseHtml
        End Try

        'Set the new HTML to the Response.
        rdObjects.ResponseHtml = sRepHtml

    End Sub

End Class
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
