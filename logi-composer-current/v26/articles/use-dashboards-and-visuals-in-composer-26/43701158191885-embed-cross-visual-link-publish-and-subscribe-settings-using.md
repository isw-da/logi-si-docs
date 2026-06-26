---
title: "Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript"
id: 43701158191885
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701158191885-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript
updated_at: 2026-05-29T14:09:10Z
---

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided: `publish` and `subscribe`. After `embed.js` is run (see [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)), these methods become available for use with the global `Zoomdata` object on `window`.

Cross-visual links (channels) are used primarily for cross-visual filtering. Visuals can publish cross-visual filters for cross-visual links. Other visuals can listen (subscribe) to the links and apply them when a cross-visual filter is specified.

#### Prerequisites

Embedding applications should listen for the `composer-dashboard-loaded` event on the first embedded dashboard before calling these methods. See [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events).

See the following topics:

* [Supported Zoomdata Methods](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122942477-Supported-Zoomdata-Methods)
* [Supported Cross-Visual Publish JavaScript Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701142769165-Supported-Cross-Visual-Publish-JavaScript-Properties)
* [Published Cross-Visual JavaScript Message Structure](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113024781-Published-Cross-Visual-JavaScript-Message-Structure)
* [Supported Cross-Visual Subscribe JavaScript Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701125866253-Supported-Cross-Visual-Subscribe-JavaScript-Properties)
* [Embedded Dashboard Cross-Visual Publish and Subscribe Example](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122930317-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example)
