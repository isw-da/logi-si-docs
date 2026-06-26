---
title: "Determine How Many Nodes to Deploy"
id: 4405851082263
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851082263-Determine-How-Many-Nodes-to-Deploy
updated_at: 2021-09-21T01:28:46Z
---

# Determine How Many Nodes to Deploy

# Determine How Many Nodes to Deploy

To effectively implement high availability in your Composer environment, at least two nodes, each containing the following microservices, are required.

* Composer Web App microservice
* Query Engine microservice
* Data Writer microservice
* Appropriate connector microservices for your installation
* Configuration microservice

The Service Monitor, Screenshot, and Tracing microservices are not required on every node, but Composer recommends that you install these microservices on at least two nodes in your cluster to ensure that management of the nodes is retained should one node fail.

Finally, the Consul instance and the PostgreSQL data store used to store metadata, configuration data, and tracing data must be available to all the nodes in your Composer cluster. We recommend that you cluster the Consul instance and your PostgreSQL data store to ensure there is no single point of failure.
