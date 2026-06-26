---
title: "Manage Composer Microservices Using the Command Line Utility"
id: 34932658973325
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility
updated_at: 2026-05-26T22:06:16Z
---

# Manage Composer Microservices Using the Command Line Utility

# Manage ComposerMicroservices Using the Command Line Utility

You can use the `zdmanage` CLI command to manage the various microservices that are deployed in the Composer environment. This command line utility is automatically installed when installing your software using the automated installation script. This utility script wraps underlying UNIX commands to help you perform common management operations such as stopping and starting Composer microservices.

## Prerequisites

To use the command line utility tool, you need root access.

## Using the Command Line Utility Tool

The `zdmanage` command line utility is located in the following directory:

/opt/zoomdata/bin/zdmanage

The `zdmanage` CLI command syntax is as follows:

zdmanage services <command> <service\_name>

The following commands (`<command>`) are supported:

| Command | Action |
| --- | --- |
| `list` | Displays all the Composer microservices installed in your deployment. |
| `status` | Provides a status of all Composer microservices in your environment. |
| `start` | Starts Composer microservices.  The order in which microservices should be restarted is described in  [Microservice Startup Order](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Microse). |
| `stop` | Stops Composer microservices. |
| `restart` | Restarts Composer microservices. |
| `enable` | Enables Composer microservices automatically when the OS starts up. |
| `disable` | Shuts down Composer microservices automatically when the OS starts up. |
| `configure` | Opens the specified Composer property file. |

For `<service_name>`, specify the microservice name or `all` (to apply the command to all Composer microservices). A complete list of the Composer microservices can be found in [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).

## Common Commands

Show all Composer microservices installed:

sudo /opt/zoomdata/bin/zdmanage services list

Provide a status of all installed Composer microservices:

sudo /opt/zoomdata/bin/zdmanage services status all

Show the status of the Composer web microservice:

sudo /opt/zoomdata/bin/zdmanage services status zoomdata

Stop a specific Composer microservice:

sudo /opt/zoomdata/bin/zdmanage services stop [zoomdata-service\_name]
