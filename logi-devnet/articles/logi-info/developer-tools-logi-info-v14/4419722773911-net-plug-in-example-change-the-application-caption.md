---
title: ".NET Plug-in - Example: Change the Application Caption"
id: 4419722773911
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722773911--NET-Plug-in-Example-Change-the-Application-Caption
updated_at: 2022-07-17T01:56:10Z
---

# .NET Plug-in - Example: Change the Application Caption

# .NET Plug-in - Example: Change the Application Caption

The following are code examples for a plug-in that alters the caption of the Logi application at runtime:

[Visual Basic]  
 Imports System.Xml.Linq  
  
 Public Class Plugin  
  
 Public Sub SetApplicationCaption(ByRef rdObjects As rdPlugin.rdServerObjects)  
 Dim xmlSettings As New XmlDocument()  
 xmlSettings.LoadXml(rdObjects.CurrentDefinition)  
 Dim eleApp As XmlElement = xmlSettings.SelectSingleNode("//Setting/Application")  
 eleApp.SetAttribute("Caption", "Greetings from the Sample Plugin! Time: " & Now.ToString)  
 rdObjects.CurrentDefinition = xmlSettings.OuterXml  
 End Sub  
  
 End Class  
  
[C#]  
 using System;  
 using System.Xml.Linq;  
 using rdPlugin;  
  
 namespace SamplePlugin  
 {  
 public class Plugin  
 {  
 public void setApplicationCaption(ref rdServerObjects rdObjects)  
 {  
 XmlDocument xmlSettings;  
 XmlElement eleApp;  
 string currentTime;  
  
 // Load the current report definition into an XmlDocument object  
 xmlSettings = new XmlDocument();  
 xmlSettings.LoadXml(rdObjects.CurrentDefinition);  
  
 // Locate the Application element and define its Caption attribute  
 eleApp = (XmlElement)xmlSettings.SelectSingleNode("//Setting/Application");  
 currentTime = DateTime.Now.ToShortTimeString();   
 eleApp.SetAttribute("Caption", "Hello from the Sample Plugin! Time: " + currentTime);  
  
 // Save the new report definition  
 rdObjects.CurrentDefinition = xmlSettings.OuterXml;  
 }   
 }  
 }
