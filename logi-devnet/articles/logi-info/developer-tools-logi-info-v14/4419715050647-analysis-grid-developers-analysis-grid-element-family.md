---
title: "Analysis Grid Developers - Analysis Grid Element Family"
id: 4419715050647
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715050647-Analysis-Grid-Developers-Analysis-Grid-Element-Family
updated_at: 2022-07-17T02:02:12Z
---

# Analysis Grid Developers - Analysis Grid Element Family

# Analysis Grid Developers - Analysis Grid Element Family

You can always manually add an Analysis Grid (AG) element to your definition. However, Logi Studio includes an "Analysis Grid Wizard" that can make the process easier. Select the Body or similar container element in the element tree, click the main menu's Wizards tab, and click the Analysis Grid item. Then follow the prompts.

* An **Analysis Grid** element. Only one may be used per report definition and it should not be used within Dashboards or Tabbed Panels.
* A **DataLayer** or **Active Query Builder** element, to retrieve the data used in tables and charts.
* One or more **Analysis Grid Column** elements, to display data that *will* be available for analysis.
* One or more **Data Table Column** elements, to display data that *will**not* be available for further analysis.
* An optional **Crosstab Comparison** element which displays column value differences in Crosstab Tables.

The example above shows a typical set of Analysis Grid elements. A few other special purpose child elements are also available.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706638359/workag_07a.png)

Why two kinds of table columns? **Analysis Grid Column** elements are used to display data and work with the grid's analysis features. However, your ability to customize them is limited. **Data Table Column** elements, on the other hand, are also available to display data *and* they allow customization, but their data can't be used for analysis. Using the two types of column elements together in an AG is common practice.

To add an **Analysis Grid Column**:

1. As shown above, select the parent **Analysis Grid** element and add an **Analysis Grid Column** element beneath it.
2. Set the **Column Header** and **ID** attributes. The Column Header value is the text that appears above each column.
3. Set the **Data Column** attribute to the name of a column returned by the data layer. Do not use tokens when the attribute name includes the word "column"; just provide the actual column name.
4. Set the **Data Type** attribute to Text, Number, or Date. Tokens can be used here to set the data type.

## Dynamic Column Visibility

When a regular Data Table Column element is used in an Analysis Grid, its visibility can be controlled dynamically by setting its **Condition** or **Show Modes** attributes. However, the Analysis Grid Column element doesn't have those attributes, so its visibility can't be controlled dynamically. Its visibility can only be controlled with Security Rights when using Logi Security.
