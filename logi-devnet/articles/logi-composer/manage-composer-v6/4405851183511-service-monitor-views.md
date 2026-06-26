---
title: " Service Monitor Views"
id: 4405851183511
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851183511--Service-Monitor-Views
updated_at: 2021-09-21T01:29:40Z
---

#  Service Monitor Views

# Service Monitor Views

The Composer Service Monitor UI includes the following views, each accessible via a menu option in the main menu on the Service Monitor UI page:

![](https://devnet.logianalytics.com/hc/article_attachments/4406747398295/service-monitor-menu_672x24.png)

Each view is described in this section.

* [*Wallboard View*](#Wallboar)
* [*Applications View*](#Applicat)
* [*Journal View*](#Journal)
* [*Downloads View*](#Download)
* [*Properties View*](#Properti)

## Wallboard View

The Wallboard view provides shows all the Composer microservice types used in your installation. You can access it by selecting the **Wallboard** menu option.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743746455/service-monitor-wallboard_672x318.png)

The Wallboard view shows how many instances of a Composer microservice are running and the length of time they have been running.

Select a microservice type to obtain detailed information about it. The detailed information available varies based on the microservice type, but may include metrics, health, environment, configuration properties, scheduled tasks, logging threads, audit log, and web mappings and HTTP traces for the microservice type.

## Applications View

Select **Applications** to access the Applications view.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743746839/service-monitor-appl_576x264.png)

The Applications view shows all the Composer microservice types used in your installation. It also identifies the instance URLs, and indicates how many instances there are of each and how long they have been running. If more than one instance of a microservice is running, you can expand the microservice type to see the specific instance URLs.

If you select the URL for a Composer microservice instance, you will launch the Composer UI for that instance. If you select the URL for a Service Monitor instance, you will launch the Service Monitor for that instance. If you select the URL for an instance of any other microservice, a page of metrics and other information appears for that instance of the microservice.

## Journal View

Select **Journal** to access the Journal view.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747399063/service-monitor-journal_576x268.png)

The Journal view allows you to review the journal entries for each Composer microservice type.

## Downloads View

Select **Downloads** to access the Downloads view.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743750295/service-monitor-downloads_576x130.png)

The Downloads view can be used to collect a diagnostics bundle for you to send to Composer Support when necessary. See [*Download the Diagnostics Bundle*](https://devnet.logianalytics.com/hc/en-us/articles/4405851038615-Download-the-Diagnostics-Bundle) for more information.

## Properties View

Select **Properties** to access the Properties view.

This view allows you to review and maintain the properties for each of the other Composer microservices. It requires that the Composer configuration microservice be installed and started first. See [*Use the Composer Configuration Microservice to Maintain Application Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859473687-Use-the-Composer-Configuration-Microservice-to-Maintain-Application-Properties).
