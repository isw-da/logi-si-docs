---
title: "Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript"
id: 34933125724685
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933125724685-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript
updated_at: 2026-05-26T22:07:48Z
---

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided: `publish` and `subscribe`. After `embed.js` is run (see [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930219405-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)), these methods become available for use with the global `Zoomdata` object on `window`.

Cross-visual links (channels) are used primarily for cross-visual filtering. Visuals can publish cross-visual filters for cross-visual links. Other visuals can listen (subscribe) to the links and apply them when a cross-visual filter is specified.

#### Prerequisites

Embedding applications should listen for the `composer-dashboard-loaded` event on the first embedded dashboard before calling these methods. See [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events).

See the following topics:

* [Supported Zoomdata Methods](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933106961933-Supported-Zoomdata-Methods)
* [Supported Cross-Visual Publish JavaScript Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933126393101-Supported-Cross-Visual-Publish-JavaScript-Properties)
* [Published Cross-Visual JavaScript Message Structure](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107048845-Published-Cross-Visual-JavaScript-Message-Structure)
* [Supported Cross-Visual Subscribe JavaScript Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933096035725-Supported-Cross-Visual-Subscribe-JavaScript-Properties)
* [Embedded Dashboard Cross-Visual Publish and Subscribe Example](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933126099597-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example)
