---
title: "Update Keyset Values From a CSV\u00a0File Using the UI"
id: 43701121159181
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121159181-Update-Keyset-Values-From-a-CSV-File-Using-the-UI
updated_at: 2026-05-29T14:10:39Z
---

# Update Keyset Values From a CSV File Using the UI

# Update Keyset Values From a CSV File Using the UI

You can update the values of a keyset from a CSV file. The CSV file must meet the following requirements:

* The data values in the file must be in a single column.
* The file must be UTF-8 formatted.
* The file cannot contain more than 1000 rows.
* The data type of the CSV values (number, time, attribute, etc.) must match the data type of the field to which the CSV keyset data will be applied.

**Update keyset values from a CSV file**

1. Review a visual in the Visual Gallery or in a dashboard.
2. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243243399821)) or select **Settings** from the [visual menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243243400589)) and then select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242478586893) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243243399821)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
3. Select **Add Filter** or, if the keyset is already used to filter the visual, select the keyset name. If you select **Add Filter**, proceed to the next step. If you select the keyset name, the keyset details are displayed and you should skip to Step 6 of this procedure.
4. Select the filter field on the Filter sidebar. Remember that the field data type must match the data type of the CSV data you will upload (for example, if the field is a numeric field, the CSV data must be also be numeric).

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.
5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.
6. Select the keyset to which you want to reupload keyset values. The keyset details appear.

   ![Review and edit your keyset values](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242474020109 "Keyset Values Details")
7. Select **Reupload Values**. An Upload Keyset Values panel appears in the Filters sidebar allowing you to specify information about the CSV file and the keyset you are updating.

   ![Set your keyset details here, and upload a new keyset if needed](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242463039629 "upload keyset values work area")

   The Name and Description fields are read-only when you update keyset values from a CSV file.
8. In the **Choose a file to Add Keyset Values** box, browse for and select the CSV file containing the updated keyset values you want to upload.

   **Note:** 
   If the upload file contains more records than are allowed by your environment configuration, the keyset will not upload and an error occurs.
9. Select **Upload Keyset** to upload the CSV file for the keyset.

   If the upload occurs successfully, a message displays that the upload was successful and the keyset details appear in the Filter sidebar. The keyset is now available to all users of this instance.
10. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.
