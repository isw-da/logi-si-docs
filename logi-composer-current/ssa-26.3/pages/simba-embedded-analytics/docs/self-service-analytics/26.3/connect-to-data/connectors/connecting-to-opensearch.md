> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the OpenSearch Connector

The Self-Service Analytics OpenSearch connector lets you access the data available in the OpenSearch storage using the Self-Service Analytics client. The Self-Service Analytics

OpenSearch connector supports the following OpenSearch versions.

* OpenSearch 2.x to 2.17

<Warning>
  You cannot import or export OpenSearch data sources (or the visuals and dashboards that use those OpenSearch data sources) if the version of the OpenSearch connector in the Self-Service Analytics environment is different from the version used by the data sources. When you change connector versions in your Self-Service Analytics environment, we recommend that you also create new data source configurations (and associated visuals and dashboards) for the newer version.
</Warning>

Before you can establish a connection from Self-Service Analytics to OpenSearch storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to OpenSearch](#connect-to-opensearch) for details specific to the OpenSearch connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

For information on securing your OpenSearch environment, see [https://docs.opensearch.org/docs/2.19/install-and-configure/configuring-opensearch/security-settings/](https://docs.opensearch.org/docs/2.19/install-and-configure/configuring-opensearch/security-settings/).

This section covers the following topics:

* [OpenSearch Connector Feature Support](#opensearch-connector-feature-support)
* [Connect to OpenSearch](#connect-to-opensearch)
* [Connect to OpenSearch Using Amazon Web Services Authentication](#connect-to-opensearch-using-amazon-web-services-authentication)
* [OpenSearch Data Source Configuration Notes](#opensearch-data-source-configuration-notes)
* [Distinct Counts and Percentiles in OpenSearch](#distinct-counts-and-percentiles-in-opensearch)
* [Tokenization in OpenSearch](#tokenization-in-opensearch)
* [OpenSearch Connector IP Address Data Type Support](#opensearch-connector-ip-address-data-type-support)
* [OpenSearch Last Value Processing](#opensearch-last-value-processing)
* [OpenSearch Composite Aggregation](#opensearch-composite-aggregation)
* [OpenSearch Source Document Storage Configurations](#opensearch-source-document-storage-configurations)
* [OpenSearch Inner Hits Configuration Property](#opensearch-inner-hits-configuration-property)

<h2 id="connect-to-opensearch">
  Connect to OpenSearch
</h2>

When establishing a connection to an OpenSearch data store, make sure you:

1. Specify the connection string in the following format:

   | Protocol | Connection String Format | Example |
   | - | - | - |
   | HTTP/HTTPS | `<schema>://<host1>:<port1>,...,<hostN>:<postN>/<prefix>` | `http://ip-10-2-2-241.ec2.internal:80/es` |
   | Transport/Transports | `<schema>://<host1>:<port1>,...,<hostN>:<portN>` | `transports://10.2.2.2:9010,10.2.2.3:9010` |

   where `<schema>` is the protocol that you want to use:

   * `http` or `https` (with SSL support)
   * `transport` or `transports` (with SSL support)

2. Specify your OpenSearch **cluster name**.

3. If required, specify your OpenSearch **User Name** and **Password**.

4. Select **Validate** to confirm your connection.

To connect to your OpenSearch cluster and data set secured by X-Pack, see .

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

### Connect to OpenSearch with a Configured Custom Certificate

If your OpenSearch cluster is configured with a custom certificate, you should configure a truststore for the Elasticsearch connector.

**Connect to an OpenSearch data store with a configured custom certificate**

1. Copy a truststore to the machine on which the OpenSearch connector is running.

2. Add the following lines to file the appropriate OpenSearch `jvm` file.

   * For Linux: `/etc/zoomdata/edc-OpenSearch.jvm`. Copy these files from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
   * For Windows: , `<install-path>/edc-OpenSearch.jvm`. Copy these files from the `<install-path>/conf` directory if a copy is not in `<install-path>`.

   ```properties theme={null}
   -Djavax.net.ssl.trustStore=<path_to_truststore>
   -Djavax.net.ssl.trustStorePassword=<truststore_password>
   ```

   Replace:

   * `<path_to_truststore>` with an absolute path to your truststore
   * `<truststore_password>` with a password for your truststore

<h2 id="connect-to-opensearch-using-amazon-web-services-authentication">
  Connect to OpenSearch Using Amazon Web Services Authentication
</h2>

You can connect the Self-Service Analytics OpenSearch connectors to your OpenSearch data store using Amazon Web Services (AWS) credentials. After connecting, the Self-Service Analytics OpenSearch connectors work with AWS OpenSearch without any restrictions.

**Connect the OpenSearch connector to your OpenSearch data store using AWS authentication:**

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

1. Specify the AWS credentials in a standard AWS-format credentials file (see [Format of the credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-creds)) and store the file in the OpenSearch connector’s file system.

2. Edit the [OpenSearch properties file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) ( `edc-OpenSearch.properties`) and locate or add the `OpenSearch.aws.show-aws-connection-params` property to the file. This property indicates whether AWS-specific connection parameters should be shown when a new connector is created or the connection properties of an existing connector are refreshed. Valid values are `true` or `false`. The default is `false` (users will *not* see new AWS connection parameters).

   Set the value of this property to `true` and save the properties file. For more information about Self-Service Analytics properties files, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

3. Create a new OpenSearch connection or edit an existing one (see [Add Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections)).

   The AWS connection parameters appear in the UI. Supply values for them as described in the following table.

   | Parameter | Specify | Description |
   | - | - | - |
   | `AUTHENTICATE_WITH_AWS_CREDENTIALS` | `true` | Indicate whether authentication with AWS credentials should be used. Note that the OpenSearch username / password specification and AWS credentials cannot be simultaneously used for authentication. Valid values are `true` or `false`; the default is `false` (AWS credentials are not used). |
   | `AWS_REGION` | a valid region name | Specify the AWS region where the target OpenSearch service is running. This parameter is optional when host names in the connection string have the standard format `<domain>.<region>.es.amazonaws.com` (the region name can be extracted from the host name). However, when specified, it has priority over the region name included in the host name. |
   | `AWS_PROFILES_CONFIG_PATH` | the path to the credentials file | Specify the location of the AWS credentials file in the OpenSearch connector’s file system. This parameter is optional when the credentials file is in the default location (`~/.aws/credentials` for the user of the connector). |
   | `AWS_PROFILE` | a valid profile name in the AWS credentials file | Specify the profile to use within the AWS credentials file. This parameter is optional if you choose to use the `default` profile in the AWS credentials file. |

4. After you have specified all parameters necessary for the connection definition, save it. See [Add Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections).

<h2 id="opensearch-composite-aggregation">
  OpenSearch Composite Aggregation
</h2>

Composite aggregations are implemented by OpenSearch connectors. This support optimizes aggregations of OpenSearch data, except for queries with:

* histograms
* time groups with WEEK granularity
* multiple groups when group fields belong to different nested contexts.

An OpenSearch configuration property `elasticsearch.query.composite-agg.max-fetch-size` in the OpenSearch configuration file (`edc-elasticsearch-7.0.properties`) can be used to specify the maximum number of buckets to return for each query within a composite aggregation. Valid values must be greater than zero; the default value is 10000. This property corresponds to the OpenSearch setting `search.max_buckets`, that also has a default value of 10000. If you elect to increase the value of the `elasticsearch.query.composite-agg.max-fetch-size property`, be sure to correspondingly increase the value of the OpenSearch `search.max_buckets` setting.

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<h2 id="distinct-counts-and-percentiles-in-opensearch">
  Distinct Counts and Percentiles in OpenSearch
</h2>

Distinct count and percentiles metrics return approximate values in OpenSearch. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

You can change the value of the precision threshold by setting the `elasticsearch.query.cardinality.precision.threshold` property in the `zoomdata.properties` file.

See OpenSearch 's documentation on the following for more information:

* For OpenSearch, see the following for [percentiles](https://docs.opensearch.org/docs/2.19/search.html?q=percentiles) and [distinct count](https://docs.opensearch.org/docs/2.19/search.html?q=distinct%20count).

The table below lists all available properties that you can modify to work with OpenSearch.

| Property | Default | Use | Notes |
| - | - | - | - |
| elasticsearch.query.cardinality.precision.threshold | 1000 | control the level of accuracy of the distinct counts | The maximum supported value is 40000. However, insightsoftware does not recommend you set such value as it may result in performance issues and the data source itself may return errors. |
| elasticsearch.query.limit.nongrouped | 10000 | set the limit for the number of non-grouped records (per shard) to execute on. | |
| elasticsearch.query.limit.grouped | 10000 | set the limit for the number of grouped records (per shard) to execute on. | |

If you need to change the default settings, add the corresponding properties (listed above) to the `zoomdata.properties` file and assign the required values. For more details, see [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files).

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<h2 id="opensearch-data-source-configuration-notes">
  OpenSearch Data Source Configuration Notes
</h2>

When setting up an OpenSearch [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview), select the indices and aliases to be queried, and select the fields to be handled. You can do this in three steps:

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
         The fields for indexes are not refreshed. If new fields are added to your data source, they are added to Self-Service Analytics only after you select the **Manual Refresh** button on the **Cache** tab of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview). If there are some changes in the existing fields (for example, if a field has been removed) they will not be applied.
       </Note>

   <Note>
     Filtering by type is not supported.
   </Note>

When you connect to your OpenSearch data source, the additional service field **type** is added. The **type** field contains all the selected OpenSearch types you can visualize as attributes on your visuals.

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<h2 id="opensearch-connector-feature-support">
  OpenSearch Connector Feature Support
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

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<h2 id="opensearch-inner-hits-configuration-property">
  OpenSearch Inner Hits Configuration Property
</h2>

Use the Self-Service Analytics OpenSearch `elasticsearch.inner-hits.size property` to specify the maximum number of hits to return per `inner_hits` query (used for raw data requests involving nested fields). The default value is 100.

If you specify a value that is too small, the number of values returned for a nested field in a document with a large number of sub-documents may be limited. If you specify a value that is too large, excessive memory may be consumed.

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<Note>
  To learn more about this property, see [inner hits.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/inner-hits.html)
</Note>

<h2 id="opensearch-connector-ip-address-data-type-support">
  OpenSearch Connector IP Address Data Type Support
</h2>

The IP Address data type is supported for OpenSearch data connectors. Fields of this type are treated as ATTRIBUTEs and can be used in:

* An OpenSearch text search box. When searching via the text search, Self-Service Analytics also supports the CIDR notation for IP addresses.
* The Group By selection box.
* Filters, although Self-Service Analytics does not support CIDR notation in filters for an IP address field. An exact match is required.
* Row-level expressions. In row-level expressions, Self-Service Analytics treats IP addresses as strings and expect an exact match.

<h2 id="opensearch-last-value-processing">
  OpenSearch Last Value Processing
</h2>

There are situations in which the OpenSearch connector cannot compute the Last Value metric correctly.

1. When the original value *is* available for a metric field, an error appears in either of the following situations:

   * Both metric and group fields are nested and related.
   * Both metric and time fields are nested and related.

   <Note>
     The OpenSearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only in the following cases:
   </Note>

   * When the metric field is nested and neither the group or time field is located in the same hierarchy (group and time fields are either at the root level or belong to another hierarchy)
   * When the Last Value is an array.

2. When the original value *is not* available for a metric field (the result is fetched from doc values or stored fields), an error appears when the metric field is nested and the time field is not located on the same or lower level in the hierarchy.

   <Note>
     The OpenSearch connector still may not always choose the maximum value among several values for the Last Value of a time field. This should happen only when the Last Value is an array.
   </Note>

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>

<h2 id="opensearch-source-document-storage-configurations">
  OpenSearch Source Document Storage Configurations
</h2>

OpenSearch data stores generally store the original JSON source documents passed when Elasticsearch performs its document indexing in the `_source` field in the index. However, some organizations disable the `_source` field to save storage and thus do not store the original JSON source documents.

Self-Service Analytics OpenSearch connectors support OpenSearch data stores with any of the following source document configurations:

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

The data sources created from connections to OpenSearch data stores with any of these configurations function almost identically.

### Known Issue Summary

The following known issues exist when the `_source` field is disabled or when it is enabled with exclusions:

* **Raw data presentation will vary, depending on the source from which the raw field data is fetched.** In particular, fused data sources may be affected where OpenSearch indices with different mappings are joined (for example, when such indices are joined by an IP field and one of them allows Self-Service Analytics to fetch the data from the original documents but another requires Self-Service Analytics to fetch the data from doc values). See [Raw Data Differences](#raw-data-differences) .
* **The last value metric may be computed incorrectly for nested fields.** Last value metrics are computed incorrectly when a time field is higher in the nested hierarchy or when a time field does not belong to the same hierarchy as the metric field.
* **Raw data is not available for some nested fields in multi-index OpenSearch data sources.** When a nested field exists in some indices but is absent in other indices, the field's raw data is not available. It is represented as having a NULL value in all documents when it is included in a table.
* **Some nested fields are not searchable in multi-index data sources.** When a nested field exists in some indices but is absent in other indices, it cannot be used in text search queries. Such fields will not be used for text searches.

<h3 id="raw-data-differences">
  Raw Data Differences
</h3>

The following Self-Service Analytics functions are impacted by the source document storage configuration of your OpenSearch data stores:

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

<h2 id="tokenization-in-opensearch">
  Tokenization in OpenSearch
</h2>

Keep in mind that OpenSearch, by default, tokenizes or analyzes fields that are of type `text`. As a result, strings consisting of two or more words may become separate fields when connected to Self-Service Analytics (for example, city names like *Las Vegas*). To disable this process and ensure that a string field is not analyzed, specify its type as `keyword`:

```yaml theme={null}
City: {
	type: "keyword"
	}
```

To learn more about tokenization in Elasticsearch, see [Get Trained Models API.](https://www.elastic.co/guide/en/elasticsearch/reference/8.2/get-trained-models.html#ml-get-trained-models-query-params)

<Warning>
  If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search).
</Warning>
