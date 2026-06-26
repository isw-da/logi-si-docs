---
title: "Create a Custom Chart Using the CLI"
id: 34932783250829
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932783250829-Create-a-Custom-Chart-Using-the-CLI
updated_at: 2026-05-26T22:10:10Z
---

# Create a Custom Chart Using the CLI

# Create a Custom Chart Using the CLI

A complete example of creating a custom chart using the custom chart CLI can be found in [A Custom Chart Tutorial](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932762204557-A-Custom-Chart-Tutorial).

**Note:** Logi Composer Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

**Create a custom chart locally using the custom chart CLI**

1. Open the Composer CLI.
2. Run the following command to create the visual.

   $ cmp-chart init <path-to-visual>

   Optionally, you can provide a type parameter. Valid values are `single-group`, `multi-group,` or `raw`. The default is `single-group`. For example:

   $ cmp-chart init -t multi-group <path-to-visual>

The `cmp-chart init` command creates a directory in the specified path containing the files you need to get started. Here is a preview of the directory tree:

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167371590541)

The following table describes the function of each file in the tree:

| File | Description |
| --- | --- |
| `package.json` | Lists the packages your visual depends on. For more information, see <https://docs.npmjs.com/creating-a-package-json-file>. |
| `src/index.css` | Your visual's CSS (style sheet) code. |
| `src/index.js` | Your visual's JavaScript code. Additional files can be used and imported into this file. |
| `visualization.json` | Contains the name, controls, and variables of your visual. |
| `webpack.config.js` | The [webpack configuration](https://webpack.js.org/configuration/). Webpack is used in visuals to bundle your code into a single file. |
