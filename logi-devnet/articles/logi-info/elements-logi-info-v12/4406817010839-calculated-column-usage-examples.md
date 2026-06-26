---
title: "Calculated Column Usage Examples"
id: 4406817010839
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817010839-Calculated-Column-Usage-Examples
updated_at: 2022-04-06T06:03:21Z
---

# Calculated Column Usage Examples

# Calculated Column Usage Examples

Here are some examples of the Calculated Column element in use.  
1. The following shows a simple implementation - calculating sales tax:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575904151/calccol_01.png)

In the definition shown above, a data table and a datalayer element have been added. A **Calculated Column** element has been added beneath the datalayer and its attributes have been configured so that it will multiply the values in the ProductSales column by a constant to produce the sales tax amount.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584173847/calccol_02.png)

The resulting sales tax amount will be placed in a new column, named calcTax, in every row of the datalayer, as shown above. The data will be accessible as the token @Data.calcTax~.
Instead of hard-coding the sales tax rate in the formula, it could be made dynamic using a token, like this:

@Data.ProductSales~ \* @Request.TaxRate~

Here's a slightly different example: the following expression uses the intrinsic IIF function to apply different tax rates, depending on other criteria:

IIF(@Data.CategoryID~ = 4, @Data.ProductSales~ \* @Request.TaxRate1~, @Data.ProductSales~ \* @Request.TaxRate2~)

Of course, your expression doesn't *have* to use data from the datalayer at all. The following example simply creates a new column and puts the elapsed seconds for every row for it:

DateDiff("s", CXMLDate("@Request.StartTime~"), CXMLDate("@Function.Time~"))

Note the use of the intrinsic [CXMLDate function](https://devnet.logianalytics.com/hc/en-us/articles/4406817861143-CXMLDate-Function), which is necessary to convert ISO formatted XML DateTime data into a format that works with the DateDiff function (and should be used with DateAdd, DatePart, and other date functions).
The possibilities are endless and allow developers a great deal of flexibility in manipulating the datalayer.

2. This example illustrates how the value created by one Calculated Column can be used in another Calculated Column.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575904791/calccol_03.png)

In the definition shown above, a second **Calculated Column** has been added beneath the datalayer. As you can see, its Formula attribute uses data from one of the retrieved data columns *and* the first calculated column.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575904919/calccol_04.png)

The resulting total amount will be placed in a new column, named calcTotal, in every row of the datalayer, as shown above. The data will be accessible as the token @Data.calcTotal~.
