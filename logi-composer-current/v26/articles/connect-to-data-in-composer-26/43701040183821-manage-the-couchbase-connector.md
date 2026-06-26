---
title: "Manage the Couchbase Connector"
id: 43701040183821
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector
updated_at: 2026-05-29T14:07:39Z
---

# Manage the Couchbase Connector

# Manage the Couchbase Connector

The Composer Couchbase connector lets you access the data available in your Couchbase Data Platform storage using the Composer client. The Composer Couchbase connector supports Couchbase version 6.0.1 and Couchbase Community Edition 6.0.0.

Before you can establish a connection from Composer to Couchbase Data Platform, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Couchbase](#Connecti) for details specific to the Couchbase connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) and [visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **N** | | |  |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A | | |  |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | N/A | | | The Couchbase & Couchbase Community Edition connector supports multivalued fields with some limitations. See the detailed description below this table. |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | **N** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **N** | | |  |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** | | |  |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | N/A | | |  |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **Y** | | |  |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **N** | | |  |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** | | |  |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** | | |  |

The following limitations exist for multivalued field support for the Couchbase connector (including nested fields when they are also multivalued fields):

* The COUNT, SUM, or AVG metric result for a computed single-value field will be inaccurate when it is combined with any multivalued field in the same query.
* The COUNT, SUM, or AVG metric result for a computed multivalued field will be inaccurate when it is combined with any other multivalued field in the same query.
* With the exception of the TEXT\_TO\_TIME row-level function, multivalued fields created using row-level expressions can only be used as a visual's group or metric (and in filters when the same multivalued field is used as the visual's group or metric).

The following examples show *valid* metric combinations:

COUNT(single\_value\_field1),SUM(single\_value\_field2),AVG(single\_value\_field3),
DISTINCT\_COUNT(single\_value\_field4), MIN(single\_value\_field5), MAX(single\_value\_field6)

COUNT(multivalue\_field),SUM(multivalue\_field),AVG(multivalue\_field),
DISTINCT\_COUNT(multivalue\_field), MIN(multivalue\_field), MAX(multivalue\_field)

DISTINCT\_COUNT(single\_value\_field), MIN(multivalue\_field1), MAX(multivalue\_field2)

The following examples show *invalid* combinations of metrics:

COUNT(single\_value\_field), SUM(single\_value\_field), AVG(single\_value\_field), MIN(multivalue\_field)

COUNT(multivalue\_field1), SUM(multivalue\_field2), AVG(multivalue\_field1), MAX(multivalue\_field2)

## Connect to Couchbase

To establish a connection to Couchbase, the default port is 8138. If SSL/TLS authentication is required, see [Configure Couchbase TLS/SSL Support](#Configur4).

By default, the Couchbase connector uses ports 8091, 8093, and 11210 in unencrypted mode and ports 18091, 18093, and 11207 in encrypted mode. Please make sure that these ports are not blocked by a firewall and are accessible to the connector.

Ordinarily, the port shown after the colon in a Couchbase URL is ignored and the defaults are used (for example, port 9999 will be ignored in `couchbase://localhost:9999`). If your Couchbase installation does not use the default ports, add at least one of the following HTTP parameters and preferably one of the carrier parameters to the Couchbase connection string. An HTTP parameter is required.

| Type | Property | Default Value |
| --- | --- | --- |
| HTTP | `bootstrapHttpDirectPort` | 8091 |
| HTTP-SSL | `bootstrapHttpSslPort` | 18091 |
| Carrier | `bootstrapCarrierDirectPort` | 11210 |
| Carrier-SSL | `bootstrapCarrierSslPort` | 11207 |

Here is an example of a valid connection string SSL (encrypted case) example using non-default HTTP port 18777 and non-default carrier port 11777:

```
couchbase://localhost?bootstrapHttpSslPort=18777&bootstrapCarrierSslPort=11777
```

## Configure Couchbase TLS/SSL Support

Couchbase can use the TLS protocol for:

* Full encryption of client-side traffic with server authentication. See [Connecting with SSL](https://docs.couchbase.com/java-sdk/2.7/managing-connections.html#ssl).
* Client authentication using X.509 certificates. This form of authentication is suitable for further Couchbase role-based access control. See [Certificate-Based Authentication](https://docs.couchbase.com/java-sdk/2.7/sdk-authentication-overview.html#certificate-based-authentication).

To support these capabilities in Composer's Couchbase connector, additional configuration is needed. See the following sections.

* [Configure TLS Server Authentication](#Configur)
* [Configure Client Certificate-Based Authentication for a Single Couchbase Connection](#Configur2)
* [Configure Client Certificate-Based Authentication for Multiple Couchbase Connections](#Configur3)

### Configure TLS Server Authentication

To enable TLS for the Couchbase server connection, add the following properties to the `edc-couchbase.properties` file:

com.couchbase.sslEnabled=true
  
com.couchbase.sslTruststoreFile=<path\_to\_truststore\_storing\_rootCertificate.jks>
com.couchbase.sslTruststorePassword=<optional\_truststore\_password>

The `com.couchbase.sslEnabled` property must be set to `true`. The path you specify for the `com.couchbase.sslTruststoreFile` property must be accessible by the Composer Couchbase connector.

For information about modifying connector properties in property files, see [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files).

### Configure Client Certificate-Based Authentication for a Single Couchbase Connection

If your installation only needs client certificate-based authentication for a single Composer Couchbase connection, specify the certificate-based authentication using connector properties. You must have a keystore containing the client's identity as well as a keystore or truststore containing the root certificate required to authenticate the server. Use one of the following setup options:

* Use a password-protected Java keystore that contains the client's identity and the root certificate. If you select this option, enable client certificate-based authentication by specifying the following connector properties in the `edc-couchbase.properties` file:

  com.couchbase.sslEnabled=true
    
  com.couchbase.sslKeystoreFile=<path\_to\_keystore\_storing\_clientID\_and\_rootCertificate.jks>
  com.couchbase.sslKeystorePassword=<mandatory\_keystore\_password>
    
  com.couchbase.certAuthEnabled=true

  The `com.couchbase.sslEnabled` and `com.couchbase.certAuthEnabled` properties must be set to `true`.
* Use a password-protected Java keystore that contains only the client's identity and a separate Java truststore containing the root certificate. This approach allows you to share a single universal truststore containing all required root certificates among different services.

  If you select this option, enable client certificate-based authentication by specifying the following connector properties in the `edc-couchbase.properties` file:

  com.couchbase.sslEnabled=true
    
  com.couchbase.sslTruststoreFile=<path\_to\_truststore\_storing\_rootCertificate\_only.jks>
  com.couchbase.sslTruststorePassword=<optional\_truststore\_password>
    
  com.couchbase.sslKeystoreFile=<path\_to\_keystore\_storing\_clientID\_only.jks>
  com.couchbase.sslKeystorePassword=<mandatory\_keystore\_password>
    
  com.couchbase.certAuthEnabled=true

  The `com.couchbase.sslEnabled` and `com.couchbase.certAuthEnabled` properties must be set to `true`.

For information about modifying connector properties in property files, see [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files).

### Configure Client Certificate-Based Authentication for Multiple Couchbase Connections

If your installation needs client certificate-based authentication for multiple Composer Couchbase connections, specify the client certificate-based authentication information using Composer connection parameters in the definition of each connection. You must have a keystore containing the client's identity as well as a keystore or truststore containing the root certificate required to authenticate the server.

Two new input boxes have been added in the Composer UI when you create a Couchbase connection. Assuming your keystore contains both the required client identity and root certificate information, specifying the keystore information using these two input boxes is sufficient.

* Use the **Key Store Path** box to specify the path to the keystore. This path must be accessible by the Composer Couchbase connector, so your system administrator must upload all client keystores to the machine where the connector is running before you define the Couchbase connection in the UI.
* Use the **Key Store Password** box to specify the mandatory password for the keystore.

If your installation only uses the TLS keystore to store the client's identity and requires a separate truststore to store the root certificate, specify the following connector truststore properties in the `edc-couchbase.properties` file:

com.couchbase.sslEnabled=true
  
com.couchbase.sslTruststoreFile=<path\_to\_truststore\_storing\_rootCertificate\_only.jks>
com.couchbase.sslTruststorePassword=<optional\_truststore\_password>

For information about modifying connector properties in property files, see [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files).
