---
title: "Cleanup MDX Data"
id: 360047203614
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047203614-Cleanup-MDX-Data
updated_at: 2022-02-07T21:54:36Z
---

# Cleanup MDX Data

## **Plugin Description**

Traditionally, MDX queries are used to retrieve data from OLAP cubes for viewing in our OLAP Grid or OLAP Table elements. However, the data retrieved can also be used with any of our other visualization elements, such as DataTables and Charts. When used for non-OLAP purposes, special characters such as square brackets and periods need to be removed from the data first. This plug-in cleans the data in a datalayer of the special characters. The download includes the plug-in .dll, a readme file, and an example report definition. (.NET)

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Public Sub CleanOLAPDataLayer(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim xmlDataFile As System.Xml.XmlDocument = rdObjects.CurrentData
        Dim parentElement As XmlNode = xmlDataFile.SelectSingleNode("rdData")
        Dim eleRow As XmlElement
        For Each eleRow In xmlDataFile.SelectNodes("/rdData/*")
            Dim newElem As XmlElement = xmlDataFile.CreateElement(eleRow.Name)
            Dim atr As XmlAttribute
            For Each atr In eleRow.Attributes
                Dim value As String = atr.Name
                value = Replace(value, "_x005B_", "")
                value = Replace(value, "_x005D_", "")
                value = Replace(value, "_x0020_", "_")
                value = Replace(value, "Measures.", "")
                value = Replace(value, ".MEMBER_CAPTION", "")
                newElem.SetAttribute(value, atr.Value)
            Next
            parentElement.ReplaceChild(newElem, eleRow)
        Next
End Sub
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
