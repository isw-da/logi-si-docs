---
title: "Service Monitor Views"
id: 43701162961037
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162961037-Service-Monitor-Views
updated_at: 2026-05-29T14:10:29Z
---

# Service Monitor Views

# Service Monitor Views

The Composer Service Monitor UI includes the following views, each accessible via a menu option in the main menu on the Service Monitor UI page:

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242380171661)

Each view is described below.

* [Wallboard View](#Wallboar)
* [Applications View](#Applicat)
* [Journal View](#Journal)
* [Downloads View](#Download)
* [Properties View](#Properti)

## Wallboard View

The Wallboard view provides shows all the Composer microservice types used in your installation. You can access it by selecting the **Wallboard** menu option.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242366451469)

The Wallboard view shows how many instances of a Composer microservice are running and the length of time they have been running.

Select a microservice type to obtain detailed information about it. The detailed information available varies based on the microservice type, but may include metrics, health, environment, configuration properties, scheduled tasks, logging threads, audit log, and web mappings and HTTP traces for the microservice type.

## Applications View

Select **Applications** to access the Applications view.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242366687885)

The Applications view shows all the Composer microservice types used in your installation. It also identifies the instance URLs, and indicates how many instances there are of each and how long they have been running. If more than one instance of a microservice is running, you can expand the microservice type to see the specific instance URLs.

If you select the URL for a Composer microservice instance, you will launch the Composer UI for that instance. If you select the URL for a Service Monitor instance, you will launch the Service Monitor for that instance. If you select the URL for an instance of any other microservice, a page of metrics and other information appears for that instance of the microservice.

## Journal View

Select **Journal** to access the Journal view.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242381011981)

The Journal view allows you to review the journal entries for each Composer microservice type.

## Downloads View

Select **Downloads** to access the Downloads view.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242381264269)

The Downloads view can be used to collect a diagnostics bundle for you to send to Composer Support when necessary. See [Download the Diagnostics Bundle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069730317-Download-the-Diagnostics-Bundle) for more information.

## Properties View

Select **Properties** to access the Properties view.

This view allows you to review and maintain the properties for each of the other Composer microservices. It requires that the Composer configuration microservice be installed and started first. See [Use the Composer  Configuration Microservice to Maintain Application Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701148945549-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties).
