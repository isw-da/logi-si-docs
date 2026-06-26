---
title: "Exporting from a Task"
id: 4406817794071
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817794071-Exporting-from-a-Task
updated_at: 2022-04-06T06:08:15Z
---

# Exporting from a Task

# Exporting from a Task

You can create tasks that include procedures that export reports or data. This is done in the task by running a "hidden instanced" of an existing Report definition and then exporting it or its data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) There is a difference between exporting reports from a Report definition and from a Process task. An export from a Report definition is written out as a *temporary**file* in your application's rdDownload folder and then that file is opened for viewing in the user's browser. The temporary file is automatically
deleted later. An export from a Process task is saved as a file in a location, and with
a filename,
you specify
and it's not opened automatically in the browser. It's *not* considered a temporary file, so it's not deleted later automatically; you may have to manage it separately.

So, exporting from a Process task is useful when you need to save a file to the web server for later use, such as:

* Archiving data or reports
* Creating attachments to be sent with e-mails
* Building a custom Data Cache (XML export) that can be used later by your reports

More information about exporting can be found in our export topics.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575564823/workproctask_11.png)

As shown in the example above, an export procedure such as **Procedure.Export PDF** is added to a task, and its **Filename** attribute is set to the fully-qualified path for the export file, including the file name and extension. The account being used to run the Logi app must have Write permissions to the storage location (usually this is already in place if you're saving to any folder within your application folder), and the @Function token for the application path can be used here, as shown above.

The **Target.PDF** element can be used to specify the **Report Definition File** to be exported. If not specified, the "Current Report" definition - the one that called the task - will be exported. Why have an option? You may have created two similar definitions - one for browsing and one for exporting.

If you specify a table in the Target.PDF element's **Data Table ID** attribute, then just that table's *data* (without headers, footers, etc.) will be exported. See Logi Studio's Information Panel text for more information about other Target element attributes that are specific to different export types.

If the original report depended on Request variables to set queries, filtering, etc. then be sure to either set the Target element's **Request Forwarding** attribute to *True*, or to use **Link Parameters**, to ensure that the exported file is similarly configured.

The elements for exports to other formats (Word, Excel, CSV, etc.) operate in a similar fashion.

DevNet includes a [sample application](https://devnet.logianalytics.com/hc/en-us/articles/360049580114-Export-File-Sample-Appliication) that demonstrates exporting using process tasks.
