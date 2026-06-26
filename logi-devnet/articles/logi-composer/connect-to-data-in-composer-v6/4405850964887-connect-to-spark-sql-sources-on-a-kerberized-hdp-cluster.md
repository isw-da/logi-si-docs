---
title: "Connect to Spark SQL Sources on a Kerberized HDP Cluster"
id: 4405850964887
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850964887-Connect-to-Spark-SQL-Sources-on-a-Kerberized-HDP-Cluster
updated_at: 2023-06-16T14:10:41Z
---

# Connect to Spark SQL Sources on a Kerberized HDP Cluster

# Connect to Spark SQL Sources on a Kerberized HDP Cluster

A secure Hortonworks Data Platform (HDP) cluster uses Kerberos authentication to validate and confirm access requests. You can set up Composer to connect to the secure HDP cluster using the following instructions.

## Prepare the Spark SQL cluster

* To enable Kerberos for HDP distribution using a Spark SQL source, refer to Hortonwork's documentation [Enabling Kerberos Authentication Using Ambari](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.1/bk_security/content/configuring_amb_hdp_for_kerberos.html).
* Kerberos authentication requires precise time correspondence on all instances to work properly. You need to enable the Network Time Protocol service in your network. For more information, access the topic  [Using the Network Time Protocol to Synchronize Time](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time).
* Set up a Thrift JDBC/ODBC server in your environment. See [Spark documentation](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html).

## Configure Composer Microservices

### Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a [principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the [CentOS](https://www.theurbanpenguin.com/configuring-a-centos-7-kerberos-kdc/) or [Ubuntu](https://help.ubuntu.com/lts/serverguide/kerberos.html#kerberos-linux-client) machine where the Composer server resides.
2. Generate the Kerberos principal and corresponding keytab for the Composer microservice. Before you proceed, make sure that:

   * The Composer microservice is running on a node with proper Kerberos configuration: `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from the Spark SQL server.
3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t <composer_principal>.keytab <composer_principal@KERBEROS.REALM>
   ```
4. Make the keytab accessible for Composer's Spark SQL connector:

   ```
   sudo mkdir /etc/zoomdata  
   sudo mv <composer_principal>.keytab /etc/zoomdata  
   sudo chown zoomdata:zoomdata /etc/zoomdata/<composer_principal>.keytab  
   sudo chmod 600 /etc/zoomdata/<composer_principal>.keytab
   ```

### Configure a Spark SQL Connector

1. Create or update the file named `/etc/zoomdata/edc-sparksql.properties`. If this file already exists, verify that the information below exists in the file:

   ```
   kerberos.krb5.conf.location=/etc/krb5.conf  
   kerberos.service.account.authentication=true  
   kerberos.service.account.principal=<composer_principal@KERBEROS.REALM>  
   kerberos.service.account.keytab.location=/etc/zoomdata/<composer_principal>.keytab
   ```
2. Restart the Spark SQL connector:

   ```
   sudo systemctl restart zoomdata-edc-sparksql
   ```

### Connect to the Kerberized Spark SQL Source

You are now ready to create the Spark SQL source:

1. Open a new browser window and log into Composer.
2. Select **Sources**.
3. Select **Spark SQL**.
4. Specify the name of your source and add a description (if desired). Then select **Next**.
5. On the **Connection** page, define the connection source. You can use an existing connection, if available, or create a new one. To create a new connection, select the **Input New Credentials** option button and specify the connection name and JDBC URL. Make sure that you enter the JDBC URL in the correct format:

   ```
   jdbc:hive2://<spark-sql-host>:10000/;principal=<spark-sql-principal@KERBEROS.REALM>
   ```

   Replace the placeholders as follows:

   * `<spark_sql_host>`: Specify the IP address or host name of the Spark SQL node to which you are connecting.
   * `<spark_sql_principal@KERBEROS.REALM>`: Enter the principal of the Spark SQL node you are connecting to. To get the list of all Spark SQL principals, navigate to Ambari > Admin > Kerberos > Advanced > Spark SQL.

     ![](https://devnet.logianalytics.com/hc/article_attachments/15359960266647) The `principal` spec contained in the JDBC URL refers to the principal of the Spark SQL node. `spark_sql_principal@KERBEROS.REALM` principal has nothing to do with the `zoomdata_principal@KERBEROS.REALM` principal specified for the Composer connector.
6. Select **Validate** and, after your connection is valid, select **Next**.

You can continue configuring the data source as described in [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).

After you have completed the configuration, Composer will begin accessing Spark SQL using `zoomdata_principal@KERBEROS.REALM` authenticated by its keytab in `/etc/zoomdata/<composer_principal>.keytab`.
