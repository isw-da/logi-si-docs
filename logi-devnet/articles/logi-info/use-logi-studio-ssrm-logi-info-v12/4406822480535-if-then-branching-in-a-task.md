---
title: "If-Then Branching in a Task"
id: 4406822480535
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822480535-If-Then-Branching-in-a-Task
updated_at: 2022-04-06T06:08:14Z
---

# If-Then Branching in a Task

# If-Then Branching in a Task

Data validation provides a fine example of *conditional branching* within a task. Tasks are excellent places to do data validation if you can't, or don't want to, do it in a Report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563116311/workproctask_09.png)

In the task example shown above, we introduce the **Procedure.If** element, which allows you to use conditional branching in your task. In the example, we want to validate a password entered by the user in a report definition. The Save button in the report calls this task and the Procedure.If element's **Expression** attribute uses an @Request token to access the password value. If the Expression attribute formula evaluates to *True*, then its child elements will be processed. If it evaluates
as *False*, the child elements are ignored and the next
sibling element down will be processed.

So, if the evaluation is *True* (the password is less than 8 characters long), we *skip* the **Procedure.SQL** element and run the **Response.Report** element. A further enhancement to this task would be to add a **Link Parameters** element beneath Response.Report to pass an error message back to the calling report.

If the evaluation is *False*, the password length is acceptable and the next sibling element, the Procedure.SQL element, is processed. Once it completes, processing goes on to the Response element at the end of the task to redirect processing elsewhere.

You can have *multiple* Procedure.If elements in a task and they can be nested. They're useful, of course, for many other purposes besides data validation and can be used any time you want to direct processing flow based on evaluation of an expression.

Several other elements are available for use in controlling conditional branching:

**Procedure.Else** - This element *must* be a sibling of, and immediately follow, a Procedure.If element. It identifies a conditional block of procedures that will be run if the Procedure.If element immediately above it evaluates to *False*. If the Else block ran, the token @Procedure.myProcedureID.rdReturnValue~ returns *True,* otherwise it returns *False*.

**Procedure.Switch** - This element works with one or more child **Procedure.Switch Case** elements to define conditional blocks of procedures to be run when a specified value matches. Use it when there are multiple conditional blocks defined and just one of them is to be run, based on the value of a variable. You can also use a child **Procedure.Switch Else** element, which runs its block of procedures if *none* of the previous Switch Case elements match the specified value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583764887/workproctask_09a.png)

The value to test against is specified in the Expression attribute and can be literal value, a token, or even JavaScript that evaluates to a value. The Data Type attribute ensures comparisons, especially of dates, are made correctly.
