---
title: "Accessing User Input Values"
id: 4406822471575
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822471575-Accessing-User-Input-Values
updated_at: 2022-04-06T06:08:06Z
---

# Accessing User Input Values

# Accessing User Input Values

Logi applications may include **User Input elements**, which *automatically* pass data to other definitions when the page is submitted.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You *do not* need to use **Link Parameters** to pass user input values. Doing so will cancel the automatic passing of them!
Accessing the data users enter is very easy:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563130263/passinfo_03.png)

As shown above, the text entered by a user is available in the target report by using the token @Request.inpUserName~. The **ID** attribute of a User Input element is appended to "@Request" to identify the data. Once again, using the correct spelling and case is essential.

Because an HTTP POST method is used when a Logi application page is submitted, data entered by users *does not* appear in the query string used to call the target report or process. Nonetheless, @Request tokens can still be used in the target report or process to access the input data.

A common use of User Input elements is to **dynamically** create **SQL queries** used in datalayers to retrieve data. For example, imagine a report page that includes an Input Select List named "inpState" that allows the user to select one of the states in the United States. When the page is submitted, the following query could be used to limit the SQL query on a subsequent page to the selected state:

SELECT \* FROM SalesData WHERE Sales\_State = '@Request.inpState~'

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The entire request token is enclosed within the usual single-quotes required for a text value in a query. At runtime, the token will be replaced with the value selected in the Input Select List.

Be careful that you don't create a situation where a NULL value in the query causes an error, or be sure to use a **Default Request Parameter** (discussed below) to ensure that your query will have a default value when its page is first displayed.

### Receiving Data From External HTML Forms

Developers may need to call a Logi report *from* an external **HTML****page** that's in another web application - not part of your Logi application. The following is an example of code used in that external page to create an HTML form that does that:

<body>  
 <form name="form1" method="post" action="**rdPage.aspx**">  
 <p>Enter Report: <input type="text" name="rdReport"></p>  
 <p>Enter Category: <input type="text" name="Category"></p>  
 <input type="submit" name="submitCategory" value="Submit">  
 </form>  
</body>

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The *action* attribute for the <form> tag is set to **rdPage.aspx**, the default page for displaying report definitions within a Logi application.

The <input> tags are coded with *name* attributes which are used to identify the request parameters when the form is submitted. The rdPage.aspx page is expecting a request parameter named **rdReport** to identify the target report, so that's required, either as user input or hard-coded as a hidden input field.

In the target report, the data entered on the HTML page in the **Category** text input control will be accessible using the token @Request.Category~.

## Sending Data To External Web Application

In the reverse case from the preceding section, you may need to have your Logi application link *to* a web page that is not part of your Logi application. This is easily done using the **Action.Link** and **Target.Link** elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575575831/passinfo_04.png)

Ordinarily, this kind of link *will no*t pass the data entered into user input elements in your Logi report to the external web page. If you have user input data that you want to submit to the external page, set the Action.Link element's **Post Input Elements** attribute to *True*, as shown above. This will submit the data, using the HTTP POST method, to the external page (it will not appear in the browser in the URL).

## Passing Hidden Data

Developers may need to pass critical identifying data to another definition within their Logi application, but may not want to have it displayed in the browser in a URL. And for good reason: a user could simply edit the URL and refresh the page, perhaps accessing privileged information. The HTTP POST approach, discussed above, is one way to pass and hide such data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575576343/passinfo_05.png)

As shown in the example above, this can also be done by using an **Input Hidden** element. This element is not displayed on the web page but acts just like any other user input element: it passes its contents to the next Logi application definition using the HTTP POST method, so it doesn't appear in the browser in the displayed URL. You can use as many Input Hidden elements as you need in a report definition.

There are a variety of ways to put data into an Input Hidden element. Its **Default Value** attribute value can be a constant or you can use a token, as shown above. You can also use scripting to insert a value into it when the page is submitted or when some other event occurs. For examples of how this is done using JavaScript, see [Passing Input Select List Captions](https://devnet.logianalytics.com/hc/en-us/articles/4406822070295-Passing-Input-Select-List-Captions).

In the target report for this example, the token @Request.hdnPassThis~ would be used to get the value of the hidden input.
