---
title: "Excel - Exporting a Report using a Process Task"
id: 4406822321047
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822321047-Excel-Exporting-a-Report-using-a-Process-Task
updated_at: 2022-04-06T06:06:06Z
---

# Excel - Exporting a Report using a Process Task

# Excel - Exporting a Report using a Process Task

The following example, for Logi Info only, shows how to create a **process task** that exports data automatically:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575707543/exportexcel_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583943575/exportexcel_03a.png)

1. In your Process definition, add a **Procedure.Export Native Excel** element to your Task, as shown above.
2. In the element's **Filename** attribute, specify the output path and filename, on the web server, for the exported report. The filename should include the ".xlsx" or ".xls" file extension. For example, this value uses a token to export the report to a folder called *myExports* within your application folder: @Function.AppPhysicalPath~\myExports\myfile.xlsx
3. If the folder you're exporting to is not within your Logi app root folder, ensure that the account or Application Pool used to run your application has been granted full control file access permissions on the folder.
4. In the example above, note the user of a **Procedure.Delete File** element before the Procedure.Export Native Excel element. The export *will not overwrite* an existing file, so this element is used to delete any older version before the export occurs; no error will occur if there's no existing file to delete. Set its **Filename** attribute value to match the Export Native Excel element's Export File Name attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563299095/exportexcel_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575707799/exportexcel_04a.png)

4. Add the required **Target.Native Excel** element.
5. In the element's **Report Definition File** attribute, specify the report to be exported.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) In a Process definition, the *CurrentReport* option that appears in the suggested values for this attribute cannot be used. You *must* specify the actual name of the report.

What Happens: When your task runs, the specified report will be exported to a temporary file in your application folder's rdDownload folder on the web server; when ready the temp file is then copied to your output file. Temporary files on the server are cleaned up automatically over time.
