---
title: "Overriding Default Show Modes with Action.Report"
id: 4406822657943
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822657943-Overriding-Default-Show-Modes-with-Action-Report
updated_at: 2022-04-06T06:10:27Z
---

# Overriding Default Show Modes with Action.Report

# Overriding Default Show Modes with Action.Report

In [Setting the Report-Level Default Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4406822658967-Setting-the-Report-Level-Default-Show-Modes) we learned that use of the *rdShowModes* query string variable will override a report's Default Show Modes setting. The query string variable can be included when calling a report by using a number of methods, including **Link Parameters**. One of the easiest methods is available when using **Action.Report** and **Target.Report** elements to call the next report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575415959/showmodes_04.png)  

The example above shows a simple **Label** element, used as a link, with Action.Report and Target.Report elements beneath it. If the Target.Report element's **Report Show Modes** attribute is given a value, as shown above, that value will be automatically paired with the rdShowModes keyword and placed in the query string of the URL that calls the target report. The resulting URL would look like this:

http://localhost/myLogiApp/rdPage.aspx?rdReport=EmployeeReport&rdShowModes=ShowHROnly

Great runtime flexibility is possible because the Report Show Modes attribute value can be an @Data, @Request, or other token. Multiple comma-separated values, or tokens, can also be entered.

The following elements also have a Report Show Modes attribute that can be used in the same way:

* Action.Refresh Element
* Target.CSV
* Target.NativeExcel
* Target.NativeWord
* Target.PDF
* Target.Widget
