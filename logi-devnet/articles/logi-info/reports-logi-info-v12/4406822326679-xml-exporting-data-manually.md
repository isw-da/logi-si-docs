---
title: "XML - Exporting Data Manually"
id: 4406822326679
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822326679-XML-Exporting-Data-Manually
updated_at: 2022-04-06T06:06:09Z
---

# XML - Exporting Data Manually

# XML - Exporting Data Manually

Here's an example of how to create a report with a link that allows data to be exported manually by the user:

### 

1. In your report definition, add an **Action.Export XML** element as the child of a **Label**, **Image**, **Button** or **Chart** element, as shown above.
2. Below it, add the required **Target.XML** child element.
3. If the data to be exported is part of the *current report*, you don't need do anything else. Just save your definition and browse your report. It's that simple. The default settings will export the current reports' data.

What happens when the link is clicked? The report's data is exported to a temporary .XML file which is created in your application's rdDownload folder on the web server. The temp file is then opened automatically in your browser (or in whatever tool the .xml file extension has been associated with in the OS). From there, you can save it to a file, if desired.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) XML files opened in a browser are usually formatted for easier viewing, which may introduce extraneous characters. If you want to save a "clean" copy of the XML (which is necessary if you want to use the file as a data source later), right-click the displayed XML and select your browser's "View source" option, then save that display to a file.
Only the data from the datalayer is exported; headers, footers, paging, images, etc. from the source report are not exported. Any conditions, filters, aggregations, etc. that have been applied to the datalayer will be reflected in the exported data.
The following table provides explanations for the Target.XML element's attributes, which are all optional:

| Attribute | Description |
| --- | --- |
| Frame ID | Specifies the **frame** for the target page. Leave blank for the current browser window, or select *NewWindow* to open a new browser window. You can also specify an existing frame identifier to re-use the same window for each request. |
| ID | Specifies a unique identifier for this element. |
| Report Definition File | Specifies the name of the report definition file that contains the data to be exported. Default: *the current report* |
| Request Forwarding | Specifies whether request variables will be passed to the report definition file that contains the data to be exported. Has no effect if the current report is being exported. |

The temporary files generated during the export are **cleaned up** automatically over time.
