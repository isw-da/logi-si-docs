---
title: "Working with Column Headers"
id: 4419722796951
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722796951-Working-with-Column-Headers
updated_at: 2024-04-04T19:09:05Z
---

# Working with Column Headers

# Working with Column Headers

A *column header* contains optional information at the top of a specific Data Table column. Generally, column headers consist of text but, in a Logi application, they can include images and even user input controls, like buttons and links. Text or images may be a link that, when clicked, sorts the table on the column in alternating ascending and descending order.

![](https://devnet.logianalytics.com/hc/article_attachments/7522843285399/dtcols_04.png)

The Column Header row is the first row in the table, as shown above.
To configure a column header:

1. Select one of the **Data Table Column** elements in the definition.
2. Set the **Header Type** attribute to *Image* if an image is desired in the column header. If left blank, the default value is *Text*.
3. In the **Column Header** attribute value, type the desired text or choose an image from the drop-down list of choices.
4. The column header text is *centered* by default. However, you can apply a different class to *all* of the column headers at once by setting the parent Data Table element's **Column Header Class** attribute, or apply one individually to one or more columns by using their own Column Header Class attribute.

## Using Extra Column Headers

Column headers normally consist of a single line title, but Logi Studio makes it easy for developers to add additional content if necessary. Developers can create extra column headers with multiple rows, containing text, links or images.

![](https://devnet.logianalytics.com/hc/article_attachments/7522826673175/dtcols_05_552x237.png)

In the example above, an **Extra Column Header** element has been added as a child of a Data Table Column. It contains New Line and Label elements and the effect is to make a 2-line column header for the Customer ID column, as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/7522801637143/dtcols_06_600x209.png)

Another example, shown above, includes a column with a check box, for selecting rows, a common implementation in Data Tables. The Extra Column Header in this case includes two links that refresh the table, checking or unchecking all rows. The **Link Parameters** elements pass either a "1" (All) or nothing (None) when the report is refreshed, and the Input check box element uses the passed Request variable as its **Default Value** and "1" as its **Checked Value**.

## Hiding Table Headers

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Control whether your message includes table headers on an individual Data Table when there is no data to display by setting the new attribute 'Hide Header If No Data' to "True":

![](https://devnet.logianalytics.com/hc/article_attachments/7522790376471/hide_header_if_no_data_true.png)

As a result, your message will look like this:

![](https://devnet.logianalytics.com/hc/article_attachments/7522785635351/no_header.png)

To control the header display for all Data Tables on an application level, set the InfoGo constant 'rdHideDatatableHeaderIfNoData' to "True". By default, this constant is "False". For more information, see [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants).

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)

* For managed Data Tables/Crosstabs, the 'Hide Header If No Data' attribute overrides the 'rdHideDatatableHeaderIfNoData' constant, while AG/SSRM Data Tables/Crosstabs take the constant value.
* By default, the values for both the attribute and the constant is "False" and "Default", respectively.
