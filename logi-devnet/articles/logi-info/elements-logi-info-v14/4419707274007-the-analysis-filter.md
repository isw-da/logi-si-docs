---
title: "The Analysis Filter"
id: 4419707274007
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707274007-The-Analysis-Filter
updated_at: 2022-07-17T02:02:19Z
---

# The Analysis Filter

# The Analysis Filter

The Analysis Filter provides a mechanism that allows users to filter data at runtime and immediately updates visualizations dependent on that data.

The following topics introduce developers to the **Analysis Filter** super-element:

* [Using the Analysis Filter Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4419715048727-Analysis-Filter-Using-the-Analysis-Filter-Wizard#Wizard)
* [Analysis Filter Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715045655-Analysis-Filter-Attributes#Attributes)
* [Analysis Filter Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715046551-Analysis-Filter-Column-Attributes#AFCAttribs)
* [Using the Analysis Filter Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419700094871-Analysis-Filter-Using-the-Analysis-Filter-Elements#Using)
* [Saving Individual User Settings](https://devnet.logianalytics.com/hc/en-us/articles/4419715047575-Analysis-Filter-Saving-Individual-User-Settings#Settings)
* [Filtering with Query String Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4419700093847-Analysis-Filter-Filtering-with-Query-String-Parameters#QSParams)
* [Using Analysis Filters in Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4419715049623-Analysis-Filter-Using-Analysis-Filters-in-Dashboards#Dashboards)
* [Customizing Analysis Filter Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419700092951-Analysis-Filter-Customizing-the-Analysis-Filter-Appearance#Customizing)

## About the Analysis Filter

The **Analysis Filter** allows users to apply filtering, at runtime, to the datalayers that support their visualizations. Changes made to the filtering immediately causes the visualizations to be updated.

As a super-element, the Analysis Filter has an interface that users can interact with at runtime. The interface can be configured and restricted depending on the use-case requirements.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706634135/workaf_01.png)

The example above shows the Analysis Filter in use with a Data Table. If the user checks or unchecks one of the filters, the Data Table will be refreshed accordingly (the refresh can include the entire page or just selected elements). The Analysis Filter has two developer-controlled viewing modes: Simple and Design.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699536023/workaf_03.png)

In **Simple** view, shown above, users can click an existing filter description to display input controls and change the filtering value.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699536279/workaf_02.png)

In **Design** view, a "gear" icon is displayed; clicking it opens a control panel, shown above, that can be used to manage filters.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706634391/workaf_02a.png)

The controls provide a variety of tools for creating, editing, grouping, and removing filters, as shown above.

When using "In List" or "Not In List" comparisons in filters, multiple values can be entered, separated by commas. However, the values themselves may *include* commas, causing incorrect comparisons.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714636567/workaf_19.png)

To address this, values for these types of filters are now represented in the controls by visual "pills" that enclose the complete value, as shown above. The filter uses the complete string within the pill during its comparison operation.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714636823/workaf_20.png)

Pills with included commas are created by entering the first part of the value and pressing comma. This creates a blue pill as shown above. Then place your cursor *inside* the pill and type the rest of the value. Press tab to exit the pill and repeat the process for the next value, if desired.

The Analysis Filter is usually used to compare column data and a value you enter, but you can also directly compare the values in two data columns:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699536663/workaf_21.png)

To do this, first select a Filter Column, as shown above, and a supported Comparison operator: *=, <, <=, >, Not =, In List, Not In List, Starts With, Contains, Not Starts With, Not Contains,* Like, Not Like.

Then select the second column from the list displayed when you click the **[]** button, or enter the column name within square brackets.

## Retaining User Settings

Filters users create or modify can be saved between sessions and made available to them during their next session (this is discussed in more detail below).
