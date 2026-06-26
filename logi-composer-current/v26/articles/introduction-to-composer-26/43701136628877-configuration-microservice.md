---
title: "Configuration Microservice"
id: 43701136628877
section: "Introduction to Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136628877-Configuration-Microservice
updated_at: 2026-05-29T14:09:00Z
---

# Configuration Microservice

# Configuration Microservice

The Composer configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Composer to easily integrate with its Spring-based microservices. It provides the mechanism by which Composer property settings can be maintained using the Service Monitor. The property settings are persisted in a supported PostgreSQL data store or in a GitHub repository.

A `config-server-upload.jar` utility is available that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the PostgreSQL data store, where the configuration microservice can maintain them. See [Migrate Properties to the Configuration Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120193677-Migrate-Properties-to-the-Configuration-Server).

For complete information, see [Use the Composer  Configuration Microservice to Maintain Application Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701148945549-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties).
