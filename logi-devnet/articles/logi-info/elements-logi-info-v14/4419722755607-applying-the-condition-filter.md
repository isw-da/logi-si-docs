---
title: "Applying the Condition Filter"
id: 4419722755607
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722755607-Applying-the-Condition-Filter
updated_at: 2022-07-17T02:24:58Z
---

# Applying the Condition Filter

# Applying the Condition Filter

The following example illustrates how the **Condition Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/7522848206743/condfilter_01.png)

1. As shown above, a Condition Filter element is added as a child of a datalayer element.
2. Its **Condition** attribute value is set to a formula that compares the data in the datalayer to some value. Note that no leading equals sign (=) is required for the expression here.

When the example is executed, the datalayer reads in all the data from the CSV data file, then the Condition Filter **removes** all records other than those where the condition formula evaluates to *True;* in this case, where the values in the *UnitPrice* column are greater than or equal to 40. All that remains in the datalayer for use in the report are records whose *UnitPrice* values are less than 40.
The Condition Filter element's **Condition** attribute supports built-in functions (see [Built in Functions and Operators](https://devnet.logianalytics.com/hc/en-us/articles/4419715078679-Built-in-Functions-and-Operators)) and JavaScript functions and can evaluate them to filter data:

![](https://devnet.logianalytics.com/hc/article_attachments/7522879211287/condfilter_02.png)

1. As shown above, a Condition Filter element is added as a child of the datalayer element.
2. Its **Condition** attribute value is set to a formula that uses the built-in function *Left()* to compare the data in the datalayer to some value. Note that no leading equals sign (=) is required here.

When executed, the datalayer reads in all the data from the CSV data file, then the Condition Filter evaluates the formula and **removes** all records where the first letter of the *Category* column is not the letter *"C".* All that remains in the datalayer for use in the report are records whose *Category* column values begin with "C".
Compound expressions, using AND and OR operators, can also be used in the Condition attribute.
