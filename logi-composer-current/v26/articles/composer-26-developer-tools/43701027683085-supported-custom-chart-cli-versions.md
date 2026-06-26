---
title: "Supported Custom Chart CLI\u00a0Versions"
id: 43701027683085
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027683085-Supported-Custom-Chart-CLI-Versions
updated_at: 2026-05-29T14:07:59Z
---

# Supported Custom Chart CLI Versions

# Supported Custom Chart CLI Versions

Custom charts in Logi Composer can be created and managed using the Logi Composer Custom Chart CLI tool.

* Logi Composer Custom Chart CLI version 1 (`composer-chart-cli`) supports Logi Composer 7.10 and later, through this current release.
* CLI version 6 (`zoomdata-chart-cli`) supports Composer 7.10 and earlier.
* CLI version 5 (`zoomdata-chart-cli`) supports Composer 7.9 and earlier.

**Note:** Composer v24 Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

A custom chart is bundled before it is pushed to the Logi Composer server. Bundling can be accomplished using a tool such as webpack. This creates a `/dist` directory containing the necessary files required to send the visual to the Logi Composer server.

Existing custom charts from older CLI versions (5 and 6) use the same directory structure as the Logi Composer Custom Chart CLI version 1 directory structure.
