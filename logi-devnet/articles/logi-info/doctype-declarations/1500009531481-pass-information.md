---
title: "Pass Information"
id: 1500009531481
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531481-Pass-Information
updated_at: 2021-06-17T01:58:33Z
---

# Pass Information

# Pass Information

The process of passing information between Logi reports and processes and external applications is essential to building **robust** and **flexible** Logi applications. This updated topic discusses the subject.

* Use Request Parameters
* [Access User Input Values](#Input)
* [Work with @Request Tokens](#WorkingWith)
* [Query String Limits](#Limits)
* [Access Global Data with Tokens](#Global)
* [Use HTML5 Local Storage](#LocalStorage)

## Use Request Parameters

Logi reports and processes are called using URLs, which may include a Query String. The most common method of passing information in Logi applications is with **request parameters**, using the HTTP "GET" method. This is a example of a URL for a Logi report:

http://www.myReportSite.com/myApp/rdPage.aspx?rdReport=OrdersReport&addRecord=True

and for a Logi process:

http://www.myReportSite.com/myApp/rdProcess.aspx?rdProcess=SiteTasks&rdTaskID=MemberLogin&UID=123

Both examples contain a **Query String** (the portion after the "?") which consists of multiple name and value pairs connected with an equals sign (e.g. UID=123) and separated by an ampersand. These name-value pairs are the request parameters.

Information can be passed from one report or process to another using request parameters:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771645463/passinfo_01.png)

The example above shows a report definition with a **Button** element that calls another report when clicked. The Action.Report element has two child elements: **Target.Report**, which specifies the report being called, and a **Link Parameters** element.

**Attributes** entered for the Link Parameters element wind up, as request parameters, in the **query string** used to call the next report or process task. Look at the earlier sample report URL and the example above; note how the Link Parameters attribute name and value becomes a request parameter key value pair.

In the report called when the Button is clicked (the target report) the request parameter information can be accessed using @Request tokens. The format of the token is @Request.<*LinkParameterName>~*

In the case of the example above, the token @Request.addRecord~ would have a value of *True*. Tokens are case-sensitive so careful spelling is required when using them.

[Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009516062-Token-Reference) provides additional general information about tokens.

Any application, whether web- or desktop-based, Logi application or not, that can redirect a user on the basis of a URL can make use of request parameters in the query string to pass information to a Logi report or process task definition.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771645719/passinfo_02.png)

As shown in the example above, the value of request parameter **received in one report** (editMode) can be assigned to a Link Parameter with a different name (addRecord) and **passed to another report**.

### Encoding Characters

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

### Avoid Passing Full Query String as a Parameter

Although the @Function.QueryString~ token makes it easy to do, we *do not recommend* that you pass an entire query string as a single Link Parameter, rather than passing its parts and then re-assembling them at the target definition.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778535703/passinfo_02a.png)

Passing the entire query string often results in double-encoding of the query string, raises cross-browser compatibility and URL length-limit issues, and can produce difficult-to-diagnose errors.

## Access User Input Values

Logi applications may include **User Input elements**, which *automatically* pass data to other definitions when the page is submitted.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771462807/stopicon.gif) You *do not* need to use **Link Parameters** to pass user input values. Doing so will cancel the automatic passing of them!

Accessing the data users enter is very easy:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771645975/passinfo_03.png)

As shown above, the text entered by a user is available in the target report by using the token @Request.inpUserName~. The **ID** attribute of a User Input element is appended to "@Request" to identify the data. Once again, using the correct spelling and case is essential.

Because an HTTP POST method is used when a Logi application page is submitted, data entered by users *does not* appear in the query string used to call the target report or process. Nonetheless, @Request tokens can still be used in the target report or process to access the input data.

A common use of User Input elements is to **dynamically** create **SQL queries** used in datalayers to retrieve data. For example, imagine a report page that includes an Input Select List named "inpState" that allows the user to select one of the states in the United States. When the page is submitted, the following query could be used to limit the SQL query on a subsequent page to the selected state:

SELECT \* FROM SalesData WHERE Sales\_State = '@Request.inpState~'

Note that the entire request token is enclosed within the usual single-quotes required for a text value in a query. At runtime, the token will be replaced with the value selected in the Input Select List.

Be careful that you don't create a situation where a NULL value in the query causes an error, or be sure to use a **Default Request Parameter** (discussed below) to ensure that your query will have a default value when its page is first displayed.

### Receive Data From External HTML Forms

Developers may need to call a Logi report *from* an external **HTML****page** that's in another web application - not part of your Logi application. The following is an example of code used in that external page to create an HTML form that does that: 

|  |  |
| --- | --- |
|  | <body>     <form name="form1" method="post" action="**rdPage.aspx**">        <p>Enter Report: <input type="text" name="rdReport"></p>        <p>Enter Category: <input type="text" name="Category"></p>        <input type="submit" name="submitCategory" value="Submit">    </form> </body> |

Note that the *action* attribute for the <form> tag is set to **rdPage.aspx**, the default page for displaying report definitions within a Logi application.

The <input> tags are coded with *name* attributes which are used to identify the request parameters when the form is submitted. The rdPage.aspx page is expecting a request parameter named **rdReport** to identify the target report, so that's required, either as user input or hard-coded as a hidden input field.

In the target report, the data entered on the HTML page in the **Category** text input control will be accessible using the token @Request.Category~.

### Send Data To External Web Application

In the reverse case from the preceding section, you may need to have your Logi application link *to* a web page that is not part of your Logi application. This is easily done using the **Action.Link** and **Target.Link** elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778535959/passinfo_04.png)

Ordinarily, this kind of link *will no*t pass the data entered into user input elements in your Logi report to the external web page. If you have user input data that you want to submit to the external page, set the Action.Link element's **Post Input Elements** attribute to *True*, as shown above. This will submit the data, using the HTTP POST method, to the external page (it will not appear in the browser in the URL).

### Pass Hidden Data

Developers may need to pass critical identifying data to another definition within their Logi application, but may not want to have it displayed in the browser in a URL. And for good reason: a user could simply edit the URL and refresh the page, perhaps accessing privileged information. The HTTP POST approach, discussed above, is one way to pass and hide such data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778536215/passinfo_05.png)

As shown in the example above, this can also be done by using an **Input Hidden** element. This element is not displayed on the web page but acts just like any other user input element: it passes its contents to the next Logi application definition using the HTTP POST method, so it doesn't appear in the browser in the displayed URL. You can use as many Input Hidden elements as you need in a report definition.

There are a variety of ways to put data into an Input Hidden element. Its **Default Value** attribute value can be a constant or you can use a token, as shown above. You can also use scripting to insert a value into it when the page is submitted or when some other event occurs. For an example of how this is done using JavaScript, see [Pass Input Select List Captions](https://devnet.logianalytics.com/hc/en-us/articles/1500009515262-Pass-Input-Select-List-Captions).

In the target report for this example, the token @Request.hdnPassThis~ would be used to get the value of the hidden input.

## Work with @Request Tokens

A Logi report or process that uses @Request tokens within its definition is "expecting" to receive these token from whatever calls it. Developers can **independently****test** reports to see what Request variables are expected by adding the request parameter &rdPrompt=True to the end of the URL used to call it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778536471/passinfo_06.png)

As shown above, when that request parameter is present in the URL, a special page with a form will be displayed with **text input fields** for every Request variable that the report or process is expecting. The developer can fill in the values and then run the report using them.

The above is also an example of how a request parameter can be used as a "switch" to toggle some feature on or off; this is often useful for **showing** or **hiding** elements in applications.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778536727/passinfo_07.png)

Similarly, if a report is expecting request parameters, the **Test Parameters** panel in Studio, shown above, will be visible beneath the Attributes panel and can be used to enter values for testing purposes.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771646231/passinfo_08.png)

As shown above, the diagnostic **Debugger Trace** page (accessible when debugging is turned on) shows the @Request tokens and their values.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778536983/passinfo_09.png)

**Target.Report** elements have a **Request Forwarding** attribute, as shown above. When set to **True**, all of the request parameters that were sent to the current report will be **forwarded** to the target report when the button is clicked.

This may sound like good thing, but it should be used with *caution*, because the application may pass **system request parameters** in addition to those that you specify and the **query string** may wind up getting very lengthy, especially if a sequence of reports keeps forwarding their parameters. This can be problematic because some browsers have a **length limit** on the URL they can handle (see section below).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  It's a good practice to **actively manage** your request parameters, rather than using Request Forwarding, to ensure that you know what's getting passed and when.

### Use Default Request Parameters

Imagine a report that lists salespeople based on their year-to-date sales volume and uses this SQL query:

SELECT TOP @Request.inpRowsToShow~ FROM SalesStaff ORDER BY YTDSales DESC

The report page includes an Input Text element, that has an ID of *inpRowsToShow*, so that at runtime the user can specify the number of rows to be shown in the report's data table. The report calls itself when a button is clicked, in order to refresh the data displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778537239/passinfo_10.png)

In order to ensure that @Request.inpRowsToShow~ has a value in the SQL query, so that *some* data is retrieved the first time the report is displayed, a **Default Request Parameters** element can be included at the top of the report definition. Its attributes define an *inpRowsToShow* parameter with a value of 25, as shown above.

If **no request parameter** with the name *inpRowsToShow* is passed in the query string that calls this report or as a form field, then the value defined in the Default Request Parameters element will be used. If such a request parameter or form field does exist, then its value will be used and this element will be ignored. This ensures that, in any case, when the report is displayed at least the top 25 records in the query will be shown.

## Query String Limits

As mentioned earlier, there *are* limits on the amount of data you can pass in a query string. The first limit is **length**: browsers do not accept an unlimited number of characters in a URL. Moreover, the limit varies by browser, as follows:

| Browser | Max URL Bytes |
| --- | --- |
| IE 5, 6, 7, 8, 9 | 2,048 |
| Firefox | 65K |
| Chrome & Safari | 80K |
| Opera | 190K |

Trying to pass very large amounts of data in the query string is generally *not* a good idea. For example, instead of querying data in Report 1 and then passing *all* of it to Report 2 in the query string, you might instead pass only the key data and re-execute the database query in Report 2. If it's not feasible to run the database query twice, another approach is to use linked datalayers that span the two reports, sharing the query results.

The second limit is in the Logi Server Engine itself. It uses a fixed-size **array** with **100****rows** to process request parameters. If you try to pass 101 parameters in your query string, an "index out of range" error will occur.

In summary, when passing data in query strings, don't exceed the length limit of the target browsers and don't pass more than 100 items as request parameters.

## Access Global Data with Tokens

In a Logi application there are two sources of data that can be considered "global" in scope: **Session** variables and **Cookies**. These are values that, once set, are available to *all* report and process definitions in an application. As such, they're an unrestricted method of "passing" information between report and process definitions.

Logi application Session variables and Cookies can be set in both report and process definitions. They can also be set by entities *outside* a Logi application and used in the Logi application. In the case of a Logi application for Java, there are special circumstances for Session variable sharing with external Java applications. For more information, see [Introduction to Logi Reporting with Java](https://devnet.logianalytics.com/hc/en-us/articles/1500009531261-Introduction-to-Logi-Reporting-with-Java).

Session variable and Cookie values can be read in a Logi app using the @Session and @Cookie tokens. For example, if a process task creates a session variable called UserName, it can be accessed in any report definition with the token @Session.UserName~.

### Cookie Limitations

While we don't recommend that you use cookies to manage large amounts of data, they are very useful, so you should understand their limitations. Modern browsers adhere to the cookie limits described in **RFC 2965**. They will manage:

* At least 300 cookies total
* At least 20 cookies per unique host or domain name
* At least 4,096 per cookie (name and value text)

Popular browsers extend the maximum number of cookies allowed per unique host or domain name as follows:

| Browser | Max Cookies | Max Bytes/Cookie |
| --- | --- | --- |
| IE 7\*, 8, 9, 10 | 50 | 4,096 |
| Firefox | 50 | 4,097 |
| Chrome & Safari | no limit | 4,097 |
| Opera 9 | 30 | 4,096 |

\* after system patch. Without patch, limit is 20 cookies. See this [MS Knowledgebase article](http://support.microsoft.com/kb/941495).

Generally, if the you attempt to set a domain cookie that exceeds the number of cookies allowed, the oldest cookie is deleted and the new cookie is accepted.

## Use HTML5 Local Storage

If a browser supports the HTML5 **Local Storage** technology, Logi User Input elements can optionally store their data using it. Data
stored this way is retained between
sessions on the client machine and is *automatically* restored as an Input element's
default value when the page is redisplayed. The Local Storage size limit
is approximately 5 MB and all values are stored as strings. There is no explicit method or token currently available in Logi apps for storing and retrieving data in Local Storage other than with an Input Element, however, it is accessible using scripting.

keywords: url length limit
