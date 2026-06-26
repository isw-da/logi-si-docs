---
title: "Comparing, Sorting, and Summarizing Columns"
id: 4406817228951
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817228951-Comparing-Sorting-and-Summarizing-Columns
updated_at: 2022-04-06T06:04:49Z
---

# Comparing, Sorting, and Summarizing Columns

# Comparing, Sorting, and Summarizing Columns

It's not uncommon to need to include the *difference*, either as a value or as a percentage, between two or more Value Columns in a crosstab table. There are two approaches to creating this information.

## The Crosstab Comparison Element

The **Crosstab Comparison** element makes it easy to visually understand the differences between values in crosstab columns:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563423895/xtabtable_12.png)

Each column is compared with the previous column and an indicator arrow or colored background is shown if the value increased or decreased. The amount of increase or decrease can be displayed as a numeric and/or percentage difference.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584061719/xtabtable_13.png)

As shown above, comparisons between columns can be indicated by colored arrows and percentages or literal values, within each column cell or in tooltips that appear when the mouse is hovered on a value. Instead of the colored arrows, you can display a colored cell background, covering a spectrum, to indicate the differences.

The unique attributes of the Crosstab Comparison element are:

| Attribute | Description |
| --- | --- |
| Comparison Show Tooltips | Enables display of the numerical difference in a tooltip when the mouse is hovered over a crosstab value. Display options include *Percent*, *Value*, *All*, or the default, *None*. |
| Comparison Show Values | Enables display of the numerical difference in the crosstab cells. Display options include *Percent*, *Value*, *All*, or the default, *None*. The Format attribute can be used to format the displayed numbers. |
| Comparison Style | Specifies how differences will be indicated visually. Options include *None*, *ColorSpectrum*, and the default, *Arrows*. |
| Format | Specifies a format for values or percentages displayed. For more information, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817477911-Format-Data). |
| High Color Value | When *ColorSpectrum* has been selected as the Comparison Style, specifies the color to be used for the highest value in the numeric range. Default: *Green* |
| Low Color Value | When *ColorSpectrum* has been selected as the Comparison Style, specifies the color to be used for the lowest value in the numeric range. Default: *Red* |
| Medium Color Value | When *ColorSpectrum* has been selected as the Comparison Style, specifies the color to be used for the value in the middle of the numeric range. |

If the Crosstab Table element's **Draggable Columns** attribute has been set to *True*, and the Crosstab Comparison element is in use, when columns are dragged to change their order, their comparison values will be automatically updated.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Because the calculations made by this element do not affect the table's datalayer, it's not possible to summarize or sort the results.

## Calculating Comparisons Using Tokens

The second approach to Value Column comparisons allows other calculations, such as comparisons to current dates or to external values, and is accomplished entirely within the **Label** element used to present the results.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584061975/xtabtable_14.png)

In the example above, a **Crosstab Table Label Column** element ("colDifference") has been added with a **Label** element beneath it. The Label element's **Caption** attribute includes a formula that relies on the fact that crosstab table value columns can be individually addressed using the tokens @Data.rdCrosstabValue-0~, @Data.rdCrosstabValue-1~, ...@Data.rdCrosstabValue-*n*~.

To display the *difference* between two values, for example, the Label caption would use this formula:

=@Data.rdCrosstabValue-1~ - @Data.rdCrosstabValue-0~

And, we can add the same element again to display the *percentage difference* between two values. The child Label element beneath it would use this formula in its Caption attribute:

=IIF(@Data.rdCrosstabValue-1~ - @Data.rdCrosstabValue-0~ < 1, (@Data.rdCrosstabValue-1~ - @Data.rdCrosstabValue-0~)/@Data.rdCrosstabValue-0~, (@Data.rdCrosstabValue-1~/@Data.rdCrosstabValue-0~) - 1 )

Both Label elements need to have their Format attributes set properly to display the numeric value correctly.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575804567/xtabtable_15.png)

With both of these difference calculations included, the resulting crosstab table looks like the example shown above. Again, because the calculations do not affect the table's datalayer, it's not possible to summarize or sort the results.

## Sorting and Summarizing Columns

As mentioned earlier, you can apply a Sort Filter element beneath your datalayer, before or after the Crosstab Filter, to sort the actual data. In addition, you can use sorting elements within the table columns.

The sorting and summary features for Crosstab Table Label Columns are functionally similar to those for data table columns: **Sort** and **Data Column Summary** child elements are added beneath them.

However, because of its special dynamic-column nature, the Crosstab Table Value Columns element has its own special sort element: the **Crosstab Value Column Sort** element is used to sort by value columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563425943/xtabtable_17.png)

When using a standard Data Column Summary element to summarize crosstab Value columns, set its **Data Column** attribute to *rdCrosstabColumn*, as shown above.

A standard **Summary Row** element is added to create a row across the bottom of the crosstab table to display the summarized value for each column with a Data Column Summary element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575804823/xtabtable_18.png)

And the results look like the example shown above. By default, the Summary Row element's columns inherit the formatting and alignment of the value column above them.

For more precise control of the summary row, you may use **Column Cell** elements (beneath Crosstab Table Label Columns) and/or **Crosstab Table Summary Column** elements (beneath Crosstab Table Value Columns) to construct the row. These allow you to span rows and columns and set custom alignment and formatting.
