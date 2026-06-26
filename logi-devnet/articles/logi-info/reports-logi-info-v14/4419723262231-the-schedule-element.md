---
title: "The Schedule Element"
id: 4419723262231
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723262231-The-Schedule-Element
updated_at: 2022-07-17T02:23:01Z
---

# The Schedule Element

# The Schedule Element

The **Schedule** element makes it easy to create and edit Scheduler Tasks. Because it's a super-element, adding it to a report definition automatically creates a user interface for a Scheduler task.

![](https://devnet.logianalytics.com/hc/article_attachments/7522702101399/usingsched_01.png)

As shown above, the user interface presented by the Schedule element allows the user to select criteria for the Scheduler task. It's dynamic and will present more or fewer controls as required. For example, in the image above right, when a Monthly schedule is selected, the element expands vertically to display the months (a horizontal expansion, to the right, instead is also an option).

The Schedule element is built as an HTML table and has typical table attributes, such as Layout, Width, and Width Scale, used to control its size. The Schedule element also uses the following other attributes:

| Attribute | Description |
| --- | --- |
| Format | Specifies the format of the Start and End dates in the UI. Other format choices are shown but have no effect. Default: *System Short Date format* |
| Schedule Intervals | A comma-separated list of the interval modes that will be displayed in the UI. This can be used to limit the type of Schedules tasks that can be created and saved. Valid choices are *Once*, *Daily*, *Weekly*, *Monthly,* *Minutes,* and *Hourly*. Default: *All modes* |
| Schedule Orientation | Specifies how the UI expands when certain interval modes are selected. *Horizontal* places the configuration options for the selected interval mode to the right of the interval, start date, end date and start time inputs. *Vertical* (the default) places the configuration options below them. |
| ScheduleXML | A string of XML data that represents the date-time-interval data for a Scheduler task. This can be typed into this attribute's value as a "hard-coded" string or placed there using tokens such as @Local. This provides the mechanism for reading a schedule task, using Local Data and DataLayer.Scheduler, from the Scheduler database and placing the retrieved data into the Schedule element for manipulation by the user. |
| Show Days Of The Week | Specifies that a checklist of days-of-the-week will be displayed when the *Weekly* interval mode is selected. Default: *True* |
| Show Months | Specifies that a checklist of months will be displayed when the *Monthly* interval mode is selected. Default: *True*. |
| Show Process Parameters | Specifies that additional controls, used to add any number of name-value pairs of parameters used to run a Scheduler task, will be displayed. This is primarily used for administrative applications. Default: *False*. |
| Show Schedule XML | Specifies that, as options are selected in the UI and the XML data is generated, it will be displayed to the developer below the element. This is intended to be used for debug purposes only. Default: *False* |
| Template Modifier File | Specifies the name of a template modifier file that can be used to alter the user interface. Can be used, for example, to change language- and culture-specific control Captions. New for 14.2 You can also use this attribute to set a default Time Zone for scheduled reports. |

The element's UI *does not* display the ProcessXML value, a string of XML data that includes the task name, application URL, process definition file name, and process task ID, nor does it display the Task Name and Run As values. These values are available, however, from the Scheduler database as columns for retrieval using DataLayer.Scheduler and, if desired, the developer can create a UI to display and update them outside of the Schedule element interface.

As mentioned above, the **Schedule** element has a **Show Schedule XML** attribute which can be turned on during development to assist in understanding scheduling intervals:

![](https://devnet.logianalytics.com/hc/article_attachments/7522702122775/usingsched_02.png)

The image above shows what the display looks like when the Show Schedule XML attribute is set to *True*. If you change the interval selections, the ScheduleXML display will be immediately updated with new values.

Parameters that are to be passed to the process task at runtime can also be stored in the Scheduler task. For more information, see [Working with Process Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4419723265303-Working-with-Process-Parameters).

## Using CSS with the Schedule Element

Many presentation aspects of the Schedule element can be customized through the use of CSS classes. The default style sheet used by the element is <application folder>\rdTemplate\rdSchedule\rdScheduleStyle.css

Classes in this default style sheet can be overridden by copying them into, and altering them in, your own application style sheet. *Do not modify the default style sheet.*

For example, this class adds additional **space** between the UI's labels and input controls:

.rdScheduleColumnGap {  
width: 15px; /\* add more space between labels and controls \*/  
 }

and this one adds a **background color** to the element:

.rdSchedule TABLE {  
border-collapse: collapse;  
border-width: 0px;  
background-color: AliceBlue; /\* add BG color so element is obvious \*/  
 }

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) HTML tables are used within the Scheduler super-element, and so you can count on working with table-related HMTL tags to make some CSS changes.
