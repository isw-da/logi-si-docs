---
title: "Product Transition for Symphony Users"
id: 46598739387405
section: "Symphony Users"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46598739387405-Product-Transition-for-Symphony-Users
updated_at: 2026-10-12T20:18:58Z
---

# Product Transition for Symphony Users

With the release of 26.2, Symphony has been restructured into two separate offerings/products.

* Content previously managed in Visual Data Discovery or as embedded Visual Data Discovery content will be supported in Composer v26.2 [and later releases of Self-Service Analytics](https://embedded-analytics.zendesk.com/introduction "Composer 26.2 and later releases").
* Content previously managed in Managed Dashboards and Reports will be supported in [Dundas BI 26.2 and later releases of Custom Analytics](https://www.dundas.com/support/learning/documentation/ "Dundas BI 26.2 and later releases").

## Authentication Updates

Along with this update, if you used Symphony with Visual Data Discovery embedded content or Managed Dashboard APIs, you must update your [authentication workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701127697165 "authentication workflow"). Symphony used the Dundas BI authentication model, but going forward, will use the [Composer API](https://embedded-analytics.insightsoftware.com/api-current/ "Composer  API") authentication model.

## API Updates

API user management orchestration is also impacted by this transition. Symphony Tenants, Users and Groups were managed by Managed Dashboards (Dundas BI). For a successful transition, you must retarget the API calls to Composer 26.2 or later releases before you update your environment.

## Managing Your Environment Updates and Transition

For more information on how to plan and work through this transition, reach out to Technical Support for assistance.

## Documentation Updates

* [Simba Self-Service Analytics](https://embedded-analytics.zendesk.com/introduction)
* [Simba Custom Analytics](https://www.dundas.com/support/learning/documentation/)
