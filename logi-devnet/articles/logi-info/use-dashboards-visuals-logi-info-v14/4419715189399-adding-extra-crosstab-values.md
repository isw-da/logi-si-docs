---
title: "Adding Extra Crosstab Values"
id: 4419715189399
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715189399-Adding-Extra-Crosstab-Values
updated_at: 2022-07-17T02:24:50Z
---

# Adding Extra Crosstab Values

# Adding Extra Crosstab Values

By default, the **Crosstab Filter** produces a single value for each column and row combination. In order to generate additional values for the Total Sales data for our Crosstab Table, we need to use an **Extra Crosstab Value Column** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522831663255/xtabtable_31.png)

As shown above, this element simply identifies a column from the datalayer ("OrderTotals") and the aggregation to be applied to it.

A **Crosstab Table Value Columns** element ("colOrderTotal") is also added to display the values.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) A special token is needed to access that data: *@Data.rdCrosstabValue-ODTotal~*.

The token identifier combines the reserved word "rdCrosstabValue", then a dash "-", and then the ID of the element beneath the Crosstab Filter that represents the value column ("ODTotal"). This token is used in the **Caption** attribute of a **Label** element beneath
the Crosstab Table Value Columns element we added.

![](https://devnet.logianalytics.com/hc/article_attachments/7522853563927/xtabtable_32.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding "HTML Attribute Params" to your Crosstab Table enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

Next, we'll repeat the previous steps in order to add an Average Unit Price column, this time using an **Extra Crosstab Calculated Column** element. In the example shown above, the average unit price is calculated using this element. The complete formula in this example is:

@Data.rdCrosstabValue-ODTotal~/@Data.rdCrosstabValue~

which divides the Order Total by the Quantity. The Order Total value is accessed using the same token discussed earlier and used to display the order total values; while the Quantity value is accessed using a similar token representing the original Value column defined in the Crosstab Filter.

![](https://devnet.logianalytics.com/hc/article_attachments/7522853569047/xtabtable_32a.png)

The elements added and configured in this step add the columns highlighted above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522816897559/xtabtable_33.png)

And, in a Preview, the table now looks like the image shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) You can use the **Secondary Crosstab Label Column** element to group Value Columns and Label Columns together. For more information, see [Working with the Crosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419715192599-Working-with-the-Crosstab-Filter).
