---
title: "Enable Kerberos Authentication for Apache Phoenix Connectors"
id: 34932719212429
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932719212429-Enable-Kerberos-Authentication-for-Apache-Phoenix-Connectors
updated_at: 2026-05-26T22:06:27Z
---

# Enable Kerberos Authentication for Apache Phoenix Connectors

# Enable Kerberos Authentication for Apache Phoenix Connectors

Support for Kerberos authentication for Composer Apache Phoenix connectors is only provided for Phoenix 4.7 (and later) connectors. It is not provided for any version of the Phoenix QueryServer connector.

**Enable Kerberos authentication for Apache Phoenix connectors:**

1. Download `hbase-site.xml` and `core-site.xml` files from the Apache HDFS and HBase microservices. For example, for Hortonworks you can use the instructions at the following link: <https://docs.cloudera.com/HDPDocuments/Ambari-2.6.2.2/bk_ambari-operations/content/downloading_client_configs.html>.
2. Add the following configuration options to the `hbase-site.xml` file:

   <property>
   <name>hbase.myclient.principal</name>
   <value>YOUR\_PRINCIPAL</value>
   </property>
   <property>
   <name>hbase.myclient.keytab</name>
   <value>PATH\_TO\_YOUR\_KEYTAB</value>
   </property>

   Substitute the ID of your Kerberos principal for `YOUR_PRINCIPAL` and the path to your Kerberos keytab file for `PATH_TO_YOUR_KEYTAB`.
3. Verify that the `core-site.xml` file contains the following entry:

   <property>
   <name>hadoop.security.authentication</name>
   <value>kerberos</value>
   </property>
4. Make sure that the Apache Phoenix connector has access to the `hbase-site.xml` and `core-site.xml` files as well as the Kerberos keytab file you identified in `PATH_TO_YOUR_KEYTAB`. We recommend that you place these files in the `/etc/zoomdata/edc-phoenix` directory.
5. Add the following property to the `/etc/zoomdata/edc-phoenix-4.7.properties` file to direct the Apache Phoenix connector to the files you created

   datasource.config.files-path=/etc/zoomdata/edc-phoenix

   **Note:** Composer does not recommend that you provide the Kerberos principal ID and keytab file path using a JDBC URL. The Apache Phoenix driver has a bug that will not refresh a ticket after expiration.
