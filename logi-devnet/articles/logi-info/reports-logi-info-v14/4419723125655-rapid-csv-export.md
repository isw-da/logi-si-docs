---
title: "Rapid CSV Export"
id: 4419723125655
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723125655-Rapid-CSV-Export
updated_at: 2022-07-17T02:23:41Z
---

# Rapid CSV Export

# Rapid CSV Export

The Rapid CSV Export option provides a built-in capability for both the Data Table and Analysis Grid, running off the datalayer. This feature is available for Consumer and Self-Service users who export tabular data in CSV format for further analysis outside of the context of the Info application. The rapid export option greatly improves the performance of exporting large data, as compared to the regular CSV export option. To review a detailed list of the differences between the native CSV and rapid CSV export, see [Exporting to CSV File](https://devnet.logianalytics.com/hc/en-us/articles/4419722898711-Exporting-to-CSV-File).

To export your data using the Rapid CSV Export, access your Data Table in the Analysis Grid and select the **export** icon.

Then, select **CSV** from the drop-down list:

![](https://devnet.logianalytics.com/hc/article_attachments/7522806303255/select_csv_export.png)

Your download will appear in the bottom of the web browser, or may open automatically, depending on your machine's configuration.

The Data Table displays in CSV format in whichever program you have set to open with the download. The example below shows the exported CSV file in Excel:

![](https://devnet.logianalytics.com/hc/article_attachments/7522806324119/csv_export.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 The report title, grouping, summary, and filter information display on the export results, if your application has been configured for it.

The availability of different types of exports is under developer control. In Info Studio, you can set the new attribute on the Target.CSV element called "ExportDataPreference" (Formatted, Empty {default}, or Rapid ). This preference can be set on a global application level by setting a restricted constant "rdExportDataPreference" to *Rapid*:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820585239/rapid_export.png)

For more information about how to configure your Info application to export to CSV, see [CSV - Exporting Data Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419707568663-CSV-Exporting-Data-Manually).
