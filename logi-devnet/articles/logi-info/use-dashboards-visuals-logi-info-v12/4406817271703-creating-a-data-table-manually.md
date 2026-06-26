---
title: "Creating a Data Table Manually"
id: 4406817271703
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817271703-Creating-a-Data-Table-Manually
updated_at: 2022-04-06T06:05:05Z
---

# Creating a Data Table Manually

# Creating a Data Table Manually

You can create a datatable in Studio manually by adding the appropriate elements to a report definition.

To do this, simply add the necessary elements to your definition in Studio. After you add your first **Data Table Column** and its child elements (Label, Sort, etc.), you can speed things up by copying and pasting it into the element tree as many times as necessary, then going back and configuring the individual elements. Copying the Data Table Column element will also copy all of its child elements, too.

In these circumstances, the issue of **spelling** becomes more important. @Data tokens are case-sensitive and column names must be spelled accurately. To ensure that you know exactly how column names are spelled, you may care to turn on **debugging** and view the actual data in the datalayer. For more information about debugging, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports).

## Data Table Attributes

The Data Table element includes the following attributes:

| Attribute | Description |
| --- | --- |
| Accessible Headers | Specifies whether or not to set the HTML "Headers" attribute, which can improve the accessibility and readability of tables. Default value: *False*. |
| Accessible Summary | Specifies whether or not to create a "table content summary", which has no visual effect but is used by screen readers to improve accessibility. Default value: *False*. |
| Ajax Paging and Sorting | Enables AJAX-style paging and sorting. When the user moves to another page of table data, or sorts a column, only the table portion of the page is updated. This method prevents the web page from flickering or losing its scroll position. This alters the behavior of the browser's "Back" button because the page history isupdated with AJAX Paging. Default value: *False* |
| Alternate Row Class | Specifies a style class to be used for every other row of the table, making it easier to read across the columns in single row. Themes include a class called**ThemeAlternatingRow** which you can assign, if desired. |
| Border | Specifies, in pixels, the width of a border, if any, to be displayed around the table. A value of 1 displays a thin border. |
| Caption | Specifies the text of a caption, or "title", that will appear above the table. Leave this blank to suppress it. |
| Caption Class | Specifies a style class to be applied to the caption text entered in the previous attribute. |
| Cell Spacing | Specifies the width, in pixels, of the space between table cells, if any. Default value: *0*. |
| Class | Specifies a style class to be applied to the table as a whole. |
| Column Header Class | Specifies a style class to be applied to the column headers. |
| Draggable Columns | Specifies if the user can reposition columns by dragging the column header side-to-side. When enabled, any changed column positions are remembered for the table for the current session. Draggable Columns may not be used when there are custom header rows in use with columns that span multiple columns. Default value: *False* |
| Hide When Zero Rows | Specifies if the Data Table is to be hidden when the datalayer returns zero rows. Default value: *False* |
| Keep Scroll Position | When enabled, causes the browser's horizontal and vertical scroll positions to be retained when the current report is redisplayed without first going to another report. Use this to refresh the current report while avoiding resetting the scroll position to the top. Default value: *False* |
| Layout | Specifies if the table layout should be automatically determined by all the data (*Auto*) or just the first row of data (*Fixed*). If *Fixed* is specified, the column layout is determined based on the width of the values in the *first* data row, instead of adjusting the column widths by examining data in *every* row. This can help with formatting issues, and can also significantly improve large table performance. Default value: *Auto* |
| Remember Sort | Specifies whether or not to retain the user's sort selection. When *True*, and the user sorts the data table on a particular column, the report will be redisplayed with the same sort order the next time the report is displayed. Sort selections are retained only for the user's current session. Default value: *False* |
| Resizable Columns | When enabled, a small icon appears on the right edge of the column header when the mouse hovers over it and the user can resize columns at runtime by dragging the icon right or left to a different width. The updated column width are remembered for the table for the duration of the current session. You may not use Resizable Columns when there are custom header rows in use with columns that span multiple columns. Default value: *False* |
| Row Class | Specifies a style class to be applied to the table rows. This value can be an @Data token, so the class can be applied dynamically based on the data. |
| Security Right ID | When specified, access to this element can be controlled with Logi Security. Specifythe ID of a Right defined in the application's \_Settings Security element. Only users with matching rights will be able to see the element. |
| Sort Arrows | Specifies whether Sort direction indicators (arrows) will be displayed when the user clicks a column header to sort the table. Default value: *False* |
| Width | Specifies the total width of the data table. |
| Width Scale | Specifies the scale to be used when applying the value of the previous attribute, *px* for pixels, or *%* for percentage of the table's parent container's width. |

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Themes automatically set a number of these attributes "behind-the-scenes".

In general, the fewer attributes you have to set for a Data Table, the better. Let a Theme or the browser figure out the best combination of attributes for you.

## About Table and Column Widths

Browser engines are designed to do the best job they can with HTML tables (which is the structure underlying a Data Table) when it comes to automatically figuring out column widths. Here are some tips to make widths work for you.

First, *always set a width* for a Data Table, using its **Width** attribute.

Second, for most purposes, leave the Data Table element's **Layout** attribute *blank*. This defaults to *Auto* mode, which sets columns width to the widest data.

Third, if you're concerned about ensuring that one or two columns have a specific width, then set those widths in the appropriate Data Table Column elements but leave the widths for the *other* Data Table Column elements *blank*.
You don't need to try to figure out what the width of every column will be, ensuring it all adds up to 100% of the table width. The browser will try to guarantee the widths you've specifically set and will divide and allocate the remaining space among the remaining columns, when it can.

And remember that it *is* possible to put so many conflicting restrictions (via attribute values) in place that the browser will get confused and produce weird results. If that happens, try removing width attribute values for columns until things look normal again, then reconsider the issue.
