---
title: "Configuration Microservice"
id: 34933101946765
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933101946765-Configuration-Microservice
updated_at: 2026-05-26T22:07:43Z
---

# Configuration Microservice

# Configuration Microservice

The Composer configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Composer to easily integrate with its Spring-based microservices. It provides the mechanism by which Composer property settings can be maintained using the Service Monitor. The property settings are persisted in a supported PostgreSQL data store or in a GitHub repository.

A `config-server-upload.jar` utility is available that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the PostgreSQL data store, where the configuration microservice can maintain them. See [Migrate Properties to the Configuration Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933009933965-Migrate-Properties-to-the-Configuration-Server).

For complete information, see [Use the Composer  Configuration Microservice to Maintain Application Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933169279757-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties).
