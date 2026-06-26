---
title: "Configuring the Parent Application"
id: 4406822453143
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822453143-Configuring-the-Parent-Application
updated_at: 2022-04-06T06:07:53Z
---

# Configuring the Parent Application

# Configuring the Parent Application

The Parent application is responsible for authenticating the user (the "single sign-on") when they first connect. The authentication process should produce a valid **user ID** and optional lists of Roles (which correspond to Roles established in the Logi application) and/or Rights.

The ClientBrowserAddressquery string valueis no longer required.

When the user first requests a report or web page from the Logi application, the Parent application issues a SecureKey request to the Logi application's authentication service, using this basic format:

http://my*Server*/my*LogiApp*/rdTemplate/rdGetSecureKey.aspx?Username=*bob*&ClientBrowserAddress=*192.168.4.75*

The URL may also optionally include a list of Roles and/or Rights, using this format:

http://*myServer*/*myLogiApp*/rdTemplate/rdGetSecureKey.aspx?Username=*bob*&ClientBrowserAddress=*192.168.4.75*&Roles=*Worker,Manager*&Rights=View,Update,Delete

The rdGetSecureKey.aspx service called in the URL expects or accepts these standard query string values in the URL:

| Parameter | Description |
| --- | --- |
| Username | (Required) The user ID authenticated during the single sign-on process. In your Logi application this can be referenced using @Function.Username~. This token is available for the current user's session and may be referenced in any Logi definition file, including within other child elements of Security, such as Roles and/or Rights. |
| ClientBrowserAddress | (Required) The IP address of the requesting user's computer. This IP address is *not* the address of the Parent application server. In the Parent application, this IP address should be determined dynamically; in the example code provided below, for example, the address is determined using Request.UserHostAddress. This query string valueis no longer required. For Java applications, this *must* be in IPv4 format (such as 127.0.0.1) and, if the server supports both IPv4 and IPv6, you may need to force the IPv4 connection by setting this Java Option:  -Djava.net.preferIPv4Stack=true. See [Working within NAT or Proxy Environments](https://devnet.logianalytics.com/hc/en-us/articles/4406817741719-Working-within-NAT-or-Proxy-Environments) for additional information relevant to NAT or proxy environments. |
| Roles | (Optional) A comma-separated list of the security roles for this user, determined during the single sign-on process. This comma-separated list becomes your list of Logi application user Roles. The list can be referenced using @Function.UserRoles~ throughout the Logi application, and may be used to assign user rights within the security element. |
| Rights | (Optional) A comma-separated list of the security rights for this user, determined during the single sign-on process. This comma-separated list becomes your list of Logi application user Rights. The list can then referenced as @Function.UserRights~ throughout the Logi application. |

You may also create your own custom query string variables to send other information into the Logi application:

http://*myServer*/*myLogiApp*/rdTemplate/rdGetSecureKey.aspx?Username=*bob*&ClientBrowserAddress=*192.168.4.75&*Roles=*Worker,Manager&myCustomParam1=10&myCustomParam2=120*

These extra values will be assigned to session variables in the Logi application and can be accessed using @Session tokens. For example, @Session.myCustomParam1~ would equal 10 and @Session.myCustomParam2~ would equal 120.
Remember
that theses tokens are case-sensitive and you will need to match the spelling in the query string *exactly* when using them.

The ClientBrowserAddress query string valueis no longer required.

## Using POST vs GET

For additional security, or if you have a lot of custom query string variables or really long values, you may elect to POST the URL and its query parameters. The Logi application will examine the HTTP request for them automatically, regardless of whether they were sent using HTTP POST or GET.

## Using the SecureKey

The Logi application's authentication service returns a SecureKey to the Parent application, which then *redirects* the user's request to the Logi application, passing the SecureKey as an additional query string parameter. The URL for this redirect will look something like this, using the two keywords *rdReport* and *rdSecureKey*:

http://m*yServer*/my*LogiApp*/rdPage.aspx?**rdReport**=my*DesiredReport*&**rdSecureKey**=*1a34c56f7b89*

## Sample Code

The following Visual Basic.NET code provides an example of the two things you'll need to do in a Parent application: request a SecureKey and redirect the user's report request using the SecureKey.

Your Parent application may have multiple links to the Logi application, so the following code is an example of a function that can be called from the click event handlers for any of those links. It assumes the user name, user Roles, and user Rights have been placed into session variables as part of the login authentication process and that the Logi application base URL has been specified in the Web.config file.

Public Function getSecureKey() As String  
  
' define parts of the SecureKey request URL  
' Logi application base URL is set in Web.config file  
Dim strLogiAppBaseURL As String = ConfigurationManager.AppSettings("LogiAppBaseURL")  
Dim strGetKeyURL As String = "/rdTemplate/rdGetSecureKey.aspx?Username=" & Session("UserName") & "&Roles="\_  
 & Session("UserRoles") & "&Rights=" & Session("UserRights")  
Dim strClientAddr As String = "&ClientBrowserAddress=" & Request.UserHostAddress  
  
' define web request and response receiver  
Dim webRequest As Net.HttpWebRequest  
Dim webResponse As Net.WebResponse|  
webRequest = Net.HttpWebRequest.Create(strLogiAppBaseURL & strGetKeyURL & strClientAddr)  
  
' send the SecureKey request to the Logi app  
Try  
webResponse = webRequest.GetResponse()  
Catch ex As Exception  
' if server has Basic or NTLM authentication, try to set creds from the current process  
If ex.Message.IndexOf("401") <> -1 Then  
webRequest.Credentials = Net.CredentialCache.DefaultCredentials  
webResponse = webRequest.GetResponse()  
Else  
Throw ex  
End If  
End Try  
  
' receive the response and return it as function result  
Dim sr As New IO.StreamReader(webResponse.GetResponseStream())  
getSecureKey = sr.ReadToEnd()  
  
End Function

The event handler code for the links to the Logi application might look like this:

Protected Sub lbtnReports\_Click(ByVal sender As Object, ByVal e As EventArgs) Handles lbtnReports.Click  
  
' identify the Logi report definition to be displayed by this menu item or link  
Dim strLogiDefName As String = "Default"  
  
' get the Logi application base URL, which is set in the Web.config file  
Dim strLogiAppBaseURL As String = ConfigurationManager.AppSettings("LogiAppBaseURL")  
  
' get a SecureKey for this request  
Dim strSecureKey As String = getSecureKey()  
  
'redirect to Logi app  
Response.Redirect(strLogiAppBaseURL & "/rdPage.aspx?rdReport=" & strLogiDefName \_  
 & "&rdSecureKey=" & strSecureKey)  
  
End Sub

Additional coding examples in other languages are available in [SecureKey Coding Examples](https://devnet.logianalytics.com/hc/en-us/articles/4406822502167-SecureKey-Coding-Examples).

## Debugging SecureKey Requests

It can be very helpful, when developing applications, to view the information being sent between the Parent application and the Logi application during the SecureKey request.

To do this, temporarily provide a value for the Security element's **SecureKey Shared Folder**. This will cause SecureKeys to appear there as XML files, so you can see when they're created. You can open and examine them in order to determine what's being passed in the SecureKey requests.

We also offer a SecureKey test program (.NET environment only) which is available for download from DevNet; it displays the SecureKey information in a test exchange: <https://clm.logianalytics.com/downloads/info/TestSecureKey.zip>
