---
title: "Embeddable Analytics"
id: 4402537834391
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537834391-Embeddable-Analytics
updated_at: 2021-09-15T02:22:10Z
---

# Embeddable Analytics

# Embeddable Analytics

Composer was built for extensibility and for integrating business intelligence into other applications. Integrations can be used to pass context between applications and Composer as part of your workflow or data exploration experience.

There are several options for embedding analytics:

* White-label for rebranding Composer to display another organization’s logo, fonts, colors, etc. See [*Product Customizations*](https://devnet.logianalytics.com/hc/en-us/articles/4402537833111-Product-Customizations).
* Programmatic integration using JavaScript libraries to call Composer REST APIs. See [*Embed a Visual in Your Web Page*](https://devnet.logianalytics.com/hc/en-us/articles/4402537685015-Embed-a-Visual-in-Your-Web-Page).
* Data integration using the Composer API to run a query from your application and then display or use the data pulled by the query. The query definition is invoked by an *action* in the Composer UI and is based on the filters applied to a Composer visual and on the data and limit specifications in the application integration definition for the visual data source. The invoked action creates the query definition and sends it to your application. See [*Integrate Visual Data Into Your Applications*](https://devnet.logianalytics.com/hc/en-us/articles/4402552712983-Integrate-Visual-Data-Into-Your-Applications).

The behavior of Composer visuals and dashboards when they are embedded into your applications is controlled by the interactivity settings for the visuals themselves. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

Composer REST APIs use common design practices to be easily navigable by any user. The APIs are documented with Swagger, allowing for interactive experiences when conducting experimentation and testing.

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753450007/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
