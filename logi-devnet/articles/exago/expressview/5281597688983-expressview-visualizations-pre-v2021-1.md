---
title: "ExpressView: Visualizations (pre-v2021.1)"
id: 5281597688983
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281597688983-ExpressView-Visualizations-pre-v2021-1
updated_at: 2022-05-03T22:09:03Z
---

# ExpressView: Visualizations (pre-v2021.1)

# ExpressView: Visualizations (*pre-v2021.1*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

**Visualizations** allow data to be showcased in a visual format. They allow data to be scanned quickly for patterns and trends. Charts can be easily made and customized in ExpressViews, in as little as one click.

![6DEFDHQ1c1.png](https://devnet.logianalytics.com/hc/article_attachments/5432273498519/6defdhq1c1.png)

An ExpressView Visualization

To add a chart to an ExpressView:

1. Click the **Show Visualization** ![ShowViz.png](https://devnet.logianalytics.com/hc/article_attachments/5432220914071/showviz.png) icon in the top toolbar. A bar chart is added and populated with the data from the ExpressView.
2. In the Visualizations pane, select the type of chart you want to use. The chart immediately swaps to that type. Choose from *Bar and Column*, *Pie and Other Single-Series*, *Line and Area* or *Miscellaneous*.

When **Run Mode** is on, click on a chart series to drill down into the data for that series. This filters the data columns to only the series you select.

You can add many more personal touches, small or large, to the visualizations you create. See the following sections for details on how to customize visualizations.

## Choosing Chart Data

When a visualization is first added, the application presets the chart fields to try to match the ExpressView data as closely as possible. This may not always match the data that you want the chart to use.

To see the chart data fields, click the **Visualizations ![VizMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432303731735/vizmenu.png)**icon in the pane on the right side of the screen, then click the **Data** tab. There are two sections: **Labels** and **Values**.

### Labels

The **Labels** field is a group of data values, each iteration of the group represented as a series on the chart. For example, using an Employees group field as the label field represents each employee as a series.

Several charts allow an additional labels field. This is useful if you have a nested group, which represents common series to be measured across several groupings. For example, to compare the number of sales per product per employee, you could add a nested Product field as a second label to the aforementioned employees chart.

To add a chart label, either:

* Drag a data field onto the chart and release on the **Add Label** area.
* In the Visualizations pane, click the **Data** tab. Either:
  + Drag a data field to the **Labels** area.
  + Click ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Label**, then select a field from the **Field** list.

![screen.expressview_drag_field_to_chart_label.png](https://devnet.logianalytics.com/hc/article_attachments/5432273521815/screen.expressview_drag_field_to_chart_label.png) ![screen.expressview_drag_field_to_data_label.png](https://devnet.logianalytics.com/hc/article_attachments/5432268770711/screen.expressview_drag_field_to_data_label.png)  

Drag a field onto the visualization or onto the Data tab to add it as a label

### Values

The **Values** field is the data values to plot on the chart for each iteration of each labels group. For example, the number of sales per employee.

Several charts allow for multiple values fields. This is useful if you have common series to be measured across several groupings, and the values fields are in the same data row. For example, the number of sales and number of lost sales per employee.

To add a chart value, either:

* Drag a data field onto the chart and release on the **Add Value** area.
* In the Visualizations pane, click the **Data** tab. Either:
  + Drag a data field to the **Values** area.
  + Click ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Value**, then select a field from the **Field** list.

![screen.expressview_drag_field_to_chart_value.png](https://devnet.logianalytics.com/hc/article_attachments/5432305875991/screen.expressview_drag_field_to_chart_value.png) ![screen.expressview_drag_field_to_data_value.png](https://devnet.logianalytics.com/hc/article_attachments/5432221438487/screen.expressview_drag_field_to_data_value.png)  

Drag a field onto the visualization or onto the Data tab to add it as a value

## Interactive Editing of ExpressView Visualizations

You can invert the data, change the Type, Theme, Legend Location, or Sort of ExpressView visualizations by simply right-clicking with the introduction of interactive HTML to ExpressViews in *v2018.2*.

![rightclickchartchange.png](https://devnet.logianalytics.com/hc/article_attachments/5432306026263/rightclickchartchange.png)

[![Concept Link Icon](https://devnet.logianalytics.com/hc/article_attachments/5432159914263/transparent.gif)See Also](javascript:void(0);)
