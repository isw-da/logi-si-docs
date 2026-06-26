---
title: "Migrate Custom Charts"
id: 4405859243927
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859243927-Migrate-Custom-Charts
updated_at: 2021-09-21T01:27:38Z
---

# Migrate Custom Charts

# Migrate Custom Charts

The custom chart CLI version 4 was introduced with Zoomdata 3.2. CLI version 5 was introduced in Composer 6.3. Older versions of the CLI (version 3 and earlier) create custom charts using different commands and a different file structure.

Composer recommends that you install CLI version 4 or 5 globally and migrate your custom charts created using version 3 or earlier to the new format as described here. Support for CLI version 3 has been dropped. The following table lists the version of the CLI supported by different versions of Zoomdata and Composer.

| CLI Version | Supported Versions |
| --- | --- |
| 4 | Zoomdata 4 and Composer 5.9 and earlier |
| 5 | Composer 5.9.1 and later |

Read about the file structure, API route differences, and command differences in [*File Structure Differences*](#File), [*API Route Differences*](#API%C2%A0Rout), and [*CLI Command Differences*](#CLI) before you complete the migration steps provided in [*Migration Procedure*](#Migratio).

## File Structure Differences

The following pictures depict the file structures of a customer visual created using the custom chart CLI.

#### Version 3 Custom Chart CLI File Structure

![](https://devnet.logianalytics.com/hc/article_attachments/4406743897879/cli-v3_308x197.png)

#### Version 4 & 5 Custom Chart CLI File Structure

![](https://devnet.logianalytics.com/hc/article_attachments/4406743898647/cli-v4_218x195.png)

## API Route Differences

Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

## CLI Command Differences

The command differences between CLI version 3 and CLI versions 4 and 5 are described in the following table:

| Command | CLI Version Support | | Description |
| --- | --- | --- | --- |
| v3 | v4/v5 |
| `zd-chart add` | Yes | No | Use the `zd-chart import` command instead in CLI version 4. |
| `zd-chart init` | No | Yes | Use this CLI version 4 command to create a new visual in a folder you specify. This command combines the functions of the `zd-chart create` and `zd-chart pull` commands. |
| `zd-chart edit` | Yes | Yes | With CLI version 4, this command updates the visual locally, but no longer pushes the updated visual to the server. |
| `zd-chart push` | Yes | Yes | With CLI version 4, this command pushes the new version 4 bundled format of a custom chart to the server. |
| `zd-chart import <zip-file-path>` | No | Yes | Use this CLI version 4 command to import a visual in a zip file. |
| `zd-chart watch` | Yes | Yes | With CLI version 4, this command watches changes in the `src` directory and pushes them to the server. |
| `zd-chart create` | Yes | No | Use the `zd-chart init` command instead in CLI version 4. |
| `zd-chart pull` | Yes | No | Use the `zd-chart init` command instead in CLI version 4. |

## Migration Procedure

The examples given in the procedure below describe how to migrate an existing custom chart (`old_bar`) to a new custom chart (`new_bar`) using the new version of the CLI. These examples assume you are using the globally installed `zoomdata-chart-cli`.

To migrate a custom chart created using CLI v3 to CLI 4 or CLI 5:

1. Create a new visual using the custom chart CLI version 4 or 5 `$zd-chart init` command. For example, the following command creates a new bar visual called `new_bar`:

   ```
   $ zd-chart init new_bar
   ```
2. Create a `/libs` directory inside the new custom chart. The following commands set up a `new_bar/libs` directory:

   ```
   $ cd new_bar  
   $ mkdir libs
   ```
3. Update the `package.json` file. Add dependencies for all libraries that you have in the older custom chart to the libraries for the new custom chart, except for the `echarts-all.js` and `zchart.js`. files. For example:

   ```
   "dependencies": {  
   "d3": "^3.5",  
   "lodash": "3.10.1",  
   ...  
   },
   ```
4. Copy the `visualization.json` file from the directory for the older custom chart to the directory for the new custom chart.
5. Copy the `echarts-all.js` and `zchart.js` files from the older custom chart `/libs` directory to the new custom chart `/libs` directory.
6. Copy the contents of the `/components` directory from the older custom chart to the `/src/components` directory of the new custom chart.
7. Add dependencies and import statements for all third-party libraries for the new custom chart. For example:

   ```
   "dependencies": {  
   "d3": "^3.5",  
   "lodash": "3.10.1",  
   "jquery": "^3.3.1"  
   },
   ```
8. Change the `src/index.js` file for the new custom chart.

   * Add imports from `./libs`
   * Add imports from `./src/components` (the order is important)

   For example:

   ```
   import '../libs/echarts-all';  
   import '../libs/zchart';  
   import * as d3 from 'd3';  
   import _ from 'lodash';  
   import './components/a3_HorizontalBarsMultiMetric';  
   import './components/a4_VerticalBarsMultiMetric';  
   import './components/style.css';  
   import './components/z6_initter';
   ```
9. Add your custom code for the new custom chart.
10. Install the dependencies.

    ```
    $ npm install
    ```
11. Build the new custom chart.

    ```
    $ npm run build
    ```
12. Push the new custom chart to the server.

    ```
    $ zd-chart push -d ./dist
    ```
