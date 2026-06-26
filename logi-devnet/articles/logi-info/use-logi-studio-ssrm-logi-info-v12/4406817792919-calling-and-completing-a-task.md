---
title: "Calling and Completing a Task"
id: 4406817792919
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817792919-Calling-and-Completing-a-Task
updated_at: 2022-04-06T06:08:14Z
---

# Calling and Completing a Task

# Calling and Completing a Task

In order to use a task, you must *call* it, and when it completes, it needs to *redirect* processing to someplace else.

## Calling a Task from a Report Definition

As Logi report developers, we're used to "calling" one report definition from another report definition, using links, buttons, or events. When doing that, we can pass information to the next report using **Link Parameters** and we know that **User Input** element values are POST'ed to the next report as Request variables. The same is true when calling a Process task from a report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583766935/workproctask_05.png)

In the Report definition example shown above, an **Action.Process** element is used beneath a Label element to redirect processing to a task. The Action element's attributes identify the **Process Definition File** and the **Task ID** of the task to be called; these values can be selected from drop-down lists. A **Link Parameters** element can also be used beneath the Action element, if desired, to pass information to the task.

When processing is transferred to the task, the Link Parameters and any User Input element values will be available in the task as Request variables and can be used there via @Request tokens.

## Calling a Task when a Report Loads

You can have a task run *automatically* when a Report definition loads.
This "onLoad event" behavior allows you to set variables, run procedures, and accomplish any
other initializations you might want to do, and then redirect the browser
back to the report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583767191/workproctask_25.png)

As shown above, the **Startup Process** element is
added to a Report definition, and its attributes are set to
identify the desired Process Definition and Task ID for the "startup
task".

Any Request variables *in the query string* used to call
the report definition will automatically be available as Request tokens in the
Process task called with this element. For example, the @Request.rdReport~ token will contain the name of the report definition specified in the URL. Note that any parameters set using **Default Request Parameters** element *are not* passed to the task.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You can use a **Response**
element at the end of the startup task to redirect the browser to a
specific report definition after the task completes but this is *optional*. Without one, the browser will be automatically redirected back to the original report definition.

The element's **Condition** attribute can be used to dynamically control when the Startup Process will be called.

*Multiple* Startup Process elements may be used to call different process tasks; they'll be run sequentially, one after the other.

## Calling a Task from a URL

You can also call a process task directly from a URL, using the following syntax:

http://www.myReportSite.com/myLogiApp/rdProcess.aspx?rdProcess=myTasks&rdTaskID=taskUpdate&myParam=1

where *rdProcess* and *rdTaskID* are required and additional request variables, such as *myParam*, are optional.

This URL can be used, for example, with an **Action.Link** element, or even from an external application.

## Calling a Task from Another Task

Under certain circumstances, you may want to transfer operations from one task directly to another task.

The **Procedure.Process Task** element lets you directly call another task, in the same or in a different Process definition. A child Link Parameters element can be used to pass values to the target task. This does *not* operate like a function - the designated task will be executed but operations will not "return" to the first task afterwards.

You can also use a more "manual" approach, with the Response.Link element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563118615/workproctask_06.png)

In this case, you would use a **Response.Link** element, as shown above and, in its **Target.Link** child element's **URL** attribute, use the syntax shown in the previous section for calling a task from a URL. You can use @Request tokens right in the URL to forward request variables sent to the first task, so they'll be available in the second task, like this:

http://www.mySite.com/myApp/rdProcess.aspx?rdProcess=myTasks&rdTaskID=taskNext&myVar=@Request.myVar~

Recursion and nesting do not exist for tasks; one task just leads to another and the last task needs to handle redirection to a visible web page.

## Calling a Task at Session Start

You can have a task run *automatically* when a user session begins (i.e., when the application is browsed by a user for the first time). This allows you to set variables, run procedures, and accomplish any other "startup" work you might want to do, and then redirect the browser to a report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563118871/workproctask_07.png)

As shown above, the **Startup Process** element is added to the \_Settings definition, and its attributes are set to identify the desired Process Definition and Task ID for the "startup task".

Any Request variables in the query string used to call the application will automatically be available as Request tokens in the Process task called with this element. For example, the @Request.rdReport~ token will contain the name of the report definition specified in the URL. Note that any parameters set using **Default Request Parameters** element *are not* passed to the task.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You can use a **Response** element at the end of the startup task to redirect the browser to a specific report definition after the task completes but this is *optional*. Without one, the browser will be automatically redirected to the application's default report definition.

The element's **First Session Only** attribute can be used to prevent the Startup Process from being called if the application is called recursively.

*Multiple* Startup Process elements may be used to call different process tasks; they'll be run sequentially, one after the other.

## Completing a Task

When processing is transferred to a task and it completes, there is no "stack" to unwind, no built-in return path back to the calling Report definition. As the developer, you must explicitly transfer processing somewhere else after a task completes. If you don't, your user will be left looking at a blank browser screen!

![](https://devnet.logianalytics.com/hc/article_attachments/4417583768087/workproctask_08.png)

Tasks use **Response** elements, as shown above, which end a task by redirecting processing, usually back to a Report definition. You can also redirect instead to another task, as discussed earlier. You should ultimately redirect to a visible page so the user sees something in their browser.

The **Response.Raw** element can be used to complete a task and gives you full control of the response. This can be especially useful when building a REST API call from a Process. Response.Raw responds with a value and optional response headers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563119383/workproctask_34.png)

In the example above, the Response.Raw element is used to provide response values using @Procedure tokens. Its **Response Header Params** child element can be used to provide custom response headers and values. The Response.Raw element's attributes are:

* **Content Type** - If left blank, the default content type is *text/plain; charset=utf-8*
* **Status Code** - The HTTP response status code; if left blank, the default value is *200*
* **Status Description** - The HTTP response status description; if left blank, the default value is *OK*
* **Value** - The response value; @Procedure tokens may be used here.
