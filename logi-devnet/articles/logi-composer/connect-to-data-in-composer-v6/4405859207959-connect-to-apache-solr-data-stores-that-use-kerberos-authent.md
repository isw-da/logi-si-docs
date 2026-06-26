---
title: "Connect to Apache Solr Data Stores That Use Kerberos Authentication"
id: 4405859207959
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859207959-Connect-to-Apache-Solr-Data-Stores-That-Use-Kerberos-Authentication
updated_at: 2021-09-21T01:27:17Z
---

# Connect to Apache Solr Data Stores That Use Kerberos Authentication

# Connect to Apache Solr Data Stores That Use Kerberos Authentication

A secure standalone or cloud Apache Solr can use Kerberos authentication to validate and confirm access requests. You can set up Composer to connect to the secure Solr using the following instructions.

## Configure Composer Microservices

### Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a [principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the [CentOS](https://www.theurbanpenguin.com/configuring-a-centos-7-kerberos-kdc/) or [Ubuntu](https://help.ubuntu.com/lts/serverguide/kerberos.html#kerberos-linux-client) machine where the Composer server resides.
2. Generate the Kerberos principal and corresponding keytab for Composer microservice.
   Before you proceed, make sure that:

   * Composer microservice is running on a node with proper Kerberos configuration:
     `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from the Apache Solr server.
3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t <composer_principal>.keytab <composer_principal@KERBEROS.REALM>
   ```
4. Make the keytab accessible for Composer's Apache Solr connector:

   ```
   sudo mkdir /etc/zoomdata  
   sudo mv <composer_principal>.keytab /etc/zoomdata  
   sudo chown zoomdata:zoomdata /etc/zoomdata/<composer_principal>.keytab  
   sudo chmod 600 /etc/zoomdata/<composer_principal>.keytab
   ```

### Configure the Composer Apache Solr Connector

1. Create or update the file named `/etc/zoomdata/edc-apache-solr.properties`. If this file already exists, verify that the information below exists in the file:

   ```
   kerberos.krb5.conf.location=/etc/krb5.conf  
   kerberos.service.account.authentication=true  
   kerberos.service.account.principal=<composer_principal@KERBEROS.REALM>  
   kerberos.service.account.keytab.location=/etc/zoomdata/<composer_principal>.keytab
   ```
2. Restart the Apache Solr connector:

   ```
   sudo systemctl restart zoomdata-edc-apache-solr
   ```

After you have obtained Kerberos credentials and configured the connector properties, follow the instructions provided in [*Connect to Apache Solr*](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector#Connecti) to complete the connection.
