> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Dremio Connector

The Self-Service Analytics Dremio connector lets you access the data available in Dremio from supported versions of MySQL and MS SQL Server data stores using the Self-Service Analytics client. The Self-Service Analytics Dremio connector supports Dremio Community and Enterprise Editions version 4.1 through 4.8.

Before you can establish a connection from Self-Service Analytics to Dremio storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Dremio](#connect-to-dremio) for details specific to the Dremio connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

### Feature Support

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| - | - |
| [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov) | **N** |
| [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots) | **Y** |
| [Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2) | **N** |
| [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) | **N** |
| [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts) | **Y** |
| [Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values) | N/A |
| [Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields) | **Y** |
| [Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time) | **Y** |
| [Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time) | **Y** |
| [Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values) | **Y** |
| [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms) | **Y** |
| [Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso) | **N** |
| [Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value) | **Y** |
| [Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback) | **Y** |
| [Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2) | N/A |
| [Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures) | N/A |
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | N/A |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **N** |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | N/A |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **N** |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **N** |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **N** |

<h3 id="connect-to-dremio">
  Connect to Dremio
</h3>

The Dremio JDBC driver 3.0.6 is used by and included in the Dremio connector. Driver drop-in is supported, so you can replace this JDBC driver if you want. By default, the Dremio connector uses port 8142.

To create a Dremio connector, you must provide three parameters:

* The JDBC URL in a format supported by Dremio:

  ```
  jdbc:dremio:direct=<DREMIO_COORDINATOR>:<JDBC_PORT>[;schema=<OPTIONAL_SCHMEMA>]
  ```

  or

  ```
  jdbc:dremio:zk=<ZOOKEEPER_QUORUM>:<ZK_PORT>[;schema=<OPTIONAL_SCHEMA>]
  ```

* A valid user name

* A valid password.

### Live Mode and Playback Considerations

Dremio supports reflections instead of indices. For more information about Dremio reflections, see [https://docs.dremio.com/acceleration/](https://docs.dremio.com/acceleration/). Because Dremio does not support indices, Self-Service Analytics cannot accurately determine which date and number fields are playable, so it treats **all** date and time fields as playable, by default. Consequently, use livemode and playback judiciously when you are working with large data sets. Switch playback and live mode on only for visuals you know that the corresponding SQL queries are covered by a reflection and can be accelerated.

If you do not use Dremio reflections and are concerned that the default playability of all date and number fields might be misused and impact performance, you can switch this feature off using the connector configuration property: `metadata.detection.mark-all-date-and-int-fields-playable`. Valid values are `true` (on) and `false` (off). The default setting for this property is `true`.
