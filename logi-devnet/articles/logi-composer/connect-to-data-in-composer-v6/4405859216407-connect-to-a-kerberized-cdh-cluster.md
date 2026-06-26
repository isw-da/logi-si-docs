---
title: "Connect to a Kerberized CDH Cluster"
id: 4405859216407
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859216407-Connect-to-a-Kerberized-CDH-Cluster
updated_at: 2021-09-21T01:27:19Z
---

# Connect to a Kerberized CDH Cluster

# Connect to a Kerberized CDH Cluster

A secure CDH Cluster uses Kerberos authentication to validate and confirm access requests. You can set up Composer to connect to the secure CDH Cluster using the instructions provided below. Before establishing a connection to either type of cluster, review the prerequisites and be sure to obtain your Kerberos credentials.

* [*Obtain Kerberos Credentials*](#Obtainin)
* [*Configure an Impala Connector*](#Conf)
* [*Configure a Cloudera Search Connector*](#Configur)
* [*Connect to a Kerberized Data Source*](#Connecti)
* [*Use TLS Encryption with Kerberos Authentication*](#Using)

### Prerequisites

* To enable Kerberos for CDH distribution using Cloudera manager, see Cloudera's documentation [Configuring Authentication in Cloudera Manager.](https://docs.cloudera.com/documentation/manager/5-1-x/Configuring-Hadoop-Security-with-Cloudera-Manager/cm5chs_authentication_cm.html)

* Kerberos authentication requires precise time correspondence on all instances to work properly. You need to enable the Network Time Protocol service in your network. For more information, access the topic [Using the Network Time Protocol to Synchronize Time](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time).

## Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a
[principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the machine where Composer Impala connector is installed.
2. Generate the Kerberos principal and corresponding keytab for Composer microservice. Before you proceed, make sure that:

   * Composer or a Connector is running on a node with proper Kerberos configuration: `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from Impala server.
3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t zoomdata_principal .keytab zoomdata_principal@KERBEROS.REALM
   ```
4. Make the keytab accessible for the Composer Server or a connector:

   ```
   sudo mkdir /etc/zoomdata  
   sudo mv zoomdata_principal.keytab /etc/zoomdata  
   sudo chown zoomdata:zoomdata /etc/zoomdata/zoomdata_principal.keytab  
   sudo chmod 600 /etc/zoomdata/zoomdata_principal.keytab
   ```

## Configure an Impala Connector

1. Create or update the file named `/etc/zoomdata/edc-impala.properties`. If this file already exists, verify that the information below exists in the file:

   ```
   kerberos.krb5.conf.location=/etc/krb5.conf  
   kerberos.service.account.authentication=true  
   kerberos.service.account.principal=zoomdata_principal@KERBEROS.REALM  
   kerberos.service.account.keytab.location=/etc/zoomdata/zoomdata_principal.keytab
   ```
2. Restart the Impala connector:

   ```
   sudo systemctl restart zoomdata-edc-impala
   ```

## Configure a Cloudera Search Connector

1. Create or update the file named `/etc/zoomdata/edc-cloudera-search.properties`. If this file already exists, verify that the information below exists in the file:

   ```
   kerberos.krb5.conf.location=/etc/krb5.conf  
   kerberos.service.account.authentication=true  
   kerberos.service.account.principal=zoomdata_principal@KERBEROS.REALM  
   kerberos.service.account.keytab.location=/etc/zoomdata/zoomdata_principal.keytab
   ```
2. Restart the Cloudera Search microservice:

   ```
   sudo systemctl restart zoomdata-edc-cloudera-search
   ```

## Connect to a Kerberized Data Source

You are now ready to create the Cloudera Search or Impala source:

1. Open a new browser window and log into Composer.
2. Select **Sources**.
3. Select **Cloudera** **Search or** **Impala**.
4. Specify the name of your source and add a description (if desired). Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743909143/next-btn_43x25.png).
5. On the Connection tab, define the connection source. You can use an existing connection, if available, or create a new one. To create a new connection, select the **Input New Credentials** option button and specify the connection name and JDBC URL. Make sure that you enter the JDBC URL in the correct format.

   For Impala, specify:

   ```
   jdbc:hive2://<impala_host>:21050/;principal=<impala_principal@KERBEROS.REALM>
   ```

   For Cloudera Search, specify:

   ```
   cloudera.domain:2181/solr
   ```

   The JDBC URL for Cloudera Search needs to be the zookeeper URL of the Kerberized cluster.

   Replace the placeholders as follows:

   * For <impala\_host>, enter the IP address/host name of the Impala node you are connecting to.
   * For <impala\_principal@KERBEROS.REALM>, enter the principal of the node you are connecting to. To get the list of all Impala principals, navigate to Cloudera Manager > Administration > Security > Kerberos Credentials.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743909527/cloudera-kerberos-cdh_480x328.png)
6. Select![](https://devnet.logianalytics.com/hc/article_attachments/4406743910167/validate-btn_57x24.png). After successful validation, the values are saved. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743911191/next-btn_40x24.png).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you run into connection issues, verify that the Composer Server was restarted successfully. Access the troubleshooting topic [*Verify the Composer Server Restart*](https://devnet.logianalytics.com/hc/en-us/articles/4405851206807-Verify-the-Composer-Server-Restart)
   for assistance.

You can continue configuring the data source as needed.

After you have completed the configuration, Composer begins accessing the data source using `zoomdata_principal@KERBEROS.REALM` authenticated by its keytab in `/etc/zoomdata/zoomdata_principal.keytab`.

## Use TLS Encryption with Kerberos Authentication

See [*Connect to Impala with TLS (SSL) Enabled*](https://devnet.logianalytics.com/hc/en-us/articles/4405850939543-Connect-to-Impala-with-TLS-SSL-Enabled) for more details.
