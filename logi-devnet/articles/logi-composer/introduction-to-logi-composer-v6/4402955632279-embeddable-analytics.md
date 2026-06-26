---
title: "Embeddable Analytics"
id: 4402955632279
section: "Introduction to  Logi Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955632279-Embeddable-Analytics
updated_at: 2021-08-07T17:31:35Z
---

# Embeddable Analytics

# Embeddable Analytics

Composer was built for extensibility and for integrating business intelligence into other applications. Integrations can be used to pass context between applications and Composer as part of your workflow or data exploration experience.

There are several options for embedding analytics:

* White-label for rebranding Composer to display another organization’s logo, fonts, colors, etc. See [*Product Customizations*](https://devnet.logianalytics.com/hc/en-us/articles/4402963022487-Product-Customizations).
* Programmatic integration using JavaScript libraries to call Composer REST APIs. See [*Embed a Visual in Your Web Page*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438231-Embed-a-Visual-in-Your-Web-Page).
* Data integration using the Composer API to run a query from your application and then display or use the data pulled by the query. The query definition is invoked by an *action* in the Composer UI and is based on the filters applied to a Composer visual and on the data and limit specifications in the application integration definition for the visual data source. The invoked action creates the query definition and sends it to your application. See [*Integrate Visual Data Into Your Applications*](https://devnet.logianalytics.com/hc/en-us/articles/4402955426455-Integrate-Visual-Data-Into-Your-Applications).

The behavior of Composer visuals and dashboards when they are embedded into your applications is controlled by the interactivity settings for the visuals themselves. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402955732247-Control-How-Users-Interact-With-a-Visual).

Composer REST APIs use common design practices to be easily navigable by any user. The APIs are documented with Swagger, allowing for interactive experiences when conducting experimentation and testing.

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
