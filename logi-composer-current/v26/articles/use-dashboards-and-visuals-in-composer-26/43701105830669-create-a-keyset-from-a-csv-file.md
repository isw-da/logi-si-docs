---
title: "Create a Keyset From a CSV\u00a0File"
id: 43701105830669
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105830669-Create-a-Keyset-From-a-CSV-File
updated_at: 2026-05-29T14:10:40Z
---

# Create a Keyset From a CSV File

# Create a Keyset From a CSV File

You can create a keyset from a CSV file. The CSV file must meet the following requirements:

* The data values in the file must be in a single column.
* The file must be UTF-8 formatted.
* The file cannot contain more than 1000 rows.
* The data type of the CSV values (number, time, attribute, etc.) must match the data type of the field to which the CSV keyset data will be applied.

**Create a keyset from a CSV file**

1. Review a visual in the Visual Gallery or in a dashboard.
2. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243219111437)) or select **Settings** from the [visual menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243207695501)) and then select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243207697037) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243219111437)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears, showing any filters that have been applied.
3. Select **Add Filter**.
4. Select a filter field on the Filter sidebar. Remember that the field data type must match the data type of the CSV data you will upload (for example, if the field is a numeric field, the CSV data must be also be numeric).

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.

     **Note:** 
     If your example uses numeric data, the tabs may vary. See [Set a Numeric Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter).
5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.
6. Select **Upload Keyset Values**. An Upload Keyset Values panel appears in the Filters sidebar allowing you to specify information about the CSV file and the keyset you are creating.

   **Note:** 
   If the upload file contains more records than are allowed by your Composer environment configuration, the keyset will not upload and an error occurs.
7. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of your Composer instance, be sure to enter a unique name.
8. Optionally, enter a description for the keyset in the **Description** box.
9. In the **Choose a file to Add Keyset Values** box, browse for and select the CSV file containing the keyset values you want to upload.

   ![Set your keyset details here, and upload a new keyset if needed](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242464089741 "upload keyset values work area")
10. Select **Upload Keyset** to upload the CSV file for the keyset.

    If the upload occurs successfully, a message displays that the upload was successful and the keyset details appear in the Filter sidebar. The keyset is now available to all users of your Composer instance.
11. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.
