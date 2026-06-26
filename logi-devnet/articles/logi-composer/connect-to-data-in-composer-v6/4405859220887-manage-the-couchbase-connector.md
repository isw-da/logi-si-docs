---
title: "Manage the Couchbase Connector"
id: 4405859220887
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector
updated_at: 2021-09-21T01:27:21Z
---

# Manage the Couchbase Connector

# Manage the Couchbase Connector

The Composer Couchbase connector lets you access the data available in your Couchbase Data Platform storage using the Composer client. The Composer Couchbase connector supports Couchbase version 6.0.1 and Couchbase Community Edition 6.0.0.

Before you can establish a connection from Composer to Couchbase Data Platform, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Couchbase*](#Connecti) for details specific to the Couchbase connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Couchbase connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **N** | | |  |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **N** | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | N/A | | |  |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **N** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | | | The Couchbase & Couchbase Community Edition connector supports multivalued fields with some limitations. See the detailed description below this table. |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **N** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **N** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | | |  |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |

The following limitations exist for multivalued field support for the Couchbase connector (including nested fields when they are also multivalued fields):

* The COUNT, SUM, or AVG metric result for a computed single-value field will be inaccurate when it is combined with any multivalued field in the same query.
* The COUNT, SUM, or AVG metric result for a computed multivalued field will be inaccurate when it is combined with any other multivalued field in the same query.
* With the exception of the TEXT\_TO\_TIME row-level function, multivalued fields created using row-level expressions can only be used as a visual's group or metric (and in filters when the same multivalued field is used as the visual's group or metric).

The following examples show *valid* metric combinations:

```
COUNT(single_value_field1),SUM(single_value_field2),AVG(single_value_field3),
DISTINCT_COUNT(single_value_field4), MIN(single_value_field5), MAX(single_value_field6)
```

```
COUNT(multivalue_field),SUM(multivalue_field),AVG(multivalue_field),
DISTINCT_COUNT(multivalue_field), MIN(multivalue_field), MAX(multivalue_field)
```

```
DISTINCT_COUNT(single_value_field), MIN(multivalue_field1), MAX(multivalue_field2)
```

The following examples show *invalid* combinations of metrics:

```
COUNT(single_value_field), SUM(single_value_field), AVG(single_value_field), MIN(multivalue_field)
```

```
COUNT(multivalue_field1), SUM(multivalue_field2), AVG(multivalue_field1), MAX(multivalue_field2)
```

## Connect to Couchbase

To establish a connection to Couchbase, the default port is 8138. If SSL/TLS authentication is required, see [*Configure Couchbase TLS/SSL Support*](#Configur4).

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

* [*Configure TLS Server Authentication*](#Configur)
* [*Configure Client Certificate-Based Authentication for a Single Couchbase Connection*](#Configur2)
* [*Configure Client Certificate-Based Authentication for Multiple Couchbase Connections*](#Configur3)

### Configure TLS Server Authentication

To enable TLS for the Couchbase server connection, add the following properties to the `edc-couchbase.properties` file:

```
com.couchbase.sslEnabled=true
  
com.couchbase.sslTruststoreFile=<path_to_truststore_storing_rootCertificate.jks>
com.couchbase.sslTruststorePassword=<optional_truststore_password>
```

The `com.couchbase.sslEnabled` property must be set to `true`. The path you specify for the `com.couchbase.sslTruststoreFile` property must be accessible by the Composer Couchbase connector.

For information about modifying connector properties in property files, see [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files).

### Configure Client Certificate-Based Authentication for a Single Couchbase Connection

If your installation only needs client certificate-based authentication for a single Composer Couchbase connection, specify the certificate-based authentication using connector properties. You must have a keystore containing the client's identity as well as a keystore or truststore containing the root certificate required to authenticate the server. Use one of the following setup options:

* Use a password-protected Java keystore that contains the client's identity and the root certificate. If you select this option, enable client certificate-based authentication by specifying the following connector properties in the `edc-couchbase.properties` file:

  ```
  com.couchbase.sslEnabled=true
    
  com.couchbase.sslKeystoreFile=<path_to_keystore_storing_clientID_and_rootCertificate.jks>
  com.couchbase.sslKeystorePassword=<mandatory_keystore_password>
    
  com.couchbase.certAuthEnabled=true
  ```

  The `com.couchbase.sslEnabled` and `com.couchbase.certAuthEnabled` properties must be set to `true`.
* Use a password-protected Java keystore that contains only the client's identity and a separate Java truststore containing the root certificate. This approach allows you to share a single universal truststore containing all required root certificates among different services.

  If you select this option, enable client certificate-based authentication by specifying the following connector properties in the `edc-couchbase.properties` file:

  ```
  com.couchbase.sslEnabled=true
    
  com.couchbase.sslTruststoreFile=<path_to_truststore_storing_rootCertificate_only.jks>
  com.couchbase.sslTruststorePassword=<optional_truststore_password>
    
  com.couchbase.sslKeystoreFile=<path_to_keystore_storing_clientID_only.jks>
  com.couchbase.sslKeystorePassword=<mandatory_keystore_password>
    
  com.couchbase.certAuthEnabled=true
  ```

  The `com.couchbase.sslEnabled` and `com.couchbase.certAuthEnabled` properties must be set to `true`.

For information about modifying connector properties in property files, see [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files).

### Configure Client Certificate-Based Authentication for Multiple Couchbase Connections

If your installation needs client certificate-based authentication for multiple Composer Couchbase connections, specify the client certificate-based authentication information using Composer connection parameters in the definition of each connection. You must have a keystore containing the client's identity as well as a keystore or truststore containing the root certificate required to authenticate the server.

Two new input boxes have been added in the Composer UI when you create a Couchbase connection. Assuming your keystore contains both the required client identity and root certificate information, specifying the keystore information using these two input boxes is sufficient.

* Use the **Key Store Path** box to specify the path to the keystore. This path must be accessible by the Composer Couchbase connector, so your system administrator must upload all client keystores to the machine where the connector is running before you define the Couchbase connection in the UI.
* Use the **Key Store Password** box to specify the mandatory password for the keystore.

If your installation only uses the TLS keystore to store the client's identity and requires a separate truststore to store the root certificate, specify the following connector truststore properties in the `edc-couchbase.properties` file:

```
com.couchbase.sslEnabled=true
  
com.couchbase.sslTruststoreFile=<path_to_truststore_storing_rootCertificate_only.jks>
com.couchbase.sslTruststorePassword=<optional_truststore_password>
```

For information about modifying connector properties in property files, see [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files).
