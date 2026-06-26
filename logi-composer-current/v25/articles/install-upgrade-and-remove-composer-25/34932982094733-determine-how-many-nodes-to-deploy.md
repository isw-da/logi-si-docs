---
title: "Determine How Many Nodes to Deploy"
id: 34932982094733
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982094733-Determine-How-Many-Nodes-to-Deploy
updated_at: 2026-05-26T22:07:22Z
---

# Determine How Many Nodes to Deploy

# Determine How Many Nodes to Deploy

To effectively implement high availability in your Composer environment, at least two nodes, each containing the following microservices, are required.

* Composer Web App microservice
* Query Engine microservice
* Data Writer microservice
* Appropriate connector microservices for your installation
* Configuration microservice

The Service Monitor and Screenshot microservices, as well as distributed tracing services, are not required on every node. Install these microservices on at least two nodes in your cluster to ensure that management of the nodes is retained should one node fail.

Finally, the Consul instance and the PostgreSQL data store used to store metadata, configuration data, and tracing data must be available to all the nodes in your Composer cluster. We recommend that you cluster the Consul instance and your PostgreSQL data store to ensure there is no single point of failure.
