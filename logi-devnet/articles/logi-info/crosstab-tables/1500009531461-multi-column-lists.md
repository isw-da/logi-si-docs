---
title: "Multi-Column Lists"
id: 1500009531461
section: "Crosstab Tables"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531461-Multi-Column-Lists
updated_at: 2021-06-17T01:58:32Z
---

# Multi-Column Lists

# Multi-Column Lists

A **multi-column list** is a very basic type of tabular data table that allows data to be arranged in columns. Unlike a traditional data table, with its rows and columns, a multi-column list displays all its data in cells typically arranged into a small number of columns. Developers should consider this primarily as a means of creating "lists", rather than as a way to present data in a table.

* About Multi-Column Lists
* [Create a Multi-Column List](#Creating)

## About Multi-Column Lists

The following illustrates the difference between a data table and a multi-column list:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771646999/multicol_01.png)

As shown above, all the data from **one record** is available in **one cell** of the multi-column list.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778538519/multicol_02.png)

The multi-column list shown above is organized so that the data is arranged from **top-to-bottom** in the first column, showing all the information from one record in individual cells, then from top-to-bottom in the second column. The number of columns is configurable.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771647255/multicol_03.png)

The example above shows the same data in a **3-column** list. Note that because the orientation of this list is "Down", the sort order (based on Last Name) causes the data to be arranged in a top-to-bottom fashion.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771647511/multicol_04.png)

Now the list, shown above, has been switched to the "Across" orientation, so the sort order runs **left-to-right**

Developers can choose any type of datalayer element to retrieve data for the list. **Label** elements are used to display the data, and developers can combine them with other types of elements to organize the data.

The **Data Multi-Column List** element is used to create the list in a report definition. Multi-column lists are different from other types of data tables in that the number of columns that can be displayed is not dependent on the datalayer. Data Table Column elements *are**not* used and, instead, developers set the Data Mult-Column List element's **Columns** attribute to a numeric value that determines the fixed number of columns the list will display.

The number of rows displayed is determined automatically by distributing the data in the columns, based on the list orientation, beginning with the upper left-hand corner of the list. Any elements (other than datalayer elements) placed below a Data Multi-Column List element are repeated for each row of data in the datalayer. Content that must appear only once in the final report should not be placed within a multi-column list.

## Create a Multi-Column List

Creating a multi-column list involves configuring the list, retrieving data for the list, and displaying the list. The element itself does the work of arranging the data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771647767/multicol_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778538775/multicol_05a.png)

1. Add a **Data Multi-Column List** element to your definition.
2. Set the **Columns** attribute to the desired number of list columns.
3. Set the **ID** attribute.
4. Set **Multi-list Direction** attribute to control the data layout. Set it to *Across* to display data left-to-right: a new table cell is created for each row in the data layer. Set it to *Down*, the default, to display data top-to-bottom.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771648023/multicol_06.png)

5. Beneath the Data Multi-Column List element, add a **DataLayer** element and configure it as necessary.
6. Beneath the Data Multi-Column List element, add **Label** elements, **New Lines**, etc. as needed. Note that Data Table Column elements are not necessary. Use a standard **@Data** token for the Label element's Caption attributes to display the data.
