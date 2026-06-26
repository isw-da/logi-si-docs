---
title: "Advanced Reports: Templates"
id: 5281564145303
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281564145303-Advanced-Reports-Templates
updated_at: 2022-05-03T22:09:20Z
---

# Advanced Reports: Templates

# Advanced Reports: Templates

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> **Document Templates** are an optional feature. Check with the system administrator for more information.

An Advanced Report can be used to dynamically fill out fields in forms and other documents. Placeholders in the document are dynamically linked to fields in the report. When executed, the form or document is merged with the report data.

![screen.templatereport.png](https://devnet.logianalytics.com/hc/article_attachments/5432412023959/screen.templatereport.png)

Report layout in the Advanced Report Designer

![screen.templatepreview.png](https://devnet.logianalytics.com/hc/article_attachments/5432323086743/screen.templatepreview.png)

Report data

![screen.templateout.png](https://devnet.logianalytics.com/hc/article_attachments/5432384040599/screen.templateout.png)

W9 template form with data merged from report

This topic covers the three stages of working with document templates:

1. [1. Creating Template Documents](#1.)
2. [2. Linking Document Templates to a Report](#2.)
3. [3. Executing Template Reports](#3.)

## 1. Creating Template Documents

The process for making templates differs between the three supported document types: [PDF Templates](#PDF), [Word Templates](#Word), and [Microsoft Excel Templates](#Microsof) as do the available features.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Close the template file before running or saving a report that uses it.

### PDF Templates

PDF templates support static fields and limited-repeating fields. PDFs are convenient for pre-existing and standardized forms, such as for government or business.

To create a PDF template:

1. Open the form in a PDF editor program, such as Adobe Acrobat or PDFescape.
2. Add form fields where you will insert report data. For fields where text may span multiple lines, select the multi-line property.
3. Give each form field a unique name following these guidelines:
   * For *static fields*, which appear only once per template instance — use any name, with the exception of the format reserved for repeating fields.
   * For *repeating fields*, which are mapped to consecutive values in a repeating cell or in a detail section — use the following naming format: `Name.0, Name.1,...`  
     Where `Name` is shared by the repeating fields, and `0` maps to the first value, `1` maps to the next value, and so on.
   * For *checkboxes* — use an *If()* function whose results are “X” for a checked box and ” ” (space) for an unchecked box. For example, `=if({Employees.Title} = 'Sales Representative', 'X', ' ')`.
4. Save the PDF. Then continue with the instructions in [2. Linking Document Templates to a Report](#2.).

### Word Templates

Word templates support static fields, limited and unlimited-repeating fields, and conditional suppression.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Supported file types are `.doc`, `.docx`, and `.rtf`. Report templates exported as “RTF” will save to the original file type.

To create a Word template:

1. Open a document in Microsoft Word or a compatible document editor.
2. Add text where you want to insert report data.
3. Select the text, or in the case of repeating fields, a region of text, and insert a bookmark.  
   ![screen.wordtemplate_bookmarksadded.png](https://devnet.logianalytics.com/hc/article_attachments/5432384051735/screen.wordtemplate_bookmarksadded.png)
4. Give each bookmark a unique name, as follows:
   * For *static fields*, which appear only once per template instance — use any name, with the exception of the formats reserved for repeating and conditional fields.
   * For *limited-repeating fields*, which are mapped to consecutive values in a repeating cell — use the following naming format: `FieldName_0, FieldName_1, ...` Where `Name` is shared by the repeating fields, and `0` maps to the first value, `1` maps to the next value, and so on.
   * For *unlimited-repeating fields,* which are mapped to all the values in a repeating cell — use the following naming format: `RepeatForEach_FieldName` Where `FieldName` is a unique name. A RepeatForEach section in a template follows similar structure and purpose to grouping within reports. It is used to organize information under repeating groups within templates, arranging related information on the same page and separating groups with page breaks.![screen.wordtemplate_bookmarks.png](https://devnet.logianalytics.com/hc/article_attachments/5432400105239/screen.wordtemplate_bookmarks.png)
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > Bookmark formatting for unlimited-repeating fields must follow specific spacing requirements. The opening bookmark bracket should be placed one line before the repeating field section begins, and the closing bookmark bracket should be placed one line after the repeating field sections ends. Refer to the *Employee Information* example above for a visual reference. If this formatting is not followed, an “itemStart and itemEnd must be contained in one text body” error may be thrown.
5. *Optional*: To conditionally show or hide text:
6. Select the text and add a bookmark with the following naming format: `KeepIF_FieldName` Where `FieldName` is a unique name.
7. In the report, map this field to a cell with a formula that returns 1 if the text should be shown, and 0 if the text should be hidden. For example, `=If({Products.ProductName} = "Chai", 1, 0)`
8. Save and close the file. Then continue with the instructions in [2. Linking Document Templates to a Report](#2.).

### Microsoft Excel Templates

Excel templates work differently than other types. Templates are used to fill Excel columns with report data. This is useful for passing data to Excel charts, pivot tables, and macros.

To create an Excel template:

1. Open a workbook in Microsoft Excel or a compatible spreadsheet editor.
2. The first worksheet is used for dynamic report data. *Repeating cells* are mapped to columns in the worksheet. For each column where you will add report data, enter a unique name to the topmost cell in the column. All following cells must be empty. All other worksheets will remain unchanged by the report.![screen.exceltemplatefile.png](https://devnet.logianalytics.com/hc/article_attachments/5432454175511/screen.exceltemplatefile.png)

   Formatting an Excel file to be used as a template
3. Save the file. Then continue with the instructions in [2. Linking Document Templates to a Report](#2.).

## 2. Linking Document Templates to a Report

To use a report to fill out a template:

![screen.reporttemplatesexmaple_pdf.png](https://devnet.logianalytics.com/hc/article_attachments/5432454229911/screen.reporttemplatesexmaple_pdf.png)

Editing of fields in exported PDF templates, v2018.2+

1. Enter field data in cells on the report. For repeating data:
   * Repeating cells mapped to static template fields make a new instance of the template for each repeat.
   * Repeating cells mapped to limited-repeating template fields make a new instance of the template each time the number of values exceeds the limit.  
     **Note:** This is often undesirable. Ensure that there are appropriate constraints on the data and enough fields to fit it all.
   * Repeating cells mapped to unlimited-repeating template fields never make a new instance of the template. Overflowing data is cut off.
2. *v2021.1+:* On the ![SettingsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432122354839/settingsmenu.png)**Advanced** menu, click ![Template.png](https://devnet.logianalytics.com/hc/article_attachments/5432193608599/template.png) **Templates** to open the **Report Templates** dialog.
3. *pre-v2021.1:* On the ![SettingsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432122354839/settingsmenu.png)**Settings** menu, click ![Template.png](https://devnet.logianalytics.com/hc/article_attachments/5432193608599/template.png) **Template** to open the **Report Templates** dialog. Select an existing template or click the **Upload** button to upload a new one.
4. For each template field:
   * Select a report cell containing text or data. Images, visualizations, and other widgets are not supported.
   * Leave it blank. Any bookmarked text shows as-is in the output.
   * Select whether or not to allow editing of that field in the exported PDF file using the **Allow Edit** checkbox. v2018.2+
5. Click **OK**.

To remove a template from a report:

1. From the **Template** dialog, select the *blank* option from the template list.
2. Click **OK**.

## 3. Executing Template Reports

To generate the filled out forms or documents, simply **Export** the report in the same format as the template file (for example for a PDF template file, export the report as a PDF. For a Word template, export as RTF). Reports can be exported from the toolbar or from the main menu.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Template reports must be exported in the same file type as the template (that is a PDF template report must be exported as a PDF file). Review the General Section of the Report Options topic for details on how to control report export types.

### Referencing Data Exported to Excel Templates

When using an Excel Template there are two ways for Charts or Pivot Tables to reference the populated report data:

* [Named Ranges](#Named)
* [Row References](#Row)

#### Named Ranges

Excel has a concept of a Named Range which can be used by Charts or Pivot Tables to refer to a range of cells. When building the template, name ranges by:

1. On Excel’s ribbon, navigate to the **Formulas** tab and click the **Name Manager** icon.  
   ![4862xgbx5Z.png](https://devnet.logianalytics.com/hc/article_attachments/5432323185175/4862xgbx5z.png)
2. Click **New** to add a new named range.
   1. The **Name** must match the name of the first worksheet in the file.
   2. The **Scope** should be *Workbook* if the chart or PivotTable will reside on a different worksheet than the first one.
   3. *Optional:* add a comment
   4. In the **Refers to** field, select the upper left and upper right boundaries of the range. For example, to select all of the data from columns A–J, select those cells or enter `DATA!$A$1:$J$1`.  
      > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
      >
      > When the report is exported, the range will automatically be expanded to include all of the rows.
3. When building the Excel chart or PivotTable, use the Named Range created in steps 1–2 as its data source.  
   ![s7jJmjmH9o.png](https://devnet.logianalytics.com/hc/article_attachments/5432400237975/s7jjmjmh9o.png)

#### Row References

Instead of using Named Ranges, each Chart or PivotTable can be set to reference the first two rows on the first worksheet. For example, a template with 5 columns would reference `=Sheet1!$A$1:$E$2`. When the report is exported, the range will automatically be expanded to include all of the rows.
