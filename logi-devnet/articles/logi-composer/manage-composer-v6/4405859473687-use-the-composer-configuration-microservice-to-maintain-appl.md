---
title: "Use the Composer Configuration Microservice to Maintain Application Properties"
id: 4405859473687
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859473687-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties
updated_at: 2021-11-24T14:54:49Z
---

# Use the Composer Configuration Microservice to Maintain Application Properties

# Use the Composer Configuration Microservice to Maintain Application Properties

You can use the Service Monitor to review and maintain the properties for each of the other Composer microservices. It provides a centralized location where Composer configuration properties can be maintained. However, it requires that the Composer configuration microservice be configured and started first.

The Composer configuration microservice is packaged with the [Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration) server, which allows Composer to easily integrate with its Spring-based microservices and provides the mechanism by which Composer property settings can be persisted in a supported PostgreSQL metastore or in a GitHub repository. The following diagram depicts this relationship.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743750551/spring-cloud-config-server-relationship_480x243.png)

After the Composer configuration microservice is installed and started, the properties can be maintained on the Service Monitor's Properties tab.

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Composer servers to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [*Migrate Properties to the Configuration Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405859368471-Migrate-Properties-to-the-Configuration-Server).

See the following sections:

* [*Set Up the Configuration Microservice Metadata Store or Repository*](https://devnet.logianalytics.com/hc/en-us/articles/4405859472535-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository)
* [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice)
* [*Maintain Application Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405851182359-Maintain-Application-Properties)
