---
title: "Web Service with Complex Header"
id: 360047205234
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047205234-Web-Service-with-Complex-Header
updated_at: 2022-02-07T21:52:26Z
---

# Web Service with Complex Header

## **Plugin Description**

This plug-in allows demonstrates how, using the .NET framework, to work with a web service that requires a complex header as well as a method call. The download includes the complete VB.NET projects for the plug-in and a test web service, and a sample report definition.

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
' Complex Web Service extra code has been added at the very end of this


'How to write a Plugin:
'-------------------------
'First, examine this sample plugin DLL, and the lgxReportDev Sample Plugin application.
'Include rdPlugin.dll in the references.
'Routines called by lgxReportDev must have a single parameter; rdPlugin.rdServerObjects.
'Return information back to lgxReportDev by changing values in rdServerObjects,
'  such as the CurrentDefinition, or Session variables.

'How to deploy a Plugin:
'-------------------------
'The output DLLs go into _Plugins folder next to bin in the ReportDev project.

'How to debug a Plugin:
'-------------------------
'Right-click the project name from the Solution Explorer and choose Properties. 
'Click Common Properties > References Path. 
'Ensure that the path points to the bin folder of the LGX application using the plug-in. 
'Click Configuration Properties > Build. 
'Ensure that the Output Path points to the _Plugins folder of the LGX application using the plug-in. 
'Click Configuration Properties > Debugging. 
'Select the "Startup URL" option. 
'Set the Start URL.  It is the URL used to access the LGX application, like "http://localhost/myweb/rdPage.aspx?rdReport=myReport".
'Check "ASP.NET Debugging".
'Click Apply to save the changes, then click OK. 
'In the web folder's web.config file, set debug=true, like:
'		<compilation defaultLanguage="vb" debug="true" />
'When compiling, you may see this error: "Could not copy temporary files to the output directory."
'Either restart the ASP.NET process or the IIS server.  (The iisreset.exe command is convenient for this purpose.)

'

Imports System.Xml
Imports System.Web.Services
Imports System.Web.Services.Protocols

Public Class Plugin

    ''''''''''''''''''''''''''''''''''''''
    Public Sub SetApplicationCaption(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim xmlSettings As New XmlDocument()
        xmlSettings.LoadXml(rdObjects.CurrentDefinition)
        Dim eleApp As XmlElement = xmlSettings.SelectSingleNode("//Setting/Application")
        eleApp.SetAttribute("Caption", "Greetings from the Sample Plugin!  Time: " & Now.ToString)
        rdObjects.CurrentDefinition = xmlSettings.OuterXml
    End Sub

    ''''''''''''''''''''''''''''''''''''''
    Public Sub SetCustomerQuery(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim xmlDefinition As New XmlDocument()
        xmlDefinition.LoadXml(rdObjects.CurrentDefinition)
        Dim eleDataLayer As XmlElement = xmlDefinition.SelectSingleNode("//Report/Body/DataTable/DataLayer")
        If IsNothing(eleDataLayer) Then
            Throw New Exception("The report is missing the DataLayer element.")
        End If

        'Use a Request variable to set set the SELECT query.
        Dim sSelect As String
        Select Case rdObjects.Request("Continent")
            Case "NA"
                sSelect = "SELECT * FROM Customers WHERE Country IN('USA','Mexico','Canada')"
            Case "SA"
                sSelect = "SELECT * FROM Customers WHERE Country IN('Argentina','Brazil','Venezuela')"
            Case "EU"
                sSelect = "SELECT * FROM Customers WHERE Country IN('UK','Sweden','France','Spain','Switzerland','Austria','Portugal','Ireland','Belgium','Germany','Finland','Poland','Denmark')"
            Case Else
                sSelect = "SELECT * FROM Customers"
        End Select

        eleDataLayer.SetAttribute("Source", sSelect)
        rdObjects.CurrentDefinition = xmlDefinition.OuterXml
    End Sub

    ''''''''''''''''''''''''''''''''''''''
    Public Sub GetProducts(ByRef rdObjects As rdPlugin.rdServerObjects)
        'This has been updated to use either the XMLDocument or XML Filename to pass data.
        Dim xmlData As System.Xml.XmlDocument = Nothing
        Dim sReturnFile As String = Nothing
        If (rdObjects.CurrentData IsNot Nothing) Then
            xmlData = rdObjects.CurrentData
        ElseIf (rdObjects.CurrentDataFile IsNot Nothing) AndAlso (IO.File.Exists(rdObjects.CurrentDataFile)) Then
            xmlData = New XmlDocument()
            xmlData.Load(rdObjects.CurrentDataFile)
            sReturnFile = rdObjects.ReturnedDataFile
        Else
            Throw New Exception("No XML data was passed to the GetProducts plugin method.")
        End If

        Dim sDataLayerParentID As String = rdObjects.PluginParameters("DataLayerParentID")
        Dim eleRow As XmlElement

        eleRow = xmlData.DocumentElement.AppendChild(xmlData.CreateElement(sDataLayerParentID))
        eleRow.SetAttribute("ProductName", "Milk")

        eleRow = xmlData.DocumentElement.AppendChild(xmlData.CreateElement(sDataLayerParentID))
        eleRow.SetAttribute("ProductName", "Bread")

        eleRow = xmlData.DocumentElement.AppendChild(xmlData.CreateElement(sDataLayerParentID))
        eleRow.SetAttribute("ProductName", "Beer")

        If (sReturnFile IsNot Nothing) Then
            'If we got the data by filename, we need to return the updated file.
            xmlData.Save(sReturnFile)
        End If

    End Sub


    ''''''''''''''''''''''''''''''''''''''
    Public Sub AddPriceColumn(ByRef rdObjects As rdPlugin.rdServerObjects)
        'This has been updated to use either the XMLDocument or XML Filename to pass data.
        Dim xmlData As System.Xml.XmlDocument = Nothing
        Dim sReturnFile As String = Nothing
        If (rdObjects.CurrentData IsNot Nothing) Then
            xmlData = rdObjects.CurrentData
        ElseIf (rdObjects.CurrentDataFile IsNot Nothing) AndAlso (IO.File.Exists(rdObjects.CurrentDataFile)) Then
            xmlData = New XmlDocument()
            xmlData.Load(rdObjects.CurrentDataFile)
            sReturnFile = rdObjects.ReturnedDataFile
        Else
            Throw New Exception("No XML data was passed to the AddPriceColumn plugin method.")
        End If

        Dim sColumnName As String = rdObjects.PluginParameters("PriceColumnName")
        Dim eleRow As XmlElement
        For Each eleRow In xmlData.SelectNodes("/rdData/*")
            Select Case eleRow.GetAttribute("ProductName")
                Case "Milk"
                    eleRow.SetAttribute(sColumnName, "3.25")
                Case "Bread"
                    eleRow.SetAttribute(sColumnName, "3.75")
                Case "Beer"
                    eleRow.SetAttribute(sColumnName, "4.50")
            End Select
        Next

        If (sReturnFile IsNot Nothing) Then
            'If we got the data by filename, we need to return the updated file.
            xmlData.Save(sReturnFile)
        End If

    End Sub

    ''''''''''''''''''''''''''''''''''''''
    Public Sub SetDataTableColumns(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim sDataTableID As String = rdObjects.PluginParameters("DataTableID")
        Dim xmlDefinition As New XmlDocument()
        xmlDefinition.LoadXml(rdObjects.CurrentDefinition)
        Dim eleDataTable As XmlElement = xmlDefinition.SelectSingleNode("//*[@ID='" & sDataTableID & "']")

        'This has been updated to use either the XMLDocument or XML Filename to pass data.
        Dim xmlData As System.Xml.XmlDocument = Nothing
        Dim sReturnFile As String = Nothing
        If (rdObjects.CurrentData IsNot Nothing) Then
            xmlData = rdObjects.CurrentData
        ElseIf (rdObjects.CurrentDataFile IsNot Nothing) AndAlso (IO.File.Exists(rdObjects.CurrentDataFile)) Then
            xmlData = New XmlDocument()
            xmlData.Load(rdObjects.CurrentDataFile)
            sReturnFile = rdObjects.ReturnedDataFile
        Else
            Throw New Exception("No XML data was passed to the SetDataTableColumns plugin method.")
        End If
        Dim eleFirstRow As XmlElement = xmlData.SelectSingleNode("/rdData/*")
        If Not IsNothing(eleFirstRow) Then
            Dim atr As XmlAttribute
            For Each atr In eleFirstRow.Attributes
                'Create a new DataTableColumn element under the DataTable.
                Dim eleDataTableColumn As XmlElement = eleDataTable.AppendChild(xmlDefinition.CreateElement("DataTableColumn"))
                eleDataTableColumn.SetAttribute("ID", "col" & atr.Name)
                eleDataTableColumn.SetAttribute("Header", atr.Name)
                'Create the Label element
                Dim eleLabel As XmlElement = eleDataTableColumn.AppendChild(xmlDefinition.CreateElement("Label"))
                eleLabel.SetAttribute("ID", "lbl" & atr.Name)
                eleLabel.SetAttribute("Caption", "@Data." & atr.Name & "~")
            Next
        End If
        If (sReturnFile IsNot Nothing) Then
            'If we got the data by filename, we need to return the updated file.
            xmlData.Save(sReturnFile)
        End If

        rdObjects.CurrentDefinition = xmlDefinition.OuterXml
    End Sub

    ''''''''''''''''''''''''''''''''''''''
    Public Sub subHighlightText(ByRef rdObjects As rdPlugin.rdServerObjects)
        With rdObjects
            Dim sElementID As String = .PluginParameters("ElementID")
            Dim sFindInputName As String = .PluginParameters("FindInputName")
            Dim sStyle As String = .PluginParameters("Style")
            Dim sFindValue As String = .Request.Form(sFindInputName)
            If IsNothing(sFindValue) Then sFindValue = .Request(sFindInputName)
            If Not IsNothing(sFindValue) AndAlso sFindValue.Length <> 0 Then

                'Load the ResponsesHtml string into an XmlDocument object.
                Dim xmlHtml As New XmlDocument()
                xmlHtml.LoadXml(.ResponseHtml)
                'Find all SPAN elements under the element with the specified ElementID.
                Dim nlSpans As XmlNodeList = xmlHtml.SelectNodes("//*[@id='" & sElementID & "']//SPAN")
                Dim eleSpanText As XmlElement
                For Each eleSpanText In nlSpans
                    'Split the SPAN into 3 SPANs to highlight the first match.
                    Call subSplitHighlightSpan(xmlHtml, eleSpanText, sFindValue, sStyle)
                Next

                .ResponseHtml = xmlHtml.OuterXml
            End If
        End With
    End Sub
    Private Sub subSplitHighlightSpan(ByVal xmlHtml As XmlDocument, ByVal eleSpanText As XmlElement, ByVal sFindValue As String, ByVal sStyle As String)
        Dim nFindLocation As Integer = eleSpanText.InnerText.ToLower.IndexOf(sFindValue.ToLower)
        If nFindLocation <> -1 Then
            'The search string was found.  Break the SPAN into 3 SPANs.
            Dim sOriginal As String = eleSpanText.InnerText
            'Set the first SPAN element.
            eleSpanText.InnerText = sOriginal.Substring(0, nFindLocation)
            'Make the highlighted SPAN element.
            Dim eleNewSpan As XmlElement = eleSpanText.ParentNode.InsertAfter(xmlHtml.CreateElement("SPAN"), eleSpanText)
            eleNewSpan.SetAttribute("style", sStyle)
            eleNewSpan.InnerText = sOriginal.Substring(nFindLocation, sFindValue.Length)
            'Make the final SPAN element.
            eleNewSpan = eleSpanText.ParentNode.InsertAfter(xmlHtml.CreateElement("SPAN"), eleNewSpan)
            eleNewSpan.InnerText = sOriginal.Substring(nFindLocation + sFindValue.Length)
            'Recursively call again with this last SPAN.  There may be more matches.
            Call subSplitHighlightSpan(xmlHtml, eleNewSpan, sFindValue, sStyle)
        End If
    End Sub

    ''''''''''''''''''''''''''''''''''''''
    Public Function GetVirtualMemorySize(ByRef rdObjects As rdPlugin.rdServerObjects) As String
        Dim p As System.Diagnostics.Process = Diagnostics.Process.GetCurrentProcess
        Return p.VirtualMemorySize64
    End Function

    ''''''''''''''''''''''''''''''''''''''
    Public Sub CallComScripting(ByRef rdObjects As rdPlugin.rdServerObjects)
        'This sample demonstrates one way to call a COM object.
        Dim scr As Object = CreateObject("MSScriptControl.ScriptControl")
        scr.Language = "VBScript"
        Dim x As String = scr.Eval("1 + 2")
        scr = Nothing
    End Sub


    ''''''' extra code added here '''''''''''''''''''''''''''''''


    Public Sub GetWSData(ByRef rdObjects As rdPlugin.rdServerObjects)

        Dim xmlData As System.Xml.XmlDocument = rdObjects.CurrentData
        Dim eleRow As XmlElement

        Dim soapRequest As localhost.BasicService = New localhost.BasicService()
        Dim soapHeader As localhost.MyHeader = New localhost.MyHeader()

        soapHeader.UserName = "Bob"
        soapHeader.Password = "xxxxxxx"

        ' Add the MyHeader SOAP header to the SOAP request.
        soapRequest.MyHeaderValue = soapHeader

        ' Call the XML Web service method.
        Dim results As String = soapRequest.GetOrderStatsByDay("14/12/2010", "31/12/2010")

        ' Add the results of the method call into the XML document

        eleRow = xmlData.DocumentElement.AppendChild(xmlData.CreateElement("rdData"))
        eleRow.SetAttribute("Value", results)

    End Sub
End Class
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
