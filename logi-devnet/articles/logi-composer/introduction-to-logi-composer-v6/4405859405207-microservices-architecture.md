---
title: "Microservices Architecture"
id: 4405859405207
section: "Introduction to  Logi Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859405207-Microservices-Architecture
updated_at: 2021-09-21T01:29:08Z
---

# Microservices Architecture

# Microservices Architecture

The Composer platform is architected as a set of loosely-coupled Java microservices. Unlike traditional business intelligence software, which is deployed as a monolithic application, a microservices architecture allows for the following benefits:

* Faster deployment of new functionality
* Optimal resource management
* Faster recovery in some failure scenarios
* Greater deployment flexibility

Each Composer microservice runs in its own Java Virtual Machine (JVM) to optimize memory allocation and runtime attributes to meet its function and load. A failure in one microservice does not take down all Composer, and recovery is faster because only the failed microservice needs to restart. Deploying new functionality, such as an updated or custom data store connector, occurs by auto-discovery, and without requiring a server restart.

Separately, Composer centralizes its metadata store in a relational database and includes an internal messaging queue. The communication protocols used by the microservices include WebSockets (for real-time bidirectional communication) and HTTP/S.

For more information about individual microservices, see:

* Composer server microservice for its [*Web-Based User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4405851120663-Web-Based-User-Interface)
* [*Query Engine Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859406231-Query-Engine-Microservice)
* [*Data Connector Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851116951-Data-Connector-Microservices)
* [*Data Writer Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851118743-Data-Writer-Microservice)
* [*Service Monitor Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859407511-Service-Monitor-Microservice)
* [*Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851115799-Configuration-Microservice)
* [*Service Discovery Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851117847-Service-Discovery-Microservice)
* [*Screenshot Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851119639-Screenshot-Microservice)
* [*Tracing Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859408535-Tracing-Microservice)

The following links provide general information about all Composer microservices:

* [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference)
* [*Composer Microservice Startup Order*](https://devnet.logianalytics.com/hc/en-us/articles/4405851150615-Composer-Microservice-Startup-Order)
* [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices)
* [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices)
* [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices)
* [*Manage Composer v6 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4405850885527-Manage-Composer-v6-Microservices-Using-the-Command-Line-Utility)
