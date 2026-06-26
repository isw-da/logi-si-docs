---
title: "Getting Data with DataLayer.Scheduler"
id: 4406818023703
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818023703-Getting-Data-with-DataLayer-Scheduler
updated_at: 2022-04-06T06:09:43Z
---

# Getting Data with DataLayer.Scheduler

# Getting Data with DataLayer.Scheduler

A special datalayer element, **DataLayer.Scheduler**, is used to retrieve data from the Scheduler database. The query it uses can be restricted by providing default values for some of the element's attributes. When examining or editing a Scheduler task with User Input elements, this datalayer is typically used with **Local Data** so that the data retrieved is widely available to other elements in the definition, using @Local tokens. It can also be used beneath a **Data Table** to display
all Scheduler tasks.

DataLayer.Scheduler has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the element ID of a Connection.Scheduler element in the \_Settings definition. Connects the datalayer to the Scheduler database. |
| ID | Specifies a unique element ID. |
| Include Task Result Error Message | Specifies whether task error messages will be included in the data. If set to *True*, the datalayer will include an ErrorMsg column containing error message text from any failed Scheduler tasks. The default value is *False*. |
| Scheduler Application ID | Specifies the first 20 characters of the name of a Logi application or any other categorizing text developers want to use. If not blank, acts as a Condition Filter and limits the datalayer query results to Scheduler tasks with matching values for this column. Max: 20 characters. |
| Scheduler Custom Column 1 Scheduler Custom Column 2 | Specifies a value of any kind with a maximum length of 1,000 characters. If not blank, used to limit the datalayer query results to Scheduler tasks that match this column's value. |
| Scheduler RunAs | Specifies a User Name value to be used when a Scheduler task is executed and Logi Security is enabled. The name is provided to Logi Security in order to ensure that reports are run with appropriate security control. Leave blank if Logi Security is not enabled. Max: 50 characters. |
| Scheduler Task ID | Specifies the unique ID of a Scheduler task (these IDs are created and returned when new Scheduler tasks are created). If not blank, used to limit the datalayer query results to Scheduler tasks for the specified task ID. |
| Scheduler Task Name | Specifies a unique name given to a Scheduler task, generally for easier task identification. If not blank, used to limit the datalayer query results to Scheduler tasks for the specified task name. Max: 50 characters. |

When DataLayer.Scheduler runs, it retrieves the following data columns for each stored Scheduler task:

| Column | Description |
| --- | --- |
| TaskID | Unique Scheduler task ID. |
| ApplicationID | Logi application name. |
| TaskName | Descriptive name for Scheduler task. |
| CustomColumn1 | Value selected by developer./ |
| CustomColumn2 | Value selected by developer. |
| IsDisabled | "True" or "False" - Indicates state of this Scheduler task; disabled tasks are not executed. |
| ScheduleXML | XML data containing date-time-interval specific information. Example:  <Schedule Type="Once" StartDate="2013-02-05" EndDate="2013-02-27" FirstRunTime="13:48" /> |
| ProcessXML | XML data containing Process-specific information. Example:  <ProcessTask ProcessFile="myProcess.Run" TaskID="RunSalesReport" URL="http://localhost/myApplication" PhysicalPath="C:\Projects\myApplication"><LinkParams inpCategory="3" /></ProcessTask> |
| TimeCreated | ISO format timestamp for creation of this Scheduler task.  Example: 2013-02-03T16:37:18-05:00 |
| TimeModified | ISO format timestamp for modification of this Scheduler task.  Example: 2013-02-03T16:37:18-05:00 |
| TimeLastRun | ISO format timestamp for this Scheduler task's last run.  Example: 2013-02-03T16:37:18-05:00 |
| TimeNextRun | ISO format timestamp for this Scheduler task's next scheduled run.  Example: 2013-02-03T16:37:18-05:00 |
| RunAs | The User Name to pass to Logi Security when the Scheduler task is executed. Ignored when the Schedule task runs if Logi Security is not enabled. For more information, see [Running and Deleting Scheduler Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4406822599191-Running-and-Deleting-Scheduler-Tasks). |
| WasSuccessfulLastRun | "True" or "False" -Indicates if last run of this Scheduler task was successful (i.e. occurred without errors). |
| TaskResults | Fully-qualified path and name of task results file on the server. Will not exist if tasks have never been run. Examples:  (.NET) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Log\  rdSchedulerTask-8-d55cadb8-e243-437d-8587-d190417bdcb2.xml (Java) C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java\Log\  rdSchedulerTask-8-d55cadb8-e243-437d-8587-d190417bdcb2.xml |
| IsRunning | "True" or "False" -Indicates if this Scheduler task is currently running. |
| ErrorMsg | If the datalayer's **Include Task Result Error Message** attribute is set to *True*, this column will include the error message text for any failed tasks. |
| ScheduleDescription | Plain language description of date-time-interval information for this task: Example: At 1:48 PM on 02/05/2013 |
| ProcessUrl | URL for the web application in which the Process definition file named in the next field resides. Example: http://localhost/myWebApp |
| ProcessFile | Name of the Process definition file, without a file extension, that contains process task to be executed when the Scheduler task runs. *Do not include the .lgx file extension*. |
| ProcessTaskID | Name of the process task, within the process definition named in the previous attribute, that will be executed when the Scheduler task runs. |
| ProcessParams | List of parameters to be passed to the process task that will be executed when the Scheduler task runs. Example: <LinkParams CategoryID="4" /> |

In order to edit an existing Scheduler task, it's the developer's responsibility for retrieve the data for the task and then provide it to the Schedule element, described below.
