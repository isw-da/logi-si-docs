---
title: "Migrate Properties to the Configuration Server"
id: 4405859368471
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859368471-Migrate-Properties-to-the-Configuration-Server
updated_at: 2021-09-21T01:28:47Z
---

# Migrate Properties to the Configuration Server

# Migrate Properties to the Configuration Server

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. See [*Use the Composer Configuration Microservice to Maintain Application Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859473687-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties) and [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice) for information about the configuration microservice.

A utility is provided that can be used to migrate the microservice properties from your standalone Composer server to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. The utility is located in the zoomdata tarball at `…/scripts/zoomdata/config-server-upload.jar`.

Run this utility using the following syntax:

```
java -jar config-server-upload.jar <service> <properties-file> <config-service-url>
```

where `<service>` is the microservice name, `<properties-file>` is the fully qualified file name of the properties file you want to migrate, and `<config-service-url>` is the URL of the configuration microservice (usually `http://localhost:8888/api/environment`).

The following example migrates the properties from `/etc/zoomdata/zoomdata.properties` for the Composer microservice to the configuration data in the high availability PostgreSQL data store at the URL `http://localhost:8888/api/environment`:

```
java -jar /opt/zoomdata/scripts/zoomdata/config-server-upload.jar zoomdata /etc/zoomdata/zoomdata.properties http://localhost:8888/api/environment
```

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) In high availability environments, you will need to run this utility for every type of microservice in the environment to ensure that you can maintain the properties for all microservices in the Service Monitor.
