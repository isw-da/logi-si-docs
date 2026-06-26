---
title: "Analysis Grid Auto-Columns"
id: 360047202714
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047202714-Analysis-Grid-Auto-Columns
updated_at: 2022-02-07T21:55:32Z
---

# Analysis Grid Auto-Columns

## **Plugin Description**

This plug-in provides an "Auto Columns" feature, similar to that available for DataTables, for the Analysis Grid. Columns will automatically be created for the AG, with special formatting applied for dates, currencies, and column headers. Download includes plug-in .dll, VB source code, and an example report definition. (.NET)

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Xml
Imports System.Web
Imports System.IO
Imports System.Text.RegularExpressions



Public Class LogiPlugin


	Public Sub SetAgColumns(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim sAgTableID As String = rdObjects.PluginParameters("AgTableID")
        Dim sDateFormat As String = rdObjects.PluginParameters("AgDateFormat")
        Dim sCurrencyCols As String = rdObjects.PluginParameters("AgCurrencyColumns")
        Dim bPopUpValues As Boolean = rdObjects.PluginParameters("AgPopUpValuesFilter")
        Dim bFixHeaders As Boolean = rdObjects.PluginParameters("AgFixHeaders")
        
		Dim xmlDefinition As New XmlDocument()
        xmlDefinition.LoadXml(rdObjects.CurrentDefinition)
        Dim eleAgTable As XmlElement = xmlDefinition.SelectSingleNode("//*[@ID='" & sAgTableID & "']")

        Dim xmlData As System.Xml.XmlDocument = rdObjects.CurrentData
        Dim eleFirstRow As XmlElement = xmlData.SelectSingleNode("/rdData/*")
        If Not IsNothing(eleFirstRow) Then
            Dim atr As XmlAttribute
            For Each atr In eleFirstRow.Attributes
                'Create a new AnalysisGridColumn element under the DataTable.
                Dim eleAgTableColumn As XmlElement = eleAgTable.AppendChild(xmlDefinition.CreateElement("AnalysisGridColumn"))
                'Set the AG Column attributes, ID , Header, DataColumn, DataType, and Format (if necessary)
                eleAgTableColumn.SetAttribute("ID", "col" & atr.Name)

                'Mod the header to remove underscores and check for CamelCase to split
                Dim headerText As String = atr.Name
                If bFixHeaders = True Then
                    headerText = Replace(atr.Name, "_", " ")
                    headerText = Regex.Replace(headerText, "([a-z])([A-Z])", "$1 $2")
                End If

                eleAgTableColumn.SetAttribute("Header", headerText)
                eleAgTableColumn.SetAttribute("DataColumn", atr.Name)
                'check if the value is a number to apply the correct DataType
                If IsNumeric(atr.Value) Then
                    'check if the value is part of the currency cols list to apply currency formatting
                    If InStr(sCurrencyCols, atr.Name) > 0 Then
                        eleAgTableColumn.SetAttribute("Format", "Currency")
                    End If
                    eleAgTableColumn.SetAttribute("DataType", "Number")
                    'check if the value is a date to apply the correct format otherwise set as text
                ElseIf IsDate(atr.Value) Then
                    eleAgTableColumn.SetAttribute("DataType", "DateTime")
                    eleAgTableColumn.SetAttribute("Format", sDateFormat)
                    'if you want pop ups in filter, then all dates will be given the calendar option
                    If bPopUpValues = True Then
                        eleAgTableColumn.SetAttribute("PopupValuesForFilter", "Calendar")
                    End If
                Else
                    eleAgTableColumn.SetAttribute("DataType", "Text")
                    'if you want pop ups in filters, then all text data will be given the list option
                    If bPopUpValues = True Then
                        eleAgTableColumn.SetAttribute("PopupValuesForFilter", "List")
                    End If
                End If
            Next
        End If
        rdObjects.CurrentDefinition = xmlDefinition.OuterXml
    End Sub
	
End Class	
```

## 

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
