---
title: "Working with Process Parameters"
id: 4406818029335
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818029335-Working-with-Process-Parameters
updated_at: 2022-04-06T06:09:44Z
---

# Working with Process Parameters

# Working with Process Parameters

Parameters, in the format of name-value pairs, can be stored with a Scheduler task and passed to the target Process task when the Scheduler task runs. The **Schedule** element includes an user input control set that it displays for entering and editing these parameters. Its appearance in the UI is controlled by the element's **Show Process Parameters** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562999959/usingsched_04.png)

As shown above, the Schedule element's interface can be used to add a number of parameters at runtime. As the parameters are entered, they're assembled into an XML string and placed into a hidden input control with the ID *rdProcessParams\_<Schedule Element ID>*.

## Saving the Parameters

When a Process task is called to save the task data, the XML string of parameters is passed to it as a request variable. The elements used to store Scheduler data, Procedure.Scheduler Create Task and Procedure.Scheduler Update Task, will automatically look for and use this request variable and store the parameters with the Scheduler task.

## Retrieving the Parameters

We need to reverse the previous process to retrieve the stored parameters and load them into the Schedule element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583650455/usingsched_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563000215/usingsched_05a.png)

The example shown above is of a definition that will allow users to edit stored Scheduler tasks. A DataLayer.Scheduler, a child of Local Data, is used to retrieve data for the desired Scheduler task. Then a **Default Request Parameters** element is used with a Local token to create a request variable named *rdProcessParams\_<Schedule Element ID>* with the value of the ProcessParams column in the datalayer. This will automatically load any stored parameters into the Schedule element interface,
so that they can be edited.
