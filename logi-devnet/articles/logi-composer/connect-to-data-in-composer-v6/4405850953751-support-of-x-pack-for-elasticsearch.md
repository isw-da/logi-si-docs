---
title: "Support of X-Pack for Elasticsearch"
id: 4405850953751
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850953751-Support-of-X-Pack-for-Elasticsearch
updated_at: 2021-09-21T01:30:41Z
---

# Support of X-Pack for Elasticsearch

# Support of X-Pack for Elasticsearch

Composer allows you to connect to your Elasticsearch cluster and data set secured by X-Pack.

X-Pack is an add-on offering for Elasticsearch that aims at securing the data on your cluster. Learn more about [X-Pack](https://www.elastic.co/guide/en/x-pack/current/elasticsearch-security.html).

## Configure Cluster or Index Privileges for a User

To connect to the Elasticsearch cluster, you need to create an Elasticsearch user and configure the access privileges for this user.

The access permissions for the Elasticsearch user determine the scope of the data available for querying by Composer users.

To work with Elasticsearch data, use X-Pack to grant the following minimal access privileges to the Elasticsearch user:

* **Monitor** privileges for [Elasticsearch Cluster](https://www.elastic.co/guide/en/shield/current/shield-privileges.html#privileges-list-cluster)
* **Manage** (to get the metadata) and **Read** (to read data) privileges for [Index](https://www.elastic.co/guide/en/shield/current/shield-privileges.html#privileges-list-indices)

After the Elasticsearch user permissions are configured, you can proceed with connecting to a data source.

## Add Libraries Required to Connect Using a Transport Protocol

Composer extracts specific libraries needed to support secured connections to Elasticsearch clusters over a transport protocol. The Composer Elasticsearch connector starts and works normally without these libraries, except when you want to use secured transport connections. To use secured transport connections, you must download and enable these libraries. If you attempt to establish a secured transport connection to an Elasticsearch cluster without the required libraries, an error will occur when you try to validate the connection.

To download and enable the transport-required libraries:

1. Download the required libraries to `/usr/local/share/java/zoomdata/edc-elasticsearch-<x.x>/`, where `<x.x>` is the version of Elasticsearch.

   ```
   mkdir -p /usr/local/share/java/zoomdata/edc-elasticsearch-<x.x>  
   wget -P /usr/local/share/java/zoomdata/edc-elasticsearch-<x.x> <library URL>
   ```

   The following table provides a list of the required libraries for each supported Elasticsearch version, with URLs:

   | Composer Connector | Library Name | Version | License | URL |
   | --- | --- | --- | --- | --- |
   | Elasticsearch 6.0 | org.elasticsearch.client:x-pack-transport | 6.0.0 | Commercial Software End User License Agreement (<https://www.elastic.co/eula>) | <https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/6.0.0/x-pack-transport-6.0.0.jar> |
   | org.elasticsearch.plugin:x-pack-api | <https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-api/6.0.0/x-pack-api-6.0.0.jar> |
   | com.unboundid:unboundid-ldapsdk | 3.2.0 | GPLv2, LGPLv2.1, or UnboundID Free Use License (<https://docs.ldap.com/ldap-sdk/docs/LICENSE-UnboundID-LDAPSDK.txt>) | <https://mvnrepository.com/artifact/com.unboundid/unboundid-ldapsdk/3.2.0> |
   | Elasticsearch 7.0 | org.elasticsearch.client:x-pack-transport | 7.0.0 | Commercial Software End User License Agreement (<https://www.elastic.co/eula>) | <https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/7.0.0/x-pack-transport-7.0.0.jar> |
   | org.elasticsearch.plugin:x-pack-core | <https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-core/7.0.0/x-pack-core-7.0.0.jar> |
   | com.unboundid:unboundid-ldapsdk | 3.2.0 | GPLv2, LGPLv2.1, or UnboundID Free Use License (<https://docs.ldap.com/ldap-sdk/docs/LICENSE-UnboundID-LDAPSDK.txt>) | <https://mvnrepository.com/artifact/com.unboundid/unboundid-ldapsdk/3.2.0> |

   For example:

   ```
   mkdir -p /usr/local/share/java/zoomdata/edc-elasticsearch-6.0  
   wget -P /usr/local/share/java/zoomdata/edc-elasticsearch-6.0 https://artifacts.elastic.co/maven/org/elasticsearch/client/x-pack-transport/6.0.0/x-pack-transport-6.0.0.jar
   wget -P /usr/local/share/java/zoomdata/edc-elasticsearch-6.0 https://artifacts.elastic.co/maven/org/elasticsearch/plugin/x-pack-api/6.0.0/x-pack-api-6.0.0.jar
   wget -P /usr/local/share/java/zoomdata/edc-elasticsearch-6.0 http://central.maven.org/maven2/com/unboundid/unboundid-ldapsdk/3.2.0/unboundid-ldapsdk-3.2.0.jar
   ```
2. Update the `datasource.driver-config.jar-path` property value in the appropriate Elasticsearch connector property file to point to the directory path containing all the libraries you downloaded or to a comma-separated list combining all library paths. For example:

   ```
   datasource.driver-config.jar-path=/usr/local/share/java/zoomdata/edc-elasticsearch-6.0
   ```

   or

   ```
   datasource.driver-config.jar-path=/usr/local/share/java/zoomdata/edc-elasticsearch-6.0/x-pack-transport-6.0.6.jar,
   /usr/local/share/java/zoomdata/edc-elasticsearch-6.0/x-pack-api-6.0.0.jar,
   /usr/local/share/java/zoomdata/edc-elasticsearch-6.0/unboundid-ldapsdk-3.2.0.jar
   ```

   See [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files) to determine the correct Elasticsearch property file to use and where to save it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Composer discourages changing properties in the `/opt/zoomdata/conf` directory. Instead we recommend that you copy the files you want to change to the `/etc/zoomdata` directory and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded. In addition, you can quickly determine what changes you've made to a properties file using `diff`. For example:

   ```
   diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
   ```

   or

   ```
   diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
   ```
3. Restart the Elasticsearch connector microservice. For example:

   ```
   sudo systemctl restart zoomdata-edc-elasticsearch-6.0
   ```

## Connection Via HTTP or Transport Protocol and Using SSL

You can connect to your Elasticsearch cluster using either HTTP or transport protocols. SSL is optional for the HTTP connection but is required for transport connections when connecting to an X-Pack secured Elasticsearch cluster.
