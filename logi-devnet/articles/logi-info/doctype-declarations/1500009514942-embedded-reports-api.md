---
title: "Embedded Reports API"
id: 1500009514942
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514942-Embedded-Reports-API
updated_at: 2021-06-17T01:58:18Z
---

# Embedded Reports API

# Embedded Reports API

The **Embedded Reports API** provides developers with easy and agile methods for embedding Logi report components into other, non-Logi web pages. This topic provides the following information about the API:

* Include the API
* [Embed Static Reports using Markup](#Markup)
* [Embed Dynamic Reports using Javascript](#Javascript)
* [Access Embedded Reports on Different Domains](#Domains)
* [Prevent Session Timeout](#Timeout)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771817623/attnicon_15x15.gif)*Note that the Windows version of the **Safari** browser does not currently work with the Embed API.*

## Include the API

The Embedded Reports API, which is a Javascript file, is:

*<yourLogiApp>*/rdTemplate/rdEmbedApi/rdEmbed.js

To use it, include a link to it at the end of your custom HTML page, just above the </body> tag:

```
1. <body>
2. ...
3. <script src="http://<yourLogiApp>/rdTemplate/rdEmbedApi/rdEmbed.js" type="text/Javascript">
4. </script>
5. </body>
```

Next, create a div element to contain the embedded Logi report, and give it a unique id attribute.

```
1. <div id="div1" />
```

Then decide which of the two following embedding approaches, described in the following sections, you want to use: **Markup** or **Javascript**.

Note: The Embedded Reports API works well with all modern browsers, but some features (such as auto-sizing and accessing embedded reports) will not work with older browser, such as IE6 and IE7.

## Embed Static Reports Using Markup

Static embedding allows you to embed a Logi report simply by manipulating the markup tags. This is done by adding the appropriate data-\* attributes to the div container you've already created:

```
1. <div id="div1" data-applicationUrl="yourLogiAppURL" data-report="yourReportName" data-autoSizing="all"></div>
```

The attributes are:

| Attribute | Description |
| --- | --- |
| data-applicationUrl | Required  The URL of your Logi Info application. |
| data-report | Required  The Logi report definition name. |
| data-autoSizing | Required  Specifies automatic resizing of the container div to show the entire report or include scroll bars. Valid values include:  `"none", "height", "width", "all"`. |
| data-linkParams | A name-value collection of report parameters.  Example:`{'Year':'2010', 'CustomerId' : 1}`. |
| data-secureKey | A SecureKey value; required when using SecureKey Authentication. |

### Example 1: Simple Static Embedded Report

```
1. <div id="div1" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable" data-autoSizing="all"></div>
```

### Example 2: Static Embedded Report with Parameters for use in Query

Style can also be added to the div to give it a border and background color.

```
1. <div id="div2" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable data-autoSizing="all" data-linkParams="{'CustomerID' : 'VINET',
   'StartDate' : '01/01/1996'}" class="divFrame" ></div>
```

### Example 3: Using a Fixed-Size Layout

By default, embedded reports fill 100% of their div container. To control the report size, you can specify the div element's size with width and/or height style attributes. If the embedded report's physical size is greater than its div container, the report will automatically show scrollbars. You can hide the scrollbars by using style for the div element: overflow(-x | -y): none;.

```
1. <div id="div3" style="width:350px; height:150px;" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable" data-linkParams="{'CustomerID' : 'CHOPS'}" ></div>
```

When you specify a size in this way, you can skip the normally required data-autoSizing attribute.

## Embed Dynamic Reports using Javascript

You can also use Javascript and the EmbeddedReporting object from the API to embed reports. This object has three primary methods: **create**, **get**, and **remove**. Remember that Javascript is case-sensitive!

All three methods operate with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| applicationUrl | string | Required  The URL of your Logi Info application. |
| report | string | Required  The Logi report definition name. |
| autoSizing |  | Required  Specifies automatic resizing of the container div to show the entire report or include scroll bars. Valid values include:  `"none", "height", "width", "all"`. |
| linkParams | array | A name-value collection of report parameters.  Example: `{"Year":"2010", "CustomerId" : 1}`. |
| secureKey | string | A SecureKey value; required when using SecureKey Authentication. |
| iframeId | string | Read Only  Returns the id attribute value of the iframe element that contains the embedded report. |
| iframe | object | Read Only  Returns the iframe DOM object that contains the embedded report page |

### Use the create() and remove() Methods

1. Create a container for the report in the HTML markup:

```
1. <div id="reportContainer" />
```

2. In your Javascript code, create array of report options:

```
1. var options = {};
2. options.applicationUrl = "http://sampleapps.logianalytics.com/LogiApp";
3. options.report = "EmbeddedReports.DataTable";
4. options.autoSizing = "all";
5. options.secureKey = "";
6. options.linkParams = {"CustomerID" : "VINET", "StartDate" : "01/01/2009" };
```

3. Create a report instance:

```
1. var report = EmbeddedReporting.create('reportContainer', options);
```

4. Remove the report instance:

```
1. EmbeddedReporting.remove('reportContainer');
```

Try it:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778662167/embedapi_02.png)  ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778662423/embedapi_03.png)

Here's the Javascript used in this page, with the onClick events for the two buttons, to create and remove the report:

```
1. function CreateReport() {
2. var options = {
3. applicationUrl : "http://sampleapps.logianalytics.com/LogiApp",
4. report : "EmbeddedReports.DataTable",
5. autoSizing : "all",
6. linkParams : { "CustomerID": "VINET", "StartDate": "01/01/1976" }
7. };

9. var report = EmbeddedReporting.create('reportContainer', options);
10. }

12. function RemoveReport() {
13. EmbeddedReporting.remove('reportContainer');
14. }
```

### Use the get() Method

To manipulate existing reports created with the API, start by getting the report object, using its container div ID:

```
1. var report = EmbeddedReporting.get('containerId')
```

Report object properties can be directly manipulated:

```
1. EmbeddedReporting.get('containerId').report = "SalesByMonth"
```

The report object also has these methods available:

| Method | Description |
| --- | --- |
| loadReport() | Loads or refreshes an embedded report. Example: EmbeddedReporting.get('containerId').loadReport() |
| setParam(name, value) | Updates or inserts a parameter into the report parameters collection. Example: EmbeddedReporting.get('containerId').setParam("startDate", "01/01/2012") |
| getParam(name) | Returns a parameter value from the report parameters collection.  Example: EmbeddedReporting.get('containerId').getParam("startDate") |
| removeParam(name) | Removes a parameter from the report parameters collection. Example: EmbeddedReporting.get('containerId').removeParam("startDate") |
| removeAllParams() | Removes all parameters from the report parameters collection. Example: EmbeddedReporting.get('containerId').removeAllParams() |

Usage examples follow below.

### Example 1: Update Report Parameters

1. Create an embedded report using HTML markup:

```
1. <div id="div5" class="divFrame" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable" data-autoSizing="all"></div>
```

2. Add controls to the HTML page, then set onClick event to call this Javascript function:

```
1. function UpdateReportParameters() {
2. var reportObj = EmbeddedReporting.get("div5");
3. var lst = document.getElementById('customerId');
4. var customer = lst.options[lst.selectedIndex].value;
5. reportObj.setParam("CustomerID", customer);
6. reportObj.loadReport();
7. }
```

Try it:

Customer: ANATR
BERGS
CHOPS
GREAL
 
![](https://logianalytics.zendesk.com/hc/article_attachments/4402778662679/embedapi_04.png)

### Example 2: Select Different Reports

1. Create an embedded report using HTML markup:

```
1. <div id="div6" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable" data-autoSizing="height" ></div>
```

2. Add controls to the HTML page, then set onClick event to call this Javascript function:

```
1. function ChangeReport() {
2. var reportObj = EmbeddedReporting.get("div6");
3. var lst = document.getElementById('lstReports');
4. var reportName = lst.options[lst.selectedIndex].value;
5. reportObj.report = reportName;
6. reportObj.loadReport();
7. }
```

Try it:

Available reports: EmbeddedReports.DataTable
EmbeddedReports.Chart
EmbeddedReports.AnalysisGrid
 
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771817879/embedapi_05.png)

## Access Embedded Reports on Different Domains

When an embedded report is hosted on a server in a different domain, you can't directly access a its DOM elements and Javascript functions due to iFrame cross-domain access policy restrictions. However, the EmbeddedReporting object provides functionality to get around those restrictions, using these methods:

**execEmbeddedFunction(functionName, arg1, arg2, ...argN, callback)**  
Executes a Javascript function in an embedded report and returns its execution result.

Our example Logi app contains a report definition named EmbeddedReports.Elements and it includes this Javascript function:

```
1. function SayHello(firstName, secondName) {
2. var hello = "Hi " + firstName + " " + secondName + "!"
3. return hello;
4. }
```

We can use the execEmbeddedFunction method to remotely execute this function and then we can display its results locally.

1. Embed the report using HTML markup:

```
1. <div id="div7" class="divFrame" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.Elements" data-autoSizing="height"></div>
```

and here's the report:

2. Enter values for arg1 and arg2 on the current HTML page to send to the report's function, and click Execute:

Execute this:  
arg1:  
arg2:  
Callback to:  
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771818135/embedapi_06.png)

Here's the supporting Javascript included in the current HTML page and called when you click Execute:

```
1. function runEmbeddedFunction() {
2. var funcName = document.getElementById('inpExecuteThis').value;
3. var args1 = document.getElementById('inpArg1').value;
4. var args2 = document.getElementById('inpArg2').value;
5. var callback = document.getElementById('inpCallbackTo').value;

7. var report = EmbeddedReporting.get('div7');
8. report.execEmbeddedFunction(funcName, args1, args2, callback);
9. }

11. function showResults(result) {
12. alert(JSON.stringify(result, null, 2));
13. }
```

**getElementAttribute(selector, attributeName, callback)**  
Returns an object with two properties: elements and values. The elements property contains a list of elements, which matched the search query. The values property contains a list of attribute values. The selector argument should represent a valid CSS ID selector string.

1. Embed the report using HTML markup:

```
1. <div id="div8" class="divFrame" data-applicationUrl="http://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.Elements" data-autoSizing="all" ></div>
```

and here's the report:

2. Enter a CSS selector (#elementID) to specify the element, and an attribute name, and click Execute.

Element selector:  
Attribute name:
 
Callback To:   
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771818135/embedapi_06.png)

Here's the supporting Javascript included in the current HTML page and called when you click Execute:

```
1. function GetElementAttribute() {
2. var elementSelector = document.getElementById('inpSelector').value;
3. var attrName = document.getElementById('inpAttrName').value;
4. var callback = document.getElementById('inpCallbackTo').value;

6. var report = EmbeddedReporting.get('div8');
7. report.getElementAttribute(elementSelector, attrName, callback);
8. }

10. function showResults(result) {
11. alert(JSON.stringify(result, null, 2));
12. }
```

Note that values for **Input Text Area** and **Input Select List** elements cannot be retrieved using this method; you must write a separate function to extract their values and call it with execEmbeddedFunction() instead.

**setElementAttribute(selector, attributeName, attributeValue, callback)**  
Sets an attribute value of element inside an embedded report. Returns
"true" when the element was found and an attribute has been updated
successfully. The `selector` argument should represent a valid CSS selector string.

1. We'll use the report we embedded in the previous example.

2. Enter a CSS selector (#elementID), an attribute name and value, and click Execute. Scroll up to see the result.

Selector:  
Attribute name:
 
Attribute value:
 
Callback To:    
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771818135/embedapi_06.png)

Here's the supporting Javascript included in the current HTML page and called when you click Execute:

```
1. function SetElementAttribute() {
2. var elementSelector = document.getElementById('inpSelector').value;
3. var attrName = document.getElementById('inpAttrName').value;
4. var attrValue = document.getElementById('inpAttrValue').value;
5. var callback = document.getElementById('inpCallbackTo').value;

7. var report = EmbeddedReporting.get('div8');
8. report.setElementAttribute(elementSelector, attrName, attrValue, callback);
9. }

11. function showResults(result) {
12. alert(JSON.stringify(result, null, 2));
13. }
```

Note that, if the specified attribute does not exist, this method will create it and then set its value. Values for **Input Text Area** and **Input Select List** elements cannot be set using this method; you must write a separate function to set their values and call it with execEmbeddedFunction() instead.

## Prevent Session Timeout

The parent application and its embedded Logi reports may be hosted on separate web servers and, if so, there will be independent session state maintained for them on each host. Session expiration on either host may cause problems. The Embed API provides functionality for preventing session timeout for parent and embedded reports. To use it, create a simple web page in the parent application, without any visual elements, and use the following method to "ping" it at specified intervals.

**keepSessionsAlive(pingPageUrl, interval)**  
Pings parent and Logi servers at the defined interval (in milliseconds). Default interval is 60000 (1 minute).

```
1. EmbeddedReporting.keepSessionsAlive("http://myParentApplication/pingMe.aspx", interval)
```

This function automatically determines the URL of the embedded Logi reports and pings a standard page that's supplied with the Logi Info product, so you *don't* have to create a page to ping in the Logi application. Note that this technique only works with a single Logi application; if you have reports from multiple Logi applications embedded in the same parent application, this method *will not* ping all the Logi applications.
