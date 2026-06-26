---
title: ".NET Plug-in - Plug-in Class Properties and Methods"
id: 4406817215895
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817215895--NET-Plug-in-Plug-in-Class-Properties-and-Methods
updated_at: 2022-04-06T06:04:42Z
---

# .NET Plug-in - Plug-in Class Properties and Methods

# .NET Plug-in - Plug-in Class Properties and Methods

Logi plug-ins for .NET are written in Visual Studio or a similar development tool, using the rdServerObjects class, which resides in the rdPlugin.dll assembly and is a member of the rdPlugin namespace. You instantiate this class in your code and it provides access to the Logi application and its data. The class object is defined in your code as:

[Visual Basic]   
public Class rdServerObjects[C#]  
public class rdServerObjects  

Once instantiated, the object provides the following properties and methods for use with your custom code:

* [AddDebugMessage()](#AddDebugMessage())
* [CurrentData](#CurrentData)
* [CurrentDataFile](#CurrentDataFile)
* [CurrentDefinition](#CurrentDefinition)
* [CurrentElement](#CurrentElement)
* [CurrentHttpContext](#CurrentHttpContext)
* [PluginParameters](#PluginParameters)
* [ReplaceTokens()](#ReplaceTokens())
* [Request](#Request)
* [ResponseHtml](#ResponseHtml)
* [ReturnedDataFile](#ReturnedDataFile)
* [Session](#Session)
* [SettingsDefinition](#SettingsDefinition)

Here are the object's methods and parameters:

|  |
| --- |
| **AddDebugMessage()** |
| This method inserts an entry into the Debugger Trace Report: [Visual Basic] Public Sub AddDebugMessage(Optional ByVal CurrentEvent As String,   Optional ByVal ProgramObject As String,  Optional ByVal ObjectValue As String,   Optional ByVal More Info As Object )[C#] public void AddDebugMessage(string CurrentEvent, string ProgramObject, string ObjectValue, object More Info);**Parameters**: CurrentEvent - text to be inserted in the Debug Trace page's Event column ProgramObject - text to be inserted in the Debug Trace page's Object column ObjectValue - text to be inserted in the Debug Trace page's Value column More Info - object (XML data or XSL code) that is displayed via link inserted in the Debug Trace page's Value column  The time value for the entry inserted into the Debugger is provided automatically. |
| **CurrentData** |
| Returns an [XmlDocument](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument?redirectedfrom=MSDN&view=net-6.0) object containing the data in all of the datalayers. [Visual Basic] Public CurrentData As System.Xml.XmlDocument[C#] public System.Xml.XmlDocument CurrentData; |
| **CurrentDataFile** |
| Returns a string object containing of the fully-qualified path and filename for the cache file containing the XML data retrieved by the datalayer. [Visual Basic] Public CurrentDataFile As String [C#] public string CurrentDataFile; |
| **CurrentDefinition** |
| Returns a string object containing the XML source code of the current report definition. [Visual Basic] Public CurrentDefinition As String[C#] public string CurrentDefinition; |
| **CurrentElement** |
| Returns an [XmlElement](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmlelement?redirectedfrom=MSDN&view=net-6.0) object containing the XML source code of the current element. Only available when using Data Layer Plugin Call and Procedure.Plugin Call elements. [Visual Basic] Public CurrentElement As System.Xml.XmlElement [C#] public System.Xml.XmlElement CurrentElement; |
| **CurrentHttpContext** |
| Returns an [XmlDocument](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument?redirectedfrom=MSDN&view=net-6.0) object containing all HTTP-specific information, including Application, Session, Server, Request, and Response objects. [Visual Basic] Public CurrentHttpContext As System.Web.XmlDocument[C#] public System.Web.XmlDocument CurrentHttpContext; |
| **PluginParameters** |
| Returns a [Hashtable](https://docs.microsoft.com/en-us/dotnet/api/system.collections.hashtable?redirectedfrom=MSDN&view=net-6.0) object containing the parameters, if any, passed to the plug-in. [Visual Basic] Public PluginParameters As System.Collections.Hashtable[C#] public System.Collections.Hashtable PluginParameters; |
| **ReplaceTokens()** |
| Returns a string object containing the sTokens parameter with some or all of its tokens replaced with their current values, and with other optional effects applied. [Visual Basic] Public Function ReplaceTokens(ByVal sTokens As String,   Optional ByVal bDuplicateSingleQuotes As Boolean = False,   Optional ByVal eleDataLayerRow As System.Xml.XmlElement,   Optional ByVal bDuplicateBracketedQuotes As Boolean = False,   Optional ByVal bAssumeNonQuotedAsNumeric As Boolean = False,   Optional ByVal TokenList() As String,   Optional ByVal bSqlInjectionGuard As Boolean = False) As String[C#] public string ReplaceTokens(string sTokens,   bool bDuplicateSingleQuotes,   XmlElement eleDataLayerRow,   bool bDuplicateBracketedQuotes,   bool bAssumeNonQuotedAsNumeric,   string TokenList,   bool bSqlInjectionGuard);**Parameters**:  sTokens - string containing Logi tokens, such as @Data.LastName~, to be replaced with current values.  bDuplicateSingleQuotes - if *True*, causes any single-quotes in sTokens to be doubled in return string. eleDataLayerRow - XmlElement containing the data that will be used to replace the @Data tokens in sTokens.  bDuplicateBracketedQuotes - if *True*, double-quotes embedded in a token value will be included in return string.  bAssumeNonQuotedAsNumeric - if *True*, replacement processing will handle unquoted, numeric token values as numbers.  TokenList - comma-separated list of token types, indicating the types to be replaced; other types will be skipped.  bSqlInjectionGuard - if *True*, replacement processing checks all token values for potentially dangerous SQL strings. |
| **Request** |
| Returns an [HttpRequest](https://docs.microsoft.com/en-us/dotnet/api/system.web.httprequest?redirectedfrom=MSDN&view=netframework-4.8) object, which can be used to access HTTP Request values sent by the client to a Logi application. [Visual Basic] Public Request As System.Web.HttpRequest[C#] public System.Web.HttpRequest Request; |
| **ResponseHtml** |
| Returns a String object containing the HTML for the rendered response page; available when the *FinishHtml* event completes. [Visual Basic] Public ResponseHtml As String[C#] public String ResponseHtml; |
| **ReturnedDataFile** |
| Returns a String object containing the fully-qualified path and filename for the cache file which contains the manipulated XML data after processing. [Visual Basic] Public ReturnedDataFile As String [C#] public string ReturnedDataFile; |
| **Session** |
| Returns an [HttpSessionState](https://docs.microsoft.com/en-us/dotnet/api/system.web.sessionstate.httpsessionstate?redirectedfrom=MSDN&view=netframework-4.8) object, which can be used to access Session variable values related to the current Logi application session. [Visual Basic] Public Session As System.Web.SessionState.HttpSessionState[C#] public System.Web.SessionState.HttpSessionState Session; |
| **SettingsDefinition** |
| Returns a read-only [XmlDocument](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument?redirectedfrom=MSDN&view=net-6.0) object containing the XML of the \_Settings definition. [Visual Basic] Public ReadOnly Property SettingsDefinition() As System.Xml.XmlDocument[C#] public System.Xml.XmlDocument SettingsDefinition; |
