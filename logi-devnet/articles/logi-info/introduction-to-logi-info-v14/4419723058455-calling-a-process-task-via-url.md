---
title: "Calling a Process Task via URL"
id: 4419723058455
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723058455-Calling-a-Process-Task-via-URL
updated_at: 2022-07-17T01:42:37Z
---

# Calling a Process Task via URL

# Calling a Process Task via URL

If you're a **Logi Info** developer, the entry point for a Logi application does not have to be a report. Logi Info includes **Process tasks** and your application can be launched through a process definition rather than a report definition.

http://www.yourWebSite.com/yourLogiAppName/rdProcess.aspx?rdProcess=myProcessDef&rdTaskID=ShowMenuPage

The example URL shown above can be used to directly call a Process task, where

* The **rdProcess.aspx** page denotes that a Logi process definition is to be processed.
* The **rdProcess** argument value is the name of the Process definition file to use
* The **rdTaskID** argument value is the name of the Process task to run

This approach can be very useful if you want do logging, or send notifications, or accomplish any of a number of other activities that need to be done before showing the user the first report page.
Use of a **Response.Link** element with a URL is also the only way to have one Process task call another Process task.
As always, when working with tasks, ensure that you have a final Response.Report element that's processed at the end of the task or your user will be left seeing nothing but a blank page.
