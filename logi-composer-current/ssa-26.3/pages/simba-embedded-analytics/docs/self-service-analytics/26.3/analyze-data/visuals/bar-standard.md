> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Bar, Line, and Combo Charts

## Standard Bar Charts

Standard bar charts are based on one metric and one or two attributes, as follows:

* **Plain**: Based on 1 metric and 1 attribute
* **Clustered**: Based on 1 metric and 2 attributes
* **Stacked**: Based on 1 metric and 2 attributes
* **100% Stacked**: Based on 1 metric and 2 attributes

Standard bar charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

This topic describes:

* [Configure Settings for a Specific Bar Chart](#configure-settings-for-a-specific-bar-chart)
* [Configure Colors for a Specific Bar Chart](#configure-colors-for-a-specific-bar-chart)
* [Understand Visual Color Condition Thresholds](#understand-visual-color-condition-thresholds)

<h3 id="configure-settings-for-a-specific-bar-chart">
  Configure Settings for a Specific Bar Chart
</h3>

**Change the settings for a specific bar chart**

1. Edit the bar chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Bar Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-std-settings-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=d18f29fc8f5495dc0141f0a9e36c6f75" alt="Adjust settings for your bar chart here" width="391" height="641" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-std-settings-25-1.png" />

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Orientation</td>
         <td>Select Horizontal or Vertical orientation for the bars.</td>
       </tr>

       <tr>
         <td>Cumulative Sum</td>

         <td>
           When enabled, Self-Service Analytics updates the visual to add the previous value to the next value, and both the original and cumulative value for selected items are displayed as a tool tip.

           <br />

           In Bar visuals, this feature is only available when data is grouped by a Time field, and when the Enable Subgroup setting is disabled.
         </td>
       </tr>

       <tr>
         <td>Horizontal Scroll</td>
         <td>Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option.</td>
       </tr>

       <tr>
         <td>Subgroup</td>

         <td>
           Slide on (to the right) the **Enable Subgroup** slider to enable a subgroup style. After enabling a subgroup style, select the style for the chart: **Clustered Bar Chart**, **Stacked Bar Chart**, or **100% Stacked Bar Chart**.

           <br />

           If Subgroups are enabled, you can define the visibility and position of their labels.
         </td>
       </tr>

       <tr>
         <td>Show Group Labels</td>
         <td>Enable to display labels for group values.</td>
       </tr>

       <tr>
         <td>Absolute Values</td>
         <td>Enable to display the data in absolute values.</td>
       </tr>

       <tr>
         <td>Relative Values</td>
         <td>Enable to display the data in relative values.</td>
       </tr>

       <tr>
         <td>Group Labels Position or Subgroup Labels Position</td>
         <td>Select a position option for the group or subgroup labels: **Outside horizontal**, **Outside diagonal**, or **Outside vertical**.</td>
       </tr>

       <tr>
         <td>Style</td>
         <td>Specify the bar thickness for the chart.</td>
       </tr>
     </tbody>
   </table>

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-bar-chart">
  Configure Colors for a Specific Bar Chart
</h3>

**Specify the color settings for a specific bar chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual when Sub-Group is enabled.
           * For gradient color styles, use the legend’s gradient slider to show and hide your data.
         </td>
       </tr>

       <tr>
         <td>Label Color</td>
         <td>The inherited label color from the theme. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>

       <tr>
         <td>Color Metric</td>
         <td>Select the metric that affects the segment color in the visual.</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for the Self-Service Analytics UI.

           <br />

           To override the palette selected by the theme, clear the **Inherit from Theme** checkbox and select a different color palette.
         </td>
       </tr>

       <tr>
         <td>Color Mode</td>
         <td>Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen. Either specific distinct colors will be used or a gradient of colors will be used.</td>
       </tr>

       <tr>
         <td>Threshold Mode</td>

         <td>
           If you select the **Gradient** color mode, this setting cannot be changed.

           <br />

           If you select the **Distinct Colors** color mode, select either **Auto** or **Manual** from the drop-down list.

           <br />

           * **Auto**: Automatically assigns thresholds and colors for the visual.
           * **Manual**: You can change the thresholds and colors used in the visual.
         </td>
       </tr>

       <tr>
         <td>Number of colors</td>
         <td>Specify the number of colors to use for the visual.</td>
       </tr>

       <tr>
         <td>Color Rules</td>

         <td>
           Change the assigned color for each color used for the visual.

           <br />

           If you specify **Manual** threshold mode, select the thresholds used for color settings in the visual.
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="understand-visual-color-condition-thresholds">
  Understand Visual Color Condition Thresholds
</h3>

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.

* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.

* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Self-Service Analytics automatically set the thresholds or you can manually set them.

For information about supported color encoding, see [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

<h2 id="bars-histograms">
  Bars: Histograms
</h2>

Histograms require only one metric (number). The metric data range is divided into intervals and the metric values that fall within each interval are counted. The histogram plots the value counts (Volume) against the metric intervals.

Histograms are supported only by data sources that use [connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) that support the calculations necessary for histogram visuals with integer values.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **N** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

Data from Fusion data sources can be used in histograms.

* [Configure Settings for a Specific Histogram](#configure-settings-for-a-specific-histogram)
* [Configure Colors for a Specific Histogram](#configure-colors-for-a-specific-histogram)

<h3 id="configure-settings-for-a-specific-histogram">
  Configure Settings for a Specific Histogram
</h3>

**Change the settings for a specific histogram**

1. Edit the histogram you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Histogram Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-hist-settings-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=c5811bac4f027d584fbfd0245965e556" alt="define the settings for this visual" width="393" height="494" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-hist-settings-25-1.png" />

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Show Cumulative Line</td>
         <td>Select to enable the cumulative line to be displayed on your visual.</td>
       </tr>

       <tr>
         <td>Number of Bars</td>

         <td>
           Specify the number of bars:

           <br />

           * **Auto** - if you select this option, the bins for all your data set will be built and corresponding bars will be displayed.
           * **Limit to** - specify the maximum number of bars to be displayed on your visual.
           * **Bar interval** - specify the bar interval for your visual.
         </td>
       </tr>

       <tr>
         <td>Horizontal Scroll, Vertical Scroll</td>
         <td>Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option.</td>
       </tr>

       <tr>
         <td>Y-Axis Labels</td>
         <td>Select **Absolute Values**, or **Relative Values** to use absolute or relative values.</td>
       </tr>
     </tbody>
   </table>

5. Optionally, edit the number format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-histogram">
  Configure Colors for a Specific Histogram
</h3>

**Specify the color settings for a specific histogram using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar menu for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-bar-hist2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=3ad23504295d6c67647bf3d0b4fcdc94" alt="define the color properties for this visual" width="347" height="256" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-bar-hist2.png" />

3. Configure the color settings as described below. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   | Setting | Description |
   | - | - |
   | Bins Color | Select the color for the bins on the visual. Select to clear the **Inherit from theme** checkbox to define a different color manually. |
   | Cumulative Line Color | Select the color for the cumulative line on your visual. Select to clear the **Inherit from theme** checkbox to define a different color manually. |

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="bars-multiple-metric-charts">
  Bars: Multiple Metric Charts
</h2>

Multiple metric bar charts are based on multiple metrics and one attribute. They are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

This topic describes:

* [Configure Settings for a Specific Multiple Metric Bar Chart](#configure-settings-for-a-specific-multiple-metric-bar-chart)
* [Configure Colors for a Specific Multiple Metric Bar Chart](#configure-colors-for-a-specific-multiple-metric-bar-chart)

<h3 id="configure-settings-for-a-specific-multiple-metric-bar-chart">
  Configure Settings for a Specific Multiple Metric Bar Chart
</h3>

**Change the settings for a specific multiple metric bar chart**

1. Edit the multiple metric bar chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Bar: Multiple Metrics Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-multi-settings-253-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=371c384389b06329d905d18d73d0d07f" alt="define the orientation and label settings for your visual" width="393" height="573" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-multi-settings-253-1.png" />

4. Alter the settings as needed:

   | Setting | Description |
   | - | - |
   | Orientation | Select **Horizontal** or **Vertical** orientation for the bars. |
   | Horizontal Scroll, Vertical Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Show Metric Labels | Enable to display labels for metric values. |
   | Absolute Values | Enable to display the data in absolute values. |
   | Relative Values | Enable to display the data in relative values. |
   | Group Labels Position | Select a position option for the metric labels: **Outside horizontal**, **Outside diagonal**, or **Outside vertical**. |
   | Style | Specify the bar thickness for the chart. |

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-multiple-metric-bar-chart">
  Configure Colors for a Specific Multiple Metric Bar Chart
</h3>

**Specify the color settings for a specific multiple metric bar chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * Use the color selector to manually assign colors for legend items.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Label Color</td>
         <td>The inherited label color from the theme. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           Select a color palette for this specific visual.

           <br />

           Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="modify-bar-charts">
  Modify Bar Charts
</h2>

When you first create a standard bar chart or a multiple metric bar chart, the default settings specified in the data source configuration are used to create the visuals.

Use the Settings sidebar to further refine your selected bar chart.

<img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-std-settings-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=d18f29fc8f5495dc0141f0a9e36c6f75" alt="Adjust settings for your bar chart here" width="391" height="641" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bar-std-settings-25-1.png" />

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Orientation</td>
      <td>Select Horizontal or Vertical orientation for the bars.</td>
    </tr>

    <tr>
      <td>Cumulative Sum</td>

      <td>
        When enabled, Self-Service Analytics updates the visual to add the previous value to the next value, and both the original and cumulative value for selected items are displayed as a tool tip.

        <br />

        In Bar visuals, this feature is only available when data is grouped by a Time field, and when the Enable Subgroup setting is disabled.
      </td>
    </tr>

    <tr>
      <td>Horizontal Scroll</td>
      <td>Select to enable users to scroll and zoom data for this visual horizontally. Other settings you define for a visual may limit the availability of this option.</td>
    </tr>

    <tr>
      <td>Subgroup</td>

      <td>
        Slide on (to the right) the **Enable Subgroup** slider to enable a subgroup style. After enabling a subgroup style, select the style for the chart: **Clustered Bar Chart**, **Stacked Bar Chart**, or **100% Stacked Bar Chart**.

        <br />

        If Subgroups are enabled, you can define the visibility and position of their labels.
      </td>
    </tr>

    <tr>
      <td>Show Group Labels</td>
      <td>Enable to display labels for group values.</td>
    </tr>

    <tr>
      <td>Absolute Values</td>
      <td>Enable to display the data in absolute values.</td>
    </tr>

    <tr>
      <td>Relative Values</td>
      <td>Enable to display the data in relative values.</td>
    </tr>

    <tr>
      <td>Group Labels Position or Subgroup Labels Position</td>
      <td>Select a position option for the group or subgroup labels: **Inside**, **Outside horizontal**, **Outside diagonal**, or **Outside vertical**.</td>
    </tr>

    <tr>
      <td>Style</td>
      <td>Specify the bar thickness for the chart.</td>
    </tr>
  </tbody>
</table>

<h2 id="line-trend-attribute-value-charts">
  Line Trend: Attribute Value Charts
</h2>

Attribute value line charts are based on one metric, one attribute and one time attribute. Attribute value line charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) except Cloudera Search. They are supported in this environment for Apache Solr connectors for version 5.2 or later.

This topic describes:

* [Configure Settings for a Specific Attribute Value Line Chart](#configure-settings-for-a-specific-attribute-value-line-chart)
* [Configure Colors for a Specific Attribute Value Line Chart](#configure-colors-for-a-specific-attribute-value-line-chart)

For information on setting even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval).

<h3 id="configure-settings-for-a-specific-attribute-value-line-chart">
  Configure Settings for a Specific Attribute Value Line Chart
</h3>

**Change the settings for a specific attribute value line chart**

1. Edit the attribute value line chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Line Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/line-chart-att-val-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=9c65da1bfb6becff0725bc91d8e329ae" alt="define the settings for your line chart with attribute values" width="392" height="586" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/line-chart-att-val-26-2.png" />

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Display Style</td>

         <td>
           Select **Line Chart**, **Area Chart**, or **Gradient Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default.

           <br />

           * Select **Line Chart** to display your data in a simple line format, using appropriate colors.
           * Select **Area Chart** to display your data with a fill option for the line chart. This fills the visual with solid appropriate colors between the lines.
           * Select **Gradient Area Chart** to display your data with a gradient fill option for the line chart. This fills the visual with a gradient of appropriate colors from opaque to transparent between the lines.
         </td>
       </tr>

       <tr>
         <td>Display as stacked</td>
         <td>Slide this switch on (to the right) to display the visual as a stacked area chart. When turned on, the Stacking Style options become available.</td>
       </tr>

       <tr>
         <td>Stacking Style</td>

         <td>
           Select one of the stacking styles: **Stacked** or **100% Stacked**. These options are only available if the **Display as stacked** switch is on.

           <br />

           * The **Stacked** setting is the default and displays the plotted lines in a stacked format. Stacked charts are best used to show how individual values in the data relate to all of the other values for the same data.
           * The **100% Stacked** option displays the plotted lines in a stacked format but as they relate to a cumulative whole. The y-axis cumulative total is always represented as 100% in a 100% stacked format and all individual values are presented as percentages of the whole.
         </td>
       </tr>

       <tr>
         <td>Horizontal Scroll</td>
         <td>Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option.</td>
       </tr>

       <tr>
         <td>Line Thickness</td>
         <td>Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box.</td>
       </tr>

       <tr>
         <td>Smooth Curve</td>

         <td>
           Disabled by default.

           <br />

           * When disabled, lines render with straight line segments between data points.
           * When enabled, all line series are rendered with fluid spline interpolation.
         </td>
       </tr>
     </tbody>
   </table>

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-attribute-value-line-chart">
  Configure Colors for a Specific Attribute Value Line Chart
</h3>

**Specify the color settings for a specific attribute value line chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=629a3f744a75d53b31d0c9f96fec3955" alt="" width="395" height="776" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png" />

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * Use the color selector to manually assign colors for legend items.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Color Attribute</td>
         <td>Select the attribute that affects the segment color in the visual.</td>
       </tr>

       <tr>
         <td>Color Palette</td>

         <td>
           Select a color palette for this specific visual.

           <br />

           Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="line-trend-multiple-metric-charts">
  Line Trend: Multiple Metric Charts
</h2>

Multiple metric line charts are based on multiple metrics and one time attribute. Multiple metric line charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) except Cloudera Search. They are supported in this environment for Apache Solr connectors for version 5.2 or later.

This topic describes:

* [Configure Settings for a Specific Multiple Metric Line Chart](#configure-settings-for-a-specific-multiple-metric-line-chart)
* [Configure Colors for a Specific Multiple Metric Line Chart](#configure-colors-for-a-specific-multiple-metric-line-chart)

For information on setting even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval).

<h3 id="configure-settings-for-a-specific-multiple-metric-line-chart">
  Configure Settings for a Specific Multiple Metric Line Chart
</h3>

**Change the settings for a specific multiple metric line chart**

1. Edit the multiple metric line chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Line Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/line-chart-mm-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=74de2b924fbd72e0c0cb99ab5ea67953" alt="define the settings for your visual here" width="392" height="471" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/line-chart-mm-26-2.png" />

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Display Style</td>

         <td>
           Select **Line Chart**, **Area Chart**, or **Gradient Area Chart** to indicate the type of chart you want to see. **Line Chart** is selected by default.

           <br />

           * Select **Line Chart** to display your data in a simple line format, using appropriate colors.
           * Select **Area Chart** to display your data with a fill option for the line chart. This fills the visual with solid appropriate colors between the lines.
           * Select **Gradient Area Chart** to display your data with a gradient fill option for the line chart. This fills the visual with a gradient of appropriate colors from opaque to transparent between the lines.
         </td>
       </tr>

       <tr>
         <td>Cumulative Sum</td>
         <td>When enabled, Self-Service Analytics updates the visual to add the previous value to the next value, and both the original and cumulative value for selected items are displayed as a tool tip.</td>
       </tr>

       <tr>
         <td>Horizontal Scroll</td>
         <td>Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option.</td>
       </tr>

       <tr>
         <td>Line Thickness</td>
         <td>Increase or decrease the thickness of the lines in the visual using the up and down arrows in this box.</td>
       </tr>

       <tr>
         <td>Smooth Curve</td>

         <td>
           Disabled by default.

           <br />

           * When disabled, lines render with straight line segments between data points.
           * When enabled, all line series are rendered with fluid spline interpolation.
         </td>
       </tr>
     </tbody>
   </table>

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-multiple-metric-line-chart">
  Configure Colors for a Specific Multiple Metric Line Chart
</h3>

**Specify the color settings for a specific multiple metric line chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           For distinct color styles, select a data point in the legend to turn it off and on in the visual.
         </td>
       </tr>

       <tr>
         <td>Color</td>
         <td>Manually select the color for each metric using the color selector.</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           Select a color palette for this specific visual.

           <br />

           Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="edit-line-bar-trend-charts">
  Edit Line & Bar Trend Charts
</h2>

Line and bar trend charts are based on two metrics and a time attribute. They are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference), except Cloudera Search, and by Self-Service Analytics Apache Solr connectors for version 5.2 or later.

<Note>
  To edit the number or date and time format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).
</Note>

This topic describes:

* [Configure Colors for a Specific Line & Bar Trend Chart](#configure-colors-for-a-specific-line-bar-trend-chart)

For information on setting even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval).

<h3 id="configure-colors-for-a-specific-line-bar-trend-chart">
  Configure Colors for a Specific Line & Bar Trend Chart
</h3>

**Specify the color settings for a specific line & bar trend chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-line-bar2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=1e3d2bd13cb7b7c594bddd2145d1371b" alt="" width="348" height="295" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-line-bar2.png" />

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   | Setting | Description |
   | - | - |
   | Y2 Color | Select a color for the Y2 line on your visual. Select to clear the **Inherit from theme** checkbox to define a different color manually. |
   | Y1 Color | Select a color for the Y1 bars on your visual. Select to clear the **Inherit from theme** checkbox to define a different color manually. |

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="combo-charts">
  Combo Charts
</h2>

Combo charts are based on a single independent variable (usually the x-axis) and up to four dependent variables (usually the y-axes). The dependent variables can be plotted using either bar or line visual types. The independent variable (x-axis) can be any attribute or metric in the data; the dependent variables (y-axes) must be a metric (numeric field). A single attribute (independent variable) and two metrics (dependent variables) are required.

<Note>
  To edit the number or date and time format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).
</Note>

The legend on a combo chart is interactive. It allows you to show or hide different plots on the chart. By default, the plots for all of the metrics on the combo chart are shown.

If you select one of the metrics in the legend, its name is grayed out and its plot is removed from the chart. To see its plot again, select the metric in the legend again.

In the following example, the plot for the `Planned Sales (Sum)` metric is not shown on the chart and its name is grayed out in the legend. Adjust metric label visibility, values displayed, and positioning as needed.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/combo-cht-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=fdf3f903d96ba37af3a10b20f55cd667" alt="a combo chart with multiple axes and options enabled" width="1040" height="582" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/visuals/combo-cht-26-2.png" />

Hover over a metric to see details about visible and hidden metrics in a tool tip format.

Combo charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

This topic describes:

* [Configure Settings for a Specific Combo Chart](#configure-settings-for-a-specific-combo-chart)
* [Configure Colors for a Specific Combo Chart](#configure-colors-for-a-specific-combo-chart)

<h3 id="configure-settings-for-a-specific-combo-chart">
  Configure Settings for a Specific Combo Chart
</h3>

**Change the settings for a specific combo chart**

1. Edit the combo chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Combo Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/combo-std-settings-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=2a4b14dd874e2fd95df151503a0b2992" alt="Use this work area to define settings for the combo chart visual" width="391" height="880" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/combo-std-settings-25-1.png" />

4. Alter settings as needed:

   | Setting | Description |
   | - | - |
   | Horizontal Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Enable Y3 | Use this switch to enable or disable the third dependent variable (on the Y3 axis) on the combo chart. When disabled, the Y3 variable is not plotted. |
   | Enable Y4 | Use this switch to enable or disable the fourth dependent variable (on the Y4 axis) on the combo chart. When disabled, the Y4 variable is not plotted. |
   | Y1 Axis Visual Style | Use the drop-down list to select a visual style for the Y1 axis variable. Select **Bar**, **Line**, or **Cumulative Line**. Enable **Use Percentage Axis** to display as a percentage. |
   | Y2 Axis Visual Style | Use the drop-down list to select a visual style for the Y2 axis variable. Select **Bar**, **Line**, or **Cumulative Line**. Enable **Use Percentage Axis** to display as a percentage. |
   | Y3 Axis Visual Style | Use the drop-down list to select a visual style for the Y3 axis variable. Select **Bar**, **Line**, or **Cumulative Line**. Enable **Use Percentage Axis** to display as a percentage. |
   | Y4 Axis Visual Style | Use the drop-down list to select a visual style for the Y4 axis variable. Select **Bar**, **Line**, or **Cumulative Line**. Enable **Use Percentage Axis** to display as a percentage. |
   | Show Metric Labels | Enable to display labels for metric values. |
   | Absolute Values | Enable to display the data in absolute values. |
   | Relative Values | Enable to display the data in relative values. |
   | Group Labels Position | Select a position option for the metric labels: **Outside horizontal**, **Outside diagonal**, or **Outside vertical**. |

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-combo-chart">
  Configure Colors for a Specific Combo Chart
</h3>

**Specify the color settings for a specific combo chart using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/combo-color.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=a2a42f08e71f9c65bb1d3caf35f22edc" alt="" width="349" height="769" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/combo-color.png" />

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Label Color</td>
         <td>The inherited label color from the theme. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>

       <tr>
         <td>Y2, Y3, Y4 Color</td>
         <td>Select colors for the Y2, Y3, and Y4 dependent variables plotted on the combo chart. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>

       <tr>
         <td>Color Palette</td>
         <td>Select the color palette for the Y1 axis for this specific combo chart. Select to clear the **Inherit from theme** checkbox to define a different color manually.</td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h2 id="waterfall">
  Waterfall
</h2>

Waterfall visuals are based on at least one time attribute and one or multiple metrics, and can incorporate positive and negative values. You can include a [reference line](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers#use-reference-lines), [grid lines](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rulers), and a Totals bar. Waterfall visuals with multiple metrics are supported by all Self-Service Analytics [data connectors.](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference)

For information on setting even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval).

### Configure Settings for a Waterfall Visual

**Change the settings for a waterfall visual**

1. Edit the waterfall visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Waterfall Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/waterfall-stgs-25-1.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=72067a05c363eec534e028e789c48811" alt="use this menu to change the settings fo ryour waterfall visual" width="390" height="474" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/waterfall-stgs-25-1.png" />

4. Alter the settings as needed:

   | Setting | Description |
   | - | - |
   | Horizontal Scroll, Vertical Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Show Metric Labels | Enable to show the field names as labels in the visual. Disable to hide the field names. |
   | Absolute Value | Enable to show the absolute value represented by each waterfall bar. Disable to hide the absolute value. |
   | Show Total | Enable to show a total representation of all information included in the waterfall bars. |
   | Label | By default, the Label for total is Total; change as needed. |
   | Bar Thickness | Adjust the thickness of the bars in your visual as needed. |

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the visual, or dashboard and the visual with updated settings.

### Configure Colors for a Waterfall Visual

**Specify the color settings for a Waterfall Visual using the Color sidebar**

1. Edit the visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears. If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

   Select the color icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Color sidebar for the visual appears.

3. Configure the color settings as described below. As you change the color settings, the legend at the top of the Color sidebar shows how the legend will appear on the visual. Supported color specifications are described in [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Legend</td>

         <td>
           Enable or disable to display a dynamic legend in this visual. Dynamic legends allow you to temporarily add or remove data shown in the visual.

           <br />

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * For gradient color styles, use the legend’s gradient slider to show and hide your data.
           * Use the color selector to manually assign colors for legend items.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Color</td>

         <td>
           Manually select the colors for each metric using the color selector. Visuals that incorporate positive and negative values displays color options paired as **\<field>** and **\<field> (Negative)**. Options include

           <br />

           * Select individual colors to choose a custom color for any or all metrics. Custom colors are listed by metric in the **Assigned Colors** work area.
           * Select **Reset Colors** in the Assigned Colors work area to revert your colors to their previous saved state.
         </td>
       </tr>

       <tr>
         <td>Total Color</td>
         <td>Manually select a color for the Total using the color selector, or select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           Select a color palette for this specific visual.

           <br />

           Select the **Inherit from theme** checkbox to use the color palette specified by the [theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

### Multiple Metrics in a Waterfall Visual

If you use multiple metrics in your waterfall visual, you can control the order in which the metrics appear in the waterfall. Add one or more metrics to the Y axis in the order you would like them to appear. The first one you add will be the left most metric, and subsequent metrics will appear to the right of existing metrics.
