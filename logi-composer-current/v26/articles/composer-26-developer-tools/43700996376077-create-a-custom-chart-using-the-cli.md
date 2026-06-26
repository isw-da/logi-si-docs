---
title: "Create a Custom Chart Using the CLI"
id: 43700996376077
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996376077-Create-a-Custom-Chart-Using-the-CLI
updated_at: 2026-05-29T14:11:26Z
---

# Create a Custom Chart Using the CLI

# Create a Custom Chart Using the CLI

A complete example of creating a custom chart using the custom chart CLI can be found in [A Custom Chart Tutorial](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701028307597-A-Custom-Chart-Tutorial).

**Note:** Composer v24 Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

**Create a custom chart locally using the custom chart CLI**

1. Open the Composer CLI.
2. Run the following command to create the visual.

   $ cmp-chart init <path-to-visual>

   Optionally, you can provide a type parameter. Valid values are `single-group`, `multi-group,` or `raw`. The default is `single-group`. For example:

   $ cmp-chart init -t multi-group <path-to-visual>

The `cmp-chart init` command creates a directory in the specified path containing the files you need to get started. Here is a preview of the directory tree:

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242715883789)

The following table describes the function of each file in the tree:

| File | Description |
| --- | --- |
| `package.json` | Lists the packages your visual depends on. For more information, see <https://docs.npmjs.com/creating-a-package-json-file>. |
| `src/index.css` | Your visual's CSS (style sheet) code. |
| `src/index.js` | Your visual's JavaScript code. Additional files can be used and imported into this file. |
| `visualization.json` | Contains the name, controls, and variables of your visual. |
| `webpack.config.js` | The [webpack configuration](https://webpack.js.org/configuration/). Webpack is used in visuals to bundle your code into a single file. |
