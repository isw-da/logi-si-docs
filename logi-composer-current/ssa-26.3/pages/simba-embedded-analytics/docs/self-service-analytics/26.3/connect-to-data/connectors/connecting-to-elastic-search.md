> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Elasticsearch Connector

The Self-Service Analytics Elasticsearch connector lets you access the data available in the Elasticsearch storage using the Self-Service Analytics client. The Self-Service Analytics Elasticsearch connector supports the following Elasticsearch versions.

* Elasticsearch 7.0 - 7.17

  <Note>
    Use the Elasticsearch 7 connector to connect to OpenSearch earlier than 2.x. To connect to OpenSearch 2.x and higher, use the [OpenSearch connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch).
  </Note>

* Elasticsearch 8.1 - 8.17

<Warning>
  You cannot import or export Elasticsearch data sources (or the visuals and dashboards that use those Elasticsearch data sources) if the version of the Elasticsearch connector in the Self-Service Analytics environment is different from the version used by the data sources. For example, you cannot import an Elasticsearch 7 data source you have exported if your Self-Service Analytics environment only has an Elasticsearch 8 connector defined. When you change connector versions in your Self-Service Analytics environment, we recommend that you also create new data source configurations (and associated visuals and dashboards) for the newer version.
</Warning>

Before you can establish a connection from Self-Service Analytics to Elasticsearch storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Elasticsearch](#connect-to-elasticsearch) for details specific to the Elasticsearch connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

This section covers the following topics:

* [Elasticsearch Connector Feature Support](#elasticsearch-connector-feature-support)
* [Connect to Elasticsearch](#connect-to-elasticsearch)
* [Connect to Elasticsearch Using Amazon Web Services Authentication](#connect-to-elasticsearch-using-amazon-web-services)
* [Elasticsearch Data Source Configuration Notes](#elasticsearch-data-source-configuration-notes)
* [Distinct Counts and Percentiles in Elasticsearch](#distinct-counts-and-percentiles-in-elasticsearch)
* [Tokenization in Elasticsearch](#tokenization-in-elasticsearch)
* [Elasticsearch Connector IP Address Data Type Support](#elasticsearch-connector-ip-address-data-type-support)
* [Elasticsearch Last Value Processing](#elasticsearch-last-value-processing)
* [Elasticsearch 7 Composite Aggregation](#elasticsearch-7-composite-aggregation)
* [Elasticsearch Source Document Storage Configurations](#elasticsearch-source-document-storage-configurations)
* [Inner Hits Configuration Property](#inner-hits-configuration-property)
* [Support of X-Pack for Elasticsearch](#support-of-x-pack-for-elasticsearch)

<h2 id="connect-to-elasticsearch">
  Connect to Elasticsearch
</h2>

When establishing a connection to an Elasticsearch data store, make sure you:

1. Specify the connection string in the following format:

   | Protocol | Connection String Format | Example |
   | - | - | - |
   | HTTP/HTTPS | `<schema>://<host1>:<port1>,...,<hostN>:<postN>/<prefix>` | `http://ip-10-2-2-241.ec2.internal:80/es` |
   | Transport/Transports | `<schema>://<host1>:<port1>,...,<hostN>:<portN>` | `transports://10.2.2.2:9010,10.2.2.3:9010` |

   where `<schema>` is the protocol that you want to use:

   * `http` or `https` (with SSL support)
   * `transport` or `transports` (with SSL support)

2. Specify your Elasticsearch **cluster name**.

3. If required, specify your Elasticsearch **User Name** and **Password**.

4. Select **Validate** to confirm your connection.

To connect to your Elasticsearch cluster and data set secured by X-Pack, see [Support of X-Pack for Elasticsearch](#support-of-x-pack-for-elasticsearch).

### Connect to Elasticsearch with a Configured Custom Certificate

If your Elasticsearch cluster is configured with a custom certificate, you should configure a truststore for the Elasticsearch connector.

**Connect to an Elasticsearch data store with a configured custom certificate**

1. Copy a truststore to the machine on which the Elasticsearch connector is running.

2. Add the following lines to file the appropriate Elasticsearch `jvm` file.

   * For Linux: `/etc/zoomdata/edc-elasticsearch-7.0.jvm`, or `/etc/zoomdata/edc-elasticsearch-8.0.jvm`. Copy these files from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
   * For Windows: `<install-path>/edc-elasticsearch-7.0.jvm` or `<install-path>/edc-elasticsearch-8.0.jvm`. Copy these files from the `<install-path>/conf` directory if a copy is not in `<install-path>`.

   ```properties theme={null}
   -Djavax.net.ssl.trustStore=<path_to_truststore>
   -Djavax.net.ssl.trustStorePassword=<truststore_password>
   ```

   Replace:

   * `<path_to_truststore>` with an absolute path to your truststore
   * `<truststore_password>` with a password for your truststore

<h2 id="connect-to-elasticsearch-using-amazon-web-services">
  Connect to Elasticsearch Using Amazon Web Services Authentication
</h2>

You can connect the Self-Service Analytics Elasticsearch connectors to your Elasticsearch data store using Amazon Web Services (AWS) credentials. After connecting, the Self-Service Analytics Elasticsearch connectors work with AWS Elasticsearch without any restrictions.

<Warning>
  AWS does not support Elasticsearch v8.0.
</Warning>

**Connect the Elasticsearch connector to your Elasticsearch data store using AWS authentication:**

1. Specify the AWS credentials in a standard AWS-format credentials file (see [Format of the credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-creds)) and store the file in the Elasticsearch connector’s file system.

2. Edit the [Elasticsearch properties file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) (`edc-elasticsearch-7.0.properties`) and locate or add the `elasticsearch.aws.show-aws-connection-params` property to the file. This property indicates whether AWS-specific connection parameters should be shown when a new connector is created or the connection properties of an existing connector are refreshed. Valid values are `true` or `false`. The default is `false` (users will *not* see new AWS connection parameters).

   Set the value of this property to `true` and save the properties file. For more information about Self-Service Analytics properties files, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

3. Create a new Elasticsearch connection or edit an existing one (see [Add Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections)).

   The AWS connection parameters appear in the UI. Supply values for them as described in the following table.

   | Parameter | Specify | Description |
   | - | - | - |
   | `AUTHENTICATE_WITH_AWS_CREDENTIALS` | `true` | Indicate whether authentication with AWS credentials should be used. Note that the Elasticsearch username / password specification and AWS credentials cannot be simultaneously used for authentication. Valid values are `true` or `false`; the default is `false` (AWS credentials are not used). |
   | `AWS_REGION` | a valid region name | Specify the AWS region where the target Elasticsearch service is running. This parameter is optional when host names in the connection string have the standard format `<domain>.<region>.es.amazonaws.com` (the region name can be extracted from the host name). However, when specified, it has priority over the region name included in the host name. |
   | `AWS_PROFILES_CONFIG_PATH` | the path to the credentials file | Specify the location of the AWS credentials file in the Elasticsearch connector’s file system. This parameter is optional when the credentials file is in the default location (`~/.aws/credentials` for the user of the connector). |
   | `AWS_PROFILE` | a valid profile name in the AWS credentials file | Specify the profile to use within the AWS credentials file. This parameter is optional if you choose to use the `default` profile in the AWS credentials file. |

4. After you have specified all parameters necessary for the connection definition, save it. See [Add Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections).

<h2 id="elasticsearch-7-composite-aggregation">
  Elasticsearch 7 Composite Aggregation
</h2>

Composite aggregations are implemented by Elasticsearch 7 connectors. This support optimizes aggregations of Elasticsearch 7 data, except for queries with:

* histograms
* time groups with WEEK granularity
* multiple groups when group fields belong to different nested contexts.

An Elasticsearch 7 configuration property `elasticsearch.query.composite-agg.max-fetch-size` in the Elasticsearch 7 configuration file (`edc-elasticsearch-7.0.properties`) can be used to specify the maximum number of buckets to return for each query within a composite aggregation.

Valid values must be greater than zero; the default value is 10000. This property corresponds to the Elasticsearch setting `search.max_buckets`, that also has a default value of 10000.

If you elect to increase the value of the `elasticsearch.query.composite-agg.max-fetch-size property`, be sure to correspondingly increase the value of the Elasticsearch `search.max_buckets` setting.

<h2 id="distinct-counts-and-percentiles-in-elasticsearch">
  Distinct Counts and Percentiles in Elasticsearch
</h2>

Distinct count and percentiles metrics return approximate values in Elasticsearch. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

You can change the value of the precision threshold by setting the `elasticsearch.query.cardinality.precision.threshold` property in the `zoomdata.properties` file.

See Elasticsearch's documentation on the following for more information:

* For Elasticsearch version 7, see the following for [percentiles](https://www.elastic.co/guide/en/elasticsearch/reference/7.0/search-aggregations-metrics-percentile-aggregation.html) and [distinct count](https://www.elastic.co/guide/en/elasticsearch/reference/7.0/search-aggregations-metrics-cardinality-aggregation.html).
* For Elasticsearch version 8, see the following for [percentiles](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/search-aggregations-metrics-percentile-aggregation.html) and [distinct count](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/search-aggregations-metrics-cardinality-aggregation.html).

The table below lists all available properties that you can modify to work with Elasticsearch.

| Property | Default | Use | Notes |
| - | - | - | - |
| elasticsearch.query.cardinality.precision.threshold | 1000 | control the level of accuracy of the distinct counts | The maximum supported value is 40000. However, we do not recommend you set this value as it may result in performance issues and the data source itself may return errors. For more info, refer to the [Precision Control](https://www.elastic.co/guide/en/elasticsearch/reference/2.0/search-aggregations-metrics-cardinality-aggregation.html#_precision_control) section by Elasticsearch. |
| elasticsearch.query.limit.nongrouped | 10000 | set the limit for the number of non-grouped records (per shard) to execute on. | |
| elasticsearch.query.limit.grouped | 10000 | set the limit for the number of grouped records (per shard) to execute on. | |

If you need to change the default settings, add the corresponding properties (listed above) to the `zoomdata.properties` file and assign the required values. For more details, see [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files).

<h2 id="elasticsearch-data-source-configuration-notes">
  Elasticsearch Data Source Configuration Notes
</h2>

When setting up an Elasticsearch-based [data source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview), select the indices and aliases to be queried, and select the fields to be handled. You can do this in three steps:

1. Select indices and aliases to be queried on the Source Creation tab.

2. Select indices **Manually** or **Automatically**.

   * If you want to get the data only from specific indices, select the **Manually** option and choose the corresponding indices from the list **Select Indices**.

   * The **Automatically** option is more flexible. It lets you set the pattern by which the indices will be selected automatically.

     For this option, you can select one of the pattern types. Note that when no indices match the pattern while querying, your visuals are returned empty.

     * **Native** - specify the pattern for index names. Use an asterisk (\*) to replace one character or a set of characters.

       For example, you want to get all the indices whose name starts with ***log*** and ends with ***16***. In this case, specify the following pattern:

       ```
       log*16
       ```

     * **Time Based** - set the time pattern to get the matching indices. [Check the supported date and time patterns](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#convert-attributes-to-time-fields-in-data-source-field).

       For example, the time pattern YYYY-MM will return all the indices, whose name will match the pattern in the following examples. Note that if the Index Name includes text with the time and date pattern, you need to enclose the text portion in brackets \[ ]:

       **Examples:**

       | Index Name | Pattern |
       | - | - |
       | 2022-01 | YYYY-MM |
       | 2022-3 | YYYY-Q |
       | 10:23:11 | HH:MM:SS |
       | logstash-2022-06-14 | \[logstash-]YYYY-MM-DD |

       <Note>
         The fields for indexes are not refreshed. If new fields are added to your data source, they are added to Self-Service Analytics only after you select the **Manual Refresh** (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f7b35df88bf64ec08419feda8123e37a" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/refresh-field-button.png" />) button on the **Cache** tab of the [data source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview). If there are some changes in the existing fields (for example, if a field has been removed) they will not be applied.
       </Note>

   <Note>
     Filtering by type is not supported.
   </Note>

When you connect to your Elasticsearch data source, the additional service field **type** is added. The **type** field contains all the selected Elasticsearch types you can visualize as attributes on your visuals.

<h2 id="elasticsearch-connector-feature-support">
  Elasticsearch Connector Feature Support
</h2>

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th colSpan={3}>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2)</td>
      <td colSpan={3}>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search)</td>
      <td colSpan={3}>**Y**</td>
      <td>You can sort keyword searches by Best Match and Most Recent (when you select a preferred time field from the source). Filter your search results by selecting fields in the Filter modal. Select **Clear All** to clear filtered search results.</td>
    </tr>

    <tr>
      <td>[TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters)</td>
      <td colSpan={3}>**N**</td>
      <td>Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters)</td>
      <td colSpan={3}>**N**</td>
      <td>Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>
  </tbody>
</table>

<h2 id="inner-hits-configuration-property">
  Inner Hits Configuration Property
</h2>

Use the Self-Service Analytics Elasticsearch `elasticsearch.inner-hits.size property` to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100.

If you specify a value that is too small, the number of values returned for a nested field in a document with a large number of sub-documents may be limited. If you specify a value that is too large, excessive memory may be consumed.

<Note>
  To learn more about this property, see [inner hits.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/inner-hits.html)
</Note>

<h2 id="elasticsearch-connector-ip-address-data-type-support">
  Elasticsearch Connector IP Address Data Type Support
</h2>

The IP Address data type is supported for Elasticsearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An Elasticsearch text search box. When searching via the text search, Self-Service Analytics also supports the CIDR notation for IP addresses as described in the Elasticsearch documentation ([https://www.elastic.co/guide/en/elasticsearch/reference/current/ip.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/ip.html)).
* The Group By selection box.
* Filters, although Self-Service Analytics does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Self-Service Analytics treats IP addresses as strings and expect an exact match.

<h2 id="elasticsearch-last-value-processing">
  Elasticsearch Last Value Processing
</h2>

There are situations in which the Elasticsearch connector cannot compute the Last Value metric correctly.

1. When the original value *is* available for a metric field, an error appears in either of the following situations:

   * Both metric and group fields are nested and related.
   * Both metric and time fields are nested and related.

   <Note>
     The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only in the following cases:
   </Note>

   * When the metric field is nested and neither the group or time field is located in the same hierarchy (group and time fields are either at the root level or belong to another hierarchy)
   * When the Last Value is an array.

2. When the original value *is not* available for a metric field (the result is fetched from doc values or stored fields), an error appears when the metric field is nested and the time field is not located on the same or lower level in the hierarchy.

   <Note>
     The Elasticsearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only when the Last Value is an array.
   </Note>

<h2 id="elasticsearch-source-document-storage-configurations">
  Elasticsearch Source Document Storage Configurations
</h2>

Elasticsearch data stores generally store the original JSON source documents passed when Elasticsearch performs its document indexing in the `_source` field in the index. However, some organizations disable the `_source` field to save storage and thus do not store the original JSON source documents.

Self-Service Analytics Elasticsearch 7 and 8 connectors support Elasticsearch data stores with any of the following source document configurations:

* Source documents disabled. For example:

  ```
  ...
  "mappings": {
     "_source": {
        "enabled": false
     },
  }
  ...
  ```

* Source documents enabled, but with some source exclusions. For example:

  ```
  ...
  "mappings": {
     "_source": {
        "enabled": true,
        "includes": [
           "order_*"
        ],
        "excludes": [
           "order_items.*"
        ]
     }
  },
  ...
  ```

* Source documents enabled, with no exclusions.

  ```
  ...
  "mappings": {
     "_source": {
        "enabled": true
     }
  },
  ...
  ```

The data sources created from connections to Elasticsearch data stores with any of these configurations function almost identically.

### Known Issue Summary

The following known issues exist when the `_source` field is disabled or when it is enabled with exclusions:

* **Raw data presentation will vary, depending on the source from which the raw field data is fetched.** In particular, fused data sources may be affected where Elasticsearch indices with different mappings are joined (for example, when such indices are joined by an IP field and one of them allows Self-Service Analytics to fetch the data from the original documents but another requires Self-Service Analytics to fetch the data from doc values). See [Raw Data Differences](#raw-data-differences) .
* **The last value metric may be computed incorrectly for nested fields.** Last value metrics are computed incorrectly when a time field is higher in the nested hierarchy or when a time field does not belong to the same hierarchy as the metric field.
* **Raw data is not available for some nested fields in multi-index Elasticsearch data sources.** When a nested field exists in some indices but is absent in other indices, the field's raw data is not available. It is represented as having a NULL value in all documents when it is included in a table.
* **Some nested fields are not searchable in multi-index data sources.** When a nested field exists in some indices but is absent in other indices, it cannot be used in text search queries. Such fields will not be used for text searches.

<h3 id="raw-data-differences">
  Raw Data Differences
</h3>

The following Self-Service Analytics functions are impacted by the source document storage configuration of your Elasticsearch data stores:

* The data source collection preview on the Indices tab of the data source configuration
* Tables
* Text search results
* Last value metric computations.

Self-Service Analytics fetches the raw value of a field (including its last value metric result) in the following order:

1. If the field is stored, the stored value is fetched.
2. If the field is available in the original stored document, the value in the original stored document is fetched.
3. If doc values are available for the field and the field is not a text field, the doc value is fetched. For more information, see [Text Field Raw Data Considerations](#text-field-raw-data-considerations).

Results vary based on the source from which the value was fetched, as described in the following table:

<table>
  <thead>
    <tr>
      <th>Value Fetched From</th>
      <th>Differences from the original stored document</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>The stored value</td>

      <td>
        * NULL values in arrays are excluded.
        * Arrays may be sorted, completely or partially.
        * Numeric values may be approximated.
        * IPv6 addresses are normalized.
      </td>
    </tr>

    <tr>
      <td>The doc value</td>

      <td>
        * NULL values in arrays are excluded.
        * Arrays may be sorted, completely or partially.
        * Duplicates in `string (keyword)` arrays are excluded, completely or partially.
        * Numeric values may be approximated.
        * IPv6 addresses are normalized.
      </td>
    </tr>
  </tbody>
</table>

<h4 id="text-field-raw-data-considerations">
  Text Field Raw Data Considerations
</h4>

Doc values are enabled by default for all fields, except for text fields. Consequently, by default, even if the original document is not stored or some fields are excluded from it, raw data is available for all fields, except for text fields.

An alternative structure called field data can be used for text fields. However, field data contains a set of terms for a text field, not its original value.

For this reason, raw data for a text field is not available if the text field is not stored in the index and cannot be fetched from the original document.

For example, the following mapping specifies that original documents should not be stored and declares two fields: `name` of type `keyword` and `description` of type `text`:

```json theme={null}
{
   "mappings": {
      "_source": {
         "enabled": false
      },
      "properties": {
         "name": {
            "type": "keyword"
         },
         "description": {
            "type": "text"
         }
      }
   }
}
```

Raw data for the text field `description` is not available in the index. To make raw data available for this field, declare it stored, as shown below:

```json theme={null}
{
   "mappings": {
      "_source": {
         "enabled": false
      },
      "properties": {
         "name": {
            "type": "keyword"
         },
         "description": {
            "type": "text",
            "store": true
         }
      }
   }
}
```

<h2 id="tokenization-in-elasticsearch">
  Tokenization in Elasticsearch
</h2>

Keep in mind that Elasticsearch, by default, tokenizes or analyzes fields that are of type `text`. As a result, strings consisting of two or more words may become separate fields when connected to Self-Service Analytics (for example, city names like *Las Vegas*). To disable this process and ensure that a string field is not analyzed, specify its type as `keyword`:

```yaml theme={null}
City: {
	type: "keyword"
	}
```

To learn more about tokenization in Elasticsearch, see [Get Trained Models API.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/get-trained-models.html#ml-get-trained-models-query-params)

<h2 id="support-of-x-pack-for-elasticsearch">
  Support of X-Pack for Elasticsearch
</h2>

Self-Service Analytics allows you to connect to your Elasticsearch cluster and data set secured by X-Pack.

X-Pack is an add-on offering for Elasticsearch 7 that aims at securing the data on your cluster, and is included in Elasticsearch 8. Learn more about [X-Pack](https://www.elastic.co/guide/en/x-pack/current/elasticsearch-security.html).

### Configure Cluster or Index Privileges for a User

To connect to the Elasticsearch cluster, you need to create an Elasticsearch user and configure the access privileges for this user.

The access permissions for the Elasticsearch user determine the scope of the data available for querying by Self-Service Analytics users.

To work with Elasticsearch data, use X-Pack to grant the following minimal access privileges to the Elasticsearch user:

* **Monitor** privileges for [Elasticsearch Cluster](https://www.elastic.co/guide/en/shield/current/shield-aaa-ov.html#privileges-list-cluster)
* **Manage** (to get the metadata) and **Read** (to read data) privileges for [Index](https://www.elastic.co/guide/en/shield/current/shield-aaa-ov.html#privileges-list-indices)
* **Reference** [Support Matrix](https://www.elastic.co/support/matrix)

After the Elasticsearch user permissions are configured, you can proceed with connecting to a data source.

### Added Libraries Required to Connect Using a Transport Protocol

Self-Service Analytics extracts specific libraries needed to support secured connections to Elasticsearch clusters over a transport protocol. The Self-Service Analytics Elasticsearch connector starts and works normally without these libraries, except when you want to use secured transport connections. To use secured transport connections, you must download and enable these libraries. If you attempt to establish a secured transport connection to an Elasticsearch cluster without the required libraries, an error will occur when you try to validate the connection.

To download and enable the transport-required libraries:

1. Download the required libraries to `/opt/zoomdata/lib/edc-elasticsearch-<x.x>/` for Linux, and for `<install-path>/lib/edc-elasticsearch-<x.x>/` Windows, where `<x.x>` is the version of Elasticsearch.

   ```bash theme={null}
   mkdir -p /opt/zoomdata/lib/edc-elasticsearch-<x.x>
   wget -P /opt/zoomdata/lib/edc-elasticsearch-<x.x> <library URL>
   ```

   The following table provides a list of the required libraries for each supported Elasticsearch version, with URLs:

   <table>
     <thead>
       <tr>
         <th>Self-Service Analytics Connector</th>
         <th>Library Name</th>
         <th>Version</th>
         <th>License</th>
         <th>URL</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td rowSpan={3}>Elasticsearch 7.0</td>
         <td>org.elasticsearch.client:x-pack-transport</td>
         <td rowSpan={2}>7.0.0</td>
         <td rowSpan={2}>Commercial Software End User License Agreement ([https://www.elastic.co/eula](https://www.elastic.co/eula))</td>
         <td>[https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/7.0.0/x-pack-transport-7.0.0.jar](https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/7.0.0/x-pack-transport-7.0.0.jar)</td>
       </tr>

       <tr>
         <td>org.elasticsearch.plugin:x-pack-core</td>
         <td>[https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-core/7.0.0/x-pack-core-7.0.0.jar](https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-core/7.0.0/x-pack-core-7.0.0.jar)</td>
       </tr>

       <tr>
         <td>com.unboundid:unboundid-ldapsdk</td>
         <td>3.2.0</td>
         <td>GPLv2, LGPLv2.1, or UnboundID Free Use License ([https://docs.ldap.com/ldap-sdk/docs/LICENSE-UnboundID-LDAPSDK.txt](https://docs.ldap.com/ldap-sdk/docs/LICENSE-UnboundID-LDAPSDK.txt))</td>
         <td>[https://mvnrepository.com/artifact/com.unboundid/unboundid-ldapsdk/3.2.0](https://mvnrepository.com/artifact/com.unboundid/unboundid-ldapsdk/3.2.0)</td>
       </tr>
     </tbody>
   </table>

   For example:

   ```bash theme={null}
   mkdir -p /opt/zoomdata/lib/edc-elasticsearch-7.0
   wget -P /opt/zoomdata/lib/edc-elasticsearch-7.0 https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/7.0.0/x-pack-transport-7.0.0.jar

   wget -P /opt/zoomdata/lib/edc-elasticsearch-7.0 https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-api/7.0.0/x-pack-api-7.0.0.jar

   wget -P /opt/zoomdata/lib/edc-elasticsearch-7.0 http://central.maven.org/maven2/com/unboundid/unboundid-ldapsdk/3.2.0/unboundid-ldapsdk-3.2.0.jar
   ```

2. Update the `loader.path` property value in the appropriate Elasticsearch connector property file to point to the directory path containing all the libraries you downloaded or to a comma-separated list combining all library paths. For example:

   ```properties theme={null}
   loader.path=/opt/zoomdata/lib/edc-elasticsearch-7.0
   ```

   or

   ```
   loader.path=/opt/zoomdata/lib/edc-elasticsearch-7.0/x-pack-transport-7.0.0.jar,
   /opt/zoomdata/lib/edc-elasticsearch-7.0/x-pack-api-7.0.0.jar,
   /opt/zoomdata/lib/edc-elasticsearch-7.0/unboundid-ldapsdk-3.2.0.jar
   ```

   See [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) to determine the correct Elasticsearch property file to use and where to save it.

   <Note>
     In version 25.3 and earlier, use the path `datasource.driver-config.jar-path`.
   </Note>

   <Note>
     insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Self-Service Analytics is next upgraded.
   </Note>

   Quickly determine what changes you have made to a properties file using `diff` in Linux. For example:

   ```bash theme={null}
   diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
   ```

   or

   ```bash theme={null}
   diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
   ```

   For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

3. Restart the Elasticsearch connector microservice. For example:

   ```bash theme={null}
   sudo systemctl restart zoomdata-edc-elasticsearch-7.0
   ```

   or

   ```bash theme={null}
   ./bootstrap-composer.ps1 -ServicesAction restart
   ```

### Connection Via HTTP or Transport Protocol and Using SSL

You can connect to your Elasticsearch cluster using either HTTP or transport protocols. SSL is optional for the HTTP connection but is required for transport connections when connecting to an X-Pack secured Elasticsearch cluster.

<h2 id="elasticsearch-what-are-the-commonly-reported-issues">
  Elasticsearch: What Are the Commonly Reported Issues?
</h2>

**Why am I unable to define a Group-by after creating a visual?**

By default, the data within an Elasticsearch data source is stored as "text" fields. However, in order to set a group-by, the field needs to be set as type "attribute" or else it will not show up in the group-by section. Please check your fields to make sure that the appropriate fields you would like to group-by are set as "attribute" within your Elasticsearch data source.

**Why do my data source fields only contain single words?**

Every string field in Elasticsearch is analyzed by default. If your field is "analyzed", this means that each individual word within your string is tokenized/indexed, so they will return as separate values. Thus, if you want Elasticsearch to respect the string and not return the string as individual entities, please make sure to set the field to be "not analyzed" within your Elasticsearch data set.
