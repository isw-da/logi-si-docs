---
title: "Using \"Pushed\" Data  "
id: 4406817028119
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817028119-Using-Pushed-Data
updated_at: 2022-04-06T06:03:28Z
---

# Using "Pushed" Data  

# Using "Pushed" Data

You can also refresh charts using data that's "pushed" to the browser. This type of update is ideal for a use case in which many users receive very frequent data updates while avoiding web server performance degradation and negative network bandwidth impacts.

This technique relies on a 3rd party service, like [Pusher.com](https://pusher.com/), to transmit the data to the application. These services essentially broadcast data received from a (Logi or non-Logi) data source application to your Logi application in the browser, using a protocol like Web Sockets. You Logi application in the browser listens for these broadcasts and uses the Real-Time Chart API to update your charts.

Here's an example:

An external PHP application (not shown) generates data periodically and sends it to Pusher.com.

The Pusher.com API library is included in our Logi definition using an **Include Script File** element, with its Script File attribute set to //js.pusher.com/2.2/pusher.min.js.

The following JavaScript code is included in the definition using an **Include Script** element:

// init the pusher API channel and bind the updates.  
var pusher = new Pusher('yourPusherID');  
var channel = pusher.subscribe('live\_data');  
  
channel.bind('new\_data', function(data) {  
// when a message has been sent to the pusher API, it will enact this code block  
var dataObj = data.feed;  
  
// target and capture the line chart object  
var chartCanvasObject = rdGetChartCanvasObject('RealtimeDataChart');  
  
for($i = 0; $i < dataObj.length; $i++){  
// load the data records to the data array  
var myData = [];  
myData.push({  
x: new Date(dataObj[$i].datetime),  
y: parseInt(dataObj[$i].value)  
});  
  
// create the new chartOptions object  
var chartOptions = {  
chart:{},  
series: [{  
id: 'RealtimeLine',   
data: myData  
}]  
};  
  
// update the line chart  
if(chartCanvasObject != null){  
// append the new data to the existing chart series  
chartCanvasObject.rdSetChartData(chartOptions, 'AppendData', 100);  
}  
}  
});

Whenever Pusher.com broadcasts new data, our Logi application will receive it and update the chart, without making a request to the Logi application web server or refreshing the web page.
