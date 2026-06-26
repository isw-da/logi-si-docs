---
title: "CSV - Exporting Data with Automation"
id: 4419707567639
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707567639-CSV-Exporting-Data-with-Automation
updated_at: 2022-07-17T01:49:52Z
---

# CSV - Exporting Data with Automation

# CSV - Exporting Data with Automation

The following example, for Logi Info only, shows how to create a **process task** that exports data automatically:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699714455/exportcsv_04.png)

1. As shown above, in your Process definition, add a **Task** element and set its ID attribute.
2. Then add a**Procedure.Export CSV** element beneath it.
3. In the element's **Filename** attribute, specify the output path and filename, on the web server, for the exported report. The filename should include the ".csv" file extension. The example shown above uses the @Function.AppPhysicalPath~ token to provide the path to the application folder.
![](https://devnet.logianalytics.com/hc/article_attachments/4419699715863/exportcsv_05.png)

4. Next, add the required **Target.CSV** child element, as shown above.
5. In the element's **Report Definition File** attribute, specify the report that contains the data to be exported. Do not select the "CurrentReport" choice in the list of suggestions as it *will not**work* in this case.
6. Your task will need to be completed, of course, with a **Response** element to run properly.

What happens when your task runs? The data from the specified report's datalayer will be exported to a temporary file in your project folder's rdDownload folder on the web server; then the temp file will be *copied* to the output file you specified.
If you try to run this task more than once, you'll receive an error. This is due to the fact that **Procedure.Export CSV** will not *overwrite* an existing file. Adding a **Procedure.Delete File** element at the beginning of the task will solve this:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714751895/exportcsv_06.png)

An example of a complete task is shown above. Note the use of the @Function again in the Procedure.Delete File element's **Filename** attribute.
