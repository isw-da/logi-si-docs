---
title: "Analysis Grid Developers - Exporting Data"
id: 4419700098711
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700098711-Analysis-Grid-Developers-Exporting-Data
updated_at: 2022-07-17T02:25:24Z
---

# Analysis Grid Developers - Exporting Data

# Analysis Grid Developers - Exporting Data

The Analysis Grid can be configured by the developer to include options to export table data to three formats: **Excel**, **CSV**, and **PDF:**

![](https://devnet.logianalytics.com/hc/article_attachments/7522856654999/workag_19.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 The application can also be configured to export the report title and filter information. By default, the report title and filter information are not included with the export. To enable this functionality, set the global constants rdIncludeReportTitleInExport and rdIncludeFilterInfoInExport to **True**.

In all cases, the exported file is written to a temporary file, which is then opened in the browser or related application for display, manipulation, printing, or storage.

![](https://devnet.logianalytics.com/hc/article_attachments/7522864798999/workag_20.png)

Developers can optimize Excel exports by adding an **Excel Column Format** element to each grid column, as shown above. This provides developers with full control over the *layout* and *appearance* of exported data in the worksheet. The element's **Data Type** attribute is especially useful for ensuring that data is correctly formatted when it arrives in Excel. There are no export-specific elements for the
other export formats.

## Export Threshold

When working with very large data sets, exports may not be practical. Developers can control this using the Analysis Grid element's **Max Rows Export** attribute specifies the maximum number of data rows that can be exported.

When the number of rows in the Analysis Grid's main table is equal to or less than this value, exports will be enabled; if the number of rows exceeds this value, exports are disabled. This allows developers to prevent users from running export requests that will take an unacceptable amount of time. The default
value for this attribute is
*100,000* rows.

If the special value -1 is entered, the default maximum limit is removed, allowing *all**rows* to be exported.

At runtime, users can reduce the number of rows in the Analysis Grid's main table, and thus enable exports, by adding one or more Analysis Grid filters.

## Rapid Export Options

Excel and CSV exports can also be configured for Rapid Export, which provides a faster mechanism for exporting large datasets. The Rapid Export feature honors basic formatting (bold, font, italics, etc), but it does not apply custom styling or group aggregation.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) You cannot export a report with more than one Data Table.

In Studio, set the attribute **Export Data Preference** (Formatted, Empty {default}, or Rapid) on the Target.NativeExcel and Target.CSV elements. This preference can also be set on a global application level by setting a restricted constant called rdExportDataPreference to *Rapid*, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820585239/rapid_export.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) The default value for the above constant is empty.

For more information, see [Rapid Excel Export](https://devnet.logianalytics.com/hc/en-us/articles/4419715446423-Rapid-Excel-Export) and [Rapid CSV Export](https://devnet.logianalytics.com/hc/en-us/articles/4419723125655-Rapid-CSV-Export).
