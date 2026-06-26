---
title: "Drill-down and Drill-through Features"
id: 4419723288471
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723288471-Drill-down-and-Drill-through-Features
updated_at: 2022-07-17T02:22:57Z
---

# Drill-down and Drill-through Features

# Drill-down and Drill-through Features

Users frequently want to be able to get the details that support the data shown in charts and there are several ways developers can provides this. Adding "drill-down" functionality involves adding **Action** elements so that clicking on the chart will present detail information.

![](https://devnet.logianalytics.com/hc/article_attachments/7522732596119/workclasscharts_40.png)

For example, adding an **Action.Report** and **Target.Report** element as children of the **Animated Chart.Pie** element will cause each wedge in a Pie chart to become a link to the target report.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) When a chart uses its own datalayer element to retrieve data, that data is accessed with an **@Chart** token, not the @Data token that's used with Data Tables.

Data specific to each pie wedge can be passed to the target report using **Link Parameters** and an @Chart token. The target report can then take action, such as filtering its own data, based on an @Request token representing the Link Parameter value.

## Automatic Drill-Through Report

Charts often use grouping to aggregate data for a consolidated view. There are times, however, when it's useful to be able to examine the detail data that was used to create that aggregation and you can provide this "drill-through" functionality with the **Group Drillthrough** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522701090199/workclasscharts_41.png)

In the example shown above, a **Group Drillthrough** element has been added beneath a Chart.Pie element. All of the element's attributes, other than **ID**, are optional but the example shows that a custom caption and an export button selection have been entered. More information about the attributes can be found in the element's [Element
Reference page](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2471&iName=GroupDrillthrough&iType=Element&iLabel=Group+Drillthrough&lnkpg=0).

The resulting pie chart looks no different than usual, but when one of its wedges is clicked, a detail report, like the example shown below, is automatically generated, containing all of the relevant detail data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522743988247/workclasscharts_42.png)

Group Drillthrough is only available for the **Chart.XY**, **Chart.Pie**, **Chart.Heatmap**, and **Chart.Scatter** elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The Group Drillthrough element is designed to work charts with datalayers that have a **Group Filter**, **Crosstab Filter**, or **Relevance Filter** child element. This has implications if you want to use Group Drillthrough and you're working with DataLayer.SQL; for example, you'll have to use a Group Filter element instead of doing the grouping in your query.

The Group Drillthrough element's attributes allow you to customize certain aspects of the detail report. You can also include **Drillthrough Column** elements beneath the Group Drillthrough element; they allow you to set the number columns that will appear in the report and to customize their appearance.
