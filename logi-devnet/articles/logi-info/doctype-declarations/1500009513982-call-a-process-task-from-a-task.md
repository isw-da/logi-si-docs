---
title: "Call a Process Task from a Task"
id: 1500009513982
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009513982-Call-a-Process-Task-from-a-Task
updated_at: 2021-06-17T01:57:59Z
---

# Call a Process Task from a Task

# Call a Process Task from a Task

**Logi Info** developers can use Processes definitions, which contain Tasks. This feature can really bring Logi applications to life. However, there is no such thing as a "Response.Task" element, so it may not be readily apparent that you *can* call one process task from another process task. Here's how:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778746135/procfromproc_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778746391/procfromproc_01a.png)

In the Process definition shown above, there are two tasks. Assume that the **TestLogin** task will be called from a report login page. It performs some validation and upon success calls the **ShowMenuPage** task using a **Response.Link** element. The URL attribute for the Target.Link element contains the following:

@Constant.MyWebServer~/rdProcess.aspx?rdProcess=MyTasks&rdTaskID=ShowMenuPage

where:

* A constant is used for the basic web server URL (i.e.,  https://devnet.LogiAnalytics.com)
* The process definition file is named in the query string (i.e., **MyTasks**)
* The target task ID is also named in the query string (i.e., **ShowMenuPage**)

The transfer from one process to another causes no visible change in the web page being viewed at the time. Link Parameters can be used to pass information from one process to the other.
