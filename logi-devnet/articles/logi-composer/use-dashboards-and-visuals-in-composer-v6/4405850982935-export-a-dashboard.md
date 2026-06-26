---
title: "Export a Dashboard"
id: 4405850982935
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard
updated_at: 2021-09-21T01:27:45Z
---

# Export a Dashboard

# Export a Dashboard

You can export your dashboards in a variety of formats. Exported dashboards enable you to share your data with others or in the case of the JSON configuration export, to transfer a dashboard to another Composer environment. Exported dashboard JSON files can only be imported into other Composer environments running the same version. See [*Import a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850983831-Import-a-Dashboard).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) When exporting, be aware that special characters are not supported. If your visual name or the name of the data source contains special characters, you need to update the name before continuing.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) To export a dashboard, you must be an administrator or a user belonging to a group with the **Can Export Dashboards & Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled.

Dashboards can be exported in the following formats:

* PNG Screenshot (as an image)
* PDF file (as an image)
* JSON configuration (for the whole dashboard). When you select this format, [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) settings are also exported with the other dashboard settings. This ensures that the exported dashboard can be imported with the same interactivity profile.

To export a dashboard:

1. On the dashboard, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743754519/dash-export.png) on the dashboard icon bar. A drop-down menu appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747441303/export-dashboard-menu_192x154.png)
2. Select the file format to which you want the dashboard exported.

   * When you select **Screenshot (PNG)**, the PNG file is created and downloaded.
   * When you select **PDF** format, the Export as PDF dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406743883287/export-dashboard-pdf_384x267.png)

     Optionally, specify a header and footer for the PDF. Slide the **Add Username** switch on (to the right) to add a user name to the PDF. Slide the **Add Timestamp** switch on (to the right) to add a time stamp to the PDF. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743721495/export-dash_90x29.png).
   * When you select **Configuration (JSON)** format, the JSON file is automatically downloaded to your computer.
