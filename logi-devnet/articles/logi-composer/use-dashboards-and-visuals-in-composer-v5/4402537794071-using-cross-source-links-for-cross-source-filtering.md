---
title: "Using Cross-Source Links for Cross-Source Filtering"
id: 4402537794071
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537794071-Using-Cross-Source-Links-for-Cross-Source-Filtering
updated_at: 2021-09-15T02:21:32Z
---

# Using Cross-Source Links for Cross-Source Filtering

# Using Cross-Source Links for Cross-Source Filtering

After you have defined cross-source links for a dashboard, you can use them in cross-source filtering. Cross-source filtering allows you to simultaneously apply the same filter across all visuals in your dashboard that use the linked fields. Cross-source filters can be applied from a visual as well as from the time bar.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) Cross-source links must be defined on the dashboard before you can use them in cross-source filtering. See [*Defining Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4402537727383-Defining-Cross-Source-Links).

## Cross-Source Filtering From Visuals

To apply a cross-source filter from a visual on the dashboard:

1. After cross-source links are created, select an area of the visual that uses a cross-source linked field. The [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu) for that area of the visual displays:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763983639/radial-menu_80x80.png)

   **Note:** You cannot create a cross-source filter using the Filters sidebar accessed when you select the filter icon for the dashboard or visual. Filters created in this way apply only to the selected visual. See [*Filter Data*](https://devnet.logianalytics.com/hc/en-us/articles/4402552815383-Filter-Data).
2. Select **Filter** on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu). The Apply filter to dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763984023/apply-filter_163x145.png)

   This dialog lists all the visuals in the dashboard that use data from:

   * The same data source
   * Different data sources with a cross-source linked field for the data you have selected.

   If you choose an area of the visual that does *not* use a cross-source linked field for the filter, only visuals that use data from the same data source show in this dialog.
3. Select the visuals to which you want to apply the filter and select **Apply**. Check **Select All** and select **Apply** to select all of the visuals.

   The cross-source filter is applied to the selected visuals.

## Cross-Source Filtering From The Time Bar

To apply a cross-source filter from the time bar, a cross-source link for time fields in the data sources must first be created. See [*Defining Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4402537727383-Defining-Cross-Source-Links).

To apply a cross-source filter using a time field from the time bar:

1. After cross-source links are created, select the time field in the time bar. The Time Bar dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763984535/time-bar_150x239.png)
2. Select the cross-source linked time field you have defined in the **Time Attribute** section.
3. Select the visuals to which you want to apply the time filter in the **Applies to** section. The **Applies to** section lists all the visuals in the dashboard that use data from:

   * The same data source
   * Different data sources with a cross-source linked field for the data you have selected.
4. Use the time bar to filter all the visuals that use the selected cross-linked time attribute.
