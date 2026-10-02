> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# A Custom Chart Tutorial

As an administrator, you can create custom charts (custom visuals) using the custom chart CLI. Download, import, and delete custom charts in the Self-Service Analytics user interface. Make custom charts visible on various menus in the Self-Service Analytics user interface.

This tutorial guides you through the process of developing a new custom chart from scratch. If you have some experience with JavaScript and you want to learn about connecting your data to charts, you are in the right place, we will walk you through the rest.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

To complete the custom chart tutorial, complete the following tutorial parts, in order:

* [Part 1: Custom Chart Basics](#part-1-custom-chart-basics)
* [Part 2: Query Variables, Chart Defaults, Data Preview, and Data Accessors](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-tut-ov-pt2)
* [Part 3: Third-Party Charting Library Integration](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-tut-ov-pt3)
* [Part 4: Custom Chart Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-tut-ov-pt4)

<h2 id="part-1-custom-chart-basics">
  Part 1: Custom Chart Basics
</h2>

This part of the custom chart tutorial introduces you to the Custom Chart CLI, how to create a chart with sample code, how to edit the chart’s code, and how to preview the chart. The following steps are performed in Part 1:

* [Step 1. Check Your Development Environment](#step-1-check-your-development-environment)
* [Step 2. Install & Configure the Custom Chart CLI](#step-2-install-configure-the-custom-chart-cli)
* [Step 3. Create a Custom Chart with Sample Code](#step-3-create-a-custom-chart-with-sample-code)
* [Step 4. Edit the Chart Code](#step-4-edit-the-chart-code)
* [Step 5. Preview the Chart](#step-5-preview-the-chart)

<h3 id="step-1-check-your-development-environment">
  Step 1. Check Your Development Environment
</h3>

Verify that you have everything set up to start creating custom charts with Self-Service Analytics.

* A valid version of `node.js` must be installed. `Node.js` is a programming tool for running JavaScript on servers and in your computer’s terminal. The Self-Service Analytics custom chart CLI is built using `node.js`.
* A valid version of `npm` must be installed. It is usually installed with `node.js`.
* Self-Service Analytics 26.3 or later must be installed.

**Verify that you have valid versions of node.js and npm installed**

1. Open a terminal window on your computer.
2. Enter `node --version` in the terminal window. The version of `node.js` installed on your computer is shown in the window. The minimum supported version of `node.js` by the Self-Service Analytics custom chart CLI is version 10.
3. Enter `npm --version` in the terminal window. The version of npm installed on your computer is shown in the window. The minimum supported version of `npm` supported by the Logi Composer custom chart CLI (`composer-chart-cli`) for Self-Service Analytics is version 1.

If `node.js` and npm are not installed, go to [https://nodejs.org/](https://nodejs.org/en/) and install the recommended version for your operating system.

<h3 id="step-2-install-configure-the-custom-chart-cli">
  Step 2. Install & Configure the Custom Chart CLI
</h3>

Self-Service Analytics uses the custom chart CLI to build, edit, and remove custom charts.

**Install and configure the CLI**

1. Enter the following command in the terminal window.

   ```bash theme={null}
   npm install composer-chart-cli@1 -g
   ```

2. After the CLI is installed, enter the following command in the terminal window:

   ```
   cmp-chart config
   ```

3. The `config` command prompts you to supply the following information:

   * Your Self-Service Analytics server URL.

   * The user name to use for authentication (typically: `admin`).

     <Note>
       You must be an administrator to manage custom visual types.
     </Note>

   * The password for the user name.

4. After entering this information, a prompt asks whether the configuration content should be stored in an encrypted file residing in your home directory (`~/.config/composer/cmp-chart.pref`). Enter **y** to finish configuring your environment.

5. Verify that everything is set up correctly by listing the custom charts available on the configured server using the following command:

   ```
   cmp-chart ls
   ```

   <Note>
     If your Self-Service Analytics instance does not have any custom charts defined, the output of this command is an empty list. If your instance does have custom charts defined, verify that they are correctly listed in the terminal window.
   </Note>

<h3 id="step-3-create-a-custom-chart-with-sample-code">
  Step 3. Create a Custom Chart with Sample Code
</h3>

You can specify one of three chart types to get you started:

* Single Group
* Multigroup
* Raw

This tutorial uses the default Single Group template — a chart skeleton with minimal code designed to make you familiar with the basics of the custom chart API.

**Complete the following steps to create a single-group custom chart:**

1. Enter the following command in the terminal window:

   ```
   cmp-chart init ./my-first-custom-chart
   ```

2. The `init` command creates a directory in the specified path containing the files you need to get started. Here is a preview of the directory tree:

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/init-dir-structure.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=3a31f1d96aa223c6095b9f4fcc99ffd7" alt="" width="325" height="188" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/init-dir-structure.png" />

   The following table describes the function of each of the files.

   | File Name | Description |
   | - | - |
   | `package.json` | Lists the packages on which your chart depends. For more information, see [https://docs.npmjs.com/creating-a-package-json-file](https://docs.npmjs.com/creating-a-package-json-file). |
   | `visualization.json` | Contains information about the name, controls, and variables of your chart. |
   | `webpack.config.js` | Contains configuration information for webpack. Webpack is used in charts to bundle your code into a single file. For more information, see [https://webpack.js.org/configuration/](https://webpack.js.org/configuration/). |
   | `src/index.js` | The main entry point to your chart’s Javascript code. Additional files can be used and imported into `index.js`. |
   | `src/index.css` | The main entry point to your chart’s CSS (style sheet) code. |

3. Install the default `devDependencies` listed in the `package.json` file. This step is required before you can work with the chart’s code. In a terminal window, `cd` to your chart’s root directory and run the following command:

   ```bash theme={null}
   npm install
   ```

4. To use a similar naming convention as the out-of-the-box charts, update the chart’s name in the `visualization.json` file to “My First Custom Chart”. Save the file.

<h3 id="step-4-edit-the-chart-code">
  Step 4. Edit the Chart Code
</h3>

Self-Service Analytics’s custom charts are comprised of CSS and JS files that make up the chart’s code. The chart CLI lets you update the chart’s code in the server in one of two ways:

* You can push an updated local copy of the chart back to the server.
* You can use **watch** mode to continuously check for changes to the local component files and automatically update your Self-Service Analytics server’s copy.

Throughout this tutorial, we continuously modify the code and preview the changes. It is best to use **watch** mode in this scenario.

**Start watch mode**

1. Compile a development version of the chart’s code using the webpack bundler. In the terminal window from the root directory of the chart, enter the following command:

   ```bash theme={null}
   npm start
   ```

2. In a different terminal window, push the chart for the first time to the configured server:

   ```
   cmp-chart push
   ```

3. Set up watch mode to continuously update the chart on the Self-Service Analytics server as the code changes. Enter the following command in the second terminal window:

   ```
   cmp-chart watch
   ```

   The `npm start` command instructs webpack to compile the code into a single `visualization.js` file and continuously watches for changes in the `src` files to update the chart as necessary. The `cmp-chart watch` command running in a separate terminal window starts watching for changes in the `visualization.json` and `visualization.js` files to push the chart changes back to the server.

4. Open the `src/index.js` file in your preferred text editor or integrated development environment. Modify the code to output some text on the chart with the total number of records returned by the default query. Change the `controller.update` function in the `src/index.js` file to contain the code below:

   ```javascript theme={null}
   controller.update = data => {
     // Called when new data arrives
     controller.element.innerHTML =
       'The total # of records returned by this query is: ' + data.length;
   };
   ```

5. Return to the terminal window where **watch** mode is enabled. A message showing that the My First Custom Chart was updated should appear.

<h3 id="step-5-preview-the-chart">
  Step 5. Preview the Chart
</h3>

Before you can preview the newly created chart in a dashboard in the Self-Service Analytics UI, you must enable it for a specific source.

1. Log into the Self-Service Analytics UI as an administrator or a user with the **Administer Sources** privilege.
2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.
3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate a data source configuration to edit, and select the **More** icon in the **Actions** column.
4. Select **Available Visual Types**. The Available Visual Types work area for this source opens.
5. Select the chart named "My First Custom Chart" and enable (toggle on) the custom chart in this data source. A message appears, confirming "My First Custom Chart" is enabled.
6. When your changes are complete, close the Available Visual Types work area.

Now let’s take a look at the new chart in a Self-Service Analytics dashboard.

1. Log into Self-Service Analytics as an administrator or a user who has been assigned to a group with the [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu. The library displays.

3. Select **Add Dashboard**. A blank dashboard appears showing options to add a new visual or existing visual.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-new.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=f5987ba67922a3642cd4568bece7e2e0" alt="" width="1035" height="392" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dashboard-new.png" />

4. Select **Add Visual** to add a new visual to the dashboard. Select **Add Existing Visual** to place an existing visual on the dashboard.

   * If you select **Add Visual**, follow the procedure described in [Manage Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash)
   * If you select **Add Existing Visual**, follow the procedure described in [Add Existing Visuals to a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#add-existing-visuals-to-a-dashboard).

5. On the **Step 1 of 2: Select a Source** dialog, select the data source in which you enabled your custom chart. The **Select a Visual Type** dialog appears.

6. Select your custom visual type ("My First Custom Chart") on the **Step 2 of 2: Select Visual Type** dialog. The visual is created and added to the dashboard.

Your chart should look similar to the following image:

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-chart-cli-cmp-v1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5531539e78aa5249531ccfd1d8578536" alt="basic custom chart example" width="3352" height="1736" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-chart-cli-cmp-v1.png" />

Cool! You have completed Part 1 of the custom chart tutorial. So far, you have learned how to install and configure the custom chart CLI, how to create a new chart with sample code, and how to update its code and preview the results. Continue to [Part 2: Query Variables, Chart Defaults, Data Preview, and Data Accessors](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-tut-ov-pt2).
