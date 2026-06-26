---
title: "Migrate Properties to the Configuration Server"
id: 43701120193677
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120193677-Migrate-Properties-to-the-Configuration-Server
updated_at: 2026-05-29T14:08:41Z
---

# Migrate Properties to the Configuration Server

# Migrate Properties to the Configuration Server

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. See [Use the Composer  Configuration Microservice to Maintain Application Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701148945549-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties) and [Configure and Start the Configuration Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128284045-Configure-and-Start-the-Configuration-Microservice) for information about the configuration microservice.

A utility is provided that can be used to migrate the microservice properties from your standalone Composer server to the Composer configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. The utility is located in the zoomdata tarball at `…/scripts/zoomdata/config-server-upload.jar`.

Run this utility using the following syntax:

java -jar config-server-upload.jar <service> <properties-file> <config-service-url>

where `<service>` is the microservice name, `<properties-file>` is the fully qualified file name of the properties file you want to migrate, and `<config-service-url>` is the URL of the configuration microservice (usually `http://localhost:8888/api/environment`).

The following example migrates the properties from `/etc/zoomdata/zoomdata.properties` for the Composer microservice to the configuration data in the high availability PostgreSQL data store at the URL `http://localhost:8888/api/environment`:

java -jar /opt/zoomdata/scripts/zoomdata/config-server-upload.jar zoomdata /etc/zoomdata/zoomdata.properties http://localhost:8888/api/environment

**Note:** 
In high availability environments, you will need to run this utility for every type of microservice in the environment to ensure that you can maintain the properties for all microservices in the Service Monitor.
