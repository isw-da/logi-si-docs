---
title: "Connecting to MongoDB"
id: 4419707986455
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707986455-Connecting-to-MongoDB
updated_at: 2022-07-17T01:26:46Z
---

# Connecting to MongoDB

# Connecting to MongoDB

The most recent .NET and Java drivers shipped with Logi Info v12.7 work with MongoDB 2.6 through 4.0. Logi Info v12.6 supports MongoDB 2.6 through 3.6. If you're using an older version of MongoDB, such as 2.4, you cannot upgrade your Logi application to Info v12.6.
A specific Connection element, **Connection.MongoDB**, to used to connect to the database.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707210007/workmongodb_02.png)

As shown above, the **Connection.MongoDB** element is added to the **\_Settings** definition, beneath the Connections element. Attributes are set appropriately for the MongoDB datasource.

A **Mongo Params** element is available for use beneath Connection.MongoDB to supply additional options when connecting to the MongoDB database. Examples of additional parameters include "connectTimeoutMS" and "maxPoolSize". Refer
to the [MongoDB connection options documentation](http://docs.mongodb.org/manual/reference/connection-string/#connections-connection-options) for a the complete list of options.
