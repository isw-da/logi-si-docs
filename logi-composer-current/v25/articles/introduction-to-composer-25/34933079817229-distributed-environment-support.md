---
title: "Distributed Environment Support"
id: 34933079817229
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933079817229-Distributed-Environment-Support
updated_at: 2026-05-26T22:07:49Z
---

# Distributed Environment Support

# Distributed Environment Support

You can deploy Composer microservices in a distribued environment. Such an environment ensures that you can minimize the downtime caused by:

* hardware or software failures due to excessive resource use or other events
* software upgrades or updates

You have two options for setting up a distributed Composer environment:

* **Load balancing:** Load balancing helps you scale Composer for hundreds of users. You can use load balancing both on-premises and with cloud deployments. A single set of microservices communicate with each other in a monolithic flow.

  For more information, see [Configure the Composer Server Behind a Load Balancer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932685439501-Configure-the-Composer-Server-Behind-a-Load-Balancer).
* **High Availability:** A high availability environment includes multiple Composer nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster. Each microservice communicates with others using service discovery.

  Different numbers of different types of microservices can be defined for the Composer nodes, although at least two of each must be installed.

  A high-availability load balancer is required to distribute the network traffic across your user-facing Composer nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Composer nodes themselves.

  For more information, see [Configure a High Availability Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933027142285-Configure-a-High-Availability-Environment).

If you have the configuration microservice configured and running, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [Migrate Properties to the Configuration Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933009933965-Migrate-Properties-to-the-Configuration-Server).
