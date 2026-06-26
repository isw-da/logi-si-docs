---
title: "Using Built-in Show Modes Values"
id: 4406818145815
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818145815-Using-Built-in-Show-Modes-Values
updated_at: 2022-04-06T06:10:28Z
---

# Using Built-in Show Modes Values

# Using Built-in Show Modes Values

Built-in values provide the easiest method of working with Show Modes. They work like switches, automatically including or excluding elements from appearing under certain standard situations. These values are:

| Built-in Value | Description |
| --- | --- |
| All | Element will always be visible |
| None | Element will never be visible |
| rdBrowser | Element will only be visible when report is viewed in a browser |
| rdExport | Element will only be visible when report is exported |
| rdExportCsv | Element will only be included when report data is exported to a CSV file |
| rdExportExcel | Element will only be included when report is exported to an Excel worksheet |
| rdExportPdf | Element will only be included when report is exported as a PDF |
| rdExportWord | Element will only be included when report is exported to a Word document |

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) When one of these built-in values is used, developers *do not* need to set a corresponding value at the Report-level. When a specific action occurs, like an export, the application will compare these values to internal system values to determine what action to take.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575415063/showmodes_02.png)

The built-in values are available for selection from a drop-down list in the Show Modes attribute value field, in the Attributes panel, as shown above. Here's an example of one of them in use:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575415319/showmodes_02a.png)

In the example above, in the main content we provide a button that lets the user export the report to PDF. However, we don't want to include the page header and footer in the PDF. By setting the **Report Header** and **Report Footer** elements' Show Modes attributes to the standard *rdBrowser* value, we ensure that they will only appear when the report is browsed, but not when it's exported to PDF.
