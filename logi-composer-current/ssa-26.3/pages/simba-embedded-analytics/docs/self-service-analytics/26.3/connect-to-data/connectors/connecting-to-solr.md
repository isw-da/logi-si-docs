> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Apache Solr Connector

The Self-Service Analytics Apache Solr connector lets you access the data available in your Apache Solr databases using the Self-Service Analytics client. The Self-Service Analytics Apache Solr connector supports Apache Solr versions 7.4 through 8.4.

Before you can establish a connection from Self-Service Analytics to an Apache Solr database, a connector server needs to be installed, configured and enabled. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Apache Solr](#connect-to-apache-solr) for details specific to the Apache Solr connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

## Feature Support

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
      <td colSpan={3}>**N**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields)</td>
      <td colSpan={3}>**N**</td>

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
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2)</td>
      <td colSpan={3}>**N**</td>
      <td>The Apache Solr JSON API does not support metrics by multivalued fields.</td>
    </tr>

    <tr>
      <td>[Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures)</td>
      <td colSpan={3}>**N**</td>

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
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation)</td>
      <td colSpan={3}>**Y**</td>

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

In addition, Apache Solr supports the Request Handler field on the Tables/Indices tab of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview). You can use this box at the top of the Field table on the Tables/Indices tab to specify a request handler plug-in that defines the logic used when executing a search request.

For Kerberos authentication instructions, see [Connect to Apache Solr Data Stores That Use Kerberos Authentication](#connect-to-apache-solr-data-stores-that-use-kerberos). For instructions on using user delegation with the Apache Solr connector, see [Configure User Delegation for the Apache Solr Connector](#configure-user-delegation-for-the-apache-solr-connector).

<h2 id="connect-to-apache-solr">
  Connect to Apache Solr
</h2>

You can configure the Self-Service Analytics Apache Solr connector to connect to a kerberized Apache Solr data store. For more information, see [Connect to Apache Solr Data Stores That Use Kerberos Authentication](#connect-to-apache-solr-data-stores-that-use-kerberos).

When establishing a connection to Apache Solr, you must provide the following information.

1. Select the hosting type: **Standalone** or **Cloud**.

2. Specify a Solr Base URL.

3. Specify the version of the Solr source that you are going to connect to in the following format: `<major>.<minor>.<patch>`. This field is optional.

   While connecting to Solr, Self-Service Analytics first checks its version. If the version is not available, Self-Service Analytics checks the version that you have specified in this field and attempts to connect that version.

4. If authentication has been set up, provide the user name and password.

## Dashboard and Visual Considerations

Distinct count and percentiles metrics return approximate values in Solr, due to the nature of the data source. The precision of the result returned by distinct count metric depends on the precision threshold setting (default value is 1000).

When you create a bar chart using an Apache Solr data source, you can search for a specific word or phrase using the search box at the top of the dashboard. The **Details** tab displays the results.

<Note>
  Fields of time groupings with low time granularity may cause loading time issues for the data source.
</Note>

<h2 id="connect-to-apache-solr-data-stores-that-use-kerberos">
  Connect to Apache Solr Data Stores That Use Kerberos Authentication
</h2>

A secure standalone or cloud Apache Solr can use Kerberos authentication to validate and confirm access requests. You can set up Self-Service Analytics to connect to the secure Solr using the following instructions.

<h3 id="configure-self-service-analytics-microservices">
  Configure Self-Service Analytics Microservices
</h3>

#### Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a [principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the [CentOS](https://www.theurbanpenguin.com/configuring-a-centos-7-kerberos-kdc/) or [Ubuntu](https://help.ubuntu.com/lts/serverguide/kerberos.html#kerberos-linux-client) machine where the Self-Service Analytics server resides.

2. Generate the Kerberos principal and corresponding keytab for Self-Service Analytics microservice. Before you proceed, make sure that:

   * Self-Service Analytics microservice is running on a node with proper Kerberos configuration: `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from the Apache Solr server.

3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t <composer_principal>.keytab <composer_principal@KERBEROS.REALM>
   ```

4. Make the keytab accessible for Self-Service Analytics's Apache Solr connector:

   ```bash theme={null}
   sudo mkdir /etc/zoomdata sudo mv <composer_principal>.keytab /etc/zoomdata sudo chown zoomdata:zoomdata /etc/zoomdata/<composer_principal>.keytab sudo chmod 600 /etc/zoomdata/<composer_principal>.keytab
   ```

#### Configure the Apache Solr Connector

1. Create or update the file named `/etc/zoomdata/edc-apache-solr.properties`. If this file already exists, verify that the information below exists in the file:

   ```properties theme={null}
   kerberos.krb5.conf.location=/etc/krb5.conf kerberos.service.account.authentication=true kerberos.service.account.principal=<composer_principal@KERBEROS.REALM> kerberos.service.account.keytab.location=/etc/zoomdata/<composer_principal>.keytab
   ```

2. Restart the Apache Solr connector:

   ```bash theme={null}
   sudo systemctl restart zoomdata-edc-apache-solr
   ```

After you have obtained Kerberos credentials and configured the connector properties, follow the instructions provided in [Connect to Apache Solr](#connect-to-apache-solr) to complete the connection.

<h2 id="configure-user-delegation-for-the-apache-solr-connector">
  Configure User Delegation for the Apache Solr Connector
</h2>

User delegation is supported by Self-Service Analytics Apache Solr connectors.

### Prerequisites

A Solr Cloud cluster, version 6.4 or later, with Kerberos authentication must be available.

### Configuration Steps

User delegation configuration for Solr is performed in two steps:

1. Enable Kerberos delegation tokens.

   To enable Kerberos delegation tokens, set the Solr configuration parameter `solr.kerberos.delegation.token.enabled` to `true` (see [Using Delegation Tokens in the Kerberos Authentication Plugin](https://lucene.apache.org/solr/guide/8_1/kerberos-authentication-plugin.html) documentation) in the `solr.in.sh` file on each Solr node.

2. Configure proxy users and delegates.

   Configuration of proxy users and delegates is performed using these parameters in the `solr.in.sh` file on each Solr node:

   * ```
     solr.kerberos.impersonator.user.<USER>.users
     ```
   * ```
     solr.kerberos.impersonator.user.<USER>.groups
     ```
   * ```
     solr.kerberos.impersonator.user.<USER>.hosts.
     ```

   Consider the following example:

   ```properties theme={null}
   solr.kerberos.impersonator.user.proxy_user.groups=finance,marketing
   solr.kerberos.impersonator.user.proxy_user.hosts=*
   ```

   In this configuration, user `proxy_user` can impersonate users belonging to groups `finance` or `marketing` when connecting to a Solr instance from any host.

   all these parameters should be stored in file `solr.in.sh` on each Solr node.
