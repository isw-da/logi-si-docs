---
title: "Adding Header Rows "
id: 4419707441687
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707441687-Adding-Header-Rows
updated_at: 2022-07-17T02:24:50Z
---

# Adding Header Rows 

# Adding Header Rows

The header row ties the crosstab value columns together and provides data-driven identification for them as well. Before proceeding, look at the header in the table below; it consists of a blank area that spans two columns, three areas that will contain data (the year number) and span three value columns each, and an area labeled "Total" that spans three columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853451927/xtabtable_39.png)

1. Start by adding a **Header Row** element to the Crosstab Table, as shown below, then "build-up" the row using a combination of elements. Set the Header Row element's required **ID** and its **Header Position** attribute to *Top*.
2. Next, add a **Column Cell** element that will be a "spacer" or placeholder; its attributes are set to span the two columns beneath it. It contains nothing.

![](https://devnet.logianalytics.com/hc/article_attachments/7522847407767/xtabtable_36.png)

1. Then, add a **Crosstab Table Header Column** element, with a required ID and configured to span three columns.

1. Beneath the Crosstab Table Header Column add a **Label** element and set its Caption attribute value to the token *@Data.rdCrosstabColumn~.* It will display the actual data from the datalayer column identified as the Crosstab Column in the Crosstab Filter's attributes (in our example, this is "OrderYear").

![](https://devnet.logianalytics.com/hc/article_attachments/7522831550743/xtabtable_37.png)

1. Finally, add a second **Column Cell** element and configure it to span three columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522844812311/xtabtable_38.png)

1. Beneath the Column Cell add a **Label** element with the word "Total" as its **Caption** attribute value.

The elements added in this step create the header row, highlighted in yellow:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853451927/xtabtable_39.png)

And the resulting table, with header looks like this:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853494551/xtabtable_40.png)

## Adding Group Header Rows

You can also add Header Rows to grouped Data or Value Columns. This feature works like the one mentioned above, but instead of creating a Header Row along the top of the Crosstab Table, it allows you to add Header Rows to any Data Columns you have *grouped* together. For information on grouping Crosstabs, see [Working with the Crosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419715192599-Working-with-the-Crosstab-Filter).

1. Add a **Header Row** element beneath a Label Column Group element and give it an ID:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759699223/headerrowcountry_1283x648.png)

1. **Save** and **refresh** your report. Info displays the Crosstab Table with the new Header Row:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820397975/crosstabheaderrow_1550x563.png)

1. You can adjust the span of the Header Row by adding a **Column Cell** element and changing the Column Span attribute. In this example, we're adjusting the Column Span to 2.
2. Add a **Label** element beneath the Column Cell and give it a Caption based on the Data Column.
3. Next, add a **Crosstab Table Header Column** and give it an ID.
4. Then, add a **Label** element beneath the Crosstab Table Header Column and give it a Caption using the special Crosstab Table token " @Data.rdCrosstabColumn~", shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522861793175/labelcrosstabcol_1306x684.png)

1. Select **Save** and **refresh** your report. Info displays the Crosstab Table with the new Header Columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853552279/crosstabheadcol_1631x577.png)

You can repeat the previous steps for the Crosstab Filter Label Column (in this example, *Region*) and additional Secondary Crosstab Label Column(s) (in this example, *Product Id*).
