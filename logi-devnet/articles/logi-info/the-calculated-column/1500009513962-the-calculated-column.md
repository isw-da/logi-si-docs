---
title: "The Calculated Column"
id: 1500009513962
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009513962-The-Calculated-Column
updated_at: 2021-06-17T01:58:00Z
---

# The Calculated Column

# The Calculated Column

The **Calculated Column** element adds a new column to a datalayer with a value that's the result of a formula, which can include data from other columns, tokens, and literals. The formula is evaluated for every row in the datalayer.

* About the Calculated Column
* [Calculated Column Attributes](#Attributes)
* [Usage Examples](#Simple)
* [NaN Errors](#Errors)

## About the Calculated Column

The Calculated Column is similar to other elements designed to *extend* the data available in a datalayer. Like the **Aggregate Column** element, the Calculated Column is added as a child element beneath a datalayer and adds a **new column** to the datalayer. This column value is **derived data** which is accessible using an @Data token.

The new column's value is the result of evaluating a formula, for all rows in the datalayer. This calculated value is populated in the new column in every
row of the datalayer and can be used in further calculations, Summary Rows, Link Params,
etc.

Similar calculations could be performed within SQL queries and *may* offer better performance when done by the database server. However, the Calculated Column element allows calculations to be performed on data from other sources too, such as web services and data files, that do not themselves offer SQL-like queries.

## Calculated Column Attributes

The attributes for the Calculated Column element are described below:

| Attribute | Description |
| --- | --- |
| Formula | (Required) A VBScript or JavaScript expression that returns a string or numeric value. Tokens, including data from other datalayer columns, literals, and intrinsic functions may be used here. *Do not* start the expression with an equals sign (=). See the **usage examples** below. Select the scripting type using the General element's Scripting Language attribute, in the \_Settings definition. |
| ID | (Required) The unique element ID for the Calculated Column element, which is also the name of the column that will be added to the datalayer. |
| Error Limit | Specifies the maximum number of times evaluating a formula can produce an error. After the limit is reached, the Calculated Column returns the value specified in the Error Result attribute value. |
| Error Result | Specifies the value to be returned when the Error Limit is reached during evaluation. Default: *blank* |
| Include Condition | (v10.0.319) Determines if the evaluation will be applied. If left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. |
| Script File | Specifies the name of an optional script file containing functions or routines called in the Formula expression. If the script file is in the \_SupportFiles folder, no path is necessary. Otherwise, specify a fully-qualified file system path and filename (tokens such as @Function.AppPhysicalPath~ may be used). |

## Usage Examples

1. The following example, which calculates sales tax, illustrates how the Calculated Column works:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771938711/calccol_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778746647/calccol_01a.png)

In the definition shown above, a data table and a datalayer element have been added. A **Calculated Column** element has been added beneath the datalayer and its attributes have been configured so that it will multiply the values in the ProductSales column by a constant to produce the sales tax amount.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778746903/calccol_02.png)

The resulting sales tax amount will be placed in a new column, named calcTax, in every row of the datalayer, as shown above. The data will be accessible as the token @Data.calcTax~.

Instead of hard-coding the sales tax rate in the formula, it could be made dynamic using a token, like this:

@Data.ProductSales~ \* @Request.TaxRate~

The following formula could be used to apply different tax rates, depending on other criteria:

IIF(@Data.CategoryID~ = 4, @Data.ProductSales~ \* @Request.TaxRate1~, @Data.ProductSales~ \* @Request.TaxRate2~)

Of course, your formula doesn't *have* to use data from the datalayer. This example simply creates a new column and puts the elapsed seconds for every row for it:

DateDiff("s", CXMLDate("@Request.StartTime~"), CXMLDate("@Function.Time~"))

Note the use of the intrinsic CXMLDate function, which is necessary to convert ISO formatted XML DateTime data into a format that works with the DateDiff function (and should be used with DateAdd, DatePart, and other VBScript-based date functions). For more information, see the CXMLDate Function section of [Special Functions and Attributes](https://devnet.logianalytics.com/hc/en-us/articles/1500009531881-Special-Functions-and-Attributes).

The possibilities are endless and allow developers a great deal of flexibility in manipulating the datalayer.

2. This example illustrates how the value created by one Calculated Column can be used in another Calculated Column.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771938967/calccol_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771939223/calccol_03a.png)

In the definition shown above, a second **Calculated Column** has been added beneath the datalayer. As you can see, its Formula attribute uses data from one of the retrieved data columns *and* the first calculated column.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771939991/calccol_04.png)

The resulting total amount will be placed in a new column, named calcTotal, in every row of the datalayer, as shown above. The data will be accessible as the token @Data.calcTotal~.

## NaN Errors

If data or other circumstances cause the Calculated Column's formula to attempt a "division by zero", the resulting value in the datalayer will be **NaN**, which stands for "Not a Number". This can cause problems or be confusing when the data is visualized.

If this kind of result is possible, developers may want to wrap their formula in an IIF statement to provide an alternative to the NaN result in the data. For example, the formula

IIF(@Data.RoomsAvailable~ <> 0, @Data.RoomRevenue~/@Data.RoomsAvailable~, "")

tests to see if a division by zero is going to happen and, if so, instead of doing the calculation, supplies an empty value in the datalayer.
