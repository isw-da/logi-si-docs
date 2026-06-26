---
title: "Exporting a Dashboard"
id: 4402537745943
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537745943-Exporting-a-Dashboard
updated_at: 2021-09-15T02:20:55Z
---

# Exporting a Dashboard

# Exporting a Dashboard

You can export your dashboards in a variety of formats. Exported dashboards enable you to share your data with others or in the case of the JSON configuration export, to transfer a dashboard to another Composer environment. Exported dashboard JSON files can only be imported into other Composer environments running the same version. See [*Importing a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537746583-Importing-a-Dashboard).

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) When exporting, be aware that special characters are not supported. If your visual name or the name of the data source contains special characters, you need to update the name before continuing.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) To export a dashboard, you must be an administrator or a user belonging to a group with the **Can Export Dashboards & Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) enabled.

Dashboards can be exported in the following formats:

* PNG Screenshot (as an image)
* PDF file (as an image)
* JSON configuration (for the whole dashboard)

To export a dashboard:

1. On the dashboard, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764029975/dash-export_17x15.png) on the dashboard icon bar. The Export dialog displays.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764030359/export-dashboard_192x131.png)
2. On the Export dialog, select the format for the export.

   * When you select **Screenshot (PNG)**, the PNG file is captured and displays in the Export dialog. Select the PNG image to download it.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406753496343/export-dashboard-png_192x242.png)
   * When you select PDF format, the Export as PDF dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406753496855/export-dashboard-pdf_192x198.png)

     Optionally, specify a header and footer for the PDF. Select **Add Username** to add a user name to the PDF. Select **Add Timestamp** to add a timestamp to the PDF. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753497111/export-dash_195x22.png).
   * When you select **Dashboard Configuration (JSON)** format, the JSON file is automatically downloaded to your computer.
