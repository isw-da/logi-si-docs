---
title: "Word - Exporting a Report Programmatically "
id: 4406817443735
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817443735-Word-Exporting-a-Report-Programmatically
updated_at: 2022-04-06T06:06:07Z
---

# Word - Exporting a Report Programmatically 

# Word - Exporting a Report Programmatically

The following example, for Logi Info only, shows how to create a process task that exports data programmatically:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563294359/exportword_02.png)

1. In your process definition, add a Task element.
2. Add a **Procedure.Delete File** element beneath the Task. The export *will not overwrite* an existing file so this element is used to delete any older version before the export occurs; no error will occur if there's no existing file to delete.
3. Add a **Procedure.Export Native** **Word** element beneath the task, as shown above.
4. In both elements' **Filename** attribute, specify the output path and filename on the web server for the exported document. The filename *should* include the .doc or .docx file extension. In the example above, this value uses a token to export the report to a folder called myExports within your project folder: @Function.AppPhysicalPath~\myExports\myfile.docx  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575706519/exportword_03.png)
5. Add the required **Target.Native Word** element, as shown above.
6. In the element's **Report Definition File** attribute, specify the report definition to be exported.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) In a Process definition, the "CurrentReport" option that appears in the suggested values for this attribute cannot be used. You *must* specify the actual name of the report.

What Happens: When your task runs, the specified report will be exported to a temporary file in your project folder's rdDownload folder on the web server; the temp file is then copied to your output file.
