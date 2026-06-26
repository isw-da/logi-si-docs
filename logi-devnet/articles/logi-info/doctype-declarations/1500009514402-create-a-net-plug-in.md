---
title: "Create a .NET Plug-in"
id: 1500009514402
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514402-Create-a-NET-Plug-in
updated_at: 2021-06-17T01:58:07Z
---

# Create a .NET Plug-in

# Create a .NET Plug-in

"Plug-ins" give Logi developers the ability to *programmatically extend* the functionality of their Logi applications. This topic discusses the development of Logi plug-ins using the .NET framework.

* Write Your Plug-in
* [Example: Change the Application Caption](#exAppCaption)
* [Example: Modify an SQL Query with a Request Variable](#exModSQL)
* [Example: Change Data in a Datalayer](#Datalayer)
* [Implement Your Plug-in](#Implementing)
* [Debug in Visual Studio 2012](#VS2012)
* [Debug in Visual Studio 2008/2005](#VS2005)
* [Plug-in Class Properties and Methods](#Properties)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  If you haven't done so already, you should read [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009531221-Logi-Plug-ins) for important supporting information before proceeding.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif)  If you're developing a **Java** plug-in, see [Create a Java Plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500009530001-Create-a-Java-Plug-in) instead.

## Write Your Plug-in

Plug-ins written for Logi .NET applications are compiled into Dynamic Link Library (.DLL) files. In the code, the **System.Web** and **System.XML.Linq** .NET *namespaces* are referenced for interactions with Logi applications and report definitions. Namespaces are collections of classes with methods for doing things with specific kinds of data or objects. You import or include them in your plug-in project.

For example, System.Web is needed to access *HTTP Request* and *Session* objects, which are often useful in a plug-in.

Logi definitions and data are handled as XML streams during processing by the web server and therefore by your plug-in, too. Much of your code will be concerned with searching, parsing, and modifying this XML. The System.XML.Linq namespace provides useful methods for doing this. If you're familiar with XPath notation, you'll find that to be very helpful as well.

### Create your plug-in project in Visual Studio:

1. Create a new Class Library project, using C#, Visual Basic, or other language of your choice.
2. Configure the project to build the .DLL output in the \_Plugins folder of the Logi application (which you may need to create). The folder's name *must* be "\_Plugins", beginning with an underscore.
3. Add a reference to the System.Web and System.XML.Linq .NET namespaces. Both may not be needed, depending on what you do in the plug-in, but you can refine that later.
4. **Logi Info & Report**: Add a reference to the file *yourLogiApp*/bin/rdPlugin.dll distributed with your Logi product.  *![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Be sure* to use the file found in the bin folder of the Logi application that will use this plug-in. It's version-specific so don't refer to it in the bin folder of some other Logi application.  
     
   **Logi ETL**: Add a reference to the EtlWebService\bin\LogiEtlWebService.dll file. Always copy this DLL locally to the build folder when compiling so that, if you upgrade ETL and the engine version of the DLL changes, your code will still function.

5. Write your plug-in code, starting with this prototype:

|  |  |
| --- | --- |
|  | [Visual Basic] Imports System.Xml.Linq Imports System.Web  Public Class Plugin     Public Sub yourMethodName(ByRef yourObjName As rdPlugin.rdServerObjects)       ' your method code goes here     End Sub End Class  [C#] using System;  using System.Xml.Linq; using System.Web;  using rdPlugin;   namespace myPlugin {     public class Plugin     {        public void yourMethodName(ref rdPlugin.rdServerObjects yourObjName)        {          // your method code goes here        }     }  } |

Add the methods and code you need to get the plug-in to do whatever it's supposed to do.

## Example: Change the Application Caption

The following are code examples for a plug-in that alters the caption of the Logi application at runtime:

|  |  |
| --- | --- |
|  | [Visual Basic]  Imports System.Xml.Linq   Public Class Plugin     Public Sub SetApplicationCaption(ByRef rdObjects As rdPlugin.rdServerObjects)       Dim xmlSettings As New XmlDocument()       xmlSettings.LoadXml(rdObjects.CurrentDefinition)       Dim eleApp As XmlElement = xmlSettings.SelectSingleNode("//Setting/Application")       eleApp.SetAttribute("Caption", "Greetings from the Sample Plugin! Time: " & Now.ToString)       rdObjects.CurrentDefinition = xmlSettings.OuterXml    End Sub   End Class  [C#]  using System;  using System.Xml.Linq;  using rdPlugin;   namespace SamplePlugin  {    public class Plugin    {       public void setApplicationCaption(ref rdServerObjects rdObjects)       {          XmlDocument xmlSettings;          XmlElement eleApp;          string currentTime;           // Load the current report definition into an XmlDocument object          xmlSettings = new XmlDocument();          xmlSettings.LoadXml(rdObjects.CurrentDefinition);           // Locate the Application element and define its Caption attribute          eleApp = (XmlElement)xmlSettings.SelectSingleNode("//Setting/Application");          currentTime = DateTime.Now.ToShortTimeString();           eleApp.SetAttribute("Caption", "Hello from the Sample Plugin! Time: " + currentTime);           // Save the new report definition          rdObjects.CurrentDefinition = xmlSettings.OuterXml;       }     }  } |

## Example: Modify a SQL Query with Request Variable

The following are code examples for a plug-in that customizes a SQL query based on a request variable:

|  |  |
| --- | --- |
|  | [Visual Basic]  Imports System.Xml.Linq   Public Class Plugin     Public Sub SetCustomerQuery(ByRef rdObjects As rdPlugin.rdServerObjects)       Dim xmlDefinition As New XmlDocument()       xmlDefinition.LoadXml(rdObjects.CurrentDefinition)       Dim xpath As String = "//Report/Body/DataTable/DataLayer"        Dim eleDataLayer As XmlElement = xmlDefinition.SelectSingleNode(xpath)       If IsNothing(eleDataLayer) Then          Throw New Exception("The report is missing the DataLayer element.")       End If        'Use a Request variable to set set the SELECT query.       Dim sSelect As String       Select Case rdObjects.Request("Continent")          Case "NA"             sSelect = "SELECT \* FROM Customers WHERE Country IN('USA','Mexico','Canada')"          Case "SA"             sSelect = "SELECT \* FROM Customers WHERE Country IN('Argentina','Brazil','Venezuela')"          Case "EU"             sSelect = "SELECT \* FROM Customers WHERE Country IN('UK','France','Spain')"          Case Else             sSelect = "SELECT \* FROM Customers"          End Select        eleDataLayer.SetAttribute("Source", sSelect)       rdObjects.CurrentDefinition = xmlDefinition.OuterXml    End Sub   End Class    [C#} using System;  using System.Xml.Linq;  using rdPlugin;   namespace SamplePlugin  {    public class Plugin    {       public void setCustomerQuery(ref rdServerObjects rdObjects)       {          XmlDocument xmlDefinition;          XmlElement eleDataLayer;          string sSelect, xpath;            // Load the current report definition into an XmlDocument object          xmlDefinition = new XmlDocument();          xmlDefinition.LoadXml(rdObjects.CurrentDefinition);           // Locate the DataLayer element in the specified XML tree          xpath = "//Report/Body/DataTable/DataLayer";          eleDataLayer = (XmlElement)xmlDefinition.SelectSingleNode(xpath);          if (eleDataLayer == null)             throw new Exception("The report is missing the DataLayer element.");           // Use a Request variable to set the SELECT query          switch (rdObjects.Request["Continent"])           {             case "NA":                sSelect = "SELECT \* FROM Customers WHERE Country IN('USA','Mexico','Canada')";                break;             case "SA":                sSelect = "SELECT \* FROM Customers WHERE Country IN('Argentina','Brazil',                           'Venezuela')";                break;             case "EU":                sSelect = "SELECT \* FROM Customers WHERE Country IN('UK','France','Spain')";                break;             default:                sSelect = "SELECT \* FROM Customers";                break;          }           // Save the SQL query to the report definition          eleDataLayer.SetAttribute("Source", sSelect);          rdObjects.CurrentDefinition = xmlDefinition.OuterXml;       }    }  } |

## Example: Change Data in a Datalayer

The following are code examples for a plug-in that converts RTF text in a datalayer to plain text. It creates an in-memory RichTextBox control, then iterates through all records in the datalayer, processing and replacing the contents of a data column.

|  |  |
| --- | --- |
|  | [Visual Basic]  Imports System.Xml.Linq Imports System.Windows.Forms.RichTextBox   Public Class Plugin     Public Sub RTF2Text(ByRef rdObjects As rdPlugin.rdServerObjects)       Dim objRTB As New System.Windows.Forms.RichTextBox()       Dim objDoc As New XmlDocument()       Dim objNodeList As XmlNodeList       Dim objNode As XmlNode        ' load the XML from the datalayer       objDoc = rdObjects.CurrentData        ' get a nodelist for all nodes (records) in XML doc       ' in XPath syntax "dtTest" equals the name of the data table,         ' and is the node name in the XML document       objNodeList = objDoc.SelectNodes("//dtTest")        ' loop thru each node, processing the "colText" attribute value,         ' which is name of column with RTF text.       ' put each value into RichTextBox as RTF, then reassign it as plain text       For Each objNode In objNodeList            objRTB.Rtf = objNode.Attributes.ItemOf("colText").Value           objNode.Attributes.ItemOf("colText").Value = objRTB.Text       Next        ' clean up       objNode = Nothing       objNodeList = Nothing       objDoc = Nothing       objRTB = Nothing     End Sub   End Class    [C#} using System;  using System.Xml.Linq;  using rdPlugin; using System.Windows.Forms;   namespace RTFPlugin  {    public class Plugin    {         public void RTF2Text(ref rdServerObjects rdObjects)         {             RichTextBox objRTB;             XmlDocument objDoc;             XmlNodeList objNodeList;              // create RichTextBox             objRTB = new RichTextBox();              // load the XML from the datalayer             objDoc = new XmlDocument();             objDoc = rdObjects.CurrentData;               // get a nodelist for all nodes (records) in XML doc             // in XPath syntax "dtTest" equals the name of the data table,              // and is the node name in the XML document             objNodeList = objDoc.SelectNodes("//dtTest");               // loop thru each node, processing the "colText" attribute value,              // which is name of column with RTF text.             // put each value into RichTextBox as RTF, then reassign it as plain text             foreach (XmlNode objNode in objNodeList)              {                 objRTB.Rtf = objNode.Attributes.GetNamedItem("colText").Value;                 objNode.Attributes.GetNamedItem("colText").Value = objRTB.Text;             }         }     }  } |

## Implement Your Plug-in

When your plug-in has been written and compiled, add the element(s) you need to call it in your Logi application. The elements used to do this are described in [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009531221-Logi-Plug-ins).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) The first time you run your Logi application, IIS will load the plug-in into memory and it will remain cached there. If you make coding changes to the plug-in and want to rebuild it, you'll need to run **stop** and **restart****IIS** (run iisreset.exe) first, in order to be able to replace the previous build.

## Debug in Visual Studio 2012

You can debug your plug-in as it runs in your Logi application, using Visual Studio (VS). The examples in this section show you how it's done in VS 2012. Ensure that you're running VS with a user account that has Administrator privileges.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771877143/createpluginnet_01.png)

Open your plug-in solution in VS and, in the Solution Explorer, select and right-click the root node, then select **Add**![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)**Existing Web Site...** Click the **Local IIS** category and select your Logi application web site's virtual directory from the list, adding it to your solution.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771877399/createpluginnet_02.png)

Right-click the Logi application web site in the Solution Explorer and select its **Property Pages** from the pop-up menu, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771877655/createpluginnet_03.png)

In the Property Pages window, shown above, select the **Build** page in the left menu, and then:

1. Select **No Build** in the list of Start actions.
2. Ensure that the appropriate .NET Framework version for your Logi application is selected.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778711319/createpluginnet_04.png)

Next, select the **Start Options** page in the left menu, as shown above, and then:

1. Select the **Start URL** radiobutton, and enter your Logi application's URL.
2. Ensure that the **Use default Web server** option is selected.
3. Ensure that the **ASP.NET** debugger option is checked. Click **OK** to save all your settings

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771877911/createpluginnet_05.png)

Finally, in the Solution Explorer, right-click your Logi application web site, and select the **Set as Startup Project** option.

You're now ready to press **F5** (or use the Debug menu) to run your solution and start debugging. The details of setting Watches, Breakpoints and other debugging-related activities are beyond the scope of this topic; refer to your Visual Studio documentation.

If you start debugging and receive the error "...Debugging failed because integrated Windows authentication is not enabled", read this [MSDN article](http://msdn.microsoft.com/en-us/library/x8a5axew(v=vs.110).aspx) for information about configuring the authentication for your Logi app virtual directory.

These settings are for a simple debugging example. Depending on the implementation of your Logi application, such as use of a remote web server, you may need to adjust some of the settings shown above.

## Debug in Visual Studio 2008/2005

You can debug your plug-in as it runs in your Logi app, using Visual Studio (VS). The technique is the same regardless of VS version, with minor differences as noted below. Ensure that you're running VS with a user account that has Administrator privileges.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771878167/createpluginnet_06.png)

Open your plug-in solution in VS and, in the Solution Explorer, select and right-click the root node, then select **Add**  ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778416151/menuarrow.gif)**Existing Web Site...** Browse to and select your Logi application web site (its virtual directory), adding it to your solution.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771878423/createpluginnet_07.png)

Right-click the Logi application site in the Solution Explorer and select its **Property Pages** from the pop-up menu, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771878679/createpluginnet_08.png)

In the Property Pages window, shown above, select the **Build** page in the left menu, and then:

1. Select **No Build** in the list of Start actions.
2. Ensure that the appropriate .NET Framework version for your Logi application is selected.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778711575/createpluginnet_09.png)

Next, select the **Start Options** page in the left menu, as shown above, and then:

1. Select the **Start URL** radiobutton, and enter your Logi application's URL.
2. To run your Logi app using the local IIS server:   
   VS 2008: Select the **Use default Web server** radiobutton.  
   VS 2005: Select the **Use custom server** radiobutton and enter the **Base URL**, as shown above.
3. Check the **ASP.NET** debugger checkbox; click **OK** to save all your settings

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778711831/createpluginnet_10.png)

Finally, in the Solution Explorer, right-click your Logi application web site, and select the **Set as Startup Project** option.

You're now ready to press **F5** (or use the Debug menu) to run your solution and start debugging. The details of setting Watches, Breakpoints and other debugging-related activities are beyond the scope of this topic; refer to your Visual Studio documentation.

If you start debugging and receive the error "...Debugging failed because integrated Windows authentication is not enabled", read this [MSDN article](http://msdn.microsoft.com/en-us/library/x8a5axew(v=vs.80).aspx) for information about configuring the authentication for your Logi app virtual directory.

These settings are for a simple debugging example. Depending on the implementation of your Logi application, such as use of a remote web server, you may need to adjust some of the settings shown above.

## Plug-in Class Methods and Properties

Logi plug-ins for .NET are written in Visual Studio or a similar development tool, using the rdServerObjects class, which resides in the rdPlugin.dll assembly and is a member of the rdPlugin namespace. You instantiate this class in your code and it provides access to the Logi application and its data. The class object is defined in your code as:

[Visual Basic]   
public Class rdServerObjects

[C#]  
public class rdServerObjects

Once instantiated, the object provides the following properties and methods for use with your custom code:

|  |  |
| --- | --- |
| * AddDebugMessage() * [CurrentData](#CurrData) * [CurrentDataFile](#CurrDataFile) * [CurrentDefinition](#CurrDef) * [CurrentElement](#CurrEle) * [CurrentHttpContext](#CurrHttpContext) * [PluginParameters](#PluginParameters) | * [ReplaceTokens()](#ReplTokens) * [Request](#Request) * [ResponseHtml](#RespHtml) * [ReturnedDataFile](#RetDataFile) * [Session](#Session) * [SettingsDefinition](#SettingsDef) |

Here are the object's methods and parameters:

|  |
| --- |
| **AddDebugMessage()** |
| This method inserts an entry into the Debugger Trace Report. (v10.0.337+)  [Visual Basic] Public Sub AddDebugMessage(Optional ByVal CurrentEvent As String,     Optional ByVal ProgramObject As String,     Optional ByVal ObjectValue As String,     Optional ByVal MoreInfo As Object )  [C#] public void AddDebugMessage(string CurrentEvent, string ProgramObject, string ObjectValue, object MoreInfo);  **Parameters**: CurrentEvent - text to be inserted in the Debug Trace page's Event column ProgramObject - text to be inserted in the Debug Trace page's Object column ObjectValue - text to be inserted in the Debug Trace page's Value column MoreInfo - object (XML data or XSL code) that is displayed via link inserted in the Debug Trace page's Value column  The time value for the entry inserted into the Debugger is provided automatically. |

|  |
| --- |
| **CurrentData** |
| Returns an [XmlDocument](http://msdn.microsoft.com/en-us/library/system.xml.xmldocument(v=VS.80).aspx) object containing the data in all of the datalayers.  [Visual Basic] Public CurrentData As System.Xml.XmlDocument  [C#] public System.Xml.XmlDocument CurrentData; |

|  |
| --- |
| **CurrentDataFile** |
| Returns a string object containing of the fully-qualified path and filename for the cache file containing the XML data retrieved by the datalayer.  [Visual Basic] Public CurrentDataFile As String  [C#] public string CurrentDataFile; |

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the list](#MethodList)

|  |
| --- |
| **CurrentDefinition** |
| Returns a string object containing the XML source code of the current report definition.  [Visual Basic] Public CurrentDefinition As String  [C#] public string CurrentDefinition; |

|  |
| --- |
| **CurrentElement** |
| Returns an [XmlElement](http://msdn.microsoft.com/en-US/library/system.xml.xmlelement(v=VS.80).aspx) object containing the XML source code of the current element. Only available when using Data Layer Plugin Call and Procedure.Plugin Call elements.  [Visual Basic] Public CurrentElement As System.Xml.XmlElement  [C#] public System.Xml.XmlElement CurrentElement; |

|  |
| --- |
| **CurrentHttpContext** |
| Returns an [XmlDocument](http://msdn.microsoft.com/en-us/library/system.xml.xmldocument(v=VS.80).aspx) object containing all HTTP-specific information, including Application, Session, Server, Request, and Response objects.  [Visual Basic] Public CurrentHttpContext As System.Web.XmlDocument  [C#] public System.Web.XmlDocument CurrentHttpContext; |

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the list](#MethodList)

|  |
| --- |
| **PluginParameters** |
| Returns a [Hashtable](http://msdn.microsoft.com/en-us/library/system.collections.hashtable(v=VS.80).aspx) object containing the parameters, if any, passed to the plug-in.  [Visual Basic] Public PluginParameters As System.Collections.Hashtable  [C#] public System.Collections.Hashtable PluginParameters; |

|  |
| --- |
| **ReplaceTokens()** |
| Returns a string object containing the sTokens parameter with some or all of its tokens replaced with their current values, and with other optional effects applied. Added in v10.0.337.  [Visual Basic] Public Function ReplaceTokens(ByVal sTokens As String,      Optional ByVal bDuplicateSingleQuotes As Boolean = False,      Optional ByVal eleDataLayerRow As System.Xml.XmlElement,      Optional ByVal bDuplicateBracketedQuotes As Boolean = False,      Optional ByVal bAssumeNonQuotedAsNumeric As Boolean = False,      Optional ByVal TokenList() As String,      Optional ByVal bSqlInjectionGuard As Boolean = False) As String  [C#] public string ReplaceTokens(string sTokens,      bool bDuplicateSingleQuotes,      XmlElement eleDataLayerRow,      bool bDuplicateBracketedQuotes,      bool bAssumeNonQuotedAsNumeric,      string TokenList,      bool bSqlInjectionGuard);  **Parameters**:  sTokens - string containing Logi tokens, such as @Data.LastName~, to be replaced with current values.  bDuplicateSingleQuotes - if *True*, causes any single-quotes in sTokens to be doubled in return string. eleDataLayerRow - XmlElement containing the data that will be used to replace the @Data tokens in sTokens.  bDuplicateBracketedQuotes - if *True*, double-quotes embedded in a token value will be included in return string.  bAssumeNonQuotedAsNumeric - if *True*, replacement processing will handle unquoted, numeric token values as numbers.  TokenList - comma-separated list of token types, indicating the types to be replaced; other types will be skipped.  bSqlInjectionGuard - if *True*, replacement processing checks all token values for potentially dangerous SQL strings. |

|  |
| --- |
| **Request** |
| Returns an [HttpRequest](http://msdn.microsoft.com/en-US/library/system.web.httprequest(v=VS.80).aspx) object, which can be used to access HTTP Request values sent by the client to a Logi application.  [Visual Basic] Public Request As System.Web.HttpRequest  [C#] public System.Web.HttpRequest Request; |

|  |
| --- |
| **ResponseHtml** |
| Returns a String object containing the HTML for the rendered response page; available when the *FinishHtml* event completes.  [Visual Basic] Public ResponseHtml As String  [C#] public String ResponseHtml; |

|  |
| --- |
| **ReturnedDataFile** |
| Returns a String object containing the fully-qualified path and filename for the cache file which contains the manipulated XML data after processing.  [Visual Basic] Public ReturnedDataFile As String  [C#] public string ReturnedDataFile; |

|  |
| --- |
| **Session** |
| Returns an [HttpSessionState](http://msdn.microsoft.com/en-US/library/system.web.sessionstate.httpsessionstate(v=VS.80).aspx) object, which can be used to access Session variable values related to the current Logi application session.  [Visual Basic] Public Session As System.Web.SessionState.HttpSessionState  [C#] public System.Web.SessionState.HttpSessionState Session; |

|  |
| --- |
| **SettingsDefinition** |
| Returns a read-only [XmlDocument](http://msdn.microsoft.com/en-us/library/system.xml.xmldocument(v=VS.80).aspx) object containing the XML of the \_Settings definition.  [Visual Basic] Public ReadOnly Property SettingsDefinition() As System.Xml.XmlDocument   [C#] public System.Xml.XmlDocument SettingsDefinition; |

Keywords: plugin, plugins
