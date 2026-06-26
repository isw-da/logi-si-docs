---
title: "Multi-Column Lists"
id: 4419707262615
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707262615-Multi-Column-Lists
updated_at: 2022-11-09T22:38:13Z
---

# Multi-Column Lists

# Multi-Column Lists

A **multi-column list** is a very basic type of tabular Data Table that
allows data to be arranged in columns. Unlike a traditional Data Table,
with its rows and columns, a multi-column list displays all its data in
cells typically arranged into a small number of columns. Developers should
consider this primarily as a means of creating "lists", rather
than as a way to present data in a table.

* [About Multi-Column Lists](#About)
* [Creating a Multi-Column List](#Creating)

## About Multi-Column Lists

The following illustrates the difference between a Data Table and a
multi-column list:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706620567/multicol_01_562x261.png)

As shown above, *all* of the data from **one record** is available
in **one cell** of the multi-column list.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706620823/multicol_02_336x426.png)

The multi-column list shown above is organized so that the data is
arranged from **top-to-bottom** in the first column, showing all the
information from one record in individual cells, then from top-to-bottom
in the second column. The number of columns is configurable.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706621079/multicol_03_378x329.png)

The example above shows the same data in a **3-column** list. Because
the direction of this list is *Down*, the sort order (based on Last
Name) causes the data to be arranged in a top-to-bottom fashion in each
column.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706621335/multicol_04_593x262.png)

Now, in the example shown above, the direction has been switched to
*Across*, so the sort order runs left-to-right.

Developers can choose any type of datalayer element to retrieve data for
the list. **Label** elements are used to display the data, and
developers can combine them with other types of elements to organize the
data.

The **Data Multi-Column List** element is used to create the list in a
report definition. Multi-column lists are different from other types of
Data Tables in that the number of columns that can be displayed is not
dependent on the datalayer. **Data Table Column** elements *are**not* used and, instead, developers set the Data Multi-Column List
element's **Columns** attribute to a numeric value that determines the
fixed number of columns the list will display.

The number of rows displayed is determined automatically by distributing
the data in the columns, based on the list orientation, beginning with the
upper left-hand corner of the list. Any elements (other than datalayer
elements) placed below a Data Multi-Column List element are repeated for
each row of data in the datalayer. Content that must appear only once in
the final report should not be placed within a multi-column list.

## Creating a Multi-Column List

Creating a multi-column list involves configuring the list, retrieving
data for the list, and displaying the list. The element itself does the
work of arranging the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706621591/multicol_05_623x240.png)

1. Add a **Data Multi-Column List** element to your definition.
2. Set the **Columns** attribute to the desired number of list columns.
3. Set the **ID** attribute.
4. Set **Multi-list Direction** attribute to control the data layout.
   Set it to *Across* to display data left-to-right: a new table cell
   is created for each row in the data layer. Leave it blank, or set it to
   *Down*, to display data top-to-bottom.
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699524631/multicol_06_602x206.png)

5. Beneath the Data Multi-Column List element, add a
   **DataLayer** element and configure it as necessary.
6. Beneath the Data Multi-Column List element, add **Label** elements,
   **New Lines**, etc. as needed. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Data Table Column elements
   are *not* necessary. Use a standard **@Data** token
   for the Label element's Caption attribute to display the data.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699524887/multicol_07_444x287.png)
7. In the example shown above, multiple Label and New Line elements have
   been added. The Label element that displays City and Region data uses a
   formula that suppresses the display of a comma after the City if there
   is no Region data.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699525143/multicol_08_564x348.png)
8. And the example above shows the resulting output. The background color
   has been set using CSS for illustration purposes.
