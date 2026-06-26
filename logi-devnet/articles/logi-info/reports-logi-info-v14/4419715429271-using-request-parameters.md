---
title: "Using Request Parameters"
id: 4419715429271
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715429271-Using-Request-Parameters
updated_at: 2022-07-17T01:40:29Z
---

# Using Request Parameters

# Using Request Parameters

Logi reports and processes are called using URLs, which may include a Query String. The most common method of passing information in Logi applications is with **request parameters**, using the HTTP "GET" method. This is a example of a URL for a Logi report:

http://www.myReportSite.com/myApp/rdPage.aspx?rdReport=OrdersReport&addRecord=True

and for a Logi process:

http://www.myReportSite.com/myApp/rdProcess.aspx?rdProcess=SiteTasks&rdTaskID=MemberLogin&UID=123

Both examples contain a **Query String** (the portion after the "?") which consists of multiple name and value pairs connected with an equals sign (e.g. UID=123) and separated by an ampersand. These name-value pairs are the request parameters.

Any application, whether web- or desktop-based, Logi application or not, that can redirect a user on the basis of a URL can make use of request parameters in the query string to pass information to a Logi report or process task definition.

## Using Link Parameters

Information can be passed from one report or process to another using request parameters. This can happen either automatically (see [Accessing User Input Values](https://devnet.logianalytics.com/hc/en-us/articles/4419707770775-Accessing-User-Input-Values)) or explicitly through the use of the **Link Parameters** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707016727/passinfo_01.png)

The example above shows a report definition with a **Button** element that calls another report when clicked. The Action.Report element has two child elements: **Target.Report**, which specifies the report being called, and a Link Parameters element.

Parameters and their attributes entered in the Link Parameters element wind up as request parameters in the **query string** used to call the next report or process task. Look at the earlier sample report URL and the example above; note how the Link Parameters attribute name and value becomes a request parameter key-value pair.

In the report called when the Button is clicked (the target report) the request parameter information can be accessed using @Request tokens. The format of the token is @Request.<*LinkParameterName>~*

In the case of the example above, the token @Request.addRecord~ would have a value of *True*. Tokens are case-sensitive so careful spelling is required when using them.

[Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4419715492631-Token-Reference) provides additional general information about tokens.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714871447/passinfo_02.png)

As shown in the example above, the value of request parameter **received in one report** (editMode) can be assigned to a Link Parameter with a different name (addRecord) and **passed to another report**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Although Link Parameter values will resolve tokens, as shown above, they *will not* evaluate expressions. For example, if you create a parameter with the value of "=1+1" and submit the report, in the next report or process task its @Request token will have a value of the string *"=1+1"*, not a numeric value of *2*.

## Encoding Characters

Certain characters are invalid in query string data, such as "&" and "?", because they're used to delimit information within the URL itself. Whenever possible, the Logi Server Engine tries to handle these situations by **encoding** the characters before placing them in a URL. However, it's not always possible to interpret the developer's intentions using this mechanism, so you may need to manually encode the text or data you pass when using Link Parameters or request forwarding.

For example, you may want to pass a value in a Link Parameter that includes an ampersand, such as "Brooks&Dunn". This causes a problem because the ampersand is an invalid URL character. The solution is to pass the encoded value for the character, instead. The encoded value consists of the "%" symbol and the hex value of the character, in this case "%26", so that value in the URL looks like "Brooks%26Dunn".

Characters that you may need to encode include:

| Character | Hex Value | Character | Hex Value |
| --- | --- | --- | --- |
| Dollar sign ("$") | 24 | Question mark ("?") | 3F |
| Ampersand ("&") | 26 | At sign ("@") | 40 |
| Plus ("+") | 2B | Space (" ") | 20 |
| Comma (",") | 2C | Quotation marks | 22 |
| Forward slash ("/") | 2F | Less than ("<") | 3C |
| Colon (":") | 3A | Greater than (">") | 3E |
| Semi-colon (";") | 3B | Pound sign ("#") | 23 |
| Equals ("=") | 3D | Percent sign ("%") | 25 |

  

## Avoid Passing Full Query String as a Parameter

Although the @Function.QueryString~ token makes it easy to do, we *do not recommend* that you pass an entire query string as a single Link Parameter, rather than passing its parts and then re-assembling them at the target definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699858839/passinfo_02a.png)

Passing the entire query string often results in double-encoding of the query string, raises cross-browser compatibility and URL length-limit issues, and can produce difficult-to-diagnose errors.
