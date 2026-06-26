---
title: "Exporting Animated Charts"
id: 360047204774
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047204774-Exporting-Animated-Charts
updated_at: 2022-02-07T21:53:29Z
---

# Exporting Animated Charts

## **Plugin Description**

This plug-in allows developers to "export" Animated Charts to PDF, Native Word, and Native Excel. Basically, the plug-in reads the report definition, finds the specified Animated Charts (.XY or .Pie) and creates a temporary, look-alike, non-Animated Chart for the purpose of the export. The download includes the .dll and its VB.NET source code.

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Xml
Imports System.Web

Public Class LogiPlugin
    Public Sub exportAnimatedCharts(ByRef rdObjects As rdPlugin.rdServerObjects)
        'check if this is an exported report - otherwise, do nothing
        If InStr(" PDF,NativeExcel,NativeWord", rdObjects.Request("rdReportFormat")) > 1 Then
            'get the list charts we want to convert from Animated
            Dim strChart As String = rdObjects.PluginParameters("chartID")
            Dim debug As String = "empty" 'for debugging element
            Dim xmlDefinition As New XmlDocument()
            xmlDefinition.LoadXml(rdObjects.CurrentDefinition)

            'find all named animated charts in the report to convert into standard charts
            Dim chartArray As Array = Split(strChart, ",")
            For Each eleChart In chartArray
                Dim thisChart As XmlElement = xmlDefinition.SelectSingleNode("//*[@ID='" & eleChart & "']")

                'debug = thisChart.OuterXml 'write the XML node into a debug var

                Dim newChart As XmlElement = xmlDefinition.CreateElement("Chart")
                'cycle throught the attributes and copy
                For Each atr In thisChart.Attributes
                    'copy all filled in attributes to the new chart
                    newChart.SetAttribute(atr.name, atr.value)
                Next

                'get the datalayer (or other child elements to add into the new chart)
                newChart.InnerXml = thisChart.InnerXml


                'check 3D and set accordingly for Bar, Line, Area Charts
                If thisChart.GetAttribute("D3") = "False" And thisChart.GetAttribute("XYChartType") = "Bar" Then
                    newChart.SetAttribute("D3", "0")
                ElseIf thisChart.GetAttribute("XYChartType") = "Line" Or thisChart.GetAttribute("XYChartType") = "Area" Then
                    newChart.SetAttribute("D3", "")
                Else
                    newChart.SetAttribute("D3", "10")
                End If

                'set general style-related attributes for background
                newChart.SetAttribute("ChartBackgroundColor", "#D2D2D2")
                If thisChart.HasAttribute("CanvasBgColor") Then
                    newChart.SetAttribute("ChartBackgroundGradientColor", thisChart.GetAttribute("CanvasBgColor"))
                Else
                    newChart.SetAttribute("ChartBackgroundGradientColor", "#E1E1E1")
                End If

                'set the chart style Pie Charts to match Animated styles for layout and labels
                If thisChart.GetAttribute("Type") = "Pie" Then
                    newChart.SetAttribute("ChartTexture", "RoundedEdge")
                    newChart.SetAttribute("D3Angle", "0")
                    newChart.SetAttribute("D3", "0")
                    Dim eleFormatData As XmlElement = xmlDefinition.CreateElement("FormatData")
                    If thisChart.HasAttribute("ChartLabelColumn") And thisChart.GetAttribute("ShowNames") = "0" Then
                        eleFormatData.SetAttribute("ChartLabelFormat", "{value}")
                    Else
                        eleFormatData.SetAttribute("ChartLabelFormat", "{label},{value}")
                        'newChart.SetAttribute("LabelLayout", "Side")
                    End If
                    newChart.AppendChild(eleFormatData)
                End If


                'set the title font properly when a chart title is set
                If thisChart.HasAttribute("ChartTitle") Then
                    Dim eleChartTitle As XmlElement = xmlDefinition.CreateElement("FontChartTitle")
                    eleChartTitle.SetAttribute("FontSize", "8")
                    eleChartTitle.SetAttribute("FontFilename", "verdana bold")
                    newChart.AppendChild(eleChartTitle)
                End If

                'set the X axis labels properly when a label Column is set
                If thisChart.HasAttribute("ChartLabelColumn") Then
                    Dim eleLabelFont As XmlElement = xmlDefinition.CreateElement("FontLabel")

                    'for XY charts we need to rotate labels, when specified, pie charts just set labels
                    If thisChart.GetAttribute("Type") <> "Pie" Then
                        If thisChart.GetAttribute("RotateNames") = "False" Then
                            eleLabelFont.SetAttribute("FontAngle", "0")
                        ElseIf thisChart.GetAttribute("ChartOrientation") = "Horizontal" Then
                            eleLabelFont.SetAttribute("FontAngle", "0")
                        Else
                            eleLabelFont.SetAttribute("FontAngle", "90")
                        End If

                    End If
                    eleLabelFont.SetAttribute("FontSize", "8")
                    eleLabelFont.SetAttribute("FontFilename", "verdana")
                    newChart.AppendChild(eleLabelFont)

                End If


                'set specific attributes for Bars
                If thisChart.GetAttribute("XYChartType") = "Bar" Then
                    newChart.SetAttribute("BarShading", "BottomLight")
                    'create the default color list for Bars
                    Dim colorList = "#B6CEE0,#F0D16F,#A8C359,#DC9A6F,#4DA0A0,#CF7D7D,#976C82,#7B965E,#B9B352,#4A9DC7,#9B4245,#A393B4,#BB7F43,#E0C09C,#A7A142,#E4959F,#EFE864,#3F76AC,#DD9742,#CE7355,#528F52"
                    Dim i = 1 'create a loop counter for colors
                    If thisChart.HasAttribute("Color") = False And InStr(thisChart.InnerXml, "ExtraXYDataColumn") = False Then
                        'when the color is empty and there aren't any extra bar columns set the random colors for bar charts
                        newChart.SetAttribute("Color", colorList)
                    ElseIf thisChart.HasAttribute("Color") = False And InStr(thisChart.InnerXml, "ExtraXYDataColumn") > 0 Then
                        newChart.SetAttribute("Color", "#B6CEE0")
                        Dim colorListArray As Array = Split(colorList, ",")
                        For Each extraXY In newChart.GetElementsByTagName("ExtraXYDataColumn")
                            extraXY.SetAttribute("Color", colorListArray(i))
                            i = i + 1
                        Next
                    End If
                End If

                'set specific attributes for Lines
                If thisChart.GetAttribute("XYChartType") = "Line" Then
                    newChart.SetAttribute("LineWidth", "4")
                    newChart.SetAttribute("ChartSymbolSize", "8")
                    newChart.SetAttribute("ChartSymbol", "SymbolCircle")
                End If

                'insert the new replacement chart under a Div after the current chart so that it can be centered with a class
                'this mimicks the centering behavior of animated charts, but causes some odd behvior in NativeWord export
                Dim newChartDiv As XmlElement = xmlDefinition.CreateElement("Division")
                Dim eleStyle As XmlElement = xmlDefinition.CreateElement("Label")
                eleStyle.SetAttribute("Caption", "<style>.rdPluginChartStyle { width: 100%; text-align: center;</style>")
                eleStyle.SetAttribute("Format", "HTML")
                newChartDiv.SetAttribute("Class", "rdPluginChartStyle")
                newChartDiv.SetAttribute("HtmlDiv", "True")
                xmlDefinition.SelectSingleNode("//Body").AppendChild(eleStyle)
                thisChart.ParentNode.InsertAfter(newChartDiv, thisChart)
                newChartDiv.AppendChild(newChart)
                'get rid of the original chart
                thisChart.ParentNode.RemoveChild(thisChart)

                'debug = debug & " " & newChartDiv.OuterXml
            Next

            'write out the results in a label for debugging purposes
            'Dim eleBody As XmlElement = xmlDefinition.SelectSingleNode("//Report/Body")
            'Dim eleLabel As XmlElement = eleBody.AppendChild(xmlDefinition.CreateElement("Label"))
            'eleLabel.SetAttribute("Caption", debug)

            rdObjects.CurrentDefinition = xmlDefinition.OuterXml

        Else
            'do nothing
        End If
    End Sub
End Class
```

## 

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
