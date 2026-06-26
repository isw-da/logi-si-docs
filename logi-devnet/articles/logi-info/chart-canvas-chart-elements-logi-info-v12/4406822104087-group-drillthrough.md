---
title: "Group Drillthrough"
id: 4406822104087
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822104087-Group-Drillthrough
updated_at: 2022-04-06T06:03:21Z
---

# Group Drillthrough

# Group Drillthrough

The Chart Canvas element's **Group Drillthrough** child element adds grouped data point links which, when clicked, display a basic drill-through report showing the detail data used to create the group.

The following topics discuss the Group Drillthrough child element:

* [Group Drillthrough Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817014167-Group-Drillthrough-Attributes#Attributes)
* [Customizing Detail Report Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406817013143-Customizing-Detail-Report-Columns#Customizimg)

## About Group Drillthrough

Data is often grouped, especially when it's related to time, to show an aggregated view of it. "Sales by Month" is an example where the data for each month is aggregated by month. It's often useful to be able to quickly examine the data in the aggregation and the Group Drillthrough element provides this feature for Chart Canvas charts.

  
![](https://devnet.logianalytics.com/hc/article_attachments/4417584172695/ccc_drill_01.png)

In the example shown above, a line chart visualizes data that's been grouped by month. When the March data point is clicked, the detail report is displayed. It contains all of the grouped data in a data table. The detail report format and styling shown are the defaults, using the stock Signal theme.
The Group Drillthrough element can be used as a child of the **Chart Canvas** element, or as the child of individual **Series** elements.
