---
title: "Embed Multiple Composer Dashboards On a Single Page"
id: 34932919997069
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919997069-Embed-Multiple-Composer-Dashboards-On-a-Single-Page
updated_at: 2026-05-26T22:07:18Z
---

# Embed Multiple Composer Dashboards On a Single Page

# Embed Multiple Composer Dashboards On a Single Page

You can embed multiple Composer dashboards on a single page of your application and in a single `<div>` in your application, including embedding one or more empty dashboards. You can also embed the same dashboard multiple times on a page and each embedded instance can use its own property settings (theme, mode, header, title). Finally, the dashboards can be embedded using different methods: you can embed one dashboard using [generated embed code](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932920270221-Embed-a-Dashboard-Using-a-Generated-Snippet-and-Trusted-Access-Tokens) and another dashboard using [JavaScript](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930219405-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

**Note:** 
When more than one dashboard is embedded in application, the [cross-visual filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107422477-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.
