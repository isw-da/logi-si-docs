---
title: "Composer Microservice Startup Order"
id: 4402963037847
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963037847-Composer-Microservice-Startup-Order
updated_at: 2021-08-07T17:31:44Z
---

# Composer Microservice Startup Order

# Composer Microservice Startup Order

The only microservices that must be started first are the Postgres and Service Discovery microservices. The other microservices are more tolerant and can be started in any order.

Composer recommends starting microservices in the following order. You can start microservices using CentOS or Ubuntu commands or using the CLI. See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402955609751-Start-Composer-Microservices) and [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438871-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility). A full list of Composer microservices can be found in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402963037079-Composer-Microservice-Name-Reference).

1. The Postgres microservice (`postgresql-<version>`) used for metadata storage (where `<version>` is the version of Postgres you have installed.
2. The Service Discovery microservice (`zoomdata-consul`) used for microservice discovery.
3. The connector microservices (in the format `zoomdata-edc-<connector_name>`) used to connect to different data stores. The following CentOS 7 example starts all available connector microservices, rather than starting them individually:

   ```
   sudo systemctl start $(systemctl list-unit-files | grep zoomdata-edc | awk ‘{print $1}‘)
   ```
4. The query engine microservice (`zoomdata-query-engine`) used for query engine processing.
5. The `zoomdata-data-writer-postgresql` microservice.
6. The following optional microservices, if they are installed.

   * `zoomdata-admin-server`
   * `zoomdata-tracing-server`
   * `zoomdata-screenshot-service`
7. The main Composer microservice (`zoomdata`).
