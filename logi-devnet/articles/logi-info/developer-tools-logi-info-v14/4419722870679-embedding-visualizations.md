---
title: "Embedding Visualizations"
id: 4419722870679
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722870679-Embedding-Visualizations
updated_at: 2022-07-17T02:08:04Z
---

# Embedding Visualizations

# Embedding Visualizations

Visualizations can be embedded into Logi applications and into non-Logi app web pages. As we've seen in previous examples, Logi Platform Services can be used directly in a Logi application. The **Thinkspace** element is available as a child of **Body**, **Division**, and **Column Cell** elements but cannot be used in Data Table Columns or Dashboards. Here are two other embedding scenarios:

## Embedding in Logi Apps Using an iFrame

You can embed a Logi definition containing a Thinkspace element in another definition in the *same* Logi application, or in a *different* Logi application, using the **SubReport** (Include Frame) element, without any special requirements.

## Embedding in HTML Pages using the Embedded Reports API

Logi Platform Services can be used with visualizations embedded into non-Logi app web pages using the Logi **Embedded Reports API**. Here's a very simple example of the HTML code required:

<html>  
<head><title>DM Embed Test</title></head>  
<body>  
 <p>This is my embedded Discovery Module test</p>  
 <div id="div1" data-applicationUrl="http://localhost/myLogiApp" data-report="Default"style="width:900px; height:900px;"></div>  
 <script src="http://localhost/myLogiApp/rdTemplate/rdEmbedApi/rdEmbed.js"type="text/Javascript"></script>  
</body>  
</html>

See [Embedded Reports API](https://devnet.logianalytics.com/hc/en-us/articles/4419715274135-Embedded-Reports-API) for information about using it.

## Embedding SuperWidgets

SuperWidgets can be embedded in Logi and other applications using JavaScript and the *Logi Platform Services API*.
