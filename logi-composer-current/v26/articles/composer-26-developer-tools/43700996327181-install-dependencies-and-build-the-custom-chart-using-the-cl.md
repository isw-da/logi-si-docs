---
title: "Install Dependencies and Build the Custom Chart Using the CLI"
id: 43700996327181
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996327181-Install-Dependencies-and-Build-the-Custom-Chart-Using-the-CLI
updated_at: 2026-05-29T14:07:57Z
---

# Install Dependencies and Build the Custom Chart Using the CLI

# Install Dependencies and Build the Custom Chart Using the CLI

To install dependencies and build the custom chart using the custom chart CLI:

1. Run the following command at the root level of the newly created custom chart to install dependencies:

   npm install
2. Run the following command at the root level of the custom chart to build the chart:

   $ npm run build

**Note:** 
Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
