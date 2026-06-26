---
title: "Drillthrough to Column Detail"
id: 4419722781975
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722781975-Drillthrough-to-Column-Detail
updated_at: 2022-07-17T02:24:48Z
---

# Drillthrough to Column Detail

# Drillthrough to Column Detail

A Crosstab Table does a great job of aggregating data and displaying it in a manner that makes it easy to see its progression or differences. There are times, however, when it's useful to be able to examine the detail data that the crosstab filter used to create the value in each column cell. The **Group Drillthrough** element provides this functionality.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816524951/xtabtable_19.png)

In the example above, a **Group Drillthrough** element has been added beneath a Crosstab Table Value Columns element. All of the element's attributes, other than ID, are optional but the example shows a custom caption and export button selections have been entered. More information about the attributes can be found in the element's [Element
Reference page](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2471&iName=GroupDrillthrough&iType=Element&iLabel=Group+Drillthrough&lnkpg=0).

![](https://devnet.logianalytics.com/hc/article_attachments/7522844482199/xtabtable_20.png)

The resulting Crosstab Table is shown above. When the cursor is hovered over a value cell, a drill-through icon is displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816542359/xtabtable_21.png)

When the icon is clicked, a report containing all of the relevant detail data, like the example shown above, is automatically generated and displayed.

The Group Drillthrough element's attributes allow you to customize the icon image that appears in the Crosstab Table and certain aspects of the detail report. You can also include **Drillthrough Column** elements beneath the Group Drillthrough element; they allow you to set the number columns that will appear in the report and to customize their appearance.
