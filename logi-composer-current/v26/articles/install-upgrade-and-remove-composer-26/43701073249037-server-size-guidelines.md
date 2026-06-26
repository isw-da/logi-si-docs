---
title: "Server Size Guidelines"
id: 43701073249037
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073249037-Server-Size-Guidelines
updated_at: 2026-05-29T14:08:49Z
---

# Server Size Guidelines

# Server Size Guidelines

To maximize the operational efficiency of Logi Composer., you need to take into account several factors to appropriately size the Logi Composer. server in your operating environment:

* Concurrent user count. This is the most important parameter that increases the load on the system. Concurrent users represent only a portion of the total number of available users in an organization who may access the Logi Composer. server at the same time. A single-node deployment can handle up to 100 concurrent users with acceptable performance. If you need more than 100 users, you should consider using several Logi Composer. nodes.
* Entity (users, data sources, visuals, dashboard, etc) count. The number of entities in the system doesn’t impact the performance of the system if you have up to 1000 instances of each entity type. If you want to support more than 1000 instances of each entity type you must allocate more resources than shown in the table below.
* Data cardinality. The amount of data processed doesn't affect the performance of Logi Composer., because Logi Composer. pushes the work for the queries down to your data stores and thus will rely on the performance of your data stores. However, if you have large data set and want to group the data by a high-cardinality field, you should increase the resource allocation for the query engine.
* High availability (HA). If your Logi Composer. environment is an HA environment, sizing requirements may double if each Logi Composer. microservice is running on multiple instances.

See also [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements) and [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support) for information about Logi Composer system requirements.

The table below reviews the recommended sizing guidelines for a single-node Logi Composer server. Keep in mind that the specifications provided are suggested starting points and reflect only **the minimum estimates**. Sizing for performance is impacted by many other factors outside of the ones mentioned here, such as where Logi Composer. resides, the types of data sources you are using, interactions between applications and data sources, and a variety of other factors.

The following sizing guidelines reflect testing of a single-node Logi Composer. server with up to 1000 concurrent users, 400 data sources, 500 dashboards, and 6000 visuals.

| Concurrent Users | Hardware Requirements | Time Opening Dashboard (12 Visuals) | Composer Web | Query Engine | Connector | PostgreSQL Metadata Store |
| --- | --- | --- | --- | --- | --- | --- |
| Up to 5 | Memory: 8 GB  CPU: 8 core Disk: 100 GB | 17 seconds | Memory: 2 GB | Memory: 1 GB | Memory: 512 MB | Memory: 512 MB |
| Up to 20 | Memory: 8 GB  CPU: 8 core Disk: 100 GB | 19 seconds | Memory: 2 GB | Memory: 1 GB | Memory: 512 MB | Memory: 512 MB |
| Up to 100 | Memory: 16 GB  CPU: 16 core Disk: 100 GB | 26 seconds | Memory: 4 GB  Configuration Settings:  `spring.datasource.hikari.maximum-pool-size=50` | Memory: 3 GB | Memory: 1 GB | Memory: 1 GB |
| Up to 1000 | Memory: 16 GB  CPU: 16 core Disk: 100 GB | 4 minutes | Memory: 5 GB  Configuration Settings:  `spring.datasource.hikari.maximum-pool-size=150 server.jetty.max-threads=1000 query.engine.service.maxConcurrentRequests=1000` | Memory: 4 GB  Configuration Settings:   ``` server.jetty.max-threads=1000 ``` | Memory: 1 GB | Memory: 1 GB |
