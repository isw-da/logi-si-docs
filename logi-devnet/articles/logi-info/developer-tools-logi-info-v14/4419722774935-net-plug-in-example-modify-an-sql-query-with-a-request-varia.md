---
title: ".NET Plug-in - Example: Modify an SQL Query with a Request Variable"
id: 4419722774935
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722774935--NET-Plug-in-Example-Modify-an-SQL-Query-with-a-Request-Variable
updated_at: 2022-07-17T01:56:07Z
---

# .NET Plug-in - Example: Modify an SQL Query with a Request Variable

# .NET Plug-in - Example: Modify an SQL Query with a Request Variable

The following are code examples for a plug-in that customizes a SQL query based on a request variable:

[Visual Basic]  
 Imports System.Xml.Linq  
  
 Public Class Plugin  
  
 Public Sub SetCustomerQuery(ByRef rdObjects As rdPlugin.rdServerObjects)  
 Dim xmlDefinition As New XmlDocument()  
 xmlDefinition.LoadXml(rdObjects.CurrentDefinition)  
 Dim xpath As String = "//Report/Body/DataTable/DataLayer"   
 Dim eleDataLayer As XmlElement = xmlDefinition.SelectSingleNode(xpath)  
 If IsNothing(eleDataLayer) Then  
 Throw New Exception("The report is missing the DataLayer element.")  
End If  
  
 'Use a Request variable to set set the SELECT query.  
 Dim sSelect As String  
 Select Case rdObjects.Request("Continent")  
 Case "NA"  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('USA','Mexico','Canada')"  
 Case "SA"  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('Argentina','Brazil','Venezuela')"  
 Case "EU"  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('UK','France','Spain')"  
 Case Else  
 sSelect = "SELECT \* FROM Customers"  
 End Select  
  
 eleDataLayer.SetAttribute("Source", sSelect)  
 rdObjects.CurrentDefinition = xmlDefinition.OuterXml  
 End Sub  
  
 End Class  
 [C#}  
using System;  
 using System.Xml.Linq;  
 using rdPlugin;  
  
 namespace SamplePlugin  
 {  
 public class Plugin  
 {  
 public void setCustomerQuery(ref rdServerObjects rdObjects)  
{  
 XmlDocument xmlDefinition;  
 XmlElement eleDataLayer;  
 string sSelect, xpath;   
  
 // Load the current report definition into an XmlDocument object  
 xmlDefinition = new XmlDocument();  
 xmlDefinition.LoadXml(rdObjects.CurrentDefinition);  
  
 // Locate the DataLayer element in the specified XML tree  
 xpath = "//Report/Body/DataTable/DataLayer";  
 eleDataLayer = (XmlElement)xmlDefinition.SelectSingleNode(xpath);  
 if (eleDataLayer == null)  
 throw new Exception("The report is missing the DataLayer element.");  
  
 // Use a Request variable to set the SELECT query  
 switch (rdObjects.Request["Continent"])   
 {  
 case "NA":  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('USA','Mexico','Canada')";  
 break;  
 case "SA":  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('Argentina','Brazil',  
 'Venezuela')";  
 break;  
 case "EU":  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('UK','France','Spain')";  
 break;  
 default:  
 sSelect = "SELECT \* FROM Customers";  
 break;  
 }  
  
 // Save the SQL query to the report definition  
 eleDataLayer.SetAttribute("Source", sSelect);  
 rdObjects.CurrentDefinition = xmlDefinition.OuterXml;  
 }  
 }  
 }
