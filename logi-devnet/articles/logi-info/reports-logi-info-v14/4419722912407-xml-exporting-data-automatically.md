---
title: "XML - Exporting Data Automatically"
id: 4419722912407
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722912407-XML-Exporting-Data-Automatically
updated_at: 2022-07-17T01:49:22Z
---

# XML - Exporting Data Automatically

# XML - Exporting Data Automatically

The following example, for Logi Info only, shows how to create a **Process task** that exports data automatically:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706826903/exportxml_03.png)

1. As shown above, in your **Process** definition, add a **Task** element and beneath it a **Procedure.Export XML** element.
2. In the element's **Filename** attribute, specify the output path and filename, on the web server, for the exported report. The filename should include the ".XML" file extension. The example shown above uses an @Function token to provide the path to the Logi application's application folder on the web server.
![](https://devnet.logianalytics.com/hc/article_attachments/4419714756119/exportxml_04.png)

3. Next, add the required **Target.XML** element, as shown above.
4. In the element's **Report Definition File** attribute, specify the report that contains the data to be exported. Do not select the *CurrentReport* option in the list of suggestions as it *will not**work*.
5. Your task will need to be completed, of course, with a **Response** element to run properly.

What happens when your task runs? The specified report data will be exported to a temporary file in your project folder's rdDownload folder on the web server; then the temp file will be copied to the output file you specified.
If you try to run this task more than once, you'll receive an error. This is due to the fact that **Procedure.Export XML** will not *overwrite* an existing file. Adding a **Procedure.Delete File** element at the beginning of the task will solve this.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706827159/exportxml_05.png)

An example of a complete task is shown above. Note the use of the @Function again in the Procedure.Delete File element's **Filename** attribute.
Logi products also include an **XSL Transform** element, which allows you to apply transformations to change the XML output format before the data is exported.
