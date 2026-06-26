---
title: "DsCalculated Column Usage Examples"
id: 4419715265431
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715265431-DsCalculated-Column-Usage-Examples
updated_at: 2022-07-17T01:50:55Z
---

# DsCalculated Column Usage Examples

# DsCalculated Column Usage Examples

Here are some examples of the DsCalculated Column element in use.

1. The following shows a simple implementation - calculating sales tax:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714741655/dscalccol_01.png)

In the definition shown above, a Data Table and a DataLayer.Data Services element have been added. A **DsCalculated Column** element has been added beneath the datalayer and its attributes have been configured so that it will multiply the values in the ProductSales column by a constant to produce the sales tax amount.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699696279/dscalccol_02.png)

The resulting sales tax amount will be placed in a new column, named calcTax, in every row of the data, as shown above. The data will be accessible as the token @Data.calcTax~.
Instead of hard-coding the sales tax rate in the expression, it could be made dynamic using a token, like this:

[ProductSales] \* @Request.TaxRate~

Here's a slightly different example: the following expression uses the IIF function to apply different tax rates, depending on other criteria:

IIF([CategoryID] == 4, [ProductSales] \* @Request.TaxRate1~, [ProductSales] \* @Request.TaxRate2~)

Of course, your expression doesn't *have* to use data from the datalayer at all. The following example simply creates a new column and puts the elapsed seconds for every row for it:

DateDiff('Second', @Request.StartTime~, DatePart('Second', Now()))

The possibilities are endless and allow developers a great deal of flexibility in manipulating the datalayer.

2. This example illustrates how the value created by one DsCalculated Column can be used in another DsCalculated Column.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706793879/dscalccol_03.png)

In the definition shown above, a second **DsCalculated Column** has been added beneath the datalayer. As you can see, its expression attribute uses data from one of the other data columns *and* the first calculated column.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706794135/dscalccol_04.png)

The resulting total amount will be placed in a new column, named calcTotal, in every row of the data, as shown above. The data will be accessible as the token @Data.calcTotal~.
