---
title: "Setting Variables in a Task"
id: 4406817798551
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817798551-Setting-Variables-in-a-Task
updated_at: 2022-04-06T06:08:16Z
---

# Setting Variables in a Task

# Setting Variables in a Task

In a task, you may need to have working variables that you can manipulate. For example, you may need to perform a calculation on a Request variable value. There are several ways to create these "local variables".

The **Procedure.Set Procedure Vars** element allows you to set variables and values that can be used for calculations, etc., within the scope of the task.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583763351/workproctask_09b.png)

Variables are created using a child **Procedure Parameters** element, which defines name-value pairs, just like other parameters elements, as shown above. The values can be set using literals, tokens, or expressions prefaced with the "=" sign. The resulting procedure variables can be referenced anywhere in the task using this token:

@Procedure.*<Procedure.Set Procedure Vars element ID>*.*<variable name>~*

Session variables can be also used in the same way for this purpose:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583763479/workproctask_10.png)

In the example above, a **Procedure.Set Session Vars** element has been added. The new session variable it creates applies the DateAdd function to a date passed as a Request variable. Now, in the Procedure.SQL element, we can use the token @Session.newStart~ to update a database table with the new date.

Session variables set in tasks are, of course, globally available and can be accessed later in report definitions and other tasks.
