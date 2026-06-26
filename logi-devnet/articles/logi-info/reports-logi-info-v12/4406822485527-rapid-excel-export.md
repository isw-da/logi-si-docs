---
title: "Rapid Excel Export"
id: 4406822485527
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822485527-Rapid-Excel-Export
updated_at: 2022-04-06T06:08:19Z
---

# Rapid Excel Export

# Rapid Excel Export

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) The Rapid Excel Export option provides a built-in capability for both the Data Table and Analysis Grid, running off the datalayer. This feature is available for Consumer and Self-Service users who export tabular data in Excel format for further analysis outside of the context of the Info application. The Rapid Export option greatly improves the performance of exporting large data, as compared to the Native Excel export option. The Rapid Export feature honors basic formatting (bold, font, italics, etc), but it does not apply custom styling or group aggregation. To review a detailed list of the differences between the native Excel and rapid Excel export, see [Export To Native Excel](https://devnet.logianalytics.com/hc/en-us/articles/4406817434775-Export-To-Native-Excel).

To export your data using the Rapid Excel Export, access your Data Table in the Analysis Grid and select the **Export** icon.

Then, select **Excel** from the drop-down list:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583759639/select_export_export.png)

Your download will appear in the bottom of the web browser, or may open automatically, depending on your machine's configuration.

The Data Table displays in Excel:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563111575/exported_data_table.png)

The availability of different types of exports is under developer control. In Info Studio, you can set the new attribute on the Target .NativeExcel element called "ExportDataPreference" (Formatted, Empty {default}, or Rapid ).. This preference can be set on a global application level by setting a restricted constant "rdExportDataPreference" to *Rapid*, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583752855/rapid_export.png)

For more information about how to configure your Info application for Rapid CSV Export, [Excel - Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4406817435799-Excel-Exporting-a-Report-Manually).
