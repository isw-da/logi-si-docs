---
title: "High Availability Environment Support"
id: 4402537835031
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537835031-High-Availability-Environment-Support
updated_at: 2021-09-15T02:22:11Z
---

# High Availability Environment Support

# High Availability Environment Support

You can deploy Composer microservices as a high availability environment. Such an environment ensures that you can minimize the downtime caused by:

* hardware or software failures due to excessive resource use or other events
* software upgrades or updates

In a high availability Composer environment, you can deploy multiple instances of Composer to ensure that at least one instance of its microservices operates continuously. A load balancer is required to distribute the network traffic across your user-facing Composer nodes. Microservice load balancing and failover occur automatically within the Composer nodes themselves. In addition, you can monitor all microservices and collect diagnostic trace information for them using the Service Monitor in conjunction with the Tracing microservice. For more information, see [*Configure a High Availability Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4402552829847-Configure-a-High-Availability-Environment).

If you have the configuration microservice configured and running, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [*Migrating Properties to the Configuration Server*](https://devnet.logianalytics.com/hc/en-us/articles/4402537810711-Migrating-Properties-to-the-Configuration-Server).
