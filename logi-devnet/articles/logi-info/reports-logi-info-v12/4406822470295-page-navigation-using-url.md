---
title: "Page Navigation Using URL"
id: 4406822470295
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822470295-Page-Navigation-Using-URL
updated_at: 2022-04-06T06:08:04Z
---

# Page Navigation Using URL

# Page Navigation Using URL

If a data table has been paginated, there are scenarios in which you might want to navigate to a specific table page. For example, suppose your data table has drill-down links in it and you'd like to return to the same data table page after drilling-down to a detail report. Yes, the "Back" button on your browser will accomplish the same thing, but there may be circumstances in which you don't want to rely on it.

When you navigate away from the paginated data table, a special Request variable is included in the URL that calls the next report. You can use that variable in the link used to return to the data table report to ensure you return to the same data table page.

To do this, include these two Link Parameters in the return link:

| Parameter Name | Parameter Value |
| --- | --- |
| *<myTableID>*-PageNr | @Request.*<myTableID>*-PageNr~ |
| rdNewPageNr | True |

where *<myTableID>* is the element ID of the paginated data table.

Logi Info developers may want to run a process task and then return to the same data table page. This can be done by passing @Request.*<myTableID>*-PageNr~ to the task and then assigning its value to a Link Parameter named rdNewPageNr when calling the data table report.
