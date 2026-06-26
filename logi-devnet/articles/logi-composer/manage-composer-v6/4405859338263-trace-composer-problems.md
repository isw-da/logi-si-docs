---
title: "Trace Composer Problems"
id: 4405859338263
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859338263-Trace-Composer-Problems
updated_at: 2021-09-21T01:28:25Z
---

# Trace Composer Problems

# Trace Composer Problems

The Composer tracing microservice provides some limited distributed tracing for Composer microservices. It collects information about requests and provides the ability to associate logs of the other microservices with the collected information. The tracing microservice name is `zoomdata-tracing-server`. To use the training microservice, you must install and start it to collect tracing information.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Only use the tracing microservice with assistance from Composer Support.

Composer tracing is enabled by default and is automatically discovered by the Consul and Composer microservices. No additional configuration should be necessary.

Web browser access is available on port 9411 (by default), however the interface does not require authentication at this time and access can only be restricted at the firewall. See [*Configure the Tracing Microservice Port*](https://devnet.logianalytics.com/hc/en-us/articles/4405851044887-Configure-the-Tracing-Microservice-Port).

* [*Install the Composer Tracing Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405851043991-Install-the-Composer-Tracing-Microservice)
* [*Enable and Disable Distributed Tracing*](https://devnet.logianalytics.com/hc/en-us/articles/4405851043095-Enable-and-Disable-Distributed-Tracing)
* [*Configure the Tracing Microservice Port*](https://devnet.logianalytics.com/hc/en-us/articles/4405851044887-Configure-the-Tracing-Microservice-Port)
* [*View a Trace*](https://devnet.logianalytics.com/hc/en-us/articles/4405851042199-View-a-Trace)
* [*Persist Traces*](https://devnet.logianalytics.com/hc/en-us/articles/4405851040407-Persist-Traces)
* [*Export a Trace*](https://devnet.logianalytics.com/hc/en-us/articles/4405851039511-Export-a-Trace)
* [*View an Exported Trace*](https://devnet.logianalytics.com/hc/en-us/articles/4405851041303-View-an-Exported-Trace)
