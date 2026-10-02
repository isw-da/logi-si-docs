> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Amazon Redshift Connector

The Self-Service Analytics Amazon Redshift connector lets you access the data available in Amazon Redshift storage using the Self-Service Analytics client. The Amazon Redshift connector supports Amazon Redshift versions 1.0 to 2.1.0.32.

Before you can establish a connection from Self-Service Analytics to Amazon Redshift storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Amazon Redshift](#connect-to-amazon-redshift) and [Troubleshoot the Amazon Redshift Connector](#troubleshoot-the-amazon-redshift-connector) for details specific to the Amazon Redshift connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

## Feature Support

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
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | N/A |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **Y** |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | N/A |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **Y** |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **N** |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **Y** |

<Note>
  Amazon Redshift returns whole numbers for aggregates on columns of type DECIMAL and NUMERIC types which have a 0 scale (in other words, 0 decimal places).
</Note>

<h2 id="connect-to-amazon-redshift">
  Connect to Amazon Redshift
</h2>

<h3 id="verify-the-mtu-size-of-self-service-analytics">
  Verify the MTU Size of Self-Service Analytics
</h3>

Before you can establish a connection between Amazon Redshift and Self-Service Analytics, you must verify that the size of the maximum transmission unit (MTU) on your Self-Service Analytics server is set to 1500.

The MTU size determines the maximum size, in bytes, of a packet that can be transferred in one Ethernet frame over your network connection. If your MTU size is too large for the connection, you might experience incomplete query results, your query might hang, or the connection might be dropped altogether. For more information, see: [https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-drop-issues.html](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-drop-issues.html).

To review the MTU value, use the `ip` command:

```
$ ip addr show eth0
```

If you need to edit the MTU value and set the size to 1500, use the following `ip` command:

```
$ ip link set dev eth0 mtu 1500
```

### Configure and Reference the JDBC Driver

The Amazon Redshift connector requires a JDBC driver to be configured before you connect. You can download the driver from the vendor's site. If you are upgrading, keep in mind you need to configure the JDBC driver- see [Upgrade Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server). For more information, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver). The JDBC Driver for Redshift has more than one jar file that needs to be downloaded: be sure to place the files in the same location to avoid any issues.

When setting up your Amazon Redshift connection, you need to specify the JDBC URL. You can find the URL on the **Configuration** tab of a cluster under **Cluster Database Properties**. The format varies slightly based on the type of database being connected. For Amazon Redshift, use the following format: `jdbc:redshift://HOSTNAME:PORT/DATABASE_NAME` . If authentication has been set up, provide the user name and password.

<h2 id="troubleshoot-the-amazon-redshift-connector">
  Troubleshoot the Amazon Redshift Connector
</h2>

The Self-Service Analytics Amazon Redshift connector lets you access the data available in Amazon Redshift storage using the Self-Service Analytics client. You can troubleshoot out of memory errors that may occur when executing heavy queries against large databases.

### Out Of Memory Errors

To troubleshoot out of memory errors, you will need to set the connector log to [DEBUG mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#configure-self-service-analytics-logs). Edit the Redshift configuration file, `edc-redshift.properties`. See [Connector Properties and Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files). Use the information available in the log to adjust your environment to prevent further errors.

After you set your log to DEBUG mode, run your queries again. Review the logs, and use one or more approaches to resolve the out of memory issues.

* Rewrite your most memory-consuming queries to return more granular results.
* Increase the RAM allocation in your Self-Service Analytics environment for this connector. See [Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings).
* Increase the `wlm_query_slot` count in your AWS environment. See [Troubleshooting queries - Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting.html).
