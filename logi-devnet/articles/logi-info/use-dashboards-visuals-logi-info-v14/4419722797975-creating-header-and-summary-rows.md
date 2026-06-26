---
title: "Creating Header and Summary Rows"
id: 4419722797975
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722797975-Creating-Header-and-Summary-Rows
updated_at: 2022-07-17T02:24:41Z
---

# Creating Header and Summary Rows

# Creating Header and Summary Rows

**Header** and **Summary** rows allow you to display data column
summary information on the first (excluding the Column Header row) and/or
last rows of a Data Table. You can customize these rows by adding
individual **Column Cell** elements.

The easiest way to display summary information is to use special summary
elements with each Data Table Column to be summarized and then create a
header and/or summary row, as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/7522815530903/dtrows_01_617x228.png)

1. Ensure that each Data Table Column to be summarized has a child
   **Data Column Summary** element, as shown above.
2. Set its attributes to produce the desired summary of the desired column,
   as shown above.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522801572247/dtrows_02.png)
3. Select the parent Data Table element and add a **Header Row** or
   **Summary Row** element to the definition, as shown above.
4. Set its **Caption** attribute to display a title in the first column
   of the header/summary row.
5. When using a Summary Row and Interactive Paging, set its
   **Last Page Only** attribute to *True* to show the summary only
   on the last page of the Data Table, otherwise it will appear at the
   bottom of every page.

![](https://devnet.logianalytics.com/hc/article_attachments/7522815570839/dtrows_03.png)

The example above show the typical result, with the summary row at the
bottom.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The cells generated for the summary row automatically
inherit the formatting and alignment of the columns above them.

A standard header or summary row works well when *every* data column
contains summary information. However, for Data Tables with numerous
columns and/or columns with non-numeric data, a *customized* header
or summary row may be a better solution. Here's how to create a customized
header:

![](https://devnet.logianalytics.com/hc/article_attachments/7522843276183/dtrows_04_562x277.png)

1. Ensure that each Data Table Column to be summarized has a child
   **Data Column Summary** element.
2. Select the parent Data Table element and add a **Header Row** element
   to the definition.
3. Beneath it, add one or more **Column Cell** elements.
4. Add **Label** elements beneath the Column Cell elements to display
   the summary data and use the @Data token to retrieve the summarized
   values, using on the ID of the Data Column Summary elements you added.
   For example, @Data.avgDiscount~.

The formatting and alignment of the Data Table columns is
*not* inherited when using Column Cell elements, so you must set
these individually.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) In the example shown above, the Header Row element has
*three* Column Cell child elements, but the Data Table has
*four* columns. This is handled by setting the first Column Cell
element's **Column Span** attribute to span *2* columns, allowing
for the difference.

## New for 14.1 Hiding Table Headers

Control whether your message includes table headers on an individual Data Table when there is no data to display by setting the new attribute 'Hide Header If No Data' to "True":

![](https://devnet.logianalytics.com/hc/article_attachments/7522790376471/hide_header_if_no_data_true.png)

As a result, your message will look like this:

![](https://devnet.logianalytics.com/hc/article_attachments/7522785635351/no_header.png)

To control the header display for all Data Tables on an application level, set the InfoGo constant 'rdHideDatatableHeaderIfNoData' to "True". By default, this constant is "False". For more information, see [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants).

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)

* For managed Data Tables/Crosstabs, the 'Hide Header If No Data' attribute overrides the 'rdHideDatatableHeaderIfNoData' constant, while AG/SSRM Data Tables/Crosstabs take the constant value.
* By default, the values for both the attribute and the constant is "False" and "Default", respectively.
