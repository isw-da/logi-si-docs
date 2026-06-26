---
title: "Connect to Elasticsearch"
id: 4405850941591
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850941591-Connect-to-Elasticsearch
updated_at: 2021-09-21T01:27:23Z
---

# Connect to Elasticsearch

# Connect to Elasticsearch

When establishing a connection to an Elasticsearch data store, make sure you:

1. Specify the connection string in the following format:

   | Protocol | Connection String Format | Example |
   | --- | --- | --- |
   | HTTP/HTTPS | `<schema>://<host1>:<port1>,...,<hostN>:<postN>/<prefix>` | http://ip-10-2-2-241.ec2.internal:80/es |
   | Transport/Transports | `<schema>://<host1>:<port1>,...,<hostN>:<portN>` | transports://10.2.2.2:9010,10.2.2.3:9010 |

   where <schema> is the protocol that you want to use:

* `http` or `https` (with SSL support)
* `transport` or `transports` (with SSL support)

Bear in mind that you must specify the hosts within one cluster.

2. Specify your Elasticsearch **cluster name**.
3. If required, specify your Elasticsearch **User Name** and **Password**.
4. Select **Validate** to confirm your connection.

To connect to your Elasticsearch cluster and data set secured by X-Pack, see [*Support of X-Pack for Elasticsearch*](https://devnet.logianalytics.com/hc/en-us/articles/4405850953751-Support-of-X-Pack-for-Elasticsearch).

## Connect to Elasticsearch with a Configured Custom Certificate

If your Elasticsearch cluster is configured with a custom certificate, you should configure a truststore for the Elasticsearch connector.

To connect to an Elasticsearch data store with a configured custom certificate:

1. Copy a truststore to the machine on which the Elasticsearch connector is running.
2. Add the following lines to file `/etc/zoomdata/edc-elasticsearch-6.0.jvm` or `/etc/zoomdata/edc-elasticsearch-7.0.jvm`. Copy these files from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.

   ```
   -Djavax.net.ssl.trustStore=<path_to_truststore>  
   -Djavax.net.ssl.trustStorePassword=<truststore_password>
   ```

   Replace:

   * `<path_to_truststore>` with an absolute path to your truststore
   * `<truststore_password>` with a password for your truststore
