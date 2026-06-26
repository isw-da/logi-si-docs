---
title: "Supported Custom Chart CLI\u00a0Versions"
id: 4405859246103
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859246103-Supported-Custom-Chart-CLI-Versions
updated_at: 2021-09-21T01:27:37Z
---

# Supported Custom Chart CLI Versions

# Supported Custom Chart CLI Versions

Composer supports the following versions of its custom chart CLI: 4 and 5.

Custom chart CLI version 4 must be used with Zoomdata 4 and with Composer 5.9 and earlier. CLI version 5 should be used with Composer 5.9.1 and later.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

A custom chart is bundled before it is pushed to the Composer server. Bundling can be accomplished using a tool such as webpack. This creates a `/dist` directory containing the necessary files required to send the visual to the Composer server.

Composer recommends that you install custom chart CLI version 4 or 5 globally and migrate any existing custom charts from older CLI versions to the CLI version 4 and 5 directory structure. See [*Migrate Custom Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859243927-Migrate-Custom-Charts).
