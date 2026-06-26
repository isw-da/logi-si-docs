---
title: "Visual Basic (.NET)"
id: 4406817829015
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817829015-Visual-Basic-NET
updated_at: 2022-04-06T06:08:27Z
---

# Visual Basic (.NET)

# Visual Basic (.NET)

The following code example is written in Visual Basic,for use with the .NET framework:

```
1. ' set up the SecureKey call
2. ' define parts of the SecureKey request URL
3. Dim strLogiAppBaseURL As String = "http://<yourServer>/<LogiApp>"
4. Dim strUserName = "Bob"
5. Dim strUserRoles = "Admin"
6. Dim strUserRights = "Manager"
7. Dim strClientBrowserAddr As String = Request.UserHostAddress

9. ' build complete URL to Logi app
10. Dim strGetKeyURL As String = "/rdTemplate/rdGetSecureKey.aspx?Username=" & strUserName & "&Roles=" & strUserRoles & "&Rights=" & strUserRights & "&ClientBrowserAddress=" & strClientBrowserAddr
11. Dim strFinalURL As String = strLogiAppBaseURL & strGetKeyURL

13. ' define web request and response receiver
14. Dim webRequest As Net.HttpWebRequest
15. Dim webResponse As Net.WebResponse
16. webRequest = Net.HttpWebRequest.Create(strFinalURL)

18. ' attempt to make SecureKey call
19. Try
20. webResponse = webRequest.GetResponse()
21. Catch ex As Exception
22. ' if server has Basic or NTLM authentication, try to set credentials from the current process
23. If ex.Message.IndexOf("401") <> -1 Then
24. webRequest.Credentials = Net.CredentialCache.DefaultCredentials
25. webResponse = webRequest.GetResponse()
26. Else
27. Throw ex
28. End If
29. End Try

31. ' receive the response and return it as function result
32. Dim sr As New IO.StreamReader(webResponse.GetResponseStream())
33. getSecureKey = sr.ReadToEnd()
```
