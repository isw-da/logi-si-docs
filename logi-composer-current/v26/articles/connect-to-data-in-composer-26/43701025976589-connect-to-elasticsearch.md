---
title: "Connect to Elasticsearch"
id: 43701025976589
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025976589-Connect-to-Elasticsearch
updated_at: 2026-05-29T14:07:44Z
---

# Connect to Elasticsearch

# Connect to Elasticsearch

When establishing a connection to an Elasticsearch data store, make sure you:

1. Specify the connection string in the following format:

   | Protocol | Connection String Format | Example |
   | --- | --- | --- |
   | HTTP/HTTPS | `<schema>://<host1>:<port1>,...,<hostN>:<postN>/<prefix>` | `http://ip-10-2-2-241.ec2.internal:80/es` |
   | Transport/Transports | `<schema>://<host1>:<port1>,...,<hostN>:<portN>` | `transports://10.2.2.2:9010,10.2.2.3:9010` |

   where `<schema>` is the protocol that you want to use:

* `http` or `https` (with SSL support)
* `transport` or `transports` (with SSL support)

Bear in mind that you must specify the hosts within one cluster.

**Important:** 
Elasticsearch 8 does not support transports. Use an `http://` or `https://` connection when connecting to or upgrading to Elasticsearch 8 by updating your connection string as needed, for example, replace `transport://1.1.1.1:9300,2.2.2.2:9300` with `https://localhost:9200`.

2. Specify your Elasticsearch **cluster name**.
3. If required, specify your Elasticsearch **User Name** and **Password**.
4. Select **Validate** to confirm your connection.

To connect to your Elasticsearch cluster and data set secured by X-Pack, see [Support of X-Pack for Elasticsearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701010802957-Support-of-X-Pack-for-Elasticsearch).

## Connect to Elasticsearch with a Configured Custom Certificate

If your Elasticsearch cluster is configured with a custom certificate, you should configure a truststore for the Elasticsearch connector.

**Connect to an Elasticsearch data store with a configured custom certificate**

1. Copy a truststore to the machine on which the Elasticsearch connector is running.
2. Add the following lines to file the appropriate Elasticsearch `jvm` file.

   * For Linux: , `/etc/zoomdata/edc-elasticsearch-7.0.jvm`, or `/etc/zoomdata/edc-elasticsearch-8.0.jvm`. Copy these files from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
   * For Windows: , `<install-path>/edc-elasticsearch-7.0.jvm` or `<install-path>/edc-elasticsearch-8.0.jvm`. Copy these files from the `<install-path>/conf` directory if a copy is not in `<install-path>`.

   -Djavax.net.ssl.trustStore=<path\_to\_truststore>  
   -Djavax.net.ssl.trustStorePassword=<truststore\_password>

   Replace:

   * `<path_to_truststore>` with an absolute path to your truststore
   * `<truststore_password>` with a password for your truststore
