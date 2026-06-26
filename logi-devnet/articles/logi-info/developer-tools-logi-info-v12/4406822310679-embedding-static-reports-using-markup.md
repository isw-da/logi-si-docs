---
title: "Embedding Static Reports using Markup"
id: 4406822310679
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822310679-Embedding-Static-Reports-using-Markup
updated_at: 2022-04-06T06:05:56Z
---

# Embedding Static Reports using Markup

# Embedding Static Reports using Markup

Static embedding allows you to embed a Logi report simply by manipulating the markup tags. This is done by adding the appropriate data-\* attributes to the div container you've already created:

```
1. <div id="div1" data-applicationUrl="yourLogiAppURL" data-report="yourReportName" data-autoSizing="all"></div>
```

The attributes are:

| Attribute | Description |
| --- | --- |
| data-applicationUrl | Required The URL of your Logi Info application. |
| data-report | Required The Logi report definition name. |
| data-autoSizing | Required Specifies automatic resizing of the container div to show the entire report or include scroll bars. Valid values include:`"none", "height", "width", "all"`. |
| data-heightOffset | Embedded content frame padding has been increased to 20px. This attribute allows you to override that value, if desired. |
| data-linkParams | A name-value collection of report parameters.  Example: `{'Year':'2010', 'CustomerId' : 1}`.   You may not use a parameter named "UserName". |
| data-secureKey | A SecureKey value; required when using SecureKey Authentication. |
| data-widthOffset | Embedded content frame padding is 20px. This attribute allows you to override that value, if desired. |

## Example 1: Simple Static Embedded Report

```
1. <body>
2. div id="div1" data-applicationUrl="https://sampleapps.logianalytics.com/logiapp" 
    data-report="EmbeddedReports.DataTable" data-autoSizing="all"></div>
3. <script src="https://sampleapps.logianalytics.com/logiapp/rdTemplate/rdEmbedApi/rdEmbed.js"  
    type="text/Javascript"></script>
4. </body>
```

  

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) It's very important that the <script> statement that includes rdEmbed.js be the *last line of code* before the </body> tag in your HTML or else the API will not work.

## Example 2: Static Embedded Report with Parameters for use in Query

Style can also be added to the div to give it a border and background color.

```
1. <div id="div2" data-applicationUrl="https://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable data-autoSizing="all" data-linkParams="{'CustomerID'
   : 'VINET', 'StartDate' : '01/01/1996'}" class="divFrame" ></div>
```

## Example 3: Using a Fixed-Size Layout

By default, embedded reports fill 100% of their div container. To control the report size, you can specify the div element's size with width and/or height style attributes. If the embedded report's physical size is greater than its div container, the report will automatically show scrollbars. You can hide the scrollbars by using style for the div element: overflow(-x | -y): none;.

```
1. <div id="div3" style="width:350px; height:150px;" data-applicationUrl="https://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.DataTable" data-linkParams="{'CustomerID' : 'CHOPS'}" ></div>
```

When you specify a size in this way, you can skip the normally required data-autoSizing attribute.
