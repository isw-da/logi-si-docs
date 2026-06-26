---
title: "Using Widgets in Non-Logi Apps"
id: 4406817652887
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817652887-Using-Widgets-in-Non-Logi-Apps
updated_at: 2022-04-06T06:07:24Z
---

# Using Widgets in Non-Logi Apps

# Using Widgets in Non-Logi Apps

You can also directly embed these widgets into HTML pages and non-Logi applications, using JavaScript.
In the following example, we'll assume that Logi Info and the Discovery Module are installed on a web server named "Jupiter". We'll also assume that the HTML page that will embed a widget is being served from "Nomad12".
Here are the steps necessary to embed a widget in an HTML page:

1. On Jupiter, modify the settings file to accept a request from Nomad12. Assuming a default installation location, the file is:

   C:\LogiAnalytics\Discovery\platform\settings\logiApplicationService.json

   {  
   "disableSchemaValidation": false,   
   "logiApplicationService": {  
   "description": "Platform logiApplicationService Configuration",  
   "logLevel": "error",  
   "corsOriginWhiteList": "http://Nomad12",  
   "accessTokenGracePeriod": 120,  
   "system": {  
   "pollingIntervalSeconds": 15,  
   "pollingTimeoutMinutes": -1  
   },

Find the **corsOriginWhiteList** entry, highlighted above, and change it to accept requests from Nomand12. Save the file.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The "\*" wild-card value will not work in this situation - you *must* provide a value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583823127/introsuperwidgets_30.png)

2. Stop and restart the **Logi Application Service** and **Logi Data Service** services or daemons, shown above.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583823255/introsuperwidgets_31_513x297.png)
3. On Jupiter, find, copy, and save the ID of the widget you want to embed. This can be found in several places, including the SuperWidget Authoring Tool in Logi Studio, as shown above, or through the SuperWidget element's widget selector, which was used at the top of this page.
4. Here's the format of the JavaScript you'll add to your HTML page on Nomad12, in the page body wherever you want the widget to appear:

<script  
 src="http://*hostServer:port*/api/platform/system.configs/*widgetID*?interpolate=true&amp;$format=application/javascript">  
</script>

The example below shows the script with the values for our example filled in.

<script  
 src="http://Jupiter:3000/api/platform/system.configs/vdd1c55be-0eb0-4afc-b10a-34b2ab4ad7f8?interpolate=true&amp;$format=application/javascript">  
</script>

Other <script> tag parameters are also valid, such as:

id="myID" style="width:800px; height:700px;" theme="Arizona"

5. Browse your HTML page and the widget will appear in it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Users will be required to login to the widget the first time they browse the page and again if their session expires.
