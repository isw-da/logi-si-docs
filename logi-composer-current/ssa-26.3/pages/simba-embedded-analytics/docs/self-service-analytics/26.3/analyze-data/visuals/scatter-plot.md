> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Comparison and Relationship Charts

## Scatter Plots

Scatter plots are based on three metrics and one attribute. They are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

<Note>
  To edit the number or date and time format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).
</Note>

## Configuring Colors for a Specific Scatter Plot

**Specify the color settings for a specific scatter plot using the Color sidebar**

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
         <td>Group By Color Palette</td>

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

<h2 id="floating-bubble-charts">
  Floating Bubble Charts
</h2>

Floating bubble charts are based on two metrics and two attributes. Floating bubble charts are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) except Cloudera Search. They are supported by Self-Service Analytics Apache Solr connectors for version 5.2 or later.

<Note>
  To edit the number or date and time format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).
</Note>

The default settings used for floating bubble charts vary, based on the data source selected for the chart.

This topic describes:

* [Configure Settings for a Floating Bubble Chart](#configure-settings-for-a-floating-bubble-chart)
* [Configure Colors for a Specific Floating Bubble Chart](#configure-colors-for-a-specific-floating-bubble-chart)

<h3 id="configure-settings-for-a-floating-bubble-chart">
  Configure Settings for a Floating Bubble Chart
</h3>

**Change the settings for a specific floating bubble chart**

1. Edit the floating bubble chart you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Floating Bubble Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bubble-sttgs-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=1eff5a9f07024d3cf81bec6e03480477" alt="Adjust settings for your floating bubble chart here" width="393" height="444" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/bubble-sttgs-25-1.png" />

4. Alter the settings as needed:

   | Setting | Description |
   | - | - |
   | Horizontal Scroll, Vertical Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-floating-bubble-chart">
  Configure Colors for a Specific Floating Bubble Chart
</h3>

**Specify the color settings for a specific floating bubbles chart using the Color sidebar**

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
         <td>Group By Color Palette</td>

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

<h2 id="box-plots">
  Box Plots
</h2>

Box plots are based on one metric and one or more attributes. Groups and subgroups to expand the depth of the information you provide in this visual type. Box plot visuals can be used only with data sources that use [connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) that support percentile calculations necessary for box plots.

<Note>
  To edit the number or date and time format for this visual, see [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).
</Note>

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**N**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**N**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**N**</td>
      <td>The Apache Solr versions prior to 5.3 used by Cloudera Search do not have the percentile aggregations required for box plots built in.</td>
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**N**</td>
      <td>Mongo DB data stores do not support the kind of aggregation needed for box plots out of the box.</td>
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>

Data from Fusion data sources can be used in box plots.

This topic describes:

* [Configure Settings for a Specific Box Plot](#configure-settings-for-a-specific-box-plot)
* [Configure Colors for a Specific Box Plot](#configure-colors-for-a-specific-box-plot)

<h3 id="configure-settings-for-a-specific-box-plot">
  Configure Settings for a Specific Box Plot
</h3>

**Change the settings for a specific box plot**

1. Edit the box plot you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Bar Chart Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/box-plt-set-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=b8f706de59e010be0ec157abe85f9fc3" alt="Adjust settings for your box plot here" width="394" height="443" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/box-plt-set-25-1.png" />

4. Alter the settings as needed:

   | Setting | Description |
   | - | - |
   | Horizontal Scroll, Vertical Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |
   | Enable Subgroup | Slide on (to the right) the **Enable Subgroup** slider to enable a subgroup option. You can then define a subgroup in the visual. |

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save the dashboard and the visual with its updated settings.

<h3 id="configure-colors-for-a-specific-box-plot">
  Configure Colors for a Specific Box Plot
</h3>

If you share your data in groups and subgroups, you can apply color attributes as needed.

**Specify the color settings for a specific box plot using the Color sidebar**

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
         <td>Group By Color Palette</td>

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

<h2 id="heat-maps">
  Heat Maps
</h2>

Heat maps are based on one metric and two attributes. Heat maps are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) except Cloudera Search.

This topic describes:

* [Configure Settings for a Specific Heat Map](#configure-settings-for-a-specific-heat-map)
* [Configure Colors for a Specific Heat Map](#configure-colors-for-a-specific-heat-map)
* [Understand Visual Color Condition Thresholds](#understand-visual-color-condition-thresholds)
* [Understand Visual Color Condition Thresholds](#configure-colors-for-a-specific-heat-map)

<h3 id="configure-settings-for-a-specific-heat-map">
  Configure Settings for a Specific Heat Map
</h3>

**Change the settings for a specific heat map**

1. Edit the heat map you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The Heat Map Settings sidebar for the visual appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/heat-sttgs-25-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=3f1705d2df9dee89b723295c3b556353" alt="use this work area to define settings for this visual" width="395" height="442" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/heat-sttgs-25-1.png" />

4. Alter the settings as needed:

   | Setting | Description |
   | - | - |
   | Show Values | Slide the **Show Values** slider on (to the right) to show the number of records (volume) in heat map cells. |
   | Horizontal Scroll, Vertical Scroll | Select to enable users to scroll and zoom data for this visual. Other settings you define for this visual may limit the availability of this option. |

5. Optionally, edit the number or date and time format for this visual. See [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting) and [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting).

6. Select the save icon to save your updated settings.

<h3 id="configure-colors-for-a-specific-heat-map">
  Configure Colors for a Specific Heat Map
</h3>

**Specify the color settings for a specific heat map using the Color sidebar**

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

           * For distinct color styles, select a data point in the legend to turn it off and on in the visual.
           * For gradient color styles, use the legend’s gradient slider to show and hide your data.

           <br />

           If available, enable or disable a static legend for this visual.
         </td>
       </tr>

       <tr>
         <td>Color Metric</td>
         <td>Select the metric that affects the segment color in the visual.</td>
       </tr>

       <tr>
         <td>\<type> Color Palette</td>

         <td>
           If **Inherit from Theme** is selected, the color palette is determined by the theme selected for your software UI.

           <br />

           To override the palette selected by the theme, clear the **Inherit from Theme** checkbox and select a different color palette.
         </td>
       </tr>

       <tr>
         <td>Color Mode</td>

         <td>
           Select **Distinct Colors** or **Gradient** to identify the way colors are used on the screen.

           <br />

           Either specific distinct colors will be used or a gradient of colors will be used.
         </td>
       </tr>

       <tr>
         <td>Threshold Mode</td>

         <td>
           If you selected the **Gradient** color mode, this setting cannot be changed. If you selected the Distinct Colors color mode, select either **Auto** or **Manual** from the drop-down list.

           <br />

           **Auto** will automatically assign thresholds and colors for the visual.

           <br />

           **Manual** enables you to change the thresholds and colors used on the visual.
         </td>
       </tr>

       <tr>
         <td>Number of colors</td>
         <td>Specify the number of colors to use for the visual.</td>
       </tr>

       <tr>
         <td>Color Rules</td>

         <td>
           Color rules allow you to change the colors for each color used for the visual.

           <br />

           In addition, if you specified a **Manual** threshold mode, you can select the thresholds used for color settings in the visual.
         </td>
       </tr>
     </tbody>
   </table>

4. Close the Color sidebar and the color settings are dynamically applied to the visual.

5. Select the save icon to save the dashboard and the visual with its updated settings.

<h4 id="understand-visual-color-condition-thresholds">
  Understand Visual Color Condition Thresholds
</h4>

You can set threshold color conditions for metric-based visuals. At least two color settings are required. In addition, thresholds are specified between each color setting. (So three color settings require two threshold settings; four color settings require three threshold settings, etc.)

* The color for Color 1 is used when the value of the color metric is less than the first threshold value.

* The color for Color 2 is used when the value of the color metric falls between the first and second threshold values.

* If only three colors are used for the visual, the color for Color 3 is used when the value of the color metric is greater than or equal to the second threshold value.

  If more than three colors are used, the color for Color 3 is used when the value of the color metric falls between the second and third threshold values.

  When more than three colors are used, the colors continue to be applied in this pattern for all threshold settings; any color metric values greater than the last threshold setting have the final color applied.

You can have Self-Service Analytics automatically set the thresholds or you can manually set them.

For information about supported color encoding, see [Specify Colors](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/specifying-colors).
