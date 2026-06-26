---
title: "Standard Logi Application Files"
id: 4419707739415
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707739415-Standard-Logi-Application-Files
updated_at: 2024-01-02T19:05:00Z
---

# Standard Logi Application Files

# Standard Logi Application Files

You'll find these standard files in an application root folder; *do not* remove, rename, or alter them:

* **rdChart.aspx** - Builds and displays charts
* **rdPage.aspx** - Displays report definitions
* **rdProcess.aspx** - Processes tasks contained in process definitions
* **rdErrorLog** - Error logs (only present if Error Logging has been turned on)
* **rdDebug.aspx** - Generates and displays debug output (made obsolete in v10.0.259+).

Each Logi application also includes several standard files that you *can* customize, described below:

##### Default.aspx

The default web page registered with the web server is Default.aspx:

<%@ Page Language="vb" %>  
<%  
 Dim sQueryText as String  
 If Request.RawUrl.indexof("?") <> -1 Then   
 sQueryText = Request.RawUrl.substring(Request.RawUrl.indexof("?"))  
 End If  
 Response.Redirect("rdPage.aspx" & sQueryText)  
 %>

The code above redirects users to rdPage.aspx; the main web page for displaying report definitions. You can replace the contents of Default.aspx with your own HTML. Any query string parameters submitted with the URL are also passed to rdPage.aspx. For example, the following links take viewers to the same location:

http://www.Logiapps.com/LogiReportSamples/WebService/Default.aspx?ZipCode=90210&Miles=25

http://www.Logiapps.com/LogiReportSamples/WebService/**rdPage.aspx**?ZipCode=90210&Miles=25

##### Global.asax:

You can create your own Global.asax files for integrated Logi applications.

Sub Application\_Start(ByVal sender As Object, ByVal e As EventArgs)  
Dim rdMaint As New rdMaint.Maintenance()  
rdMaint.AppStart()  
 End Sub

Sub Session\_Start(ByVal sender As Object, ByVal e As EventArgs)  
Dim rdServer As New rdServer.rdSession()  
Call rdServer.SessionStart()  
 End Sub

The Application\_Start and Session\_Start event handlers are customizable but *must* be present and, at a minimum, contain the code shown above.

##### rdLogon.aspx:

All Logi applications are provided with a basic login page, which is used if Logi Security is enabled:

![](https://devnet.logianalytics.com/hc/article_attachments/7522792733463/appoverview_06.png)

However, you can completely customize the rdLogon.aspx page and even rename the file. The following HTML tags for the login form are required to be present:

* <form id=frmLogon action='<%=Session("rdLogonReturnUrl") %>' method=post>
* <input id="rdUsername" type="text" size="20" name="rdUsername">
* <input id="rdFormLogon" type="hidden" name="rdFormLogon" value="True">
* <input id="rdPassword" type="password" size="20" name="rdPassword">
* <%=Session("rdLogonFailMessage") %>

Assuming that Logi Security is being used, you can present a custom logon page by configuring it in \_Settings:

![](https://devnet.logianalytics.com/hc/article_attachments/7522838538775/appoverview_05.png)

1. Open the \_Settings definition to view its elements, as shown above.
2. Select the **Security** element.
3. Select the **Logon Page** attribute and enter the filename of your custom login page.

##### 

##### Web.config:

The Web.config file contains many useful settings for the entire Logi application. However, the Web.config file for a Logi application is *not the standard version* found in most ASP.NET applications and replacing it with a standard file will produce unpredictable results. Therefore, integrating a Logi application with another ASP.NET application has to be done in such a way that their Web.config files do not interact with or supercede each other. Generally speaking, we *do not* recommend that such
an integration
be accomplished by physically merging the application files and folders.

Having said that, the Web.config file is an XML file that you can modify to customize authentication, impersonation, globalization, session-state settings, error messages, and more. For Logi .NET applications, many configuration settings made in IIS Manager are written directly into Web.config, and any customized settings in Web.config always override similar settings in IIS Manager. More information about the Web.config file is available at this [Microsoft web page](https://docs.microsoft.com/en-us/previous-versions/ms178684(v=vs.140)?redirectedfrom=MSDN).

##### Definition Files

In Logi Info, elements are combined in *definitions* to build web-based applications. One *report definition* is equivalent to one dynamic web page. Every Logi application contains at least one report definition and can include multiple definitions as the application grows.

![](https://devnet.logianalytics.com/hc/article_attachments/7522796753559/appoverview_03.png)

The example above shows Logi Studio's Application Panel and the seven major types of definition files found in Logi applications, which are described below:

| Folder/Definition | Description |
| --- | --- |
| \_Settings | (Required) The one [The \_Settings Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723151767-The-Settings-Definition) in every Logi application contains global configuration values for the entire application. It contains elements that define the application's virtual path, debugging capabilities, database connections, security information, and more. |
| Reports | Contains report definitions built with elements that define a dynamic web pages. A report definition typically contains report header and footer elements and a body element. The main body of the report can include any combination of text, charts, Dashboards, Data Tables, user input controls, etc. In the file system, this folder is <appRoot>/\_Definitions/\_Reports |
| Mobile Reports | Contains report definitions that are used exclusively to deliver content to mobile devices, built with a combination of common and special-purpose elements. In the file system, this folder is <appRoot>/\_Definitions/\_MobileReports |
| Widgets | Contains definitions for a special class of Logi reports that can be independently embedded into external HTML pages. In the file system, this folder is <appRoot>/\_Definitions/\_Widgets |
| Templates | Contains definitions that allow you to take advantage of forms-based reporting, using Word, Excel, and PDF forms. Template definitions model the "fill-able" form fields contained within the source template file. In the file system, this folder is <appRoot>/\_Definitions/\_Templates |
| Processes | Contains definitions that provide a level of automation and contain the logic needed to perform specific tasks within an application. Process tasks can be used to perform scheduled operations, such as exporting a report to PDF format or then emailing it to a group of recipients. In the file system, this folder is <appRoot>/\_Definitions/\_Processes |
| Data | Contains definitions that retrieve data and provide it as a JSON stream, for use by a variety of consumers, including non-Logi applications. In the file system, this folder is <appRoot>/\_Definitions/\_Data |

##### From XML to HTML...

Every definition file created with Logi Studio is an XML document, which describes multiple objects we call *elements* and their *attributes*. Elements encapsulate different types of functionality and presentation; attributes enable you to customize element properties and behavior. For example, a DataLayer element retrieves data from a data source and a Chart.Pie element creates a pie chart from the data. The Chart.Pie element contains attributes to specify the
height,
width, color, border,
and more.

![](https://devnet.logianalytics.com/hc/article_attachments/7522796765591/appoverview_04_830x230.png)

Here's an example of a simple report that illustrates elements work:

The image above left shows an example report definition, named "newReport", in Logi Studio. The report contains **Style** and **Body** elements. The Body element has a "child" element beneath it: a **Label** element, which has a **Caption** attribute.

The middle image shows the underlying XML source code for this collection of elements, as seen in Logi Studio's Source tab. You can edit this source code directly but we don't recommend it.

The Logi Server Engine processes the XML source code, generating the HTML needed to present the page in Studio's Preview tab, which is shown in the right image.
