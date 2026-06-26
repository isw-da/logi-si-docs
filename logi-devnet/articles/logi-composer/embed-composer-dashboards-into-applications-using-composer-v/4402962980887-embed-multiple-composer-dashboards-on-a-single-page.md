---
title: "Embed Multiple Composer Dashboards On a Single Page"
id: 4402962980887
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402962980887-Embed-Multiple-Composer-Dashboards-On-a-Single-Page
updated_at: 2022-04-19T21:39:26Z
---

# Embed Multiple Composer Dashboards On a Single Page

# Embed Multiple Composer Dashboards On a Single Page

You can embed multiple Composer dashboards on a single page of your application and in a single `<div>` in your application, including embedding one or more empty dashboards. You can also embed the same dashboard multiple times on a page and each embedded instance can use its own property settings (theme, mode, header, title). Finally, the dashboards can be embedded using different methods: you can embed one dashboard using [generated embed code](https://devnet.logianalytics.com/hc/en-us/articles/4402955569559-Embed-a-Dashboard-Using-a-Generated-Snippet-and-OAuth-Access-Tokens) and another dashboard using [JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4402962985111-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) When more than one dashboard is embedded in application, the [cross-visual filters](https://devnet.logianalytics.com/hc/en-us/articles/4402963028631-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.
