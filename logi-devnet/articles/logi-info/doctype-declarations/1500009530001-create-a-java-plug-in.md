---
title: "Create a Java Plug-in"
id: 1500009530001
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530001-Create-a-Java-Plug-in
updated_at: 2021-06-17T01:58:07Z
---

# Create a Java Plug-in

# Create a Java Plug-in

"Plug-ins" give Logi developers the ability to *programmatically extend* the functionality of their Logi applications. This topic discusses the development of Logi plug-ins using Java.

**IMPORTANT**: If you wish to upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8, you will need to replace the mscorlib.jar file in the application folder with the new one and restart your server. The mscorlib.jar file can be found on our [Product Download](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads "Select to access Product Dowload page") page. Please contact Support for additional assistance.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  If you haven't done so already, you should read [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009531221-Logi-Plug-ins) for important supporting information before proceeding.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif)  If you're developing a **.NET** plug-in, see [Create a .NET Plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500009514402-Create-a-NET-Plug-in) instead.

## Plug-in Class Methods and Properties

Logi plug-ins for Java are written in Eclipse or a similar development tool, using the either the LogiPluginObjects10 or LogiPluginObjects (pre-v10.0.337) class. Except as noted, this document refers to LogiPluginObjects10. The class files are:

*yourLogiApp*/WEB-INF/classes/com/logixml/plugins/LogiPluginObjects10.java  - or -   
*yourLogiApp*/WEB-INF/classes/LogiPluginObjects.java

You instantiate this class in your code and it provides access to the Logi application and its data. The class object is defined in your code as:

public class LogiPluginObjects10 (or LogiPluginObjects)  
extends java.lang.Object

Once instantiated, the object provides the following properties and methods for use with your custom code. Those with an asterisk are *not* included in the LogiPluginObjects object:

|  |  |
| --- | --- |
| * addDebugMessage\* * [get/setCurrentData](#currData) * [get/setCurrentDataFile](#currDataFile) * [get/setCurrentDefinition](#currDef) * [get/setCurrentElement](#currEle) * [get/setCurrentHttpContext](#currHttpContext) * [get/setPluginParameters](#pluginParams) * [replaceTokens](#replaceTokens)\* | * [setRequest](#gsRequest) * [getRequestParameterNames](#gsReqParamNames) * [getRequestParameterValues](#gsReqParamVals) * [get/setResponse](#gsResp) * [get/setResponseHtml](#gsRespHtml) * [get/setReturnedDataFile](#retDataFile) * [get/setSession](#getSession) * [getSettingsDefinition](#getSettings)\* |

Here are the object's methods and parameters:

|  |
| --- |
| **addDebugMessage** |
| Inserts an entry into the Debugging Trace page. (v10.0.337+)  void addDebugMessage(java.lang.String currentEvent) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject, java.lang.String      objectValue) void addDebugMessage(java.lang.String currentEvent, java.lang.String programObject, java.lang.String      objectValue, java.lang.Object moreInfo)  **Parameters**:     currentEvent - text to the inserted in the Trace page's Event column     programObject - text to the inserted in the Trace page's Object column     objectValue - text to the inserted in the Trace page's Value column     moreInfo - object, such as XML data or XSL code, that is displayed via link inserted in the Trace page's Value column  The time value for the entry is automatically provided. Note that if an error occurs within the plug-in, a fresh Trace page is generated, so any earlier messages placed with addDebugMessage are lost. |

 

|  |
| --- |
| **getCurrentData / setCurrentData** |
| Gets/sets an XML Document object containing the data in all of the datalayers.  public org.w3c.dom.Document getCurrentData() public void setCurrentData(org.w3c.dom.Document curdata) |

|  |
| --- |
| **getCurrentDataFile / setCurrentDataFile** |
| Gets/sets a string object containing of the fully-qualified path and filename for the cache file containing the XML data retrieved by the datalayer.  public java.lang.String getCurrentDataFile() public void setCurrentDataFile(java.lang.String currentDataFile) |

|  |
| --- |
| **getCurrentDefinition / setCurrentDefinition** |
| Gets/sets a string object containing the XML source code of the current report definition.  public java.lang.String getCurrentDefinition() public void setCurrentDefinition(java.lang.String curdef) |

|  |
| --- |
| **getCurrentElement / setCurrentElement** |
| Gets/sets a string object containing the XML source code of the current report definition.  public org.w3c.dom.Element getCurrentElement() public void setCurrentElement(org.w3c.dom.Element ele) |

|  |
| --- |
| **getCurrentHttpContext / setCurrentHttpContext** |
| Gets/sets an [XmlDocument](http://msdn.microsoft.com/en-us/library/system.xml.xmldocument(v=VS.80).aspx) object containing all HTTP-specific information, including Application, Session, Server, Request, and Response objects  public javax.servlet.ServletContext getCurrentHttpContext() public void setCurrentHttpContext(javax.servlet.ServletContext currHttpContext) |

|  |
| --- |
| **getPluginParameters / setPluginParameters** |
| Gets/sets a [Hashtable](http://download.oracle.com/javase/6/docs/api/java/util/Hashtable.html) object containing the parameters, if any, passed to the plug-in.  public java.util.Hashtable getPluginParameters() public void setPluginParameters(java.util.Hashtable plugPar) |

|  |
| --- |
| **replaceTokens** |
| Returns a string object containing the sTokens parameter with some or all of its tokens replaced with their current values, and with other optional effects applied. (v10.0.337+)  replaceTokens(java.lang.String sTokens) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element    eleDataLayerRow) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element    eleDataLayerRow, boolean bDuplicateBracketedQuotes) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element    eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element   eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric, java.lang.String[]   tokenList) replaceTokens(java.lang.String sTokens, boolean bDuplicateSingleQuotes, org.w3c.dom.Element   eleDataLayerRow, boolean bDuplicateBracketedQuotes, boolean bAssumeNonQuotedAsNumeric, java.lang.String[]   tokenList, boolean bSqlInjectionGuard)  **Parameters**:     sTokens - string containing Logi tokens, such as @Data.LastName~, to be replaced with current values.     bDuplicateSingleQuotes - if *True*, causes any single-quotes in sTokens to be doubled in return string.    eleDataLayerRow - XmlElement containing the data that will be used to replace the @Data tokens in sTokens.     bDuplicateBracketedQuotes - if *True*, double-quotes embedded in a token value will be included in return string.     bAssumeNonQuotedAsNumeric - if *True*, replacement processing will handle unquoted, numeric token values as numbers.     TokenList - comma-separated list of token types, indicating the types to be replaced; other types will be skipped.     bSqlInjectionGuard - if *True*, replacement processing checks all token values for potentially dangerous SQL strings.  **Throws:**    javax.xml.parsers.TranformerConfigurationException     java.lang.Exception |

|  |
| --- |
| **setRequest** |
| Sets an [HttpServletRequest](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpServletRequest.html) object and passes it as an argument to the servlet's service methods. public void setRequest(javax.servlet.http.HttpServletRequest req) |

|  |
| --- |
| **getRequestParameterNames** |
| Gets an array of the HTTP Request names sent by the client to a Logi application.  public java.util.Vector getRequestParameterNames() |

|  |
| --- |
| **getRequestParameterValues** |
| Gets an array of the HTTP Request values sent by the client to a Logi application.  public java.util.Vector getRequestParameterValues() |

|  |
| --- |
| **getResponse / setResponse** |
| Gets/sets an [HttpServletResponse](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpServletResponse.html) object containing the rendered HTML response page; available when the *FinishHtml* event completes.  public javax.servlet.http.HttpServletResponse getResponse() public void setResponse(javax.servlet.http.HttpServletResponse res) |

|  |
| --- |
| **getResponseHtml / setResponseHtml** |
| Gets/sets a String object containing the rendered HTML response page, available when the *FinishHtml* event completes.  public java.lang.String getResponseHtml() public void setResponseHtml(java.lang.String resp) |

|  |
| --- |
| **getReturnedDataFile / setReturnedDataFile** |
| Gets/sets a String object containing the fully-qualified path and filename for the cache file which contains the manipulated XML data after processing.  public java.lang.String getReturnedDataFile() public void setReturnedDataFile(java.lang.String returnedDataFile) |

|  |
| --- |
| **getSession / setSession** |
| Gets/sets an [HttpSession](http://download.oracle.com/javaee/6/api/javax/servlet/http/HttpSession.html) object, which is used to access Session values for the current Logi application session.  public javax.servlet.http.HttpSession getSession() public void setSession(javax.servlet.http.HttpSession ses)  Note that most session variables are replicated back and forth between the Logi Engine and the web server with every plug-in call. |

|  |
| --- |
| **getSettingsDefinition** |
| Gets an XML Document object representation of the \_Settings definition. (v10.0.337)  public org.w3c.dom.Document getSettingsDefinition()  **Throws:**    javax.xml.parsers.ParserConfigurationException     org.xml.sax.SAXException     java.lang.Exception |

Keywords: plugin, plugins
