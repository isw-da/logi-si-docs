---
title: "Connect to OpenSearch"
id: 43701011633805
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011633805-Connect-to-OpenSearch
updated_at: 2026-05-29T14:07:48Z
---

# Connect to OpenSearch

# Connect to OpenSearch

When establishing a connection to an OpenSearch data store, make sure you:

1. Specify the connection string in the following format:

   | Protocol | Connection String Format | Example |
   | --- | --- | --- |
   | HTTP/HTTPS | `<schema>://<host1>:<port1>,...,<hostN>:<postN>/<prefix>` | `http://ip-10-2-2-241.ec2.internal:80/es` |
   | Transport/Transports | `<schema>://<host1>:<port1>,...,<hostN>:<portN>` | `transports://10.2.2.2:9010,10.2.2.3:9010` |

   where `<schema>` is the protocol that you want to use:

* `http` or `https` (with SSL support)
* `transport` or `transports` (with SSL support)

Bear in mind that you must specify the hosts within one cluster.

2. Specify your OpenSearch **cluster name**.
3. If required, specify your OpenSearch **User Name** and **Password**.
4. Select **Validate** to confirm your connection.

To connect to your OpenSearch cluster and data set secured by X-Pack, see .

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector).

## Connect to OpenSearch with a Configured Custom Certificate

If your OpenSearch cluster is configured with a custom certificate, you should configure a truststore for the Elasticsearch connector.

**Connect to an OpenSearch data store with a configured custom certificate**

1. Copy a truststore to the machine on which the OpenSearch connector is running.
2. Add the following lines to file the appropriate OpenSearch `jvm` file.

   * For Linux: `/etc/zoomdata/edc-OpenSearch.jvm`. Copy these files from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
   * For Windows: , `<install-path>/edc-OpenSearch.jvm`. Copy these files from the `<install-path>/conf` directory if a copy is not in `<install-path>`.

   -Djavax.net.ssl.trustStore=<path\_to\_truststore>  
   -Djavax.net.ssl.trustStorePassword=<truststore\_password>

   Replace:

   * `<path_to_truststore>` with an absolute path to your truststore
   * `<truststore_password>` with a password for your truststore
