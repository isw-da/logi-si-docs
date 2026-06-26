---
title: "Launch Logi Applications for Info"
id: 1500009531381
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531381-Launch-Logi-Applications-for-Info
updated_at: 2021-06-17T01:58:31Z
---

# Launch Logi Applications for Info

# Launch Logi Applications for Info

This topic provides developers with information about techniques available to them for launching their Logi applications and for customizing them through configuration files.

* Introduction
* [Call a Report via URL](#Report)
* [Call a Process Task via URL](#Process)
* [Use Dynamic Connections](#Connections)
* [Use a Customized Global.asax File](#GlobalAsax)
* [Use a Customized Web.config File](#WebConfig)

## Introduction

Logi reports are simply web pages and, as such, they can be accessed by entering the appropriate URL in your browser. However, there are other methods for accessing reports and related Logi application features, which are discussed here. Security is not part of this discussion, though authenticated user information can be included via session variables using the same techniques.

## Call a Report via URL

Traditionally, a Logi report is called by entering the appropriate URL in a browser. This can be done manually by typing it right into the browser's address bar or it can be done via any valid HTTP link in a different Logi report, or in an entirely separate web page or application. The basic URL for a Logi report takes this form:

http://localhost/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport

http://www.yourWebSite.com/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport

The first example above is a URL that might appear on a development computer; the second, on a production server, where

* The **rdPage.aspx** page denotes that a Logi report definition is to be processed
* The **rdReport** argument value is the name of the Logi report definition file to be processed
* Additional request parameter name-value pairs can be included in the URL with separating ampersands (&).

More information about passing data in the URL's query string can found in [Pass Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009531481-Pass-Information).

### Specify Report Format or Template

You can also specify a **report format** in the query string in order to output the report in different ways. This is done using the reserved word **rdReportFormat**, as follows:

http://localhost/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport&rdReportFormat=PDF

When the example URL shown above is browsed, the report mySalesReport will be output into the browser as a PDF document. When you use this reserved word, ensure that you also use the rdReport name-value pair (in other words, don't rely on a report being the default report in your application and leave rdReport out of the URL). Other values for rdReportFormat include *NativeExcel*, *NativeWord*, *CSV*, *HtmlExport*,
*HtmlEmail*, *Excel*, *Word*, *XML*,
or *GoogleSpreadsheet.*

Similarly, you can use **rdTemplate** instead of rdReport to identify an Excel, Word, or PDF template definition to be run from a URL.

Learn more about the reserved words that can be used in a URL for special purposes in [Query String Parameter Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009531621-Query-String-Parameter-Reference).

### Use a Constant in a URL

If you're using a URL within a Logi report definition to call another report, for example, by using Action.Link, you can use a **constant** and its token to provide part or all of the URL.

Suppose, for example, you've assigned the first part of the URL "http://www.yourWebSite.com" to a constant called SiteURL, in the application's \_settings definition. The URL used to call another report or web page can then make use of that constant by using its token:

@Constant.SiteURL~/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport

An arrangement like this will let you run development and production versions of an application that differ only in the value of the SiteURL constant.

## Call a Process Task via URL

If you're a **Logi Info** developer, the entry point for a Logi application does not have to be a report. Logi Info includes **Process tasks** and your application can be launched through a process definition rather than a report definition.

http://www.yourWebSite.com/yourLogiAppName/rdProcess.aspx?rdProcess=myProcessDef&rdTaskID=ShowMenuPage

The example URL shown above can be used to directly call a Process task, where

* The **rdProcess.aspx** page denotes that a Logi process definition is to be processed.
* The **rdProcess** argument value is the name of the Process definition file to use
* The **rdTaskID** argument value is the name of the Process task to run

This approach can be very useful if you want do logging, or send notifications, or accomplish any of a number of other activities that need to be done before showing the user the first report page.

Use of a Response.Link element with a URL is also the only way to have one Process task call another Process task.

As always, when working with tasks, ensure that you have a final Response.Report element that's processed at the end of the task or your user will be left seeing nothing but a blank page.

## Use Dynamic Connections

Developers often want to make their datasource connection strings dynamic, based on some external criteria at launch, and this has to occur before report definitions are processed. There are several ways to accomplish this:

### Duplicate \_settings Definitions

If the motivation for this it to duplicate the application in several different environments (development, QA, production) but minimize changes that need to be made when moving reports through them, then the easiest approach is simply to deploy copies of all Logi application files to the different servers. Connection element **IDs** remain the same across all the \_settings definitions, but their connection string attribute values are different, as appropriate for each server. This means that
report definitions that use the connections will run on any of the servers without having to be modified. Any of the other values in \_settings, such as the Application Path, can be similarly configured.

## Use Session Variables

If you're using some other application that eventually calls a Logi application, you can use **session variables** to set the connection strings (or other values found in the \_settings definition) in the Logi application. Set these variables in the main application, and in your Logi application's \_settings definition, use @Session tokens for the values of your connection string, path, and other settings. When the Logi application is called, it will resolve these tokens into values and run the reports
based on them.

## Use Plug-ins

"Plug-ins", which are DLL's, give Logi developers the ability to
**programmatically****extend** the functionality of their Logi
applications. With them, developers can dynamically change the behavior of Logi reports at
runtime by accessing *request* and *session* variables and modifying report definitions. To support dynamic connection strings, a Plugin Call element is used in the \_settings definition to retrieve the connection string (or other values) from a session variable and then it dynamically modifies the \_settings definition by inserting the connection string value. The plug-in runs on the LoadDefinition event and so alters the definition before it's processed. Learn more about plug-ins in
[Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009531221-Logi-Plug-ins).

## Use a Customized Global.asax File

Each Logi application includes a file named Global.asax, which is standard in ASP.NET applications.

*This file is compiled in our Java products and is not accessible for customization.*

As distributed, it contains only one line of code. However, event handlers can be placed here which react to ASP.NET object events, such as Application\_BeginRequest and Session\_Start. Here's a sample:

|  |  |
| --- | --- |
|  | <%@ Application Codebehind="Global.asax.vb" Inherits="rdWeb.Global" %>   <script language="VB" runat="server">  Sub Session\_Start(ByVal sender As Object, ByVal e As EventArgs)    Dim rdServer As New rdServer.rdSession()    Dim myURLQStr As String = "rdProcess.aspx?rdProcess=myProcessDef&rdTaskID=mySessionStart"     ' start the new session     ' if session already exists, does nothing    Call rdServer.SessionStart()     ' test flag to see if session has already been started     ' if not, then do the redirect to the process task    If Session("myStartFlag") = Nothing        ' save original query string to session variable for later access        Session("myQueryString") = Request.QueryString.ToString()        ' redirect to Process task: mySessionStart       Response.Redirect(myURL)        ' set session counter        Session("myStartFlag") = 1      End If  End Sub  </script> |
|  |  |

In the example VB code above, the user is automatically redirected to a Process task called "mySessionStart" when a new session is started. The URL defined as "myURL" is a relative address, and therefore doesn't need the "http://..." part of the address.

So, as another example of how to assign dynamic datasource connection strings, the code above could be adjusted to assign a connection string to a session variable and then call a Logi report.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) Note that the two lines of code that reference the **rdServer** object *are required*, or your application will not start.

**Caveat**: this example is offered here for consideration by experienced ASP.NET developers but custom code written by developers is outside the scope of our typical support offerings.

## Use a Customized Web.config File

Each Logi application includes a file named Web.config, which is standard in ASP.NET applications.

*This text file is accessible for customization in both our .NET and our Java products.*

You can add the following section to it for connection strings:

|  |  |
| --- | --- |
|  | <connectionStrings>    <addname="myConnString"connectionString="Server=xxx; Port=nnnn; Database=xxx; uid=xxx; pwd=xxx;"/></connectionStrings> |

Under the .NET framework there are classes and methods specifically for reading from this file. In Java, a stream reader of some kind must be used. In both cases, this can be done from within one of the plug-ins described above in order to extract the connection string data and modify the \_settings definition at runtime.

The .NET framework also provides a mechanism for encrypting connection strings so that they're not held in plain text in this file.
