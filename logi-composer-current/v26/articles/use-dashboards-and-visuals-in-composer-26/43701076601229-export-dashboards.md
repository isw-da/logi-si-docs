---
title: "Export  Dashboards"
id: 43701076601229
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards
updated_at: 2026-05-29T14:11:19Z
---

# Export  Dashboards

# Export Dashboards

You can export your dashboards in a variety of formats. Exported dashboards enable you to share your data with others. JSON configuration exports allow you to transfer a dashboard to another Composer environment. See [Import Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards).

**Note:** 
Special characters are not supported for exports. If your visual name or the name of the data source contains special characters, change the name before continuing.

**Note:** 
To export a dashboard, you must be a user belonging to a group with the **Export Dashboards** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

Dashboards can be exported in the following formats:

* PNG Screenshot (as an image).
* PDF file (as an image).
* JSON configuration (for one or more entire dashboards). JSON exports include [dashboard interactivity profile](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076696717-Control-How-Users-Interact-With-a-Dashboard) settings to allow import of the same interactivity profile.
* XLSX format - as a spreadsheet with Raw Data or Visual Data. Each visual is included on its own sheet.

**Export a dashboard**

1. On the dashboard, select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243289251597) on the dashboard icon bar. A drop-down menu appears.

   ![Select how you want your dashboard data exported](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242678390029 "Export Dashboard Menu")
2. Select an export file format.

   * When you select **Screenshot (PNG)**, Logi Composer creates a PNG file. This is downloaded to your browser.
   * When you select **PDF** format, the Export as PDF dialog appears.

     ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242698669325)

     Optionally, specify a header and footer for the PDF. Slide the **Add Username** switch on (to the right) to add a user name to the PDF. Slide the **Add Timestamp** switch on (to the right) to add a time stamp to the PDF. Then select **Export**.
   * When you select **Configuration (JSON)** format, the JSON file is automatically downloaded to your browser.
   * When you select **Data (XLSX) > Raw Data** or **Data (XLSX) > Visual Data** format, the XLSX file is automatically downloaded to your browser.

**Export multiple dashboards**

1. Log in as a user with the [**Export Dashboards** privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference#Export_Dashboards). Open the Library to view a list of the dashboards you can access.
2. Select to export one or more dashboards by selecting the checkbox for a dashboard to export. The **Export Selected Items** button becomes active.
3. Select **Export Selected Items**. You browser downloads the selected items in JSON format, placing them in the location you select or the default location for your browser downloads.

Dashboards exported using the export API can include source cache settings for the data and statistics caches in the payload.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
