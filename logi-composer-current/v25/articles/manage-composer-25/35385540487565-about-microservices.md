---
title: "About  Microservices"
id: 35385540487565
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices
updated_at: 2026-05-26T22:06:00Z
---

# About  Microservices

# About Microservices

You can manage microservices in CentOS environments or in supported Ubuntu environments. You can also manage the microservices using the Composer CLI.

See the following sections:

* [Enable Microservices](#Enable)
* [Start Microservices](#Start)
* [Restart Microservices](#Restart)
* [Stop Microservices](#Stop)
* [Disable Microservices](#Disable)
* [Microservice Startup Order](#Microse)

## Enable Microservices

You can also enable microservices using the CLI. See [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility).

To enable all Composer microservices, enter the following command:

sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')

To enable a specific Composer microservice, enter the following command:

sudo systemctl enable <service>

Replace `<service>` with the name of the Composer microservice. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Start Microservices

The list of microservices can be found in [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference). The order in which microservices should be started is described in  [Microservice Startup Order](#Microse).

You can also start microservices using the CLI. See [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility).

To start all Composer microservices, enter the following command:

sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')

To start a specific Composer microservice, enter the following command:

sudo systemctl start <service>

Replace `<service>` with the name of the Composer microservice. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Restart Microservices

You can also restart microservices using the CLI. See [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility).

**To restart all** Composer **microservices, enter the following command:**

sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')

**To restart a specific** Composer **microservice, enter the following command:**

sudo systemctl restart <service>

Replace `<service>` with the name of the Composer microservice. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Stop Microservices

You can also stop microservices using the CLI. See [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility).

To stop all Composer microservices, enter the following command:

sudo systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')

To stop a specific Composer microservice, enter the following command:

sudo systemctl stop <service>

Replace `<service>` with the name of the Composer microservice. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Disable Microservices

You can also disable microservices using the CLI. See [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility).

To disable all Composer microservices, enter the following command:

sudo systemctl disable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')

To disable a specific Composer microservice, enter the following command:

sudo systemctl disable <service>

Replace `<service>` with the name of the Composer microservice. See [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Microservice Startup Order

The only microservices that must be started first are the Postgres and Service Discovery microservices. The other microservices are more tolerant and can be started in any order.

Composer recommends starting microservices in the following order. You can start microservices using CentOS or Ubuntu commands or using the CLI. See  [Start Microservices](#Start) and [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility). A full list of Composer microservices can be found in [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

1. The Postgres microservice (`postgresql-<version>`) used for metadata storage (where `<version>` is the version of Postgres you have installed.
2. The Service Discovery microservice (`zoomdata-consul`) used for microservice discovery.
3. The connector microservices (in the format `zoomdata-edc-<connector_name>`) used to connect to different data stores. The following CentOS example starts all available connector microservices, rather than starting them individually:

   sudo systemctl start $(systemctl list-unit-files | grep zoomdata-edc | awk ‘{print $1}‘)
4. The query engine microservice (`zoomdata-query-engine`) used for query engine processing.
5. The `zoomdata-data-writer-postgresql` microservice.
6. The following optional microservices, if they are installed.

   * `zoomdata-admin-server`
   * `zoomdata-screenshot-service`
7. The main Composer microservice (`zoomdata`).
