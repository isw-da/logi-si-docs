---
title: "Configure a Composer Distributed Environment"
id: 34932995107213
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932995107213-Configure-a-Composer-Distributed-Environment
updated_at: 2026-05-26T22:09:25Z
---

# Configure a Composer Distributed Environment

# Configure a Composer Distributed Environment

The Composer platform is architected as a set of loosely coupled Java microservices. They can be subdivided into the following categories when considering application availability:

* Core microservices - application components of Composer. These services provide key functionality in the application.
* Platform microservices - services that facilitate the operation and coordination between Composer's core microservices.
* Management microservices - services that provide views and controls for administration and troubleshooting of Composer's core microservices.

The communication protocols used by the microservices include WebSockets (for realtime bidirectional communication) and HTTP/HTTPS.

A metadata store is also needed to store Composer's metadata, application configuration data, and application trace data. Composer centralizes its metadata store in a relational database and includes an internal messaging queue.

The microservices and metadata store are depicted in the following diagram:

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167174971021)

You have two options for setting up a distributed Composer environment:

* **Load balancing:** Load balancing helps you scale Composer for hundreds of users. You can use load balancing both on-premises and with cloud deployments. A single set of microservices communicate with each other in a monolithic flow.

  For more information, see [Configure the Composer Server Behind a Load Balancer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932685439501-Configure-the-Composer-Server-Behind-a-Load-Balancer).
* **High Availability:** A high availability environment includes multiple Composer nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster. Each microservice communicates with others using service discovery.

  Different numbers of different types of microservices can be defined for the Composer nodes, although at least two of each must be installed.

  A high-availability load balancer is required to distribute the network traffic across your user-facing Composer nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Composer nodes themselves.

  For more information, see [Configure a High Availability Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933027142285-Configure-a-High-Availability-Environment).

Both load balancing and high availability require a centralized metadata store and a multi-node license. In a high availability environment, the metadata store can be clustered.

The configuration of load balancing and high availability are similar, but the high availability configuration is more complex in regards to its Consul configuration. To configure either, select one of the links above.

If you already have a distributed Composer environment in place, read  [Upgrade a Composer Distributed Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933183541261--Upgrade-a-Composer-Distributed-Environment) to upgrade it.
