---
title: "Calling a Report via URL"
id: 4419715402519
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715402519-Calling-a-Report-via-URL
updated_at: 2022-07-17T01:42:36Z
---

# Calling a Report via URL

# Calling a Report via URL

Traditionally, a Logi report is called by entering the appropriate URL in a browser. This can be done manually by typing it right into the browser's address bar or it can be done via any valid HTTP link in a different Logi report, or in an entirely separate web page or application. The basic URL for a Logi report takes this form:

http://localhost/yourLogiAppName/rdPage.aspx?rdReport=mySalesReporthttp://www.yourWebSite.com/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport

The first example above is a URL that might appear on a development computer; the second, on a production server, where

* The **rdPage.aspx** page denotes that a Logi report definition is to be processed
* The **rdReport** argument value is the name of the Logi report definition file to be processed
* Additional request parameter name-value pairs can be included in the URL with separating ampersands (&).

More information about passing data in the URL's query string can found in our document [Pass Information](https://devnet.logianalytics.com/hc/en-us/articles/4419723105815-Pass-Information).

## Specifying Report Format or Template

You can also specify a **report format** in the query string in order to output the report in different ways. This is done using the reserved word **rdReportFormat**, as follows:

http://localhost/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport&rdReportFormat=PDF

When the example URL shown above is browsed, the report mySalesReport will be output into the browser as a PDF document. When you use this reserved word, ensure that you also use the rdReport name-value pair (in other words, don't rely on a report being the default report in your application and leave rdReport out of the URL). Other values for rdReportFormat include *NativeExcel*, *NativeWord*, *CSV*, *HtmlExport*,
*HtmlEmail*, *Excel*, *Word*, *XML*,
or *GoogleSpreadsheet.* 
Similarly, you can use **rdTemplate** instead of rdReport to identify an Excel, Word, or PDF template definition to be run from a URL.
Learn more about the reserved words that can be used in a URL for special purposes in our document [Query String Parameter Reference](https://devnet.logianalytics.com/hc/en-us/articles/4419700077719-Query-String-Parameter-Reference).

## Using a Constant in a URL

If you're using a URL within a Logi report definition to call another report, for example, by using Action.Link, you can use a **constant** and its token to provide part or all of the URL.
Suppose, for example, you've assigned the first part of the URL "http://www.yourWebSite.com" to a constant called SiteURL, in the application's \_Settings definition. The URL used to call another report or web page can then make use of that constant by using its token:

@Constant.SiteURL~/yourLogiAppName/rdPage.aspx?rdReport=mySalesReport

An arrangement like this will let you run development and production versions of an application that differ only in the value of the SiteURL constant.
