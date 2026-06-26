---
title: "Thinkspace - Working with Crosstab Tables    "
id: 4419723318167
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723318167-Thinkspace-Working-with-Crosstab-Tables
updated_at: 2022-07-17T01:29:01Z
---

# Thinkspace - Working with Crosstab Tables    

# Thinkspace - Working with Crosstab Tables

If you'd like to see the data in a Crosstab Table, that's easy to do.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714990743/dm30_workxtabs_08.png)

Our starting point once again will be a regular Column chart, showing *Freight* by *OrderDate*, as shown above. This time the OrderDate column's **Grouping** will be set to # of Quarters = 1.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700009111/dm30_workxtabs_09.png)

Drag and drop the *LastName* pill from the Data Table into the CROSSTAB drop zone, using the Blue Dot Connector, as shown above. The chart will be re-drawn accordingly.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714990999/dm30_workxtabs_10.png)

When the *LastName* pill was
dropped, the option for the Table type in the Visualization menu
acquired a "More Options" arrow icon, circled above. Click it to see the
Table options and select the **Crosstab Table** option. The Column chart will be replaced with a Crosstab Table.

Depending on the width of your browser window, a horizontal scroll bar may appear so that you can scroll the table to additional columns to the right.

## Editing the Crosstab Table

You'll notice that the drop zones were hidden when the Crosstab Table was rendered. How can we edit the table?

![](https://devnet.logianalytics.com/hc/article_attachments/4419700009367/dm30_workxtabs_11.png)

Click the **Settings** icon in the upper right-hand corner, circled above. A panel with column pills and controls, like those above, will slide open. The pills' Sorting and gear menu icons can be clicked to sort, format, and filter the data, as usual. Let's format the *Freight* column values.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700009623/dm30_workxtabs_12.png)

Click the *Freight* pill's gear icon and select the Formatting option. Select the Custom format display and set the format string to *0>$,.2f* as shown above. This will format the values as currency and right-justify them.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707196183/dm30_workxtabs_13.png)

Let's also add a **Column Summary**, by clicking the button shown above, that will give us the totals in a row across the bottom of the table. Click **Apply** to save the changes and hide the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707196439/dm30_workxtabs_14.png)

The resulting Crosstab Table looks like the example shown above.

## Adding Multiple Column Headers

It's easy to produce a multi-level Crosstab Table, by adding more column header values:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714991383/dm30_workxtabs_15.png)

Open the crosstab editing panel again and drag-and-drop the *Freight* column pill *from the Data Table* into the Values drop zone, as shown above, left. Once in the drop zone, this second pill has automatically been given a *different**aggregating function* than the first pill. You can, of course, select the aggregating function of your choice by clicking the function name. Click **Apply** to save the changes and hide the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714991639/dm30_workxtabs_16.png)

The resulting Crosstab Table now includes separate columns for the two different aggregations of *Freight* values, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700009879/dm30_workxtabs_17.png)

Of course, you can also drop *different* column pills into the Values drop zone, as shown above, and re-order them by using the Blue Dot Connector.

## Adding Multiple Row Headers

We can also produce a multi-level Crosstab Table by adding more row header values with different groupings:

![](https://devnet.logianalytics.com/hc/article_attachments/4419700010135/dm30_workxtabs_18.png)

For example, open the editing panel again and drag-and-drop an *OrderDate* column pill from the Data Table into the Row Headers drop zone, as shown above. You may need to set the Grouping of the existing OrderDate pill to Date Units, # of Quarters = 1 before you can drop the second pill there.
When you drop the second pill there, it will be automatically grouped differently from the first one. Click its gear icon to check its Grouping configuration and, if it's not already so, set it to Date Units, # of Months = 1. Click **Apply** to save the changes and hide the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714992023/dm30_workxtabs_19.png)

The resulting Crosstab Table now includes separate rows for each month, within each quarter, as shown above.

## Switch to Crosstab Chart

You can also switch between a Crosstab Table and a crosstab chart pretty easily:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707197335/dm30_workxtabs_20.png)

Just open the Visualizations menu and select the crosstab chart of your choice. In the example above, a **Grouped Crosstab Column** chart has been selected.

Other useful Discovery Module v3.x topics include: [Thinkspace Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707848471-Thinkspace-Columns), and [Thinkspace Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419707971351-Thinkspace-Charts).
