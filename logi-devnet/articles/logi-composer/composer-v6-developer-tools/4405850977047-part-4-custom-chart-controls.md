---
title: "Part 4: Custom Chart Controls"
id: 4405850977047
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850977047-Part-4-Custom-Chart-Controls
updated_at: 2021-09-21T01:27:39Z
---

# Part 4: Custom Chart Controls

# Part 4: Custom Chart Controls

This part of the custom chart tutorial adds controls found in out-of-the-box Composer charts: axis labels/pickers, tooltips, and a radial menu. The following steps are performed in Part 4:

* [*Step 1. Add Axis Labels and Pickers*](#Axis)
* [*Step 2. Add Tooltips*](#Tooltips)
* [*Step 3. Add the Radial Menu*](#Radial)
* [*Step 4. Enable Cross-Visual Filtering*](#Cross-vis)
* [*Step 5. Add Other Controls*](#Other)
* [*Step 6. Create a Production Bundle*](#Producti)

## Step 1. Add Axis Labels and Pickers

It is very common for end-users to want to explore a data set by changing the group-by and metric fields used by a chart. Composer provides an API for chart developers to quickly add axis labels that can act as controls to replace group-by and metric selections.

Your current custom chart, created in this tutorial, has a default group-by and metric selection defined in the data source.

To add axis labels so that you can change the group-by and metric selections within the chart itself:

1. In the terminal window, change directories to the local directory of “My First Custom Chart” and enter the following command to set the custom chart CLI in watch mode, if it is not in watch mode already.

   ```
   zd-chart watch
   ```
2. In another terminal window, run the following command to compile a development version of the chart’s code using the webpack bundler:

   ```
   npm start
   ```

   For a refresher on this topic, see [*Step 4. Edit the Chart Code*](https://devnet.logianalytics.com/hc/en-us/articles/4405850974231--Part-1-Custom-Chart-Basics#Step4).
3. Edit the `src/index.js` file in your preferred text editor or integrated development environment.
4. Add the following code to the end of the `src/index.js` file:

   ```
   //...  
   controller.createAxisLabel({  
     picks: 'Group By',
     position: 'bottom',
     orientation: 'horizontal',
   });

   controller.createAxisLabel({
     picks: 'Size',
     position: 'bottom',
     orientation: 'horizontal',
   });
   ```

   The `controller.createAxisLabel` method takes an object with the configuration options of the axis label. The following table describes possible option names and values you can use:

   | Option | Description |
   | --- | --- |
   | `picks` | The name of the query variable. Use the data accessor’s `getName` method to avoid hard-coding variable names |
   | `position` | The location of the axis label in the chart widget. Valid options are `bottom`, `left`, `right`, and `top`. |
   | `orientation` | The orientation of the axis label text. Valid options are `vertical` and `horizontal`. |
5. Preview the chart in a dashboard and notice the new axis labels/pickers below the chart. Play around with the controls and notice how the chart reacts to the changes in the query.

## Step 2. Add Tooltips

In addition to axis labels, custom charts can define Composer tooltips so the custom chart’s look and feel is consistent with out-of-the-box charts.

To define the tooltips using Composer’s API:

1. Add the original Composer data to the objects in the data set. We simply need to modify the `reshapeData` function in the `src/index.js` file as follows:

   ```
   function reshapeData(data) {
     return data.map(d => ({
       name: groupAccessor.raw(d),
       value: metricAccessor.raw(d)
       datum: d
     }));
   }
   ```
2. Add `mousemove` and `mouseout` event handlers to the chart:

   ```
   chart.on('mousemove', param => {
     controller.tooltip.show({
       event: param.event.event,
       data: () => param.data.datum,
     });
   });
   ```

   ```
   chart.on('mouseout', param => {
     controller.tooltip.hide();
   });
   ```

   Notice the use of `controller.tooltip.show` and `controller.tooltip.hide`. The `show` method receives an option with the following properties:

   | Option | Description |
   | --- | --- |
   | x | The x coordinate in the screen where the tooltip should render |
   | y | The y coordinate in the screen where the tooltip should render |
   | data | Function that returns a Composer datum object |

   ### Optional Properties

   | Option | Description |
   | --- | --- |
   | event | Takes a native browser event to specify the tooltip position. An alternative to x and y properties |
   | content | Function that returns an HTML string to replace the content inside of the tooltip boxes |

   When you mouse over a pie slice, the `mousemove` handler runs and the `controller.tooltip.show` API is called to display the tooltip. Likewise, the `mouseout` event handler runs when the mouse leaves the pie slice and the `controller.tooltip.hide` API is called to hide the tooltip.

## Step 3. Add the Radial Menu

The radial menu is a control found in many of the out-of-the-box Composer charts. Visual developers select a chart’s data point to trigger the display of the radial menu. Usually, the radial menu is used to do quick filtering operations on the chart itself or other charts in the dashboard. An overview of the actions that can be selected on the radial menu can be reviewed in [*Use the Radial Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).

Composer provides an API that can be used to show the radial menu with it default actions.

To add the radial menu to your custom pie chart:

* Add the following code in the `src/index.js` file:

  ```
  chart.on('mousemove', param => {
    controller.tooltip.show({
      event: param.event.event,
      data: () => param.data.datum,
    });
  });

  chart.on('mouseout', param => {
    controller.tooltip.hide();
  });

  chart.on('click', param => {
    controller.menu.show({
      event: param.event.event,
      data: () => param.data.datum,
    });
  });
  ```

  Notice the use of `controller.menu.show`. The `show` method receives an option with the following properties:

  | Option | Description |
  | --- | --- |
  | x | The x coordinate in the screen where the menu should render |
  | y | The y coordinate in the screen where the menu should render |
  | data | Function that returns a Composer datum object |

  ### Optional Properties

  | Option | Description |
  | --- | --- |
  | event | Takes a native browser event to specify the menu position. An alternative to x and y properties |
  | menu | Used to customize the list of actions that display in the menu. Custom actions along with their callbacks can be defined. Here’s an example menu: { items: ['Exclude', 'Zoom', 'Filter', 'Filter All', 'Info', 'Trend', 'Custom'], 'Custom': function() { // some custom action } } |

  Now, whenever we click a pie slice, the radial menu displays and any of its actions can be triggered.

## Step 4. Enable Cross-Visual Filtering

If you want your new chart to interact with other charts using [cross-visual filtering](https://devnet.logianalytics.com/hc/en-us/articles/4405859347991-Use-Cross-Visual-Links-for-Cross-Visual-Filtering), some controls must be enabled using the CLI.

1. Enter the following command in the terminal window:

   ```
   zd-chart edit
   ```
2. Follow the prompts and select the **Controls** option.
3. Use the arrows and the spacebar to select:​

   * **Publish** to allow a chart with the radial menu enabled to filter other charts on a dashboard.
   * **Subscribe** to allow a chart to receive filters from other charts on the dashboard
4. Press **Enter** to make your selections.
5. Enter **N** to the prompt asking if you would like to make additional edits.
6. Refresh the custom chart in a dashboard.
7. Open the Dashboard Interactions dialog and select the **Cross-Visual Filtering** tab. See [*Understand the Cross-Visual Filtering Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859426583-Understand-the-Cross-Visual-Filtering-Tab).
8. Select your custom chart from the list on the left of the tab and configure the publish and subscribe settings for the custom chart. See [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405859420823-Publish-a-Link) and [*Subscribe a Visual to a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851136151-Subscribe-a-Visual-to-a-Link).
9. Select a pie slice in the custom pie chart to open the radial menu.

   If you published the link for the field on which the pie chart is grouped, the Filter option appears in the radial menu. Select this option to create a cross-visual filter using the link field for all the visuals on the dashboard that subscribe to the link.

## Step 5. Add Other Controls

In addition to the controls described elsewhere in this tutorial, Composer allows chart developers to show or hide controls on the chart’s menu:

![](https://devnet.logianalytics.com/hc/article_attachments/4406743890071/visualmenu.png)

The display of these controls is configured using the CLI.

To add the Color control to the chart:

1. Enter the following command in the terminal window:

   ```
   zd-chart edit
   ```
2. Follow the prompts and select the **Controls** option.
3. Use the arrows and the spacebar to select **Color** from the list.
4. Press **Enter** to make your selections.
5. Enter **N** to the prompt asking if you would like to make additional edits.
6. Refresh the custom chart in a dashboard and notice the new color control on the chart’s drop-down menu.

   If you try to use the Color control, however, the panel does not open. The color control only works if you set one of the query variables as the driver color. Since this is a pie chart with a different color per slice, modify the group-by variable to use it as the driver of color in the chart.
7. Enter the following command in the terminal window:

   ```
   zd-chart edit
   ```
8. Follow the prompts and select the **Variables** option.
9. Select **Edit a variable**.
10. Select **Group By | group |**.
11. Select **Configuration**.
12. Select **Attribute & Time**.
13. Enter **Y** to the prompt asking whether this variable will drive the color in your chart.
14. Enter **N** to the prompt asking if you would like to make additional edits.
15. Switch back to your dashboard and refresh the screen to get the latest changes to the chart. The color control should now work, but the colors displayed do not match the ones in the pie chart.
16. To fix the color mismatch, ECharts must be updated to identify the color to use for each of the pie slices. You can use a data accessor in the API. Edit the `src/index.js` file and make the following minor modification:

    ```
    function reshapeData(data) {
      return data.map(d => ({
        name: groupAccessor.raw(d),
        value: metricAccessor.raw(d),
        datum: d,
        itemStyle: {
          color: groupAccessor.color(d),
        },
      }));
    }
    ```

    Notice how the `groupAccessor` is used to extract the color since it is tied to the Group By variable that is driving the color of the chart. In the Composer dashboard, open the chart’s color palette and select the second color palette from the list.

## Step 6. Create a Production Bundle

Throughout the tutorial, you have worked with the development version of the chart’s code. When you run the `npm start` command, webpack compiles the chart’s assets into a single `visualization.js` file that is optimized for production usage. If you inspect the contents of the file, you will notice that the code is not minified and uglified. When the chart’s code is in a state that’s ready to be consumed by end-users, we recommend that you build a production version of the code that is optimized and has a reduced bundle size.

To create a production bundle:

1. Run the following command in a terminal window. This instructs webpack to create an optimized bundle in the `visualization.js` file.

   ```
   	npm run build
   ```
2. Run the following command to push the production bundle to the Composer server:

   ```
   zd-chart push
   ```

You have completed the final part of the custom chart tutorial! You are now armed with the necessary tools and knowledge to go and build new and feature-rich charts in Composer. You can also view the [Spark Cast](https://devnet.logianalytics.com/hc/en-us/articles/360051442654-Spark-Cast-Logi-Composer-Create-Custom-Visualizations-) produced about custom charts.
