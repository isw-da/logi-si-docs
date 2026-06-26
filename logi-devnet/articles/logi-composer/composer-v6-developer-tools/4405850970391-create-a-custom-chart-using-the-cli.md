---
title: "Create a Custom Chart Using the CLI"
id: 4405850970391
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850970391-Create-a-Custom-Chart-Using-the-CLI
updated_at: 2021-09-21T01:27:34Z
---

# Create a Custom Chart Using the CLI

# Create a Custom Chart Using the CLI

A complete example of creating a custom chart using the custom chart CLI can be found in [*A Custom Chart Tutorial*](https://devnet.logianalytics.com/hc/en-us/articles/4405859250711-A-Custom-Chart-Tutorial).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

To create a custom chart locally using the custom chart CLI:

1. Open the Composer CLI.
2. Run the following command to create the visual.

   ```
   $ zd-chart init <path-to-visual>
   ```

   Optionally, you can provide a type parameter. Valid values are `single-group`, `multi-group,` or `raw`. The default is `single-group`. For example:

   ```
   $ zd-chart init -t multi-group <path-to-visual>
   ```

The `zd-chart init` command creates a directory in the specified path containing the files you need to get started. Here is a preview of the directory tree:

![](https://devnet.logianalytics.com/hc/article_attachments/4406747446167/init-dir-structure_240x139.png)

The following table describes the function of each file in the tree:

| File | Description |
| --- | --- |
| `package.json` | Lists the packages your visual depends on. For more information, see <https://docs.npmjs.com/creating-a-package-json-file>. |
| `src/index.css` | Your visual's CSS (style sheet) code. |
| `src/index.js` | Your visual's JavaScript code. Additional files can be used and imported into this file. |
| `visualization.json` | Contains the name, controls, and variables of your visual. |
| `webpack.config.js` | The [webpack configuration](https://webpack.js.org/configuration/). Webpack is used in visuals to bundle your code into a single file. |
