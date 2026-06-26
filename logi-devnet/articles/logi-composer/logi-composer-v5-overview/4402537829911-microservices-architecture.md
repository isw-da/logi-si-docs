---
title: "Microservices Architecture"
id: 4402537829911
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537829911-Microservices-Architecture
updated_at: 2021-09-15T02:22:07Z
---

# Microservices Architecture

# Microservices Architecture

The Composer platform is architected as a set of loosely-coupled Java microservices. Unlike traditional business intelligence software, which is deployed as a monolithic application, a microservices architecture allows for the following benefits:

* Faster deployment of new functionality
* Optimal resource management
* Faster recovery in some failure scenarios
* Greater deployment flexibility

Each Composer microservice runs in its own Java Virtual Machine (JVM) to optimize memory allocation and runtime attributes to meet its function and load. A failure in one microservice does not take down all of Composer, and recovery is faster because only the failed microservice needs to restart. Deploying new functionality, such as an updated or custom data store connector, occurs by auto-discovery, and without requiring a server restart.

Separately, Composer centralizes its metadata store in a relational database and includes an internal messaging queue. The communication protocols used by the microservices include WebSockets (for real-time bidirectional communication) and HTTP/S.

For more information about individual microservices, see:

* Composer server microservice for its [*Web-Based User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4402552850071-Web-Based-User-Interface)
* [*Query Engine Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552847639-Query-Engine-Microservice)
* [*Data Connector Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402537828631-Data-Connector-Microservices)
* [*Data Writer Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552846743-Data-Writer-Microservice)
* [*Service Monitor Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552848535-Service-Monitor-Microservice)
* [*Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552845719-Configuration-Microservice)
* [*Service Discovery Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402537829271-Service-Discovery-Microservice)
* [*Screenshot Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402537830551-Screenshot-Microservice)
* [*Tracing Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552849303-Tracing-Microservice)

The following links provide general information about all Composer microservices:

* [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4402537845655-Composer-Microservice-Name-Reference)
* [*Composer Microservice Startup Order*](https://devnet.logianalytics.com/hc/en-us/articles/4402537846295-Composer-Microservice-Startup-Order)
* [*Starting Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402552838935-Starting-Composer-Microservices)
* [*Stopping Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402537821719-Stopping-Composer-Microservices)
* [*Restarting Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402537819031-Restarting-Composer-Microservices)
* [*Manage Composer v5 Microservices Using the Command Line Utility*](https://devnet.logianalytics.com/hc/en-us/articles/4402552719767-Manage-Composer-v5-Microservices-Using-the-Command-Line-Utility)
