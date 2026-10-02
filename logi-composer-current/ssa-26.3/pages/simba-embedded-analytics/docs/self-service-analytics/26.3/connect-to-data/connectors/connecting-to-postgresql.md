> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the PostgreSQL Connector

The Self-Service Analytics PostgreSQL connector lets you access the data available in the PostgreSQL query engine using the Self-Service Analytics client. The Self-Service Analytics PostgreSQL connector supports PostgreSQL versions 9.6 through 17.4.

Before you can establish a connection from Self-Service Analytics to PostgreSQL storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to PostgreSQL](#connect-to-postgresql) for details specific to the PostgreSQL connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

### Feature Support

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| - | - |
| [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov) | **Y** |
| [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots) | **Y** |
| [Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2) | **Y** |
| [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) | **Y** |
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
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **Y** |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | N/A |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **Y** |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **N** |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **Y** |

<h3 id="connect-to-postgresql">
  Connect to PostgreSQL
</h3>

When establishing a connection to PostgreSQL, you must provide the following.

* Specify the connection name and JDBC URL. The JDBC URL format for PostgreSQL database being connected:

  ```
  jdbc:postgresql://POSTGRESQLHOST:PORT/DATABASE_NAME
  ```

* If authentication has been set up, provide the User Name and Password.
