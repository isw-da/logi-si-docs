---
title: "Configuration Microservice"
id: 4405851115799
section: "Introduction to  Logi Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851115799-Configuration-Microservice
updated_at: 2022-01-12T21:23:10Z
---

# Configuration Microservice

# Configuration Microservice

The Composer configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Composer to easily integrate with its Spring-based microservices. It provides the mechanism by which Composer property settings can be maintained using the Service Monitor. The property settings are persisted in a supported PostgreSQL data store or in a GitHub repository.

A `config-server-upload.jar` utility is available that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the PostgreSQL data store, where the configuration microservice can maintain them. See [*Migrate Properties to the Configuration Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405859368471-Migrate-Properties-to-the-Configuration-Server).

For complete information, see [*Use the Composer Configuration Microservice to Maintain Application Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859473687-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties).
