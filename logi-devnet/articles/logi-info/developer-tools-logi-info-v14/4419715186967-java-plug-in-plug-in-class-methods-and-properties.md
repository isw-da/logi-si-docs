---
title: "Java Plug-in - Plug-in Class Methods and Properties"
id: 4419715186967
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715186967-Java-Plug-in-Plug-in-Class-Methods-and-Properties
updated_at: 2022-07-17T01:55:51Z
---

# Java Plug-in - Plug-in Class Methods and Properties

# Java Plug-in - Plug-in Class Methods and Properties

Logi plug-ins for Java are written in Eclipse or a similar development tool, using the LogiPluginObjects10 class. The class files are:

*yourLogiApp*/WEB-INF/classes/com/logixml/plugins/LogiPluginObjects10.java - or -   
*yourLogiApp*/WEB-INF/classes/LogiPluginObjects.java

You instantiate this class in your code and it provides access to the Logi application and its data. The class object is defined in your code as:

public class LogiPluginObjects10 (or LogiPluginObjects)  
extends java.lang.Object

Once instantiated, the object provides the following properties and methods for use with your custom code:

* [addDebugMessage](#addDebugMessage)
* [get/setCurrentData](#getCurrentData_/_setCurrentData)
* [get/setCurrentDataFile](#getCurrentDataFile_/_setCurrentDataFile)
* [get/setCurrentDefinition](#getCurrentDefinition_/_setCurrentDefinition)
* [get/setCurrentElement](#getCurrentElement_/_setCurrentElement)
* [get/setCurrentHttpContext](#getCurrentHttpContext_/_setCurrentHttpContext)
* [get/setPluginParameters](#getPluginParameters_/_setPluginParameters)
* [replaceTokens](#replaceTokens)
* [setRequest](#setRequest)
* [getRequestParameterNames](#getRequestParameterNames)
* [getRequestParameterValues](#getRequestParameterValues)
* [get/setResponse](#getResponse_/_setResponse)
* [get/setResponseHtml](#getResponseHtml_/_setResponseHtml)
* [get/setReturnedDataFile](#getReturnedDataFile_/_setReturnedDataFile)
* [get/setSession](#getSession_/_setSession)
* [getSettingsDefinition](#getSettingsDefinition)

Here are the object's methods and parameters:

|  |
| --- |
| **addDebugMessage** |
| Inserts an entry into the Debugging Trace page.void addDebugMessage(java.lang.String currentEvent) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject, java.lang.String objectValue) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject, java.lang.String objectValue, java.lang.Object More Info)**Parameters**: currentEvent - text to the inserted in the Trace page's Event column programObject - text to the inserted in the Trace page's Object column objectValue- text to the inserted in the Trace page's Value column More Info - object, such as XML data or XSL code, that is displayed via link inserted in the Trace page's Value column  The time value for the entry is automatically provided.  If an error occurs within the plug-in, a fresh Trace page is generated, so any earlier messages placed with addDebugMessage are lost. |
| **getCurrentData / setCurrentData** |
| Gets/sets an XML Document object containing the data in all of the datalayers. public org.w3c.dom.Document getCurrentData() public void setCurrentData(org.w3c.dom.Document curdata) |
| **getCurrentDataFile / setCurrentDataFile** |
| Gets/sets a string object containing of the fully-qualified path and filename for the cache file containing the XML data retrieved by the datalayer. public java.lang.String getCurrentDataFile() public void setCurrentDataFile(java.lang.String currentDataFile) |
| **getCurrentDefinition / setCurrentDefinition** |
| Gets/sets a string object containing the XML source code of the current report definition. public java.lang.String getCurrentDefinition() public void setCurrentDefinition(java.lang.String curdef) |
| **getCurrentElement / setCurrentElement** |
| Gets/sets a string object containing the XML source code of the current report definition. public org.w3c.dom.Element getCurrentElement() public void setCurrentElement(org.w3c.dom.Element ele) |
| **getCurrentHttpContext / setCurrentHttpContext** |
| Gets/sets an [XmlDocument](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmldocument?redirectedfrom=MSDN&view=net-6.0) object containing all HTTP-specific information, including Application, Session, Server, Request, and Response objects public javax.servlet.ServletContext getCurrentHttpContext() public void setCurrentHttpContext(javax.servlet.ServletContext currHttpContext) |
| **getPluginParameters / setPluginParameters** |
| Gets/sets a [Hashtable](https://download.oracle.com/javase/6/docs/api/java/util/Hashtable.html) object containing the parameters, if any, passed to the plug-in. public java.util.Hashtable getPluginParameters() public void setPluginParameters(java.util.Hashtable plugPar) |
| **replaceTokens** |
| Returns a string object containing the sTokens parameter with some or all of its tokens replaced with their current values, and with other optional effects applied. replaceTokens(java.lang.String sTokens) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element eleDataLayerRow) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element eleDataLayerRow, boolean bDuplicateBracketedQuotes) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric, java.lang.String[] tokenList) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric, java.lang.String[] tokenList, boolean bSqlInjectionGuard)**Parameters**:  sTokens - string containing Logi tokens, such as @Data.LastName~, to be replaced with current values.  bDuplicateSingleQuotes - if *True*, causes any single-quotes in sTokensto be doubled in return string. eleDataLayerRow - XmlElement containing the data that will be used to replace the @Data tokens in sTokens.  bDuplicateBracketedQuotes - if *True*, double-quotes embedded in a token value will be included in return string.  bAssumeNonQuotedAsNumeric - if *True*, replacement processing will handle unquoted, numeric token values as numbers.  TokenList - comma-separated list of token types, indicating the types to be replaced; other types will be skipped.  bSqlInjectionGuard - if *True*, replacement processing checks all token values for potentially dangerous SQL strings. **Throws:** javax.xml.parsers.TranformerConfigurationException  java.lang.Exception |
| **setRequest** |
| Sets an [HttpServletRequest](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpServletRequest.html) object and passes it as an argument to the servlet's service methods. public void setRequest(javax.servlet.http.HttpServletRequest req) |
| **getRequestParameterNames** |
| Gets an array of the HTTP Request names sent by the client to a Logi application. public java.util.Vector getRequestParameterNames() |
| **getRequestParameterValues** |
| Gets an array of the HTTP Request values sent by the client to a Logi application. public java.util.Vector getRequestParameterValues() |
| **getResponse / setResponse** |
| Gets/sets an [HttpServletResponse](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpServletResponse.html) object containing the rendered HTML response page; available when the *FinishHtml* event completes. public javax.servlet.http.HttpServletResponse getResponse() public void setResponse(javax.servlet.http.HttpServletResponse res) |
| **getResponseHtml / setResponseHtml** |
| Gets/sets a String object containing the rendered HTML response page, available when the *FinishHtml* event completes. public java.lang.String getResponseHtml() public void setResponseHtml(java.lang.String resp) |
| **getReturnedDataFile / setReturnedDataFile** |
| Gets/sets a String object containing the fully-qualified path and filename for the cache file which contains the manipulated XML data after processing. public java.lang.String getReturnedDataFile() public void setReturnedDataFile(java.lang.String returnedDataFile) |
| **getSession / setSession** |
| Gets/sets an [HttpSession](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpSession.html) object, which is used to access Session values for the current Logi application session. public javax.servlet.http.HttpSession getSession() public void setSession(javax.servlet.http.HttpSession ses)  Most session variables are replicated back and forth between the Logi Engine and the web server with every plug-in call. |
| **getSettingsDefinition** |
| Gets an XML Document object representation of the \_Settings definition. public org.w3c.dom.Document getSettingsDefinition()  **Throws:** javax.xml.parsers.ParserConfigurationException  org.xml.sax.SAXException  java.lang.Exception |
