---
title: "Embeddable Analytics"
id: 43701137115533
section: "Introduction to Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701137115533-Embeddable-Analytics
updated_at: 2026-05-29T14:09:06Z
---

# Embeddable Analytics

# Embeddable Analytics

Composer was built for extensibility and for integrating business intelligence into other applications. Integrations can be used to pass context between applications and Composer as part of your workflow or data exploration experience.

There are several options for embedding analytics:

* White-label for rebranding Composer to display another organization’s logo, fonts, colors, etc. See [Product Customizations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701141852301-Product-Customizations).
* Data integration using the Composer API to run a query from your application and then display or use the data pulled by the query. The query definition is invoked by an *action* in the Composer UI and is based on the filters applied to a Composer visual and on the data and limit specifications in the application integration definition for the visual data source. The invoked action creates the query definition and sends it to your application. See [Integrate Visual Data Into Your Applications](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022145933-Integrate-Visual-Data-Into-Your-Applications).

The behavior of Composer visuals and dashboards when they are embedded into your applications is controlled by the interactivity settings for the visuals themselves. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).

ComposerREST APIs use common design practices to be easily navigable by any user. The APIs are documented with Swagger, allowing for interactive experiences when conducting experimentation and testing.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

**Important:** 
Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
