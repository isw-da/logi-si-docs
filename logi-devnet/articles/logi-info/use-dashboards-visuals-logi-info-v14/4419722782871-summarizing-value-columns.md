---
title: "Summarizing Value Columns "
id: 4419722782871
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722782871-Summarizing-Value-Columns
updated_at: 2022-07-17T02:24:47Z
---

# Summarizing Value Columns 

# Summarizing Value Columns

The creation of a Summary Row at the bottom of a table with summarizing column values is a bit like creating the header row, in that it's built up column-by-column.

Begin by adding **Data Column Summary** elements beneath the columns to be summarized. The columns that show the average Unit Price do not need these elements as their summarized value can be derived by dividing the summarized values of two other columns.

![](https://devnet.logianalytics.com/hc/article_attachments/7522846956055/xtabtable_41.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The special column names, *rdCrosstabValue-ODTotal* and *rdCrosstabValue*, discussed earlier in [Adding Extra Crosstab Values](https://devnet.logianalytics.com/hc/en-us/articles/4419715189399-Adding-Extra-Crosstab-Values), are used in the Data Column Summary elements' attributes for the two extra value columns, as shown above.

The IDs of the Data Column Summary elements ("sumODTotal", "sumQuantity", etc.) will be used in the next step with an @Data token to identify the summarized data.

Similarly, Summary Row elements are then added beneath Crosstab Label Column elements that display the row (horizontal) totals for each row.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816424727/xtabtable_42.png)

In the example above, a **Summary Row** element has been added beneath the Crosstab Table. Like the Header Row, it will contains elements that "build up" the columns needed for the summaries. **Column Cell** elements are used for non-crosstab value columns and **Crosstab Table Summary Column** elements are used for the value columns.

The first Column Cell element is set to span two columns (it will be underneath the Supplier and Product columns) and contains a **New Line** element and a **Label** element with a Caption of "Totals:".

![](https://devnet.logianalytics.com/hc/article_attachments/7522816449175/xtabtable_43.png)

Next, three Crosstab Table Summary Columns have been added. The first two are used to display the summarized OrderTotal and Quantity value columns. Each contains a New Line and a Label element beneath it, as shown above. The Label elements' Caption attributes are set to the @Data token for the related Data Column Summary column.

The third Crosstab Table Summary Column is just a placeholder and needs no child elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522847029143/xtabtable_44.png)

Finally, three Column Cell elements are added, as shown above, to display the two summary totals for the row Order Total and Quantity summary columns and a final spacer column.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816506135/xtabtable_45.png)

And the resulting Crosstab Table, with header and summary rows, looks like the image above.
