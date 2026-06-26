---
title: "Excel - Specifying Excel Column Formatting"
id: 4419707574295
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707574295-Excel-Specifying-Excel-Column-Formatting
updated_at: 2023-01-30T19:49:12Z
---

# Excel - Specifying Excel Column Formatting

# Excel - Specifying Excel Column Formatting

Data exported to Excel generally arrives in the worksheet as text-type data, which may not be desirable. For example, Excel will store exported numbers as text, then "helpfully" flag their cells with a confusing little green triangle. And, of course, these values (as text) cannot then be used in calculations in the worksheet.

You can turn off this behavior in Excel using options in File![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Options![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Formulas![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Error Checking or Error Checking Rules. Or, you can click the green triangle and select "Convert
to Number". These and other remedies such as writing
scripts in Excel to do the conversions automatically are not very convenient and may not be feasible.

However, the easiest way to handle the formatting of exported data on a column-by-column basis is to use **Excel Column Format** elements. These elements provide you with the opportunity to separately optimize the appearance of report and exported output and ensure that the exported data is seen as the correct data type.

![](https://devnet.logianalytics.com/hc/article_attachments/7522814035095/exportexcel_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522799953431/exportexcel_05a.png)

The **Excel Column Format** element is added as a child of each Data Table Column element that you want to format, as shown above, and is configured to format the data exported to the worksheet.

The following table describes the attributes of the Excel Column Format element:

| Attribute | Description |
| --- | --- |
| Auto Fit Row | When set to *True* for any column, the height of the Excel rows is automatically adjusted to fit the data. |
| Column Width | Specifies the width of the Excel column, in units representing the average character width for the current font. For example, a value of 10 would indicate a column that is usually able to contain 10 characters. The column will always be wide enough to display the value of the Column Header attribute of the Data Table Column element. |
| Data Type | Specifies a data type for values in the column; also affects justification of displayed data. |
| Excel Format | Applies formatting to the data displayed in Excel. Works with the Data Type attribute, so setting the data type correctly is required for correct formatting.  In addition to the standard Logi format options you can also use custom Excel formatting strings in this attribute. For example, to right-align whole numbers and currency, use this string:  \_(\* $#,##0.00\_);\_(\* $(#,##0.00);\_(\* $"-"??\_);\_(@\_)  Refer to [this document](http://www.mbaexcel.com/excel/how-to-use-excel-custom-number-formatting/) for information about custom number formats in Excel 2007+. |
| Font Bold Font Italic | When set to *True*, displays the data in Bold or Italic fonts, respectively. |
| Font Name | Specifies the name of the font to be used for this data. Font options are presented in a drop-down list. |
| Font Size | Specifies the size, in points, of the font used for this data. |
| Shrink To Fit | When set to *True*, automatically reduces the font size of a value that is too long to be displayed in a single cell to a smaller size in order to make it fit. |
| Wrap Text | When set to *True*, causes text that is too long to be displayed in a single cell to be wrapped into additional rows. |

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Excel Column Format elements have no effect when used with a table within a **SubReport** and they are not available for use with data displayed in **More Info Rows**.
