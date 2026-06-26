---
title: "Building the Basic Table Structure"
id: 4406822220311
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822220311-Building-the-Basic-Table-Structure
updated_at: 2022-04-06T06:04:48Z
---

# Building the Basic Table Structure

# Building the Basic Table Structure

As discussed in [Working with the Crosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406817234967-Working-with-the-Crosstab-Filter), the **Crosstab Filter** element determines the basic structure of the table:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563426327/xtabtable_27.png)

The definition starts with a **Crosstab Table** element (no attributes except an element ID need be set), a datalayer to retrieve the data, and a **Crosstab Filter** element to format the data. In the filter attributes shown above, the table will have a label column for the Product Names, be grouped horizontally (crosstab) by Order Year, and the initial values will be the sum of the order Quantity.

A **Crosstab Table Label Column** element ("colProductName") and a **Crosstab Table Value Columns** element ("colQuantity") are added to the definition to display the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A special token is needed to access the Value column data: *@Data.rdCrosstabValue~*.

The token identifier uses the reserved word "rdCrosstabValue" and the token is used in the Caption attribute of a Label element beneath the Crosstab Table Value Columns element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584062615/xtabtable_27a.png)

Referring to our crosstab layout model, the seven elements added so far provide the portions highlighted in yellow above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563426711/xtabtable_28.png)

If we preview our definition at this point, the crosstab table looks like the example shown above. Now let's add another Label column to display the names of the suppliers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575806487/xtabtable_29.png)

In the previous page, the **Extra Crosstab Label Column** element was discussed. As shown above, one of these elements is added beneath the Crosstab Filter and set to use the CompanyName datalayer column to create the "Supplier" column. A **Sort Filter** is added to the datalayer and set to sort on the new Supplier column to get things into order by Supplier.

To display the new column, another **Crosstab Table Label Column** element ("colSupplier") and a **Label** element to display the data are added. Finally, adding a **Hide Duplicates** element results in a hierarchical look by hiding the supplier name in consecutive rows.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575806743/xtabtable_29a.png)

The result is the addition of the Supplier column, highlighted in yellow above in the crosstab layout model.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575806999/xtabtable_30.png)

And, in a Preview, the table now looks like the image shown above.

You will need to apply formatting to various elements, such as Crosstab Table Value Columns and Column Cells, to align the data properly. This example uses the *ThemeAlignRight* style class to do this.
