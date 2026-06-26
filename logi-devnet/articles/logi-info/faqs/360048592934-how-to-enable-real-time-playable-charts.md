---
title: "How to Enable Real-Time (playable) Charts"
id: 360048592934
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048592934-How-to-Enable-Real-Time-playable-Charts
updated_at: 2020-07-27T22:57:40Z
---

# How to Enable Real-Time (playable) Charts

Leveraging the [Real-Time Push API](https://documentation.logianalytics.com/logiinfov12/content/ccc-logi-javascript-api.htm?Highlight=2270), you will be able to create a playable, or incrementally loading chart in Logi Info.

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360082688273/mceclip0.png)

Below you can find a Logi Info Report that showcases this functionality.

### Report Components:

There are two main components of this sample. (download the complete sample below)

1. A chart canvas Element that reports Northwinds "orders" data
2. Custom Javascript that interacts with the Chart Canvas Element via the Real-Time push API.

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360072086014/mceclip1.png)

The following Javascript snippet includes a function "PlayableChart()" which consumes a json array as an argument. For every retrieved record in the JSON array, "pushData()" appends new data to the records presented in the chart canvas.

Other supporting functions playChart(),  and pauseChart() demonstrate some more ways in which you can add functions to this custom javascript.

```
// Quick Abstraction of using Logi Info's Realtime JS API to create playable charts.   
// Create holding var that can be accessed globally.   
var playableCharts = [];  
  
// Init Function for creating a PlayableChart Object  
function PlayableChart(data, chartName, seriesName, status, increment) {  
 status = status | 0; // if status isn't passed use 0  
 increment = increment | 500; // set speed to half second  
 playableCharts[chartName] = {  
 seriesName: seriesName, // we need to know the ID of the Canvas Chart Series  
 'recordNum': 10, // starting record  
 'increment': increment, // storing incrment speed for this object  
 'status': status, // initial status  
 'data' : data // storing data  
 };  
 playableCharts[chartName].run = // creating fucntion to run storing as part of obect  
 function () {  
  
  
// call the function to push data.   
 pushData(chartName, seriesName, playableCharts[chartName].data[playableCharts[chartName].recordNum].x, playableCharts[chartName].data[playableCharts[chartName].recordNum].y, 10);  
 playableCharts[chartName].recordNum ++ ; // increment record count  
 if(playableCharts[chartName].status == 1) { // see if the status has changed (so it doesn't run'  
 setTimeout(playableCharts[chartName].run, parseInt(playableCharts[chartName].increment)); // add another data point  
 }   
 }  
}  
  
function playChart(chartName) {  
 playableCharts[chartName].status = 1; // Status 1 == play  
 playableCharts[chartName].run(); // actually runs it.   
}  
  
function pauseChart(chartName) {  
 playableCharts[chartName].status = 0; // Status 0 == stop  
}  
  
function fasterChart(chartName) {  
 playableCharts[chartName].increment = playableCharts[chartName].increment - 25 // lower increment = faster  
}  
  
function slowerChart(chartName) {  
 playableCharts[chartName].increment = playableCharts[chartName].increment + 25 // larger increment == slower  
}  
  
function pushData(chartName, series, x, y, objKeep) {  
 objKeep = objKeep | 10;  
 var myData = [];  
 var chartCanvasObject = rdGetChartCanvasObject(chartName);  
 console.log(x + " " + y);  
 myData.push({  
 x: x,  
 y: parseInt(y)  
 });  
 // Create the chart object  
 var chartOptions = {  
 chart: {},  
 series: [{  
 id: series,  
 data: myData  
 }]  
 };  
 // double check the ChartCanvasObject still exists.   
 if (chartCanvasObject !== null) {  
 // Append the data.   
 chartCanvasObject.rdSetChartData(chartOptions, 'AppendData', objKeep);  
 }  
  
}
```
