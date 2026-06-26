---
title: "Configure Time Bar Defaults"
id: 4405859324311
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults
updated_at: 2021-09-21T01:28:18Z
---

# Configure Time Bar Defaults

# Configure Time Bar Defaults

The time bar feature is available for all visual styles. When enabled, it appears at the bottom of a dashboard. You can use the time bar to filter the data in your visuals by a specified time attribute. If more than one data source is used for visuals on a dashboard, the time bar shown on the dashboard depends on the visual that is selected in the dashboard. For information on using the time bar on the dashboard, see [*Use the Time Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar).

You can set time bar defaults for data sources used in your Composer environment. These defaults are specified in data source configurations and are applied to visuals that are created using the data sources. Specifically, you can specify:

* The default time field used for the time bar
* Whether playback and live mode should be available time bar features
* The default time range used for the time bar.

To specify default time bar settings for a data source configuration:

1. Make sure you are logged in as a Composer administrator or as a user assigned to a group that can edit data source configurations.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the table on the Sources page, locate and select the data source configuration you want to edit. The data source configuration wizard appears.
4. Select the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) in the data source configuration wizard.
5. Select the **Global Default Settings** bar on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab), if it is not already selected. The time bar settings appear on the right side of the tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743827351/time-bar-defaults_288x336.png)
6. In the **Time Attribute** box, select the default time field that should be used for the time bar. If you do not want the time bar to be enabled by default, select **None (Time Bar is Off)**. You can always enable and disable the time bar on the dashboard later.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743827607/time-attribute_206x128.png)

   The attribute you select is used as the default and is displayed on the time bar after you open the visual:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743830039/default-time-attr_384x236.png)
7. If the time attribute you select is *playable*, the **Enable Playback** and **Enable Live Mode** settings can be changed.

   Live mode and historical playback (also know as Data DVR) allow you to get the most from data sources using connectors that support live mode and playback (see [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback)). The only difference between live mode and historical playback is the time range that is selected:

   * Live mode refreshes field data on your visuals for fields that are indexed as playable. In live mode, your data plays forever without an end date.
   * Historical playback (Data DVR) shows the historical record of field data for fields that are indexed as playable. Playback can show up to the last moment before the current period in your data.

   Live mode and historical playback require an index or partition field. The data store should be capable of receiving new or updated data, that is, data that is not static like flat files. If the data store does not support indexing or partitioning, then live mode and historical playback are not available. For most data stores, indexing is the default. For more information about the requirements for playback, see [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback).

   * Select the **Enable Playback** checkbox to show the Play button (Data DVR functionality) on the time bar.
   * Select the **Enable Live Mode** checkbox to enable playing data in live mode.

   Note that if you select **Enable Live Mode**, **Enable Playback** is selected also, by default.
8. If you enable live mode for a data source (**Enable Live Mode** checkbox), you can set the refresh rate and delay time. The time bar defaults expand to show these settings.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743831319/live-mode-options_288x180.png)

   * Use the **Refresh Rate** box to specify the data refresh rate for the data source. The time granularity for the time field's refresh rate is defined in the **Configure** column on the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab of the [data source configuration wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).

     For information about using the REST API to identify and modify refresh rates, see
     [*Configure Data Source Refresh Rates Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4405850880919-Configure-Data-Source-Refresh-Rates-Using-the-API).
   * Use the **Delay By** box to specify the delay time when playing data in live mode.
9. Use the **From** and **To** boxes to specify the default time bar range.

   You can set the range in static time or dynamic time, or use preset ranges provided with Composer.

   * Select **Static Time** or **Dynamic Time** in the **fx** drop-down menu.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406747397399/time-bar-range-types_288x167.png)

     If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times:

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406743831575/time-bar-static-range_192x240.png)

     If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of data** and **End of data** automatically. Use the boxes to select different dynamic from and to times:

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406743832087/time-bar-dynamic-range_288x193.png)
   * Alternatively, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747424791/presets-btn.png) to fill the **From** and **To** boxes with predefined time ranges provided by Composer:

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406743832983/time-bar-presets_192x341.png)

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [*Preset Time Ranges*](https://devnet.logianalytics.com/hc/en-us/articles/4405851144983-Preset-Time-Ranges).
10. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833239/save-white-btn.png) to save the data source configuration and close the wizard.
