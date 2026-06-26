---
title: "Configure Time Bar Defaults"
id: 43701080606477
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults
updated_at: 2026-05-29T14:10:59Z
---

# Configure Time Bar Defaults

# Configure Time Bar Defaults

The time bar feature is available for all visual styles. When enabled, it appears at the bottom of a dashboard. You can use the time bar to filter the data in your visuals by a specified time attribute. If more than one data source is used for visuals on a dashboard, the time bar shown on the dashboard depends on the visual that is selected in the dashboard. For information on using the time bar on the dashboard, see [Use the Time Bar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210703629-Use-the-Time-Bar).

You can set time bar defaults for data sources used in your Composer environment. These defaults are specified in data source configurations and are applied to visuals that are created using the data sources. Specifically, you can specify:

* The default time field used for the time bar.
* Whether playback and live mode should be available time bar features.
* The default time range used for the time bar.

**Specify default time bar settings for a data source configuration**

1. Log in as a user with the **Administer Sources**[privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or write permission for this source.
2. Select **Sources**on the UI menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243252525069)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. Select the appropriate data source configuration to edit it, then access the [Global Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085233549-Global-Settings-Tab) tab of the data source.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242592828301)
4. Enable Time Bar in Time Bar Settings. This allows you to edit all available time bar settings for new visuals. See [Global Settings Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085233549-Global-Settings-Tab)
5. Select the default time field to use in the **Default Time Attribute** box.

   The attribute you select is used as default and is displayed on the time bar after you create and open a new visual:

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242582009101)

   If you select a **Default Time Attribute** that has the time zone information disabled, only the field name appears on the time bar and in this work area.
6. If the time attribute you select is *playable*, the **Enable Playback** and **Enable Live Mode** settings can be changed.

   Live mode and historical playback (also know as Data DVR) allow you to get the most from data sources using connectors that support live mode and playback (see [Live Mode and Historical Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback)). The only difference between live mode and historical playback is the time range that is selected:

   * Live mode refreshes field data on your visuals for fields that are indexed as playable. In live mode, your data plays forever without an end date.
   * Historical playback (Data DVR) shows the historical record of field data for fields that are indexed as playable. Playback can show up to the last moment before the current period in your data.

   Live mode and historical playback require an index or partition field. The data store should be capable of receiving new or updated data, that is, data that is not static like flat files. If the data store does not support indexing or partitioning, then live mode and historical playback are not available. For most data stores, indexing is the default. For more information about the requirements for playback, see [Live Mode and Historical Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback).

   * Enable the **Playback** toggle to show the Play button (Data DVR functionality) on the time bar.
   * Enable the **Live Mode** toggle to enable playing data in live mode.

   If you enable **Live Mode**, **Playback** is also enabled by default.
7. Use the **Time Range****From** and **To** boxes to specify the default time bar range.

   You can set the range in static time or dynamic time, or use preset ranges provided with Composer.

   * Select **Static Time** or **Dynamic Time** in the **fx** drop-down menu.

     ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242609308045)

     If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times:

     ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242593257101)

     If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of data** and **End of data** automatically. Use the boxes to select different dynamic From and To times:

     ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242565093389)
   * Alternatively, select **Presets...** to fill the **From** and **To** boxes with predefined time ranges provided by Composer:

     ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242609849229)

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [Preset Time Ranges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144196237-Preset-Time-Ranges).
8. If you enable live mode for a data source (**Enable Live Mode** checkbox), you can set the refresh rate and delay time. The time bar defaults expand to show these settings.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242593736333)

   * Use the **Refresh Rate** box to specify the data refresh rate for the data source. The time granularity for the time field's refresh rate is defined in the Settings sidebar menu on the [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab of the [data source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources).

     For information about using the REST API to identify and modify refresh rates, see
     [Configure Data Source Refresh Rates Using the API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701023076109-Configure-Data-Source-Refresh-Rates-Using-the-API).
   * Use the **Delay By** box to specify the delay time when playing data in live mode.
9. When your changes are complete, select **Save Settings** to save your changes.
