---
title: "Creating and Editing Scheduler Tasks"
id: 4406818021271
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818021271-Creating-and-Editing-Scheduler-Tasks
updated_at: 2022-04-06T06:09:40Z
---

# Creating and Editing Scheduler Tasks

# Creating and Editing Scheduler Tasks

Developers need to create Process definition tasks to create and edit the Scheduler task data that, typically, has been collected using the Schedule element.

The **Procedure.Scheduler Create Task** and **Procedure.Scheduler Update Task** elements are used for this purpose and have identical attributes, with the exception that the Scheduler Update Task element also includes a Scheduler Task ID attribute. They have the same attributes as the Schedule element, which was discussed on the previous page.

These two elements have an additional attribute: Scheduler Session Variables, which let your enumerate, in a comma-separated list, the Session variables that should be passed to the scheduled task when it's executed.

Both of these elements are used in Process tasks that might, for example, be called from a report definition using a "Create a New Scheduled Task" or an "Edit a Scheduled Task" link on a report page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) They require **Target.Process** child elements and use them in an unusual fashion. Instead of identifying a **destination** for program flow to be redirected to, as most Target-type elements do, these child elements' attributes are used instead to supply the Scheduler database with the Process definition **file name** and Process **task name** for the Scheduler task being created or updated.
Typically these are in the form of Request tokens passed from the calling report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583652631/usingsched_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563002391/usingsched_03a.png)

As shown in the example Process definition above, a Procedure.Create Scheduler Task element ("CreateTask") has been added to a Process task. Beneath it, a **Target.Process** element is used to identify the Process definition file and Process task that will be "called" by the Scheduler. A definition using Procedure.Update Scheduler Task looks very similar.

When a new Scheduler task is created, its **Task ID** is returned and can be accessed using a procedure token. In the example shown above, it would be available as: @Procedure.CreateTask.TaskID~ (remember that tokens are case-sensitive).
