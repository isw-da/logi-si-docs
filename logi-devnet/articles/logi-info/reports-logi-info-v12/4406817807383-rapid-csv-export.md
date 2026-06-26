---
title: "Rapid CSV Export"
id: 4406817807383
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817807383-Rapid-CSV-Export
updated_at: 2022-04-06T06:08:20Z
---

# Rapid CSV Export

# Rapid CSV Export

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) The Rapid CSV Export option provides a built-in capability for both the Data Table and Analysis Grid, running off the datalayer. This feature is available for Consumer and Self-Service users who export tabular data in CSV format for further analysis outside of the context of the Info application. The rapid export option greatly improves the performance of exporting large data, as compared to the regular CSV export option. To review a detailed list of the differences between the native CSV and rapid CSV export, see [Exporting to CSV File](https://devnet.logianalytics.com/hc/en-us/articles/4406817429271-Exporting-to-CSV-File).

To export your data using the Rapid CSV Export, access your Data Table in the Analysis Grid and select the **Export** icon.

Then, select **CSV** from the drop-down list:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575559319/select_csv_export.png)

Your download will appear in the bottom of the web browser, or may open automatically, depending on your machine's configuration.

The Data Table displays in CSV format in whichever program you have set to open with the download. The example below shows the exported CSV file in Excel:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575559575/csv_export.png)

The availability of different types of exports is under developer control. In Info Studio, you can set the new attribute on the Target.CSV element called "ExportDataPreference" (Formatted, Empty {default}, or Rapid ). This preference can be set on a global application level by setting a restricted constant "rdExportDataPreference" to *Rapid*:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583752855/rapid_export.png)

For more information about how to configure your Info application for Rapid CSV Export, see [CSV - Exporting Data Manually](https://devnet.logianalytics.com/hc/en-us/articles/4406817428119-CSV-Exporting-Data-Manually).
