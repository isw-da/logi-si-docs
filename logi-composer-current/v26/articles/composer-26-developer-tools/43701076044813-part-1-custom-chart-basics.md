---
title: "Part 1: Custom Chart Basics"
id: 43701076044813
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076044813-Part-1-Custom-Chart-Basics
updated_at: 2026-05-29T14:11:22Z
---

# Part 1: Custom Chart Basics

# Part 1: Custom Chart Basics

This part of the custom chart tutorial introduces you to the Custom Chart CLI, how to create a chart with sample code, how to edit the chart’s code, and how to preview the chart. The following steps are performed in Part 1:

* [Step 1. Check Your Development Environment](#Step)
* [Step 2. Install & Configure the Composer Custom Chart CLI](#Step2)
* [Step 3. Create a Custom Chart with Sample Code](#Step3)
* [Step 4. Edit the Chart Code](#Step4)
* [Step 5. Preview the Chart](#Step5)

## Step 1. Check Your Development Environment

Verify that you have everything set up to start creating custom charts with Composer.

* A valid version of `node.js` must be installed. `Node.js` is a programming tool for running JavaScript on servers and in your computer’s terminal. The Composer custom chart CLI is built using `node.js`.
* A valid version of `npm` must be installed. It is usually installed with `node.js`.
* Composer v22 or later must be installed.

**Verify that you have valid versions of node.js and npm installed**

1. Open a terminal window on your computer.
2. Enter `node --version` in the terminal window. The version of `node.js` installed on your computer is shown in the window. The minimum supported version of `node.js` by the Composer custom chart CLI is version 10.
3. Enter `npm --version` in the terminal window. The version of npm installed on your computer is shown in the window. The minimum supported version of `npm` supported by the Composer custom chart CLI (`composer-chart-cli`)for Composer v7.10 and later is version 1.

If `node.js` and npm are not installed, go to [https://nodejs.org/](https://nodejs.org/en/) and install the recommended version for your operating system.

## Step 2. Install & Configure the Composer Custom Chart CLI

Composer uses the custom chart CLI to build, edit, and remove custom charts.

**Install and configure the CLI**

1. Enter the following command in the terminal window.

   npm install composer-chart-cli@1 -g
2. After the CLI is installed, enter the following command in the terminal window:

   cmp-chart config
3. The `config` command prompts you to supply the following information:

   * Your Composer server URL.
   * The user name to use for authentication (typically: `admin`).

     **Note:** 
     You must be an administrator to manage custom visual types.
   * The password for the user name.
4. After entering this information, a prompt asks whether the configuration content should be stored in an encrypted file residing in your home directory (`~/.config/composer/cmp-chart.pref`). Enter **y** to finish configuring your environment.
5. Verify that everything is set up correctly by listing the custom charts available on the configured server using the following command:

   cmp-chart ls

   **Note:** 
   If your Composer instance does not have any custom charts defined, the output of this command is an empty list. If your instance does have custom charts defined, verify that they are correctly listed in the terminal window.

## Step 3. Create a Custom Chart with Sample Code

You can specify one of three chart types to get you started:

* Single Group
* Multigroup
* Raw

This tutorial uses the default Single Group template — a chart skeleton with minimal code designed to make you familiar with the basics of the custom chart API.

**Complete the following steps to create a single-group custom chart:**

1. Enter the following command in the terminal window:

   cmp-chart init ./my-first-custom-chart
2. The `init` command creates a directory in the specified path containing the files you need to get started. Here is a preview of the directory tree:

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242700515725)

   The following table describes the function of each of the files.

   | File Name | Description |
   | --- | --- |
   | `package.json` | Lists the packages on which your chart depends. For more information, see <https://docs.npmjs.com/creating-a-package-json-file>. |
   | `visualization.json` | Contains information about the name, controls, and variables of your chart. |
   | `webpack.config.js` | Contains configuration information for webpack. Webpack is used in charts to bundle your code into a single file. For more information, see <https://webpack.js.org/configuration/>. |
   | `src/index.js` | The main entry point to your chart’s Javascript code. Additional files can be used and imported into `index.js`. |
   | `src/index.css` | The main entry point to your chart’s CSS (style sheet) code. |
3. Install the default `devDependencies` listed in the `package.json` file. This step is required before you can work with the chart’s code. In a terminal window, `cd` to your chart’s root directory and run the following command:

   npm install
4. To use a similar naming convention as the out-of-the-box charts, update the chart’s name in the `visualization.json` file to “My First Custom Chart”. Save the file.

## Step 4. Edit the Chart Code

Composer’s custom charts are comprised of CSS and JS files that make up the chart’s code. The chart CLI lets you update the chart’s code in the server in one of two ways:

* You can push an updated local copy of the chart back to the server.
* You can use **watch** mode to continuously check for changes to the local component files and automatically update your Composer server’s copy.

Throughout this tutorial, we continuously modify the code and preview the changes. It is best to use **watch** mode in this scenario.

**Start watch mode**

1. Compile a development version of the chart’s code using the webpack bundler. In the terminal window from the root directory of the chart, enter the following command:

   npm start
2. In a different terminal window, push the chart for the first time to the configured server:

   cmp-chart push
3. Set up watch mode to continuously update the chart on the Composer server as the code changes. Enter the following command in the second terminal window:

   cmp-chart watch

   The `npm start` command instructs webpack to compile the code into a single `visualization.js` file and continuously watches for changes in the `src` files to update the chart as necessary. The `cmp-chart watch` command running in a separate terminal window starts watching for changes in the `visualization.json` and `visualization.js` files to push the chart changes back to the server.
4. Open the `src/index.js` file in your preferred text editor or integrated development environment. Modify the code to output some text on the chart with the total number of records returned by the default query. Change the `controller.update` function in the `src/index.js` file to contain the code below:

   controller.update = data => {  
    // Called when new data arrives  
    controller.element.innerHTML =  
    'The total # of records returned by this query is: ' + data.length;  
   };
5. Return to the terminal window where **watch** mode is enabled. A message showing that the My First Custom Chart was updated should appear.

## Step 5. Preview the Chart

Before you can preview the newly created chart in a dashboard in the Composer UI, you must enable it for a specific source.

1. Log into the Composer UI as an administrator or a user with the **Administer Sources** privilege.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243304013453)) or the [top-level navigation menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. On the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate a data source configuration to edit, and select the more menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243304019213)) button.
4. Select **Available Visual Types**. The Available Visual Types work area for this source opens.
5. Select the chart named "My First Custom Chart" and enable (toggle on) the custom chart in this data source. A message appears, confirming "My First Custom Chart" is enabled.
6. When your changes are complete, close the Available Visual Types work area.

Now let’s take a look at the new chart in a Composer dashboard.

1. Log into Composer as an administrator or a user who has been assigned to a group with the [**Administer Dashboards** privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The library displays.
3. Select **Add Dashboard**. A blank dashboard appears showing options to add a new visual or place an existing visual.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242713965197)
4. Select **Add Visual** to add a new visual to the dashboard. Select **Place Existing Visual** to place an existing visual on the dashboard.

   * If you select **Add Visual**, follow the procedure described in [Add Visuals to a Dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214171661-Add-Visuals-to-a-Dashboard)
   * If you select **Place Existing Visual**, follow the procedure described in [Add Existing Visuals to a Dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184486797-Add-Existing-Visuals-to-a-Dashboard).
5. On the **Step 1 of 2: Select a Source** dialog, select the data source in which you enabled your custom chart. The Select a **Visual** Type dialog appears.
6. Select your custom visual style ("My First Custom Chart") on the **Step 2 of 2: Select** **Visual** **Type** dialog. The visual is created and added to the dashboard.

Your chart should look similar to the following image:

![basic custom chart example](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242700730125 "basic custom chart example")

Cool! You have completed Part 1 of the custom chart tutorial. So far, you have learned how to install and configure the Composer custom chart CLI, how to create a new chart with sample code, and how to update its code and preview the results. Continue to [Part 2: Query Variables, Chart Defaults, Data Preview, and Data Accessors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700997161869-Part-2-Query-Variables-Chart-Defaults-Data-Preview-and-Data-Accessors).
