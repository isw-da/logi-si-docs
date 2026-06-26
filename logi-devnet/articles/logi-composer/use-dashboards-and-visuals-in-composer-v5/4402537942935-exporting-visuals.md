---
title: "Exporting Visuals"
id: 4402537942935
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537942935-Exporting-Visuals
updated_at: 2021-09-15T02:23:12Z
---

# Exporting Visuals

# Exporting Visuals

You can export your visuals in a variety of formats, as an image or as data. Exported visuals enable you to share your data with others.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) When exporting, be aware that special characters are not supported. If your visual title, visual name, or the name of the data source contains special characters, you need to update the name before continuing.

Visuals can be exported in the following formats:

* PNG Screenshot (as an image)
* PDF file (as an image)
* Raw data (as a CSV file)
* Aggregate visual data (as a CSV file)

#### Tips and Tricks

* For raw data exports, you can specify the number of records to be exported, sort them by an attribute, and order your records in the output file to download in the CSV format.
  The number of records you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. The default is 100,000 rows. See [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4402537687191-Configuration-Property-Files).
* To control whether a visual can be exported, use the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

To export a visual:

1. Select **Export** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). A submenu appears allowing you to select the format in which you want the visual exported.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763904791/export-visual_192x185.png)
2. Select a format on the submenu.

   * If you select **Screenshot (PNG)**, the screenshot is prepared and automatically downloaded.
   * If you select **PDF**, the Export as PDF dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406763905175/export-visual-pdf_192x138.png)

     Optionally, specify a header and footer for the PDF. Select **Add Username** to add a user name to the PDF. Select **Add Timestamp** to add a timestamp to the PDF. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763905431/export-vis_65x19.png).
   * When you select **Visual Data (CSV)**, the data is prepared and the CSV file is automatically downloaded.
   * When you select **Raw Data (CSV)**, the Export as CSV dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406753441943/export-visual-csv_192x134.png)

     Select the number of records to export in the Number of Records box. The number you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4402537687191-Configuration-Property-Files).

     Optionally, select an attribute in the Sort by box. If you select an attribute, sort order options to sort the raw data in alphabetical or reverse alphabetical option are provided. Select a sort order. The raw data will be sorted by this attribute in the requested sort order in the exported CSV file.

     When finished, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763905687/export-vis_66x20.png). The raw data CSV file is prepared and downloaded.
