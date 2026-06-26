---
title: "Adding Extra Crosstab Values"
id: 4406822217623
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822217623-Adding-Extra-Crosstab-Values
updated_at: 2022-04-06T06:04:47Z
---

# Adding Extra Crosstab Values

# Adding Extra Crosstab Values

By default, the **Crosstab Filter** produces a single value for each column and row combination. In order to generate additional values for the Total Sales data for our crosstab table, we need to use an **Extra Crosstab Value Column** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563429271/xtabtable_31.png)

As shown above, this element simply identifies a column from the datalayer ("OrderTotals") and the aggregation to be applied to it.

A **Crosstab Table Value Columns** element ("colOrderTotal") is also added to display the values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A special token is needed to access that data: *@Data.rdCrosstabValue-ODTotal~*.

The token identifier combines the reserved word "rdCrosstabValue", then a dash "-", and then the ID of the element beneath the Crosstab Filter that represents the value column ("ODTotal"). This token is used in the **Caption** attribute of a **Label** element beneath
the Crosstab
Table Value Columns element we added.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563429399/xtabtable_32.png)

Next, we'll repeat the previous steps in order to add an Average Unit Price column, this time using an **Extra Crosstab Calculated Column** element. In the example shown above, the average unit price is calculated using this element. The complete formula in this example is:

@Data.rdCrosstabValue-ODTotal~/@Data.rdCrosstabValue~

which divides the Order Total by the Quantity. The Order Total value is accessed using the same token discussed earlier and used to display the order total values; while the Quantity value is accessed using a similar token representing the original Value column defined in the Crosstab Filter.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575811607/xtabtable_32a.png)

The elements added and configured in this step add the columns highlighted above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584068119/xtabtable_33.png)

And, in a Preview, the table now looks like the image shown above.
