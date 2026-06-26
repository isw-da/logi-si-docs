---
title: "Report Wizard: Layout"
id: 5281564615959
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281564615959-Report-Wizard-Layout
updated_at: 2022-05-03T22:09:17Z
---

# Report Wizard: Layout

# Report Wizard: Layout

Use the **Layout** tab to create the data and look of the report. This page is different depending on the type of report you are making:

* **Advanced Report**: Add data fields, formulas, groups, headers, footers, and summary calculations.
* **Express Report**: Add data fields, formulas, groups, headers, footers, and summary calculations. Customize the style of the report or select a premade theme.
* **CrossTab Report**: Add data fields and formulas as row headers, column headers, or tabulation data. Select a premade theme for the report.

## Adding data (Advanced and Express Reports)

Add data fields to display in the output of the report.

![screen.reportwizard_drag_filter_field.png](https://devnet.logianalytics.com/hc/article_attachments/5432394211095/screen.reportwizard_drag_filter_field.png)

Dragging a field from the Data Field pane

Each data field is a column of associated data values; each value belongs to a row in the category. In the Preview pane, each data field has a header and some placeholder values indicating how the values from the field will look.

To show a formula instead of the data field, click the formula ![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png)

### Grouping data

If you have Sorts then you can group your data fields by one or more sort fields. To add a group:

1. For each data field, select a summary function for how the total for each group is calculated.

   ![screen.reportwizard_summary_menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432381175063/screen.reportwizard_summary_menu.png)

   *Choosing a summary function*
2. In the **Summarize By** pane, select the check box for every Sort category to group by. By default, this groups on the unique key of the category.
3. Optional: To customize which data field the group category uses:

   1. In the **Summarize By** pane, click the name of the Sort category.
   2. Select the data field from the **Summarize by each unique** list.
4. Optional: In the Summarize By pane, click the name of the Sort category to customize how the group looks:

   * Select the **Add space before each unique item** check box to add a blank row before each group.
   * Select the **Include Header at the beginning** check box to put a group field value before each group. Choose which field to use, or click the formula icon to make a formula for the text.
   * Select the **Include Total at the end** check box to include the data summary values, selected in step 1, at the end of every group.

![screen.reportwizard_summary_options.png](https://devnet.logianalytics.com/hc/article_attachments/5432364688151/screen.reportwizard_summary_options.png)

Customizing the group design

### Page header and footer

A page header is inserted by default with the name of the report. To remove the header, clear the **Page Header** check box. To edit the header, click **Page Header**. The following options are available:

* To include the report title at the top of every page, select the **Include title at the top of every page** check box.

  If you have an image in the header, choose whether the title is in a column to the Left or Right of the image, from the **Position** list. Choose how many columns the title spans.
* To include an image at the top of every page, select the **Include image at the top of every page** check box, then click **Change Image** to upload an image file.

  If you have a title in the header, choose whether the image is in a column to the Left or Right of the title, from the **Position** list. Choose how many columns the image spans.

To add a footer to every page, select the **Page Footer** check box. To edit the footer, click **Page Footer**. The following options are available:

* To include the page number at the bottom of every page, select the **Include page number at the bottom of every page** check box.

  If you have an image in the footer, choose whether the page number is in a column to the Left or Right of the image, from the **Position** list. Choose how many columns the page number spans.
* To include an image at the bottom of every page, select the **Include image at the bottom of every page** check box, then click **Change Image** to upload an image file.

  If you have a page number in the footer, choose whether the image is in a column to the Left or Right of the page number, from the **Position** list. Choose how many columns the image spans.

To include a summarization of all the data fields at the end of the report, select the **Grand Total** check box.

![screen.reportwizard_page_header_menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432364713367/screen.reportwizard_page_header_menu.png)

Customizing the page header

## Styling the report (Express Reports)

Complete styling for Express Reports in the Report Wizard. To style a cell, click the cell and then choose from the available options:

* **Layout Options**: Hide the data rows for the selected field by selecting the **Suppress Detail Rows** check box. Set the pattern by which the background colors for the data rows colors alternate. See Section Shading for details.
* **Font**: Select a font, size, and decoration for the cell text.
* **Color**: Select a color for the text and for the background of the cell.
* **Formatting**: Select any additional formatting for the data. See Cell Format.
* **Alignment**: Select how the cell contents should align to the borders of the cell.

To change the text in a header or footer, double-click the cell and edit the text. To insert a blank column between two data fields, click  **Add Blank**, then drag the column between the two fields. To resize columns, drag the left or right border of the column.

![screen.reportwizard_resize_column.png](https://devnet.logianalytics.com/hc/article_attachments/5432321823511/screen.reportwizard_resize_column.png)

![screen.reportwizard_rename_header.png](https://devnet.logianalytics.com/hc/article_attachments/5432394411671/screen.reportwizard_rename_header.png)

*Making changes to an Express Report’s design*

### Premade themes

To use a premade theme, or use one as a starting point for customization, select a theme from the **Theme** list.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Selecting a premade theme overrides the current cell styling. If you want to undo a theme selection, click the **Undo** ![Undo.png](https://devnet.logianalytics.com/hc/article_attachments/5432254416023/undo.png) icon, or press Ctrl-Z.

## What are CrossTabs?

CrossTabs are an easy way to do calculations when you have one or more groups and you want to make calculations on subdivisions of each group. CrossTabs extend horizontally for each subdivision so that you can fit many calculations in a small space.

For instructions on making CrossTabs, see [Advanced Reports: CrossTabs](https://devnet.logianalytics.com/hc/en-us/articles/5281553083159-Advanced-Reports-CrossTabs).

The CrossTab Report Wizard places the CrossTab into a new Advanced Report. When you finish, the report opens in the Report Designer. To edit the CrossTab in the Report Designer, double-click the CrossTab.
