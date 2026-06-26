---
title: "Embedding Dynamic Reports using JavaScript"
id: 4406817405975
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817405975-Embedding-Dynamic-Reports-using-JavaScript
updated_at: 2022-04-06T06:05:54Z
---

# Embedding Dynamic Reports using JavaScript

# Embedding Dynamic Reports using JavaScript

You can also use JavaScript and the EmbeddedReporting object from the API to embed reports. This object has three primary methods: **create**, **get**, and **remove**. Remember that JavaScript is case-sensitive!
All three methods operate with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| applicationUrl | string | Required The URL of your Logi Info application. |
| report | string | Required The Logi report definition name. |
| autoSizing | string | Required Specifies automatic resizing of the container div to show the entire report or include scroll bars. Valid values include:`"none", "height", "width", "all"`. |
| heightOffset | number | Embedded content frame padding has been increased to 20px. This property allows you to override that value, if desired. |
| linkParams | array | A name-value collection of report parameters.  Example: `{"Year":"2010", "CustomerId" : 1}`.   You may not use a parameter named "UserName". |
| secureKey | string | A SecureKey value; required when using SecureKey Authentication. |
| iframeId | string | Read Only Returns the id attribute value of the iframe element that contains the embedded report. |
| iframe | object | Read Only Returns the iframe DOM object that contains the embedded report page |

## Using the create() and remove() Methods

1. Create a container for the report in the HTML markup:

```
1. <div id="reportContainer" />
```

2. In your JavaScript code, create array of report options:

```
1. var options = {};
2. options.applicationUrl = "https://sampleapps.logianalytics.com/LogiApp";
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

Here's the JavaScript used in this page, with the onClick events for the two buttons, to create and remove the report:

```
1. function CreateReport() {
2. var options = {
3. applicationUrl : "https://sampleapps.logianalytics.com/LogiApp",
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

## Using the get() Method

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
