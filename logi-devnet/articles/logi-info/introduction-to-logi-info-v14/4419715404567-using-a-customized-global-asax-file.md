---
title: "Using a Customized Global.asax File"
id: 4419715404567
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715404567-Using-a-Customized-Global-asax-File
updated_at: 2022-07-17T01:42:34Z
---

# Using a Customized Global.asax File

# Using a Customized Global.asax File

Each Logi application includes a file named Global.asax, which is standard in ASP.NET applications.
*This file is compiled in our Java products and is not accessible for customization.*
As distributed, it contains only one line of code. However, event handlers can be placed here which react to ASP.NET object events, such as Application\_BeginRequest and Session\_Start.

Here's a sample:

<%@ Application Codebehind="Global.asax.vb" Inherits="rdWeb.Global" %>  
<script language="VB" runat="server">  
  
Sub Session\_Start(ByVal sender As Object, ByVal e As EventArgs)  
Dim rdServer As New rdServer.rdSession()  
Dim myURLQStr As String = "rdProcess.aspx?rdProcess=myProcessDef&rdTaskID=mySessionStart"  
  
' start the new session  
' if session already exists, does nothing  
Call rdServer.SessionStart()  
  
' test flag to see if session has already been started  
 ' if not, then do the redirect to the process task  
If Session("myStartFlag") = Nothing  
  
' save original query string to session variable for later access  
Session("myQueryString") = Request.QueryString.ToString()  
  
 ' redirect to Process task: mySessionStart  
 Response.Redirect(myURL)  
  
' set session counter  
 Session("myStartFlag") = 1  
  
End If  
End Sub  
</script>  
In the example VB code above, the user is automatically redirected to a Process task called "mySessionStart" when a new session is started. The URL defined as "myURL" is a relative address, and therefore doesn't need the "http://..." part of the address.
So, as another example of how to assign dynamic datasource connection strings, the code above could be adjusted to assign a connection string to a session variable and then call a Logi report.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The two lines of code that reference the **rdServer** object *are required*, or your application will not start.
**Caveat**: this example is offered here for consideration by experienced ASP.NET developers but custom code written by developers is outside the scope of our typical support offerings.
