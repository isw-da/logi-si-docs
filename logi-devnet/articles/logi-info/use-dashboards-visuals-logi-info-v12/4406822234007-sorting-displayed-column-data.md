---
title: "Sorting Displayed Column Data"
id: 4406822234007
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822234007-Sorting-Displayed-Column-Data
updated_at: 2022-04-06T06:04:59Z
---

# Sorting Displayed Column Data

# Sorting Displayed Column Data

Developers often need to present data tables with their data sorted in a specific order and this can be done by sorting the datalayer data. You can also give users the ability to dynamically sort columns at runtime simply by adding a child **Sort** element beneath any Data Table Column element. This causes the column header text to become a link that users can click to sort the table based on that column.

Column data is sorted in the order specified in the **First Sort Sequence** attribute when the user clicks the link; clicking it again reverses the sort order. This defaults to *Ascending* first, then *Descending*.

| To do this: | Set the following element attributes: |
| --- | --- |
| Create an initial sort order | Set the Sort element's **First Sort Sequence** attribute to Ascending or Descending.  Default: *Ascending* |
| Specify a sort order for multiple columns | Set the Sort element's **Data Column** attribute to a comma-separated list of data column names, then set the **Data Type** attribute to a comma-separated list of data types that correspond with the respective column names. |
| Remember the user's sort selections | Set the parent Data Table element's **Remember Sort** attribute to *True.*  Default: *False* |
| Display arrows in the header that indicate the sort order | Set the parent Data Table element's **Sort Arrows** attribute to *True*.  Default: *False* |
| Sort the data and update the table, without reloading the entire page | Set the parent Data Table element's **AJAX Paging and Sorting** attribute to *True*. AJAX is a technology that allows targeted portions of web pages to be updated, rather than the entire page. With this attribute enabled, when the user sorts a column by clicking its header, only the table portion of the web page will be updated, preventing the page from "flickering" or losing its scroll position. You should be aware that this alters the behavior of the browser's "Back" button because the page history is not updated when AJAX is used. If AJAX Paging and Sorting is enabled and sorting is initiated and there is more than a very brief delay, a spinning "Wait" icon will automatically be displayed to let the user know that processing is occurring. |
