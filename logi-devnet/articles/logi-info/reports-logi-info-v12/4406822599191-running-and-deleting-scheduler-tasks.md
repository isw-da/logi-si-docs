---
title: "Running and Deleting Scheduler Tasks"
id: 4406822599191
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822599191-Running-and-Deleting-Scheduler-Tasks
updated_at: 2022-04-06T06:09:42Z
---

# Running and Deleting Scheduler Tasks

# Running and Deleting Scheduler Tasks

When the Scheduler runs one of its scheduled tasks, it calls a task in a Process definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575476119/usingsched_06.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583651863/usingsched_06a.png)

The example shown above is of a task that runs a report and saves it as an HTML file. First, any older version of the file needs to be deleted, then a Procedure.Save HTML element is used to save the desired report as a file on the web server. After that users could presumably browse it or further procedure tasks could distribute it as email, etc. Finally, the task needs to end with some kind of Response element (although its target report will never be visible to anyone because the Scheduler
runs tasks in their own session). So, at the correct time, the Scheduler would simply call the RunMyReport task to get the job done.

Two other elements, **Procedure.Scheduler Run Task** and **Procedure.Scheduler Delete Task**, can be used to immediately run Scheduler tasks, and to delete them. These elements only require the connection ID of the Connection.Scheduler element and a TaskID.

For instance, you may wish to give your users the option to run a report immediately, instead of waiting for the scheduled time. This is done by creating a Process task that tells the Scheduler to run the desired Scheduler task right now.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575476503/usingsched_07.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563001623/usingsched_07a.png)

As shown above, this is done in a Process task using the Procedure.Scheduler Run Task element. Its attributes identify an existing Scheduler task by ID.

## Running Scheduler Tasks with Logi Security

If the Scheduler runs Process tasks within an application that implements Logi Security, there will be no physical user at the time (and no Login page), so what security credentials and rights will the Scheduler use?

The "user" in this case will be the one named in the value of the **RunAs** column in the Scheduler Task record in the Scheduler's database. Enter a valid user name in this column. If you want dynamic values and, for example, you're using Procedure.Create Scheduler Task to create the task, you can enter the @Function.UserName~ token in the RunAs field. This will automatically set the value to the user name of the currently logged-in user. In that way, the Scheduler will run the Process task
using the name of the user who created the scheduled
task.

In addition, if you're using a query of some kind to get Security Rights in the \_Settings definition, be sure to use that same token, @Function.UserName~, in the query *instead**of* @Request.rdUserName~. That will ensure that the query will return the correct rights when the Scheduler executes the application.

## Deleting a Task

The coding for a Process task for deleting a Scheduler task is identical to that shown above for creating a task, except that it uses a Procedure.Delete Task element.
