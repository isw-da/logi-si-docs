---
title: "Install Dependencies and Build the Custom Chart Using the CLI"
id: 4405850968599
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850968599-Install-Dependencies-and-Build-the-Custom-Chart-Using-the-CLI
updated_at: 2021-09-21T01:27:35Z
---

# Install Dependencies and Build the Custom Chart Using the CLI

# Install Dependencies and Build the Custom Chart Using the CLI

To install dependencies and build the custom chart using the custom chart CLI:

1. Run the following command at the root level of the newly created custom chart to install dependencies:

   ```
   npm install
   ```
2. Run the following command at the root level of the custom chart to build the chart:

   ```
   $ npm run build
   ```

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
