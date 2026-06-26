---
title: "Error Handling in Tasks"
id: 4406822479383
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822479383-Error-Handling-in-Tasks
updated_at: 2022-04-06T06:08:15Z
---

# Error Handling in Tasks

# Error Handling in Tasks

Error handling is an important function for any application and tasks include a special element for this purpose.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575565207/workproctask_24.png)

The **If Error** element allows you to handle errors that occur when running procedures in a task. The example above shows a typical implementation: if an error occurs when a table update is attempted, an email alert will be sent out and a redirect to a report page will occur (possibly back to the page that called the task). The actual error text can be passed to that report page, using a **Link Parameters** element, as a Request variable.

The *placement* of the If Error element is important. Errors will "bubble up" through procedures until an If Error element is found, and if not found, up through tasks and the definition itself. You have the choice of placing your error handling elements in different locations to handle different situations. Without an If Error element, the application will return an error page if an error occurs.

You may use multiple If Error elements in a task, if desired. As mentioned in the previous paragraph, you can access the error message text. This is done using this special token: @Procedure.*yourProcedureID*.ErrorMessage~

Because the element ID of the procedure is part of the token, it limits the scope of the error message availability. You can also use: @Function.LastErrorMessage~if you prefer, and its scope is application-wide.

The If Error element has an **Error Filter** attribute, which allows individual If Error elements to handle different errors. Set
the Error Filter attribute value to any text found within the error message. If the text is
found, the If Error element will handle the error. If not, the error will be ignored and the error will "bubble up". This allows you to target specific errors, and to react to them differently, if desired. If you use this approach, you'll probably want to include a final If Error element *without* any Error Filter text, to catch any errors not specifically handled by your other handlers.

The Error Filter also allows you to *ignore* errors, by specifying their error message text and then placing *no* child elements beneath the If Error element. When that error occurs, it will be considered "handled" and processing will continue with the next element after the failed procedure element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The If Error element only recognizes errors that occur *in the process task* and will not react to those that occur in a report definition run by the task. For example, if a task uses Procedure.Export CSV to export data from a report definition to CSV and an error occurs when the report is run, If Error will not see it. In this case, you can use **If Data Error** in the report
definition
to provide alternate data when the report is exported, then **Procedure.Run DataLayer Rows** to read the exported file, test its data, and take appropriate action.
