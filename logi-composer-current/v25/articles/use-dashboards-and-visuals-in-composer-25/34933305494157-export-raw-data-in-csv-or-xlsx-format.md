---
title: "Export Raw Data in CSV or XLSX Format"
id: 34933305494157
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933305494157-Export-Raw-Data-in-CSV-or-XLSX-Format
updated_at: 2026-05-26T22:08:44Z
---

# Export Raw Data in CSV or XLSX Format

# Export Raw Data in CSV or XLSX Format

When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format. When you export raw data to csv format, both numeric and date fields are exported as strings..

**Export raw data in CSV format**

1. Select **Export** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). Select an export option for your visual.
2. Select a file format on the submenu, **Raw Data > CSV**.
3. The Export as CSV dialog opens.

   ![Enter csv options here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166918238989 "Export as CSV work area")
4. Accept or change the default settings:

   * Accept or change the file name.
   * Specify the **Number of Records** to include in the export. The default is 1,000.

     **Note:** 
     The number of records you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).
   * Select a field to sort the data included in the export. The default for **Sort by** field is none. Depending on the field type selected, you have sort order options you can use to organize your data.
5. Select **Export**. Logi Composer prepares a CSV file downloaded by your browser.

**Note:** 
The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).

**Export raw data in XLSX format**

1. Select **Export** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). Select an export option for your visual.
2. Select a file format on the submenu, **Raw Data > XLSX**.
3. The Export as XLSX dialog opens.

   ![Enter XLSX options here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166934152845 "Export as XLSX work area")
4. Accept or change the default settings:

   * Accept or change the file name.
   * Specify the **Number of Records** to include in the export. The default is 1,000.

     **Note:** 
     The number of records you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).
   * Select a field to sort the data included in the export. The default for **Sort by** field is none. Depending on the field type selected, you have sort order options you can use to organize your data.
   * Select **Add Time Bar filter description to exported file** to include in the export.
   * Select **Add Visual filter description to exported file** to include in the export.
5. Select **Export**. Logi Composer prepares an XLSX file downloaded by your browser.

**Note:** 
The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).
