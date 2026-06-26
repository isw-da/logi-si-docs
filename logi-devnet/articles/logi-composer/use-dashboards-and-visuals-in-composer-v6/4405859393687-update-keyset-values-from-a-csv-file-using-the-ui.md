---
title: "Update Keyset Values From a CSV\u00a0File Using the UI"
id: 4405859393687
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859393687-Update-Keyset-Values-From-a-CSV-File-Using-the-UI
updated_at: 2021-09-21T01:29:02Z
---

# Update Keyset Values From a CSV File Using the UI

# Update Keyset Values From a CSV File Using the UI

You can update the values of a keyset from a CSV file. The CSV file must meet the following requirements:

* The data values in the file must be in a single column.
* The file must be UTF-8 formatted.
* The file cannot contain more than 1000 rows.
* The data type of the CSV values (number, time, attribute, etc.) must match the data type of the field to which the CSV keyset data will be applied.

To update keyset values from a CSV file:

1. Review a visual in the Visual Gallery or in a dashboard.
2. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743783191/add-filter-btn_104x25.png) or, if the keyset is already used to filter the visual, select the keyset name. If you select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743783191/add-filter-btn_104x25.png), proceed to the next step. If you select the keyset name, the keyset details are displayed and you should skip to Step 6 of this procedure.
4. Select the filter field on the Filter sidebar. Remember that the field data type must match the data type of the CSV data you will upload (for example, if the field is a numeric field, the CSV data must be also be numeric).

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wild card filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.
5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.
6. Select the keyset to which you want to reupload keyset values. The keyset details appear.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743783447/keyset-details_192x417.png)
7. Select **Reupload Values**. An Upload Keyset Values panel appears in the Filters sidebar allowing you to specify information about the CSV file and the keyset you are updating.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747412503/keyset-jewelry_192x285.png)

   The Name and Description fields are read-only when you update keyset values from a CSV file.
8. In the **Choose a file to Add Keyset Values** box, browse for and select the CSV file containing the updated keyset values you want to upload.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the upload file contains more records than are allowed by the Composer environment configuration, the keyset will not upload and an error occurs.
9. Select **Upload Keyset** to upload the CSV file for the keyset.

   If the upload occurs successfully, a message displays that the upload was successful and the keyset details appear in the Filter sidebar. The keyset is now available to all users of the Composer instance.
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743726487/apply-btn.png) to apply the updated keyset filter to the visual.
