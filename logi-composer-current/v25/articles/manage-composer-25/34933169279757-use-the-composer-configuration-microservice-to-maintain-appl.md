---
title: "Use the Composer\u00a0 Configuration Microservice to Maintain Application Properties"
id: 34933169279757
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933169279757-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties
updated_at: 2026-05-26T22:09:21Z
---

# Use the Composer  Configuration Microservice to Maintain Application Properties

# Use the Composer  Configuration Microservice to Maintain Application Properties

You can use the Service Monitor to review and maintain the properties for each of the other Composer microservices. It provides a centralized location where Composer configuration properties can be maintained. However, it requires that the Composer configuration microservice be configured and started first.

The Composer configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Composer to easily integrate with its Spring-based microservices and provides the mechanism by which Composerproperty settings can be persisted in a supported PostgreSQL metastore or in a GitHub repository. The following diagram depicts this relationship.

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167030145549)

After the Composer configuration microservice is installed and started, the properties can be maintained on the Service Monitor's Properties tab.

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [Migrate Properties to the Configuration Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933009933965-Migrate-Properties-to-the-Configuration-Server).

See the following topics:

* [Set Up the Configuration Microservice Metadata Store or Repository](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933184485773-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository)
* [Configure and Start the Configuration Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933169035789-Configure-and-Start-the-Configuration-Microservice)
* [Maintain Application Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933148278541-Maintain-Application-Properties)
