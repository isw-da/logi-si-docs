---
title: "Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript"
id: 4402963025687
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963025687-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript
updated_at: 2021-08-07T17:32:23Z
---

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided: `publish` and `subscribe`. After `embed.js` is run (see [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4402962985111-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)), these methods become available for use with the global `Zoomdata` object on `window`.

Cross-visual links (channels) are used primarily for cross-visual filtering. Visuals can publish cross-visual filters for cross-visual links. Other visuals can listen (subscribe) to the links and apply them when a cross-visual filter is specified.

#### Prerequisites

Embedding applications should listen for the `composer-dashboard-loaded` event on the first embedded dashboard before calling these methods. See [*Supported Composer v6 Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4402955573911-Supported-Composer-v6-Embedded-Events).

See the following topics:

* [*Supported Zoomdata Methods*](https://devnet.logianalytics.com/hc/en-us/articles/4402955641495-Supported-Zoomdata-Methods)
* [*Supported Cross-Visual Publish JavaScript Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4402955642135-Supported-Cross-Visual-Publish-JavaScript-Properties)
* [*Published Cross-Visual JavaScript Message Structure*](https://devnet.logianalytics.com/hc/en-us/articles/4402963026967-Published-Cross-Visual-JavaScript-Message-Structure)
* [*Supported Cross-Visual Subscribe JavaScript Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4402963027863-Supported-Cross-Visual-Subscribe-JavaScript-Properties)
* [*Embedded Dashboard Cross-Visual Publish and Subscribe Example*](https://devnet.logianalytics.com/hc/en-us/articles/4402955640855-Embedded-Dashboard-Cross-Visual-Publish-and-Subscribe-Example)
