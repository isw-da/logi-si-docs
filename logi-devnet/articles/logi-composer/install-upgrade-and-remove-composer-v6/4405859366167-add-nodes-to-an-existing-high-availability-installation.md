---
title: "Add Nodes to an Existing High Availability Installation"
id: 4405859366167
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859366167-Add-Nodes-to-an-Existing-High-Availability-Installation
updated_at: 2021-09-21T01:28:45Z
---

# Add Nodes to an Existing High Availability Installation

# Add Nodes to an Existing High Availability Installation

To add Composer nodes (or instances) to an existing high availability environment:

1. If not already installed, install the Composer instance as though it were a single instance (and not running in a high availability environment). See [*Install Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859373719-Install-Composer).
2. Edit the `zoomdata.properties` and `query-engine.properties` files and ensure that the JDBC settings point to the PostgreSQL data store shared by the entire Composer cluster. Also ensure that the user name and password used to access the PostgreSQL data store are correct in these files. For information about the shared PostgreSQL data store, see [*Configure a High Availability Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851083287-Configure-a-High-Availability-Environment).
3. Edit the `consul.json` file on the instance you are adding.

   ```
   vi /etc/zoomdata/consul.json
   ```
4. Verify the `consul.json` file looks like this:

   ```
   {  
   "bind_addr": "0.0.0.0",  
   "bootstrap": false,  
   "bootstrap_expect": 2,  
   "client_addr": "0.0.0.0",  
   "data_dir": "/opt/zoomdata/data/consul",  
   "server": true  
   }
   ```

   A bind address (`bind_addr`) and client address (`client_addr`) of `0.0.0.0` allow the Consul to listen over all network interfaces. Depending on your network setup, you may want to explicitly specify an IP address for this.

   The `bootstrap_expect` value is the total number of Composer nodes (instances) in your Composer cluster and must be the same value on every instance in the cluster.
5. Restart all the Composer microservices for the instance. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).
6. Join each instance to the Consul cluster by running this command:

   ```
   /opt/zoomdata/bin/zoomdata-consul join <external-Consul-node-IP>
   ```

   You can verify that the node has joined the Consul cluster by running this command:

   ```
   /opt/zoomdata/bin/zoomdata-consul members
   ```
