---
title: "Global Settings Tab"
id: 43701085233549
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085233549-Global-Settings-Tab
updated_at: 2026-05-29T14:11:01Z
---

# Global Settings Tab

# Global Settings Tab

Use the Global Settings tab to configure settings for new visuals for this data source. If you have the **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or write permission to an existing source, you can update these settings as needed.

**Note:** In this release, the user interface and workflows have changed from previous releases.

![Use this work area to define time bar settings, global filters, and other settings for a source.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242615047053 "The Global Settings tab")

Depending on the connection type or source definition, not all configuration options are available for all data sources.

* [Time Bar Settings](#Time)
* [Other Settings](#Other)
* [Global Filters](#Global)

## Time Bar Settings

If time fields are available in this data source, you can adjust the global settings here. The following table describes the time bar settings you can alter for new and existing visuals.

| Setting | Description | New Visuals | Existing Visuals |
| --- | --- | --- | --- |
| Time Bar | All settings for Time Bar Settings here are disabled if the Time Bar toggle is disabled. Enable to allow setting of time bar related values.   * Enable to allow setting of time bar related global settings here, and to enable the time bar on visuals by default. Users can disable the time bar for individual visuals as needed. * Disable to prevent setting of time bar related global settings here, and to disable the time bar on visuals by default. Users can enable the time bar for individual visuals as needed. | Yes | No |
| Default Time Attribute | Select an available time field to use, by default, for new visuals. Options vary based on the time field in your data source. | Yes | No |
| Playback | Enable to allow playback for optimal time fields, such as time fields with indexes, partitions, or other query optimizations from your data source. | Yes | No |
| Time Range | Define the time range for the time bar. By default, the time range runs from the end of the data set minus one hour to the end of the data set as dynamic time. If you don't want to use the default, you can select a preset value from **Presets...** or design your own Conditions for the From and To fields. See [Configure Time Bar Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults). | Yes | No |
| Live Mode | Enable to allow live stream updates from data sources that are not file-based data sources. When enabled, you can adjust live settings and enable a delay as needed. | Yes | Yes |
| Refresh Rate | Use Refresh Rate to specify the data refresh rate of the Default Time Attribute for this data source. The time granularity for this refresh rate is defined as Granularity on the [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab.  For information about using the REST API to identify and modify refresh rates, see [Configure Data Source Refresh Rates Using the API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701023076109-Configure-Data-Source-Refresh-Rates-Using-the-API). | Yes | Yes |
| Delay By | Use Delay By to specify the delay time when playing data in live mode. | Yes | Yes |
| Prefer Sharpening | Enable to allow Data Sharpening for data sources that support it. | Yes | Yes |
| Max Queries | When Prefer Sharpening is enabled, you can use this slider to adjust the maximum number of queries for data. See [Enable Data Sharpening and Configure Its Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078143885-Enable-Data-Sharpening-and-Configure-Its-Defaults) | Yes | Yes |

## Other Settings

The following table describes the other settings you can alter for new and existing visuals.

The following table describes the other settings you can alter for new and existing visuals.

| Setting | Description | New Visuals | Existing Visuals |
| --- | --- | --- | --- |
| Tile Provider | Select to define a default tile provider. Supported providers include OpenStreetMap, MapQuest, and MapBox. | Yes | No |
| Tile Provider URL | Provided for OpenStreetMap only. Use the default URL, or customize with your own URL. | Yes | No |
| API Key | Enter the API key for your tile provider, if needed. | Yes | No |
| Country Format | Select a country format for visuals: **Long Name**, **Formal English Name**, **ISO 2 Symbols**, or **ISO 3 Symbols**. | Yes | No |
| Enable Text Search | Enable to allow text search. Available only for supported data sources, such as ElasticSearch/Cloudera sources. See [Configure Search Box Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068987277-Configure-Search-Box-Defaults). | Yes | Yes |
| Alternative Calendars Settings | Select an available alternative calendar to use for this source. Deselect a calendar to prevent the creation of new derived fiscal time fields based on a calendar. See [Fiscal Calendars](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095868941-Fiscal-Calendars). | Yes | Yes |

## Global Filters

The following table describes the filter settings you can alter for new visuals. If you define initial filters, you can increase the performance of new visuals the first time you load them.

| Setting | Description |
| --- | --- |
| Add Filter | Select **Add Filter** to add a filter to new visuals created using this source. |
| Nest Filter | Select the Nest Filters () button to nest your filters for new visuals created using this source. |
