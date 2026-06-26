---
title: "Microservices Architecture"
id: 34933062714125
section: "Introduction to Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933062714125-Microservices-Architecture
updated_at: 2026-05-26T22:07:39Z
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

* Composer server microservice for its [Web-Based User Interface](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933102916877-Web-Based-User-Interface)
* [Query Engine Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933078692621-Query-Engine-Microservice)
* [Data Connector Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933102040205-Data-Connector-Microservices)
* [Data Writer Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933071011725-Data-Writer-Microservice)
* [Service Monitor Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933102723341-Service-Monitor-Microservice)
* [Configuration Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933101946765-Configuration-Microservice)
* [Service Discovery Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933070947085-Service-Discovery-Microservice)
* [Screenshot Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933102610573-Screenshot-Microservice)
* [Distributed Tracing for Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919325197-Distributed-Tracing-for-Composer)

The following links provide general information about all Composer microservices:

* [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference)
* [Microservice Startup Order](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Microse)
* [Start Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start)
* [Stop Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop)
* [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart)
* [Scaling Composer Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933050010381-Scaling-Composer-Microservices)
* [Manage Composer Microservices Using the Command Line Utility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658973325-Manage-Composer-Microservices-Using-the-Command-Line-Utility)
* [Composer System Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933022064781-Composer-System-Metrics)
