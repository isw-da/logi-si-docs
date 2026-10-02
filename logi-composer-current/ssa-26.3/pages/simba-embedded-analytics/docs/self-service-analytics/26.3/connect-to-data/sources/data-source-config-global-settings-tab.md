> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Global Settings Work Areas

Use the Global Settings work areas to configure settings for new visuals for this data source. If you have the **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission to an existing source, you can update these settings as needed.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/global-set-tab-26-2-cmp.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=17adfb0ba5f9850d91c21b226ebc8674" alt="Use this work area to define time bar settings, global filters, and other settings for a source." width="1308" height="727" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/global-set-tab-26-2-cmp.jpg" />

Depending on the connection type or source definition, not all configuration options are available for all data sources.

* [Time Bar Settings](#time-bar-settings)
* [Other Settings](#other-settings)
* [Global Filters](#global-filters)

<h2 id="time-bar-settings">
  Time Bar Settings
</h2>

If time fields are available in this data source, you can adjust the global settings here. The following table describes the time bar settings you can alter for new and existing visuals.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
      <th>New Visuals</th>
      <th>Existing Visuals</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Time Bar</td>

      <td>
        All settings for Time Bar Settings here are disabled if the Time Bar toggle is disabled. Enable to allow setting of time bar related values.

        <br />

        * Enable to allow setting of time bar related global settings here, and to enable the time bar on visuals by default. Users can disable the time bar for individual visuals as needed.
        * Disable to prevent setting of time bar related global settings here, and to disable the time bar on visuals by default. Users can enable the time bar for individual visuals as needed.
      </td>

      <td>Yes</td>
      <td>No</td>
    </tr>

    <tr>
      <td>Default Time Attribute</td>
      <td>Select an available time field to use, by default, for new visuals. Options vary based on the time field in your data source.</td>
      <td>Yes</td>
      <td>No</td>
    </tr>

    <tr>
      <td>Playback</td>
      <td>Enable to allow playback for optimal time fields, such as time fields with indexes, partitions, or other query optimizations from your data source.</td>
      <td>Yes</td>
      <td>No</td>
    </tr>

    <tr>
      <td>Time Range</td>
      <td>Define the time range for the time bar. By default, the time range runs from the end of the data set minus one hour to the end of the data set as dynamic time. If you do not want to use the default, you can select a preset value from **Presets...** or design your own Conditions for the From and To fields. See [Configure Time Bar Defaults](#configure-time-bar-defaults).</td>
      <td>Yes</td>
      <td>No</td>
    </tr>

    <tr>
      <td>Live Mode</td>
      <td>Enable to allow live stream updates from data sources that are not file-based data sources. When enabled, you can adjust live settings and enable a delay as needed.</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>Refresh Rate</td>

      <td>
        Use Refresh Rate to specify the data refresh rate of the Default Time Attribute for this data source. The time granularity for this refresh rate is defined as Granularity on the [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab.

        <br />

        For information about using the REST API to identify and modify refresh rates, see [Configure Data Source Refresh Rates Using the API](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2#configure-data-source-refresh-rates-using-the-api).
      </td>

      <td>Yes</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>Delay By</td>
      <td>Use Delay By to specify the delay time when playing data in live mode.</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>Prefer Sharpening</td>
      <td>Enable to allow Data Sharpening for data sources that support it.</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>Max Queries</td>
      <td>When Prefer Sharpening is enabled, you can use this slider to adjust the maximum number of queries for data. See [Enable Data Sharpening and Configure Its Defaults](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-sharpening-ov#enable-data-sharpening-and-configure-its-defaults)</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>

<h2 id="other-settings">
  Other Settings
</h2>

The following table describes the other settings you can alter for new and existing visuals.

| Setting | Description | New Visuals | Existing Visuals |
| - | - | - | - |
| Tile Provider | Select to define a default tile provider. Supported providers include OpenStreetMap, MapQuest, and MapBox. | Yes | No |
| Tile Provider URL | Provided for OpenStreetMap only. Use the default URL, or customize with your own URL. | Yes | No |
| API Key | Enter the API key for your tile provider, if needed. | Yes | No |
| Country Format | Select a country format for visuals: **Long Name**, **Formal English Name**, **ISO 2 Symbols**, or **ISO 3 Symbols**. | Yes | No |
| Enable Text Search | Enable to allow text search. Available only for supported data sources, such as ElasticSearch/Cloudera sources. See [Configure Search Box Defaults](#configure-search-box-defaults). | Yes | Yes |
| Alternative Calendars Settings | Select an available alternative calendar to use for this source. Deselect a calendar to prevent the creation of new derived fiscal time fields based on a calendar. See [Fiscal Calendars](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#fiscal-calendars). | Yes | Yes |

<h2 id="global-filters">
  Global Filters
</h2>

The following table describes the filter settings you can alter for new visuals. If you define initial filters, you can increase the performance of new visuals the first time you load them.

| Setting | Description |
| - | - |
| Add Filter | Select **Add Filter** to add a filter to new visuals created using this source. |
| Nest Filter | Select the Nest Filters (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/nest-filters-710.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=bcf149ec11047cf5a2f796672c839830" alt="" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/nest-filters-710.png" />) button to nest your filters for new visuals created using this source. |

<h2 id="cache-tab">
  Cache Tab
</h2>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

Self-Service Analytics maintains data source metadata and, optionally, a cached result set of the data and statistics from the data store for each data source configuration you define.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-25-4.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=18f80d804456cf9cda6e7be6e1e8aefb" alt="use this work area to define data cache settings, statistics stash settings, schedule refresh settings, enable caching for fields, or manually refresh one or more fields." width="1531" height="738" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cache-tab-25-4.png" />

Use the Cache tab to:

* Enable or disable **Data Cache** for this source. Any change you make to this section is automatically saved.

  * When you enable Data Cache, Self-Service Analytics caches query results and common cached data for multiple visuals that use this source.
  * When disabled, this metadata is not cached.

* Enable or disable **Statistics Cache** for this source. Any change you make to this section is automatically saved.

  * When you enable Statistics Cache, field metadata, such as minimum, maximum, and distinct values numbers are cached. You can enable and disable caching for individual field statistics when enabled.
  * When disabled, the **Fields Statistics Configuration** work area is disabled. If you disable this after setting up **Schedule Refresh Settings**, your schedule is deleted.

* Manage caching for individual fields in the **Field Statistics Configuration** work area. Any change you make to this section is automatically saved.

  * You can enable or disable caching for each field, scheduled refreshing for each field, or manually refresh each field if needed. Fields that include a statistics override that prevents refreshing are indicated by an exclamation point in a triangle.

    <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/no-refresh-data-cache-tab-710.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e733545de5d3e75bb1876ef8ecf3c0d0" alt="" width="1396" height="381" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/no-refresh-data-cache-tab-710.png" />

* Use **Schedule Refresh Settings** to define Periodic or Advanced refreshing of fields with **Schedule Refresh** enabled. If you disable Schedule Refresh Settings, any schedule you had set up previously is deleted.

* You can perform several bulk functions related to caching using menus in the header of the fields table.

  * Select the Enable Cache menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/google-api-console-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a7d543b9f56233fb502e89d6e42dafe" alt="" width="20" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/google-api-console-menu.png" />) button to quickly enable or disable caching for all fields.
  * Select the Schedule Refresh menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/google-api-console-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a7d543b9f56233fb502e89d6e42dafe" alt="" width="20" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/google-api-console-menu.png" />) button to quickly enable or disable scheduled refreshing for all fields. This is available only if you have enabled **Schedule Refresh Settings** and defined a frequency.
  * Select the refresh (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f7b35df88bf64ec08419feda8123e37a" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png" />) button for Manual Refresh to trigger a manual refresh for all fields.

You can refresh the entire data source, all the fields in a data source, or select fields in a data source. For more information, see:

* [Trigger Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#trigger-refresh-jobs)
* [Set Up a Data Source Refresh Job](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#set-up-a-data-source-refresh-job)
* [Review Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console)

<h2 id="configure-search-box-defaults">
  Configure Search Box Defaults
</h2>

The search box is available for [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr), [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search), and [Elasticsearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) data sources and is enabled by default for visuals created using these sources. It allows you to enter keywords to quickly filter the data. You can disable the search box, if needed, in the data source configuration.

### Disable the Search Box

**Disable the search box**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission for this source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. Select the appropriate data source configuration to edit it, then access the Global Settings tab of the data source.

4. Toggle off **Enable Text Search** in the **Other Settings** work area if you want to disable the text search option for new and existing visuals.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/enable-text-search-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=92f9edc82e0510587e6674bd68c27b71" alt="" width="351" height="334" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/enable-text-search-710.png" />

<Note>
  The availability of this setting depends on the data source you have selected. The Search feature is available for [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr), [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search), and [Elasticsearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) data sources.
</Note>

### Enable the Search Box

**Enable the search box**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission for this source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. Select the appropriate data source configuration to edit it, then access the Global Settings tab of the data source.

4. Toggle on **Enable Text Search** in the **Other Settings** work area if you want to enable the text search option for new and existing visuals.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/disable-text-search-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=380d69c1634b0ea3e07a206c348d4595" alt="" width="351" height="334" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/disable-text-search-710.png" />

<Note>
  The availability of this setting depends on the data source you have selected. The Search feature is available for [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr), [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search), and [Elasticsearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) data sources.
</Note>

<h2 id="configure-time-bar-defaults">
  Configure Time Bar Defaults
</h2>

The time bar feature is available for all visual types. When enabled, it appears at the bottom of a dashboard. You can use the time bar to filter the data in your visuals by a specified time attribute. If more than one data source is used for visuals on a dashboard, the time bar shown on the dashboard depends on the visual that is selected in the dashboard. For information on using the time bar on the dashboard, see [Use the Time Bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar).

You can set time bar defaults for data sources used in your Self-Service Analytics environment. These defaults are specified in data source configurations and are applied to visuals that are created using the data sources. Specifically, you can specify:

* The default time field used for the time bar.
* Whether playback and live mode should be available time bar features.
* The default time range used for the time bar.

**Specify default time bar settings for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission for this source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. Select the appropriate data source configuration to edit it, then access the Global Settings tab of the data source.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-settings-full-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=79f6b7d55fb35a27b8aa51ffc7ed27d4" alt="" width="388" height="513" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-settings-full-710.png" />

4. Enable Time Bar in Time Bar Settings. This allows you to edit all available time bar settings for new visuals. See Global Settings Work Areas

5. Select the default time field to use in the **Default Time Attribute** box.

   The attribute you select is used as default and is displayed on the time bar after you create and open a new visual:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/default-time-attr-710.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=3d6ba264c0abe23b4fc558fbef1d26df" alt="" width="612" height="235" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/default-time-attr-710.png" />

   If you select a **Default Time Attribute** that has the time zone information disabled, only the field name appears on the time bar and in this work area.

6. If the time attribute you select is *playable*, the **Enable Playback** and **Enable Live Mode** settings can be changed.

   Live mode and historical playback (also know as Data DVR) allow you to get the most from data sources using connectors that support live mode and playback (see [Live Mode and Historical Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback)). The only difference between live mode and historical playback is the time range that is selected:

   * Live mode refreshes field data on your visuals for fields that are indexed as playable. In live mode, your data plays forever without an end date.
   * Historical playback (Data DVR) shows the historical record of field data for fields that are indexed as playable. Playback can show up to the last moment before the current period in your data.

   Live mode and historical playback require an index or partition field. The data store should be capable of receiving new or updated data, that is, data that is not static like flat files. If the data store does not support indexing or partitioning, then live mode and historical playback are not available. For most data stores, indexing is the default. For more information about the requirements for playback, see [Live Mode and Historical Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback).

   * Enable the **Playback** toggle to show the Play button (Data DVR functionality) on the time bar.
   * Enable the **Live Mode** toggle to enable playing data in live mode.

   If you enable **Live Mode**, **Playback** is also enabled by default.

7. Use the **Time Range** **From** and **To** boxes to specify the default time bar range.

   You can set the range in static time or dynamic time, or use preset ranges provided with Self-Service Analytics.

   * Select **Static Time** or **Dynamic Time** in the **fx** drop-down menu.

     <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-range-types-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=402b8ad8bbec131042145646a5e63378" alt="" width="394" height="150" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-range-types-710.png" />

     If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times:

     <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-static-range-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e153a4c521a9274914d072100dc6dde9" alt="" width="405" height="377" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-static-range-710.png" />

     If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of data** and **End of data** automatically. Use the boxes to select different dynamic From and To times:

     <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-dynamic-range-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=a202921d01343886123bfb1920d2887c" alt="" width="422" height="316" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-dynamic-range-710.png" />

   * Alternatively, select **Presets...** to fill the **From** and **To** boxes with predefined time ranges provided by Self-Service Analytics:

     <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-presets-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=415dbeb3f4140aa9266d2c23e56697ee" alt="" width="230" height="352" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/time-bar-presets-710.png" />

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [Preset Time Ranges](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#preset-time-ranges).

8. If you enable live mode for a data source (**Enable Live Mode** checkbox), you can set the refresh rate and delay time. The time bar defaults expand to show these settings.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/live-mode-options-710.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=8d8881c3f906c6cd210ef757a29ce5ea" alt="" width="386" height="174" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/source-creation/live-mode-options-710.png" />

   * Use the **Refresh Rate** box to specify the data refresh rate for the data source. The time granularity for the time field's refresh rate is defined in the Settings sidebar menu on the [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab of the [data source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

     For information about using the REST API to identify and modify refresh rates, see [Configure Data Source Refresh Rates Using the API](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2#configure-data-source-refresh-rates-using-the-api).

   * Use the **Delay By** box to specify the delay time when playing data in live mode.

9. When your changes are complete, select **Save Settings** to save your changes.

<h2 id="how-self-service-analytics-caches-data">
  How Self-Service Analytics Caches Data
</h2>

Self-Service Analytics uses a visual cache to enhance performance in scenarios where large numbers of users are concurrently viewing the same shared visuals. A metadata cache is also used to store field statistics. This cached data is shared between users only if they have the same data access permissions and security context.

Caching is enabled by default for all data sources. Self-Service Analytics does not re-query the data source for data unless you manually clear the cache, or define a refresh schedule. See [Cache Tab](#cache-tab) and [Trigger Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#trigger-refresh-jobs).

Available cache settings and options include:

* **Data Cache**: Self-Service Analytics caches query results and common cached data for multiple visuals that use this source. When you create a visual that uses this source, the first data request is sent to the Self-Service Analytics cache. Self-Service Analytics returns the cached data, if available.

  If the data is not available in the cache, Self-Service Analytics next queries the data source. The results are returned and stored in the cache, and the visual displays the returned data.

* **Statistics Cache**: When enabled, field metadata, such as minimum, maximum, and distinct values numbers are cached. This toggle also controls the availability of the Field Statistics Configuration option and scheduled refresh settings.

* **Field Statistics Configuration**: When enabled, you can enable or disable caching and scheduling for individual fields, or manually refresh the cached data for individual fields. Fields that include a statistics override that prevents refreshing are indicated by an exclamation point in a triangle.

* **Schedule Refresh Settings**: Enable and define Periodic or Advanced refreshing of fields with **Schedule Refresh** enabled. If you disable Schedule Refresh Settings, any schedule you had set up previously is deleted.

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](#cache-tab).
</Note>

You can refresh the entire data source, all the fields in a data source, or select fields in a data source. For more information, see:

* [Clear the Cache for a Data Source Configuration](#clear-the-cache-for-a-data-source-configuration)
* [Disable Data Caching for a Data Source](#disable-data-caching-for-a-data-source)
* [Trigger Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#trigger-refresh-jobs)

<Note>
  You can force Self-Service Analytics to bypass the cache and to query the underlying data source by selecting **Refresh All** from a Self-Service Analytics dashboard menu.
</Note>

<h2 id="disable-data-caching-for-a-data-source">
  Disable Data Caching for a Data Source
</h2>

The Self-Service Analytics data cache is a temporary storage area containing the aggregated data from your data sources. Two caches are supported: the visual (visual data) cache and the metadata (field statistics) cache. By default, caching is enabled for all data sources using both caches. However, you can disable all caching if your data source is constantly being updated, or you do not want to allocate the required RAM or if the performance of your data source is so high you do not need to store the aggregated queries.

**Disable data caching**

1. Make sure you are logged in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the **Source** card on your home page or **Data Sources** from the main menu. The [Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit. The Source Creation work area opens.

4. Select the **Cache** tab. All the fields from your data source are listed.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=e97e1f8ea17f8cf95d2a66646841a60f" alt="use this work area to change settings for data cache, statistics cache, schedule refresh settings, or adjust individual cache and refresh settings" width="1075" height="782" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/cache-tab-262-02.png" />

5. Disable (toggle off) **Data Cache**. Data caching is disabled for the data source configuration. Data will be freshly loaded into the Self-Service Analytics cache the next time it is requested from the data source.

6. Optionally, Disable (toggle off) **Statistics Cache**. Field metadata caching is disabled for the data source configuration. Data will be freshly loaded into the cache the next time it is requested from the data source.

   If you have [set up refresh jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#set-up-a-data-source-refresh-job) for this data source, a warning appears that the jobs are disabled and the schedule deleted for this data source. Select **Ok** to continue disabling Statistics Cache and delete the schedule.

7. Exit the source data configuration when you have finished making your changes.

<h2 id="clear-the-cache-for-a-data-source-configuration">
  Clear the Cache for a Data Source Configuration
</h2>

You can manually clear the cache for a data source configuration if you are a user granted the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) or a user with **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source. Both the visual (visual data) cache and the metadata (field statistics) cache are cleared.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Clear the cache for a data source configuration**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. In the table on the Sources page, locate the row displaying the data source configuration with the cache you want to clear.

4. Select the Clear Cache button in the **Actions** column of the table. The Cache Cleanup work area opens.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cache-cleanup-data-source-710.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=49568b6d3ffeaf0f229a3d8625b25c35" alt="cache cleanup dialog box" width="388" height="225" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cache-cleanup-data-source-710.png" />

5. If available, select **[Data Cache](#cache-tab)** to clear the query results from visuals.

6. If available, select **[Statistics Cache](#cache-tab)** to clear the cache of field statistics data such as min, max, and distinct values numbers.

   <Note>
     Control the availability of caching options on the [Cache tab](#cache-tab) of a data source.
   </Note>

7. Select **Ok** to clear your selected caches for this data source. The data is freshly loaded into the Self-Service Analytics cache the next time it is requested from the data source. For more information about data caching or to disable it, see [How Self-Service Analytics Caches Data](#how-self-service-analytics-caches-data).

<Note>
  If a [Custom Range](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#filter-values-panel-fields-tab) has been defined for a field, the minimum and maximum fields used in filters remains unchanged by the action of refreshing the source data.
</Note>

<Note>
  You can force Self-Service Analytics to bypass and update the cache to query the underlying data source by selecting **Refresh** from a Self-Service Analytics dashboard menu.
</Note>
