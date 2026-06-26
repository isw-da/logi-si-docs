---
title: "Schedule Reports with Server Manager"
id: 1500009515862
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515862-Schedule-Reports-with-Server-Manager
updated_at: 2021-06-17T01:58:36Z
---

# Schedule Reports with Server Manager

# Schedule Reports with Server Manager

Customers with versions of Logi Info earlier than v9.5 can **schedule reports** to run automatically using **Server Manager**, one of the utility programs installed along with Logi managed reporting products. This topic explains the steps needed to schedule report generation using Server Manager. Topics include:

* About Server Manager
* [Use Process Definitions and Tasks](#Process)
* [Schedule a Task](#Scheduling)
* [Conclusion](#Conclusion)

Customers with versions of Logi Info v9.5 and later use a different scheduling technology, the Logi Scheduler Service, and should refer to [Introduction to Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009515482-Introduction-to-Logi-Scheduler).

## About Server Manager

Server Manager is a **utility program** that's **automatically installed** when you install Logi managed reporting products and it provides a number of application management features. Task scheduling, however, is **not available** for Logi Report.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778520087/schedrpt_02.png)

To launch it, use Start Menu -> All Programs -> Logi Info -> Server Manager, as shown above. If it does not appear on your menu, you can run it manually using C:\Program Files\LogiXML IES Dev\lgxManager.exe

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771624727/schedrpt_03.png)

The Server Manager, shown above, allows developers to complete a number of tasks, including **registering** an application with the Internet Information Server (IIS), and **upgrading** applications to a new release. (Image has been condensed for space considerations.)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778520343/schedrpt_04.png)

Expanding one of the applications in the applications tree, as shown above, reveals several other tasks that can be performed: the values in the **\_settings definition** can be viewed and modified, password-based **obfuscation** can be used to make your source code unreadable in production, and **tasks can be scheduled**. It is this last activity that is the focus of this topic.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Note that if you have installed **Logi Report**, the Server Manager will also be installed and the **Settings** and **Obfuscation** items shown above will be available, but the **Scheduled Tasks** item **will not appear**. You must have Logi Info in order to schedule tasks.

## Use Process Definitions and Tasks

Only Process **tasks** can be **scheduled**, which is why this doesn't apply to Logi Report (it does not support Processes). Report definitions themselves cannot be directly scheduled; they have to be called by a **task** in a **Process definition**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771624983/schedrpt_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778520599/schedrpt_05a.png)

Consider the example Process definition shown above, which could do the following:

* The RunDailyPieCharts task **runs a report** and saves it as an **HTML file** to a shared network location, where staff can access it.
* It also **emails** a copy of that report, as an **attachment**, to some satellite offices that are not on the network.
* Finally, it runs the report again with some special Request parameters and sends it as an **HTML-formatted email** to the CEO.

There are **many** other **report-processing actions** that can be taken in a **process task**. For example, reports can be exported in PDF, Excel, or Word format and saved to the file system.

If you are outputting a report to a file, the **system token** for the application's physical path can be very useful in this case. For example:

@Function.AppPhysicalPath~\rdDownload\DailyPieCharts.htm

Also, ensure that the ASP.NET (IIS 5.x) or NETWORK SERVICE (IIS 6.x) account has **Write** permissions to the destination folder (rdDownload in the example above).

Once your have your process task defined and tested, you're ready to **schedule it**.

## Schedule a Task

The actual **scheduling** of tasks is accomplished, as mentioned earlier, in **Server Manager**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778520855/schedrpt_06.png)

Launch Server Manager and, to begin scheduling, **select** and **right-click** the **Scheduled Tasks** item for your application, then select the **New...** item on the pop-up menu.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778521111/schedrpt_07.png)

To create a new schedule item:

1. Enter the **credentials** for an account with **administrative privileges** on the web server computer.
2. Enter the **URL** of your application.
3. Select the **Process Definition****File** name and the **Task ID** for your process task.
4. If your process needs **Request parameters** passed to it, enter them in the **Link Parameters** section.
5. Click **Save** to save your schedule item. A **scheduled task icon** will appear in the application tree.  
   If you receive an error of any kind while trying to save the schedule item, the most likely cause is that the administrator credentials provided are incorrect.
6. Click **Set Run Times**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778521367/schedrpt_08.png)

To set run times:

7. Click **New...** to create a new run time schedule.
8. Set the **frequency** and **start time** for your task. If more granularity in timing control is needed, it can be found by clicking **Advanced...**
9. Multiple run times can be scheduled for this task, if desired.
10. Click **OK** when finished.
11. Click **Save** again to ensure that your run time has been saved with your schedule item!

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771625239/schedrpt_09.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778521623/schedrpt_09a.png)

Now click on **Scheduled Tasks** under your application in the application tree and you should see your new task in the **list of scheduled tasks**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771625495/schedrpt_10.png)

If you **click** the new scheduled task **item** in the application tree, its properties are displayed and can be **edited**.

If you **right-click** the new **item**, as shown above, you can **rename** or **delete** it or **run** it immediately (great for testing purposes).

When a scheduled task runs, there is **no indication** within Server Manager that anything is happening.

## Conclusion

You have seen that **Server Manager** provides an **easy-to-configure** method of **scheduling** process **tasks** for pre-v9.5 reports. These tasks can be written to run reports and distribute them in a variety of formats, using a variety of delivery mechanisms.
