---
title: "Customizing Getting Started Tab"
id: 5281620817175
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281620817175-Customizing-Getting-Started-Tab
updated_at: 2022-05-03T22:09:01Z
---

# Customizing Getting Started Tab

# Customizing Getting Started Tab

The **Getting Started** tab is displayed as a user enters the Exago Web Application user interface. This tab can be customized by customizing HTML in a language definition file. This is done by modifying the language element `<GettingStartedContent>` in `<WebApp>\Config\Languages\en-us-getting-started.xml`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

To assist in customizing the Getting Started tab, Exago provides several [JavaScript functions](#JavaScri) and [HTML5 attributes](#JavaScri2) to open the New Report Wizard, execute reports, open other custom tabs and display reports as Dashboards.

The figure below demonstrates a custom Getting Started tab. The two charts are loaded with the `data-onloadreportname` HTML5 attribute. The links to the New Report Wizard and Dashboard Designer use the `void wrStartNewReportWizard([string reportType])` function.

![image001.png](https://devnet.logianalytics.com/hc/article_attachments/5432249318167/image001.png)
> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> It is recommended to make custom tabs in a separate language file to make it easy to change tabs by user or groups of users. See [Modifying Select Language Elements](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support#Modifyin).

## Referencing Another HTML File v2020.1+

**Getting Started** content may alternatively be sourced from an external HTML file by using the `src` attribute of the `element` node. The value must be a file relative to `<WebApp>\Config\Languages`.

In the following example, the user’s Getting Started page will be replaced by the content in `<WebApp>\Config\Languages\es-mx-getting-started.html` and the Admin Console’s Getting Started Page will be replaced by the content in `<WebApp>\Config\Languages\es-mx-admin-getting-started.html`.

[Copy](javascript:void(0);)

```
1
2
3
4
<Language>  
   <element id="GettingStartedContent"src="es-mx-getting-started.html" />  
   <element id="AdminGettingStartedContent"src="es-mx-admin-getting-started.html" />  
</Language>
```

## JavaScript Functions

It is possible to access the [JavaScript functions below](#JavaScri3) in the alternative HTML file, by including this line in the file:

```
<script defer src="WrScriptResource.axd?s=GettingStarted"></script>
```

To provide custom JavaScript beyond what is provided by Exago, the `WrScriptResource.axd` endpoint cannot be used. Instead either:

* write the JavaScript directly in the custom HTML page between standard `<script>` tags (this is the easiest). Or,
* source JavaScript files using an absolute link to a CDN or other hosting location.

## Creating Additional Custom Tabs

Additional custom tabs can be created by creating a language elements with a unique name containing the HTML content. Custom tabs can be opened with the JavaScript function [**wrAddTabbedContent**](#void2).

This example demonstrates a custom tab that has buttons to launch a report in different formats.

```
<element id="QuickReportsTab"> <button value="HTML" onclick="wrExecuteReport('My Reports\Revenue', 'html');" /> <button value="EXCEL" onclick="wrExecuteReport('My Reports\Revenue', 'excel');" /> <button value="PDF" onclick="wrExecuteReport('My Reports\Revenue', 'pdf');" /> <button value="RTF" onclick="wrExecuteReport('My Reports\Revenue', 'rtf');" /> <button value="CSV" onclick="wrExecuteReport('My Reports\Revenue', 'csv');" /></element>
```

## JavaScript Functions

To assist with the creation of custom tab content, Exago provides a number of JavaScript functions to allow custom HTML to call features of Exago.

### `void wrStartNewReportWizard([string reportType])`

|  |  |
| --- | --- |
| Description | Opens the **Report Wizard** in a new tab. Optionally, specify which wizard to open with the *reportType* argument. Available values for *reportType*:   * advanced * express * expressview * Dashboard * chained |
| Example | ``` <p>Click <span style="text-decoration:underline; cursor:pointer;" onclick="wrStartNewReportWizard();">here</span> to create a new report.</p> ``` |

### `void wrStartDuplicateReportDialog(string reportFolder\reportName)`

|  |  |
| --- | --- |
| Description | Opens the Duplicate Report dialog. |
| Remark | If the report name is null or blank Exago will use the report selected in the Main Menu. |
| Example | ``` <p>Click <span style="text-decoration:underline; cursor:pointer;" onclick=" wrStartDuplicateReportDialog();">here</span> to create a duplicate this report.</p> ``` |

### `void wrExecuteReport(string reportFolder\reportName, string format)`

|  |  |
| --- | --- |
| Description | Executes the specified report in the specified format. |
| Example | ``` <input type="button" class="Button" value="HTML" onclick="wrExecuteReport('Sales Reports\Revenue by Category','html') ``` |

### `string wrGetSelectedReportName()`

|  |  |
| --- | --- |
| Description | Returns the name of the report that is selected in the Report Tree. |
| Remark | The returned string will include the folder structure of the report separated by slashes. |

### `void wrAddTabbedContent(string ContentID, string TabName)`

|  |  |
| --- | --- |
| Description | Opens a new tab and loads the HTML stored in the element of the Language file that corresponds to the ContentID string. |
| Remark | The ContentID should match the element ID of the HTML you want to load. The TabName can match the element ID of the name you want the tab to display, or a custom string with the name of the tab. |

## JavaScript HTML5 data- Attributes

To assist with the creation of custom tab content, Exago provides a number of HTML5 data- attributes to allow custom HTML to call features of Exago.

### `data-onloadreportname="ReportFolderReportName"`

|  |  |
| --- | --- |
| Description | Executes a report as HTML and loads it into a div or iframe. Dashboards are not compatible with data-onloadreportname. |
| Remark | The report string should be formatted as “Report Folder\Report Name.” light bulb When using this function make sure the setting **Enable Debugging** in **Other settings** is **False**. |
| Example | ``` <div class="Report"  data-onloadreportname="Employee ReportsNumber of Sales by Employee"></div> ``` |

### `data-useviewer="True/False"`

|  |  |
| --- | --- |
| Description | Specifies to load a report as raw HTML or utilize Exago dynamic report viewer. |
| Remark | Default value is *true*. In cases where the dynamic capabilities of the Report Viewer is not needed set to *false* to load raw HTML. This has a similar behavior to using either ApiAction vs. GetExecute methods via the APIs. |
| Example | ``` <div class="Report"  data-onloadreportname="Employee ReportsNumber of Sales by Employee" data-useviewer= “False”></div> ``` |

### `data-enablescrolling="value"`

|  |  |
| --- | --- |
| Description | Specifies whether or not to show scroll bars. This can helpful for certain reports that may not fit exactly within the startup content. |
| Remark | Available values for *value*:  * *true* — show scroll bars (default) * *false* — do not show scroll bars |
| Example | ``` <div class="Report"  data-onloadreportname="Employee ReportsNumber of Sales by Employee" data-enablescrolling= “False”></div> ``` |

### `data-reloadinterval="value"`

|  |  |
| --- | --- |
| Description | Reloads a report every *value* seconds. |
| Remark | This function is used in conjunction with **data-onloadreportname**. |
| Example | ``` <div class="Report"  data-onloadreportname="Employee ReportsNumber of Sales by Employee" data-reloadinterval="2"></div> ``` |

### `data-allowexport="value"`

|  |  |
| --- | --- |
| Description | Specifies whether or not to show the export menu for the report. |
| Remark | Available values for *value*:  * *0* — do not show the menu (default) * *1* — show the menu |
| Example | ``` <div class="Report"  data-onloadreportname="Employee ReportsNumber of Sales by Employee" data-reloadinterval="1"></div> ``` |
