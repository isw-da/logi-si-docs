---
title: "SecureKey Code Examples"
id: 1500009515902
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515902-SecureKey-Code-Examples
updated_at: 2021-06-17T01:58:36Z
---

# SecureKey Code Examples

# SecureKey Code Examples

The topic is provided to help developers who are writing applications that will call a Logi application using Logi SecureKey Authentication. Language examples include:

* General Information
* [C# (.NET)](#CSharp)
* [Visual Basic (.NET)](#VB)
* [Java](#Java)
* [Node](#Node)
* [Perl](#Perl)
* [Ruby](#Ruby)

## General Information

Logi **SecureKey Authentication** is a technology we offer for use in "single sign-on" scenarios, where a non-Logi application (the "Parent" application), which conducts the initial user authentication, is integrated with a Logi application. SecureKey Authentication provides a method of securely accessing the integrated Logi app, and is discussed in detail in [Use Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/1500009515922-Use-Logi-SecureKey-Authentication).

This topic provides examples of the Parent application code required to establish the flow of secure exchanges with a Logi application using SecureKey.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) The examples, in several languages, are very generic and are only intended to provide the basic, necessary code. They're provided with the assumption that developers who undertake using them and extending their functionality have in-depth skills with the language selected. Other languages can also be used and success with them will, again, depend on the developer's
skills.

## C# (.NET)

The following code example is written in C#, for use with the .NET framework:

```
1. /* set up the SecureKey call */
2. // define parts of the SecureKey request URL
3. string strLogiAppBaseURL = "http://<yourServer>/<LogiApp>";
4. string UserName = "Bob";
5. string Roles = "Admin";
6. string Rights = "Manager";
7. string ClientBrowserAddress = Request.ServerVariables["REMOTE_ADDR"];

9. // build complete URL to Logi app
10. string sGetKeyURl = "/rdTemplate/rdGetSecureKey.aspx?Username=" + UserName + "&Rights=" + Rights  + "&Roles=" +  Roles + "&ClientBrowserAddress=" + ClientBrowserAddress;
11. string sFinalURL = strLogiAppBaseURL + sGetKeyURl;

13. // create and send SecureKey request
14. string sKey = "";
15. HttpWebRequest webRequest = (HttpWebRequest)HttpWebRequest.Create(sFinalURL);
16. HttpWebResponse webResponse;

18. // attempt to make SecureKey call, read return into sKey
19. try
20. {
21. webResponse = (HttpWebResponse)webRequest.GetResponse();
22. Stream myStream;
23. myStream = webResponse.GetResponseStream();
24. StreamReader sr = new StreamReader(myStream);
25. sKey = sr.ReadToEnd();
26. }
27. catch (Exception ex) // if not bad URL, send error message
28. {
29. if (ex.Message.IndexOf("401") != -1)
30. {
31. Response.Write("Not Found");
32. }
33. else
34. {
35. Response.Write(ex.Message.ToString());
36. }
37. }
```

## Visual Basic (.NET)

The following code example is written in Visual Basic, for use with the .NET framework:

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
11. Dim sFinalURL As String = strLogiAppBaseURL & strGetKeyURL

13. ' define web request and response receiver
14. Dim webRequest As Net.HttpWebRequest
15. Dim webResponse As Net.WebResponse|
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

## Java

The following code example is written in Java, for use with a JSP file:

```
1. <%@ page language="java" import="java.util.*,java.net.*,javax.servlet.*,java.io.*" %>

3. <%
4. // set up the SecureKey call
5. // define parts of the SecureKey request URL
6. String LogiAppURL;
7. String Username;
8. String Roles;
9. LogiAppURL = "http://<yourServer>/<LogiApp>";
10. Username = "Bob";
11. Roles = "1";

13. // build complete URL to Logi app
14. String getKeyURL = "/rdTemplate/rdGetSecureKey.aspx?Username=" + URLEncoder.encode(Username) + "&Roles=" + URLEncoder.encode(Roles) + "&ClientBrowserAddress=" + URLEncoder.encode(request.getRemoteAddr());
15. String finalURL = LogiAppURL + getKeyURL;

17. // back-end handshake, passing username, roles and rights to Logi app
18. URL url = new URL(response.encodeRedirectURL(finalURL));

20. // attempt to make SecureKey call
21. try {
22. // open the connection
23. URLConnection conn = url.openConnection();
24. conn.setDoOutput(true);

26. // debugging aid: use StreamWriter to write POST data
27. // OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
28. // wr.write(data);
29. // wr.flush();
30. // wr.close();

32. // get the response
33. BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
34. StringBuffer sb = new StringBuffer();
35. String line;
36. while ((line = rd.readLine()) != null) {
37. sb.append(line);
38. }
39. rd.close();

41. // set the url with the retrieved SecureKey parameter
42. LogiAppURL = LogiAppURL + "/rdPage.aspx?rdSecureKey=" + sb.toString();

44. // redirect to the application with SecureKey parameter
45. response.sendRedirect(LogiAppURL);
46. }
47. catch (Exception e) {
48. throw new Exception("Failed to get SecureKey, request URL: [" + url + "], POST data: [" + data +"]", e);
49. }
50. %>
```

## Node.js

The following code example is written in Node.js:

```
1. var express = require("express");
2. var http = require("http");
3. var app = express();

5. var LogiAppURL = "http://<yourServer>/<LogiApp>";
6. var UserName = "Bob";
7. var Roles = "Admin";
8. var Rights = "Manager";
9. var MessageBack = "";

11. /* create an app to listen on the port # specified in the app arg */
12. app.get("*", function(req, resM) {

14. /* send the SecureKey request */
15. http.get(LogiAppURL + "/rdTemplate/rdGetSecureKey.aspx?"Username=" + UserName + "&Roles=" + Roles + "&Rights=" + Rights + "&ClientBrowserAddress=" + resM.connection.remoteAddress, function(res) {

17. /* when the key is returned */
18. res.on("data", function(chunk) {
19. MessageBack = chunk;

21. /* send a response to the browser (using our Embedded Report API in this example) */
22. resM.send("<p style=\"font-size:20px;text-align:center;\" > This is a node page </p> <div id=\"divNd\" data-autoSizing=\"all\" data-applicationUrl=\"' + LogiAppURL + '\" data-report=\"Default\" data-linkParams=\"{'rdSecurekey' : '" + MessageBack + "'}\" > </div> <script src=\"' + LogiAppURL + '/rdTemplate/rdEmbedApi/rdEmbed.js\" type=\"text/Javascript\"></script>"
    );
23. });

25. /* server-side error logging */
26. }).on('error', function(e) {
27. console.log("Got error: " + e.message);
28. });
29. });

31. console.log("Web application opened.");
32. app.listen(1337);
```

## Perl

The following code example is written in the [Perl](http://www.perl.org/) language:

```
1. #!/usr/local/bin/perl

3. # Requires LWP to be installed
4. use LWP::Simple;

6. # define parts of the SecureKey request URL
7. my $logiAppUrl = 'http://<yourServer>/<LogiApp>';
8. my $user = 'Bob';
9. my $role = 'Admin';
10. my $rights = 'Manager';
11. my $clientAddress = print $ENV{REMOTE_ADDR};

13. # build complete URL to Logi app
14. my $url = $logiAppUrl . '/rdTemplate/rdGetSecureKey.aspx?Username=' . $user . '&Role=' . $role . '&Rights=' . $rights . '&ClientBrowserAddress=' . $clientAddress;

16. # make the SecureKey call and get the response
17. my $response = get $url;

19. # The response should be used as the rdSecureKey parameter value in HTML or Javascript in a Div or iFrame
20. print $response;
```

## Ruby

The following code example is written in the [Ruby](http://www.ruby-lang.org/) language:

```
1. require 'net/http'

3. # define parts of the SecureKey request URL
4. LogiAppURL = "http://<yourServer>/<LogiApp>"
5. username = "Bob"
6. roles = "Admin"
7. rights = "Manager"
8. clientaddr = Socket.unpack_sockaddr_in(socket.getpeername) >> ip  # ruby v1.9

10. # build complete URL to Logi app
11. getKeyURL = "/rdTemplate/rdGetSecureKey.aspx?Username=" << username << "&Rights=" << rights+ "&Roles=" <<  roles << "&ClientBrowserAddress=" << clientaddr
    finalURL = LogiAppURL << getKeyURL

13. # make the SecureKey call and get the response
14. result = Net::HTTP.get_response(URI.parse(finalURL))
15. sKey = result.body
16. print sKey
```
