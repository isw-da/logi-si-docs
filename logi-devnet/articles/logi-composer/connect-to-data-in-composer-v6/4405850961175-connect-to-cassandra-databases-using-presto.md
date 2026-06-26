---
title: "Connect to Cassandra Databases Using Presto"
id: 4405850961175
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850961175-Connect-to-Cassandra-Databases-Using-Presto
updated_at: 2021-09-21T01:27:28Z
---

# Connect to Cassandra Databases Using Presto

# Connect to Cassandra Databases Using Presto

You can connect to Cassandra databases using the Composer [Presto connector](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector). The Cassandra database connection must use the Composer Presto connector because Cassandra does not directly support aggregated queries.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747446935/connecting-to-cassandra_576x175.png)

Before you can establish a connection from Composer to your Cassandra database, the Presto connector must be installed, configured, and enabled first by your Composer account administrator. See [*Manage the Presto Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector).

Composer Cassandra database support was verified with Presto 319.
While other versions of Presto might work with Cassandra databases, Composer cannot guarantee them.

After the Composer Presto connector has been set up, you must specify the JDBC URL for your Cassandra database connection:

```
jdbc:presto://<presto_server>:<presto_port>/<cassandra>
```

Replace `<cassandra>` with the value of the `connector.name` property in the `/<presto_server_path>/etc/catalog/cassandra.properties` file.

If authentication has been set up, provide the corresponding user name and password.
By default, set the user name to `user`. No password is required. Make sure that the Cassandra user has enough permissions to run SELECT queries.
