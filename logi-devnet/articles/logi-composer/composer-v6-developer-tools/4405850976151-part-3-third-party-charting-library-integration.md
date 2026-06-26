---
title: "Part 3: Third-Party Charting Library Integration"
id: 4405850976151
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850976151-Part-3-Third-Party-Charting-Library-Integration
updated_at: 2021-09-21T01:27:40Z
---

# Part 3: Third-Party Charting Library Integration

# Part 3: Third-Party Charting Library Integration

This part of the custom chart tutorial explores integrating third-party charting libraries, such as D3, ECharts, and Highcharts, into your custom charts to build dynamic charts. It also covers how to create a chart container and how to use a library's API to render a standard chart. The following steps are performed in Part 3:

* [*Step 1. About Third-Party Libraries*](#Identify)
* [*Step 2. Add Libraries*](#Add)
* [*Step 3. Test Libraries*](#Test)
* [*Step 4. Create a Chart Container*](#Create)
* [*Step 5. Render the Chart*](#Render)
* [*Step 6. Handle Resizing*](#Step)

## Step 1. About Third-Party Libraries

Composer makes use of third-party libraries in the out-of-the-box charts provided with the product. Typically, these libraries fall into two categories:

* Charting libraries, which assist with the rendering of standard chart types like bar, line, pie, and scatter plot charts.
* Utility libraries, which assist with shaping data sets, formatting values, or providing useful JavaScript methods.

You can use third-party libraries to assist with the rendering and formatting requirements of a custom chart. This tutorial uses ECharts to assist with the rendering of your custom chart.

## Step 2. Add Libraries

To begin using ECharts with your custom chart:

1. Add ECharts as a dependency of the custom chart. You can do this by installing ECharts using `npm`, which provides an easy-to-use software registry that can leveraged to install packages for your custom charts.

   ```
   npm install echarts --save
   ```
2. Review the contents of the file `package.json` to ensure that Echarts is in the list of dependencies.

## Step 3. Test Libraries

To test the libraries:

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
4. Add a `console.log` line towards the top of the file, as shown:

   ```
   /* global controller */  
   import echarts from 'echarts';  
   import styles from './index.css';  
     
   console.log(echarts ? 'The library is defined.' : 'The library is undefined');const groupAccessor = controller.dataAccessors['Group By'];const metricAccessor = controller.dataAccessors.Size;//...
   ```
5. Check the contents of the browser console after adding the updated chart to a dashboard. The following image shows what the console should look like:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747443735/library-defined_844x168.png)
6. Once you confirm that the global variable is defined, you can remove the `console.log` statement.

## Step 4. Create a Chart Container

As part of its charting API, Composer provides a `<div>` element that can hold the rendered contents of your custom chart. While it is perfectly fine to use that element as the chart container, we recommend that you create a separate container inside of that element to gain full control over its styles.

To create a chart container:

1. Add the following `create chart containerconst` lines of code to the top of the `src/index.js` file:

   ```
   /* global controller */
     
   import echarts from 'echarts';
     
   import styles from './index.css';
     
     
   // create chart container  
   const chartContainer = document.createElement('div');  
   chartContainer.style.width = '100%';  
   chartContainer.style.height = '100%';  
   chartContainer.classList.add(styles.chartContainer);  
   controller.element.appendChild(chartContainer);  
     
   const groupAccessor = controller.dataAccessors['Group By'];  
   const metricAccessor = controller.dataAccessors.Size;  
   //...
   ```

   Notice the line: `controller.element.appendChild(chartContainer);`. `controller.element` is the `<div>` Composer provides with its API.
2. Modify the background color of the newly added container. Open the `src/index.css` component file, clear its contents, and add the following lines to the top of the file:

   ```
   .chartContainer {  
     background-color: #323232;
   }
   ```
3. Refresh the dashboard with the custom chart, and you should see a dark gray background for your custom chart.
4. Change the background color to background-color: `#ffffff;` to set it back to white.

## Step 5. Render the Chart

In[*Part 2: Query Variables, Chart Defaults, Data Preview, and Data Accessors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850975255-Part-2-Query-Variables-Chart-Defaults-Data-Preview-and-Data-Accessors), we defined a group-by variable and a metric variable to generate a grouped data set with a single metric value. This data structure works well with bar and pie charts. This step uses the ECharts API and its chart configuration option to create a pie chart with our data set.

1. In the `src/index.js` file, create a variable to hold an instance of the pie chart and a second variable to hold the chart configuration option. The chart’s instance is created using the `echarts.init` method and passing in a chart container. Add it right below the data accessors you created in Part 2:

   ```
   //...  
   const groupAccessor = controller.dataAccessors['Group By'];  
   const metricAccessor = controller.dataAccessors.Size;  
     
   const chart = echarts.init(chartContainer);  
   const option = {    
     series: [
       {
         name: metricAccessor.getLabel(),
         type: 'pie',
       },
     ],
   };
   //...
   ```

   Notice how we used the metric accessor to dynamically capture the name of the series.
2. Specify the **pie** series data and call the chart’s `setOption` method inside of the `controller.update` function:

   ```
   //...
   controller.update = data => {
     // Called when new data arrives
     option.series[0].data = reshapeData(data);
     chart.setOption(option);
   };
   //...
   ```

   A pie chart renders similar to this:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743891095/piecht1_576x260.png)

   Unfortunately, the pie chart is slightly cut off at the bottom, so the window needs to be resized. Read on.

## Step 6. Handle Resizing

Composer provides an API to notify the charts of a resize operation.

To resize the window:

* Add the `controller.resize` function at the end of the `src/index.js` file.

  ```
  //...
  controller.resize = (newWidth, newHeight) => {
    // Called when the widget is resized
    chart.resize();
  };
  ```

  The `resize` method of the EChart’s chart instance tells the chart to fit the new dimensions of the chart container.

Play around and add some filters or change the chart’s default configuration. You should see the data re-render as you modify the query with the filter or time bar control.

Looking Good! You now have a chart you can reuse with any data source. Continue to [*Part 4: Custom Chart Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405850977047-Part-4-Custom-Chart-Controls).
