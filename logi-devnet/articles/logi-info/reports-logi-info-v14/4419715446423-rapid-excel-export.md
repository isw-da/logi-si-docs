---
title: "Rapid Excel Export"
id: 4419715446423
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715446423-Rapid-Excel-Export
updated_at: 2022-07-17T02:23:41Z
---

# Rapid Excel Export

# Rapid Excel Export

The Rapid Excel Export option provides a built-in capability for both the Data Table and Analysis Grid, running off the datalayer. This feature is available for Consumer and Self-Service users who export tabular data in Excel format for further analysis outside of the context of the Info application. The Rapid Export option greatly improves the performance of exporting large data, as compared to the Native Excel export option. The Rapid Export feature honors basic formatting (bold, font, italics, etc), but it does not apply custom styling or group aggregation. To review a detailed list of the differences between the native Excel and rapid Excel export, see [Exporting To Native Excel](https://devnet.logianalytics.com/hc/en-us/articles/4419722903831-Export-To-Native-Excel).

To export your data using the Rapid Excel Export, access your Data Table in the Analysis Grid and select the **Export** icon.

Then, select **Excel** from the drop-down list:

![](https://devnet.logianalytics.com/hc/article_attachments/7522806205079/select_export_export.png)

Your download will appear in the bottom of the web browser, or may open automatically, depending on your machine's configuration.

The Data Table displays in Excel:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759847063/exported_data_table.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 The report title, grouping, summary, and filter information display on the export results, if your application has been configured for it.

Developers control the availability of different types of exports. In Info Studio, you can set the new attribute on the Target .NativeExcel element called "ExportDataPreference" (Formatted, Empty {default}, or Rapid ). This preference can be set on a global application level by setting a restricted constant rdExportDataPreference to *Rapid*, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820585239/rapid_export.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Additionally, Rapid Excel exports can now resolve tokens.

For more information about how to configure your Info application to export to Excel, see [Excel - Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419707572375-Excel-Exporting-a-Report-Manually).
