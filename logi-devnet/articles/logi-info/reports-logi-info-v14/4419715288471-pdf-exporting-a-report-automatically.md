---
title: "PDF - Exporting a Report Automatically"
id: 4419715288471
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715288471-PDF-Exporting-a-Report-Automatically
updated_at: 2022-07-17T02:24:27Z
---

# PDF - Exporting a Report Automatically

# PDF - Exporting a Report Automatically

The following example, for Logi Info only, shows how to create a **process task** that exports data automatically:

![](https://devnet.logianalytics.com/hc/article_attachments/7522810869015/exportpdf_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522800029591/exportpdf_03a.png)

1. In your **Process** definition, add a **Procedure.ExportPDF** element beneath your Task element.
2. In the element's **Filename** attribute, specify the output path and filename, on the web server, for the exported report. The filename should include the ".pdf" file extension. For example, this value uses a token to export the report to a folder called myExports within your project folder: @Function.AppPhysicalPath~\myExports\myfile.pdf

![](https://devnet.logianalytics.com/hc/article_attachments/7522800037015/exportpdf_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522800043031/exportpdf_04a.png)

3. Add the required **Target.PDF** element.
4. In the element's **Report Definition File** attribute, you must specify the report to be exported (a blank value is not allowed). The *CurrentReport* option in the suggested values **is not valid** in this case, which means that the report will be exported but will not reflect any sort order that the user may have applied before clicking the export link.

4. If you wish to export *only* a specific Data Table, provide its ID in the **Export Data Table ID** attribute. This prevents anything else in the report, such as headers or footers, images, etc., from being exported.

When your task runs, the specified report will be exported to a **temporary** file in your project folder's **rdDownload** folder on the web server; the temp file is then copied to your output file. The file is not opened in your browser automatically.
