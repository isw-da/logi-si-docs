---
title: "ExpressView: Visualizations (v2021.1+)"
id: 5281589549207
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281589549207-ExpressView-Visualizations-v2021-1
updated_at: 2022-05-03T22:09:03Z
---

# ExpressView: Visualizations (v2021.1+)

# ExpressView: Visualizations (*v2021.1+*)

**Visualizations**, also known as **charts** or **graphs** allow data to be showcased in a visual format. They allow data to be scanned quickly for patterns and trends. Charts can be easily made and customized in ExpressViews, in as little as one click.

![85aBFZxgwS.png](https://devnet.logianalytics.com/hc/article_attachments/5432220893079/85abfzxgws.png)

A **3D Pie Chart** visualization with pastel custom coloring showing the percentage of sales made by each salesperson, with a tooltip showing the exact percentage for Margaret Peacock

## Table of Contents

Use the links below to skip to the applicable section of this topic.

1. [Adding a Visualization](#Adding)
   1. [Type](#Type)
   2. [Data](#Data)
      1. [Labels](#Labels)
      2. [Values](#Values)
   3. [Appearance](#Appearan)
      1. [Chart Titles](#Chart3)
      2. [Chart Colors](#Chart)
      3. [Chart Data](#Chart2)
2. [Interactive Editing](#Interact)
   1. [Drilling Down](#Drilling)
   2. [Editing a Chart Directly](#Editing)
3. [Suggested Reading](#Suggeste)

## Adding a Visualization

To add a chart to an ExpressView:

1. Click the **Add Visualization**![ShowViz.png](https://devnet.logianalytics.com/hc/article_attachments/5432220914071/showviz.png) icon in the toolbar. A bar chart is added and populated with the data from the ExpressView automatically.
2. On the ![VizMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432303731735/vizmenu.png)**Visualizations** tab of the Properties Pane, select the type of chart you want to use. The chart immediately swaps to that type. Choose from *Bar and Column*, *Pie and Other Single-Series*, *Line and Area* or *Miscellaneous*. Review [Type](#Type) for more information about each type.

There are three small icons in the lower-right corner of the visualization that determine where on the canvas the chart will appear. Choose from:

* ![VizTop.png](https://devnet.logianalytics.com/hc/article_attachments/5432267451287/viztop.png) / ![VizTopSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432220957591/viztopselected.png) — the chart will appear on the top of the canvas; report data will be on the bottom
* ![VizBottom.png](https://devnet.logianalytics.com/hc/article_attachments/5432250521751/vizbottom.png) / ![VizBottomSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432272654999/vizbottomselected.png) — the chart will appear on the bottom of the canvas; report data will be on the top
* ![VizFull.png](https://devnet.logianalytics.com/hc/article_attachments/5432250570903/vizfull.png) / ![VizFullSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432250580631/vizfullselected.png) — the chart will fill the canvas; report data will be hidden

Use the ![VizMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432303731735/vizmenu.png)

**Visualizations**

### Type

Choose one of the available chart types to display. Charts are organized into four general categories. Click each type name for additional information.

* [Bar Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281549993495-Bar-Charts)
* [Pie, Doughnut, Pyramid, and Funnel Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281573747607-Pie-Doughnut-Pyramid-and-Funnel-Charts)
* [Line Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281556941463-Line-Charts)
* Miscellaneous
  + [Scatter and Bubble Charts](https://devnet.logianalytics.com/hc/en-us/articles/5281542902039-Scatter-and-Bubble-Charts)
  + [Key Performance Indicator (KPI)](https://devnet.logianalytics.com/hc/en-us/articles/5281565061527-Key-Performance-Indicator-KPI-)

### Data

#### Labels

The **Labels** field is a group of data values, for each iteration of the group represented as a series on the chart. For example, using the Product Category group field as the label field represents each category as a series.

![SZwqbvTALc.png](https://devnet.logianalytics.com/hc/article_attachments/5432221032983/szwqbvtalc.png)

A **Bar** chart with one label field on the product category, showing the number of products in each category

Several chart types allow more than one label field. This is useful for nested groups, which represent common series measured across several groups. For example, to compare the number of products in each category manufactured by a particular manufacturer, a nested manufacturer field can be added as a second label.

![CJkGCM29MW.png](https://devnet.logianalytics.com/hc/article_attachments/5432267699863/cjkgcm29mw.png)

A **Bar** chart with two label fields: one on the product category, and the other on the manufacturer’s code number showing the number of products in each category made by each manufacturer

To add a chart label, either:

* Drag a data field from the Data Objects Pane onto the chart and release on the **Add Label** drop zone.  
  ![pMM462tVb6.png](https://devnet.logianalytics.com/hc/article_attachments/5432272879895/pmm462tvb6.png)

  Adding `LastName` as a label by dragging it to the drop zone on the chart
* In the ![VizMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432303731735/vizmenu.png) Visualizations tab, click the **Data** tab. Either:
  + Drag a data field to the **Labels** drop zone.
  + Click ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Label**, then select a field from the **Field** list.

![FunDSPjRQo.png](https://devnet.logianalytics.com/hc/article_attachments/5432272910743/fundspjrqo.png)

Adding `LastName` as a label by dragging it to the drop zone in the Properties Pane

#### Values

The **Values** fields are the data values to plot on the chart for each iteration of each labels group. For example, the products per category.

Several chart types allow for multiple values fields. This is useful if there are common series to be measured across several groupings, and the values fields are in the same data row. For example, the number of products per category and the number of views of those products on the online shopping site.

![NgIpzPNWlE.png](https://devnet.logianalytics.com/hc/article_attachments/5432221075095/ngipzpnwle.png)

A **Stack Bar** chart with two values fields: one on the distinct count of model numbers and the  sum of views in the online shopping cart system for each category

To add a chart value, either:

* Drag a data field onto the chart and release on the **Add Value** drop zone.  
  ![kf3HGoEeyx.png](https://devnet.logianalytics.com/hc/article_attachments/5432267868183/kf3hgoeeyx.png)

  Adding `OrderId` as a value by dragging it to the drop zone on the chart
* In the ![VizMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432303731735/vizmenu.png) Visualizations tab, click the **Data** tab. Either:
  + Drag a data field to the **Values** area.
  + Click ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Value**, then select a field from the **Field** list.

![Fkz7n86TF4.png](https://devnet.logianalytics.com/hc/article_attachments/5432221148823/fkz7n86tf4.png)

Adding `OrderId` as a value by dragging it to the drop zone on the Properties Pane

### Appearance

Set the styling for the **Chart Titles**, **Chart Colors** and **Chart Data**:

#### Chart Titles

![3XxptcVH0W.png](https://devnet.logianalytics.com/hc/article_attachments/5432221182615/3xxptcvh0w.png)

Add a main title and subtitle, as well as X-Axis and Y-Axis labels in this section. Each title may have a unique font, color and size.

#### Chart Colors

![wmZd82SEoa.png](https://devnet.logianalytics.com/hc/article_attachments/5432289301911/wmzd82seoa.png)

Select a palette to color the chart elements with. Choose from:

* *Theme* — a variety of named color themes are available (for example *Blue Gray*, *Emerald Forest*, *Prismatic Wave*, etc…)
* *Linear Range* — choose a starting and ending color. The application will interpolate intermediate colors for 3 or more chart elements as needed.
* *Custom* — the color of each element may be explicitly specified by manually choosing colors

Check the **Use 3D Style** checkbox to enable a three-dimensional effect on the chart elements.

![cYwCnlWLNb.png](https://devnet.logianalytics.com/hc/article_attachments/5432250879895/cywcnlwlnb.png)  
![rWOVTVgobO.png](https://devnet.logianalytics.com/hc/article_attachments/5432273182359/rwovtvgobo.png)

A multi-value **Column** chart with **Use 3D Style***unchecked* (top) and *checked* (bottom)

#### Chart Data

Use the **Data Axis Min Value** and **Data Axis Max Value** fields to set the minimum and maximum values for the axes. All values in the chart must be above the **Data Axis Min Value** and less than **Data Axis Max Value** otherwise this setting will be ignored. These settings can help make a chart easier to read. For example:

![64oF71vAXv.png](https://devnet.logianalytics.com/hc/article_attachments/5432250906135/64of71vaxv.png)  
![q9wqqu8jOo.png](https://devnet.logianalytics.com/hc/article_attachments/5432304862231/q9wqqu8joo.png)

The same line chart without (top) and with (bottom) min and max values set

Use the **Exclude Values Less Than** and **Exclude Values Greater Than** settings to exclude values outside of the set range from appearing on the chart.

Use the **Sort By** dropdown to apply a secondary sort to the chart that will affect the order *Values* are added to the visualization. Choose from *Ascending* or *Descending* order by selecting from the dropdown. The options available will differ by chart type, but in general they are:

* *Report Order —* data points are added to the chart in the order they appear on the report
* *Data Labels* — data points are sorted by their *Labels*
* *Data Values* — data points are sorted by the *Values*

**Point Labels** will display the exact values of each point on the chart. Different chart types will have different options available, but in general they are:

* *Series Values* or *Point Value* — display the value of the *values* or *point*
* *Percent of Series Values* or *Percent of Point Value* — displays the percentage of the whole represented by this *value* or *point*
* *Data Labels* or *Point Label* — display the names of the *Labels* represented by each segment of the chart
* *Data Labels with Data Values* or *Point Label with Point Values* — combine the behavior of both *Data Labels* and *Series Values* modes to place both pieces of information in the label

For some charts, the **Point Labels** may be positioned with the **Label Position** setting. Choose from:

* *Auto*: allow the application to select the best orientation for you based on available space
* *![g68qOn5XeZ.png](https://devnet.logianalytics.com/hc/article_attachments/5432268236183/g68qon5xez.png)Slant:* rotate the labels 45-degrees along the axis
* *![sKYCRS3Dta.png](https://devnet.logianalytics.com/hc/article_attachments/5432268283671/skycrs3dta.png)Wrap:* texts wraps to a new line
* *![niDP7gwXFf.png](https://devnet.logianalytics.com/hc/article_attachments/5432221287063/nidp7gwxff.png) Stagger:* values are staggered along two lines so they don’t overlap
* *![7YBRqc1t7H.png](https://devnet.logianalytics.com/hc/article_attachments/5432221296535/7ybrqc1t7h.png) Rotate:* rotate the labels 90-degrees along the axis
* *![Sm9YGoPcF6.png](https://devnet.logianalytics.com/hc/article_attachments/5432289619351/sm9ygopcf6.png) None:* do not apply any change to labels, they may overlap

To include a **Legend** on the chart, click either *Right* or *Bottom.* Choose *None* to remove the legend.

The **Number Format** settings determine how numbers appear on the axes and in the **Point Labels** (if applicable):

* **Decimal Places** *—* will force a specified number of decimal places to be displayed. The symbol inserted between the whole and fractional part of the number can also be specified.
* **Use 1000 Separator** — when checked, will separate thousands places with the specified symbol
* **Use Currency Symbol** — when checked, will display the specified currency symbol in front of the value (for example $3.14)
* **Append Percent Sign (%)** — when checked, will display a percent sign (%) after the value (for example 3.14%)

## Interactive Editing

### Drilling Down

When **Live Data (Run)** is enabled, click on a chart series to drilldown the data to that series.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Because some of the data is hidden in this mode, totals and other calculations may not be accurate.

![OwtFHQFsDu.png](https://devnet.logianalytics.com/hc/article_attachments/5432273402263/owtfhqfsdu.png)

Clicking the **Fuller** series highlights only that series in the chart, and shows only those records that comprise that section of the chart

Several series may be drilled at the same time.

![THUVespRlS.png](https://devnet.logianalytics.com/hc/article_attachments/5432273425687/thuvesprls.png)

Drilling into both the **Condiments** and **Grains/Cereals** categories highlights them on the chart and shows their applicable records

Click ![AccordionDeleteItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432268623511/accordiondeleteitem.png)**Clear selected points** to remove the drilldown and return to the original report design.

### Editing a Chart Directly

Right-click on a chart to open the interactive menu.

![ng7POhmtzp.png](https://devnet.logianalytics.com/hc/article_attachments/5432251108119/ng7pohmtzp.png)

Chart interactive menu

Choose from:

* **Type** — change the chart from one type to another as in the [Type](#Type) section of the Properties Pane. Only charts of the same series type may be selected. That is, if the chart is a multi-series type of chart only other mutli-series charts may be selected.
* **Theme** — change the color palette of the chart as in the [Chart Colors](#Chart) section of the Properties Pane
* **Legend Location** — change the location of the legend
* **Sort By** — change the sort order on the chart as in the [Chart Data](#Chart2) section of the Properties Pane
* **Invert Data** — swap the data fields on the X and Y axes

## Suggested Reading

Additional resources may prove helpful when working with ExpressView and ExpressView Visualizations:

* [Charts and the Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5281542473367-Charts-and-the-Chart-Wizard)
