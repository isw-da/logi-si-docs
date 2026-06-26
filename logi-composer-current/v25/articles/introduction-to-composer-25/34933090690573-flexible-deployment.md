---
title: "Flexible Deployment"
id: 34933090690573
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933090690573-Flexible-Deployment
updated_at: 2026-05-26T22:07:48Z
---

# Flexible Deployment

# Flexible Deployment

Composer microservices and related components can be deployed on-premise, in the cloud, or in hybrid environments, provided that the host server meets ​[operating system and hardware requirements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933029670157-Installation-Prerequisites). Additionally, Composer can query supported data sources in the cloud or on-premises, provided network-level connectivity exists between the host and the data store. As a best practice, SSL should be used on connections between Composer and a data store, especially when traversing network enclaves.

As a Java web application, Composer can meet increasing user concurrency requirements through horizontal scaling. Horizontal scale-out is achieved by replicating Composer behind a load balancer with a common metadata store for all nodes. This configuration also provides a higher degree of application availability, as traffic will be routed to healthy nodes in the event of an application or hardware failure on another node.

As the Composer microservices architecture matures, more microservices will be deployed independently for greater availability and optimized load management.
