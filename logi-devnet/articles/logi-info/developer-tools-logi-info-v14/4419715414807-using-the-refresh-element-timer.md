---
title: "Using the Refresh Element Timer "
id: 4419715414807
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715414807-Using-the-Refresh-Element-Timer
updated_at: 2022-07-17T02:23:51Z
---

# Using the Refresh Element Timer 

# Using the Refresh Element Timer

Dashboards are often used to display **time-sensitive** or **transactional** data and it's very useful to be able to update the Dashboard panel contents periodically and automatically. This can be accomplished using the **Refresh Element Timer** element. This element uses AJAX techniques to automatically refresh one or more elements in a panel's content using an **a**djustable time interval.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807479063/introdash_19.png)  

The attributes for this element (all required) include:

* **Element ID** - Specifies the ID of the element that you want to periodically refresh. Multiple IDs, separated by commas, can be entered but the **scope** of each timer element is **limited** to its own panel. Multiple elements can also be refreshed by placing them under a Division element and specifying the Division element ID here. *Do not* specify elements that are children of Data Table elements (datalayers, columns, etc.)
* **ID** - Specifies a unique element ID for this element.
* **Refresh Interval** - Specifies the amount of time, **in seconds**, between refreshes of the element specified in Element ID. *Use caution* when specifying a very short interval if a large number of users will access this Dashboard: database server performance could be seriously impacted.

When there's a Data Table in the report being refreshed and it has **Interactive Paging** or **Sorting** elements, set the Data Table element's **AjaxPaging** attribute to *True*.
The Refresh Element Timer element works by **re-running** the panel's report with just those elements that are to be refreshed. The report runs using request parameters from 1) Input elements on the report, 2) LinkParams and 3) URL request parameters when Request Forwarding = *True*.
When debugging has been turned on for an application, you can view **debug information** generated for each Refresh Element Timer request. These appear as additional links at the bottom of the Debug Trace page. For more information, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419715245463-Debug-Reports).
