---
title: "ExpressView: Managing Data (pre-v2021.1)"
id: 5281603566487
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281603566487-ExpressView-Managing-Data-pre-v2021-1
updated_at: 2022-05-03T22:09:06Z
---

# ExpressView: Managing Data (pre-v2021.1)

# ExpressView: Managing Data (*pre-v2021.1*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

You can exercise some fine grained control over the actual data that appears in the **ExpressView**. You can choose styling options, you can filter down the rows to appear, and you can change the order of rows in their respective sections.

## Formatting and Style

Formatting allows you to specify a data type (for example *number*, *date, text)* for specific data fields, and choose how that data displays.

To change the data type for a field:

1. Click the **Formatting and Style ![FormatMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432316815895/formatmenu.png)**icon in the pane on the right to open the Formatting page.
2. Click the data rows to format. They will highlight in blue.  
   ![screen.expressview_format_highlight.png](https://devnet.logianalytics.com/hc/article_attachments/5432276447511/screen.expressview_format_highlight.png)

   Selecting data to format
3. In the pane on the right side of the screen, click the **Data Format**heading to open it.
4. From the **Format Type** list, select a data type from the following options:  

   ## General

   Format the data using the default settings for the environment. The application will assume the data type.

   ## Number

   Format the data as a number.

   1. In the **Decimal Places** field, enter a number for how many decimal places to display. In the field to the right, enter a symbol to use as the decimal mark.
   2. To show a delimiter every three digits, select **Use 1000 Separator**. Then, in the field to the right, enter a symbol to use as the delimiter.
   3. To show a symbol before the number, indicating that this is currency, select **Use Currency Symbol**. Then, in the field to the right, enter the symbol to show.
   4. To show a percent sign after the number, indicating that this is a percentage, select **Append Percent Sign**.
   5. To show no value if the number is 0, select **Blank When Zero**.
   6. To show the negative symbol in front of negative numbers, select **Show Negative Symbol**.
   7. To show parentheses around negative numbers, select **Show Parenthesis**.
   8. To show negative numbers in a different color, select **Color**, then enter a hex value or use the color picker to choose a color.

   ## Date

   Format the data as a date, time, or date and time. You can choose which date and time components to display, and how to show them.

   ![screen.expressview_date_format_menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432276470039/screen.expressview_date_format_menu.png)  

   Choosing a date/time format

   ## Text

   Do not apply any formatting to the data, and show it exactly as it appears in the database

If the data field cannot be formatted as a number or date, then selecting one of those options will have no effect on the appearance of the data.

## Sorting

**Sorting** allows you to set the order that the data rows appear in each section. Click the **Sorts**![Sorts Menu](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png)

You can choose which columns take precedence for sorting. The order of fields on the Sorts page is their order of precedence, from highest to lowest. Their order is also indicated by a number on the right of the column headers: The lower the number, the higher the precedence.

To set the sort precedence of data fields, either:

* On the Sorts page, drag fields up or down.
* Use ![radial menu](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png) radial >**down**![firefox_efRqq99QoP.png](https://devnet.logianalytics.com/hc/article_attachments/5432223105815/firefox_efrqq99qop.png) to give a field the highest precedence.

![screen.expressview_reorder_sort.png](https://devnet.logianalytics.com/hc/article_attachments/5432293138327/screen.expressview_reorder_sort.png)  

Dragging a sort to change its precedence

You can choose which direction to sort the data for each data field: *ascending* or *descending*. A field’s sort direction is indicated by an arrow on the right of the column header: Up ![^](https://devnet.logianalytics.com/hc/article_attachments/5432293164823/sortdescending.png)

*ascending*![v](https://devnet.logianalytics.com/hc/article_attachments/5432293184663/sortascending.png)*descending*

To change a field’s sort direction, either:

* On the Sorts page, select *asc* for ascending, or *desc* for descending.
* Click the column header to swap to the opposite direction.

## Filtering

**Filtering** allows you to narrow the scope of the ExpressView by restricting the amount of data shown.

* **Standard Filters** allow only rows whose values satisfy certain conditions to appear in the report.
* **Top N** filters allow only the rows with the top or bottom values, for either data fields or data summaries, per group iteration to appear in the report.

Click the **Filters**![funnel](https://devnet.logianalytics.com/hc/article_attachments/5432253309335/filtermenu.png)

**Standard****Top/Bottom**

### Standard Filters

To show only the data that satisfies several conditions:

1. On the Filters page, click the **Standard** tab.
2. To add a data field to filter, either:
   * Use ![radial menu](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png) radial >**right** on a data column or group.
   * Drag a data field from the **Data Pane** on the left side of the screen to the **Meet all of the following conditions** pane.  
     > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
     >
     > This allows you to filter any accessible data field, not just those on the ExpressView.
3. Choose a filter operator from the list. See Filters for details.
4. Enter a filter value or values by either
   * Entering them directly with the keyboard
   * Select them from the list of existing values. Type into the filter field to search for data values to filter.
   * Click the **Filter Function ![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png)** icon to choose a pre-defined value based on a formula programmed by the system administrator. (For example, *First Day of Current Month* or *Friday of Last Week*).
5. Repeat steps 2-4 for every filter condition that the data must satisfy in order to show.
6. If you are viewing live data, click **Apply Changes** to apply the filters.

To show only the data that satisfies at least one of several conditions:

1. On the Filters page, click the **Standard** tab.
2. To add a data field to filter, either:
   * Use ![custom.RadialButtonBlue.png](https://devnet.logianalytics.com/hc/article_attachments/5432294787351/custom.radialbuttonblue.png) radial>**right** on a data column or group. Then drag the filter to the **meet any of the following conditions** pane.
   * Drag a data field from the Data pane to the **meet any of the following conditions** pane.  
     > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
     >
     > This allows you to filter any accessible data field, not just those on the ExpressView.
3. Choose a filter operator from the list. See Filters for details.
4. Enter a filter value or values, by either
   * Entering them directly with the keyboard
   * Select them from the list of existing values. Type into the filter field to search for data values to filter.
   * Click the **Filter Function ![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png)** icon to choose a pre-defined value based on a formula programmed by the system administrator. (For example, *First Day of Current Month* or *Friday of Last Week*).
5. Repeat steps 2-4 for every filter condition, of which the data must satisfy at least one in order to show.
6. If you are viewing live data, click **Apply Changes** to apply the filters.

![screen.expressview_drag_field_to_filter.png](https://devnet.logianalytics.com/hc/article_attachments/5432293223703/screen.expressview_drag_field_to_filter.png) ![screen.expressview_filter_select.png](https://devnet.logianalytics.com/hc/article_attachments/5432276571031/screen.expressview_filter_select.png)  

Adding a field as a Standard filter

### Top/Bottom Filters

To show only the top or bottom values, for either data fields or data summaries:

1. On the Filters page, click the **Top/Bottom** tab.
2. Select the **Limit the report to the top/bottom values** check box.
3. Select either *Top* or **Bottom**, for whether you want to show the top or bottom values.
4. Enter a number for how many values you want to show.
5. Choose how you want to limit the data:
   * If you want to show the rows with the top or bottom data values for a field or group, select **Values** from the list.
   * If you want to show the groups with the top or bottom summary values for a parent group or the ExpressView, select one of the summary calculations, *Sum*, *Avg*, *Min*, *Max*, *Count*, or *Distinct Count*, from the list. See the topic on aggregation for more information.  
     > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
     >
     > Only numeric data fields support *Sum* and *Avg* calculations.
6. Select the data field or group field to filter from the **Of** list.
7. Optional: To show the top or bottom values for each iteration of a group:
   1. Click ![AddBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png) **Add Group**.
   2. Select a group field from the **For Each** list.

![screen.expressview_topn.png](https://devnet.logianalytics.com/hc/article_attachments/5432317376663/screen.expressview_topn.png)  

Adding a Top/Bottom filter
