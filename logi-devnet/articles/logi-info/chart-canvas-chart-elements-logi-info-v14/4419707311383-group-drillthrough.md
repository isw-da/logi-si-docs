---
title: "Group Drillthrough"
id: 4419707311383
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707311383-Group-Drillthrough
updated_at: 2022-07-17T02:25:18Z
---

# Group Drillthrough

# Group Drillthrough

The Chart Canvas element's **Group Drillthrough** child element adds grouped data point links which, when clicked, display a basic drill-through report showing the detail data used to create the group.

The following topics discuss the Group Drillthrough child element:

* [Group Drillthrough Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707317399-Group-Drillthrough-Attributes#Attributes)
* [Customizing Detail Report Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707313943-Customizing-Detail-Report-Columns#Customizimg)

## About Group Drillthrough

Data is often grouped, especially when it's related to time, to show an aggregated view of it. "Sales by Month" is an example where the data for each month is aggregated by month. This feature is often useful to be able to quickly examine the data in the aggregation. The **Group Drillthrough** element can be used as a child of the **Chart Canvas** element, or as the child of individual **Series** elements.

In the example below, a line chart visualizes data that has been grouped by month. When the March data point is clicked, the detail report displays, containing all of the grouped data in a Data Table:

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522863893911/ccc_drill_01.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Group Drillthrough can also be used in conjunction with the Drill To feature. To utilize this feature, ensure that your Chart Canvas or Series element includes a **Chart Drill To** child element. Once the Drill To element is enabled, selecting a data point displays a list of columns. Selecting a column re-draws the chart so that only the data representing that specific filter is shown.
From there, you can use Group Drillthrough to drill further into the data, like below:

[Your browser does not support the video tag.](https://devnet.logianalytics.com/hc/article_attachments/7522818762263/group_drillthrough.mp4)
