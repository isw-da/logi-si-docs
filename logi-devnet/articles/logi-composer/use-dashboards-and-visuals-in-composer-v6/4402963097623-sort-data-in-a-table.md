---
title: "Sort Data in a Table"
id: 4402963097623
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963097623-Sort-Data-in-a-Table
updated_at: 2021-08-07T17:33:24Z
---

# Sort Data in a Table

# Sort Data in a Table

The data in the table can be sorted by one or more columns of data. After you save the dashboard or visual, the sort settings are retained when you close it. The sort settings are also retained when you export and share the table.

To sort the rows in a table by the data in a single column:

* To sort the data in ascending order, select the column heading once.
* To sort the data in descending order, select the column heading two times.
* To return the data to its original sort order, select the column heading three times.

Remember to [save](https://devnet.logianalytics.com/hc/en-us/articles/4402962944151-Save-a-Dashboard) the dashboard if you want to retain the sort order.

To sort the data rows in a table by the data in multiple columns:

1. Sort the data in ascending or descending order by one column, as described above.
2. Hold the **Shift** key down and sort the data in ascending or descending order by a second column. The number 2 appears in the column heading and the data is sorted first by the first column selected and then by the second column selected.
3. If you hold the **Shift** key down, you can continue adding additional columns to the sort. The numbers in the column headings will continue to increment. (For example, the number 5 appears in the fifth column heading selected.)

   To interact with a multicolumn sort you must have the **Shift** key pressed. If you do not have it pressed and you select a column, the multicolumn sort is canceled and a new sort is performed using the selected column.

   You can change the order (from ascending to descending, for example) of the sort for any column by selecting it once, twice, or three times, as described above. For example, to remove a column heading from the multicolumn sort, select the column heading three times.

   When you change the order of a multicolumn sort, the sequence in which column data is evaluated for the sort is also changed. For example, suppose you initially set up a multicolumn sort that sorts the data in ascending order first by the data in the second column and then by the data in the third column. If you then decide to change the sort of the second column to descending (holding Shift and selecting the column a second time), the table is resorted first in ascending order by the second column and then in descending order by the first column. The column on which you requested the change becomes the last column evaluated for the multicolumn sort.
4. Save the dashboard and visual.
