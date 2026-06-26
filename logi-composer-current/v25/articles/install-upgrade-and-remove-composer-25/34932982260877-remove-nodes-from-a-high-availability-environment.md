---
title: "Remove Nodes from a High Availability Environment"
id: 34932982260877
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982260877-Remove-Nodes-from-a-High-Availability-Environment
updated_at: 2026-05-26T22:07:22Z
---

# Remove Nodes from a High Availability Environment

# Remove Nodes from a High Availability Environment

**Remove** Composer **nodes (or instances) from a high availability environment**

1. Run the following command on the instance:

   /opt/zoomdata/bin/zoomdata-consul leave -http-addr=http://<external-Consul-node-IP>:<port>

   where `<external-Consul-node-IP>` is the IP address of the Consul used by the high availability environment.
2. If the instance you are removing will be run standalone, edit the `zoomdata.properties``and query-engine.properties` files to point at a local PostgreSQL data store for that instance. Ensure that the JDBC settings point to the local PostgreSQL and that the user name and password used to access the local PostgreSQL data store are correct in these files. After changing the settings, restart all the Composer microservices for the instance. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

   If the instance you are removing will not be used at all, you can skip this step.
3. Edit the `consul.json` file on all the remaining Composer instances in your high availability environment.

   vi /etc/zoomdata/consul.json
4. Reduce the value specified for the `bootstrap_expect` setting by one. This value is the total number of Composer nodes (instances) in your Composer cluster and must be the same value on every instance in the cluster.
5. Restart the `zoomdata-consul` microservice on every Composer instance in the cluster to ensure they all pic up the node count change.
