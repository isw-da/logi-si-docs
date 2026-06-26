---
title: "Embed Composer Components Using JavaScript and Trusted Access"
id: 43701108006413
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access
updated_at: 2026-05-29T14:08:34Z
---

# Embed Composer Components Using JavaScript and Trusted Access

# Embed Composer Components Using JavaScript and Trusted Access

You can embed a Composer component using JavaScript.

The following components can be embedded:

* dashboards, lite dashboards
* visual authoring experience
* source editor

When components are embedded, the way in which users can interact with them is determined by settings established in their user account. See [Embedded Composer Component Controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081977869-Embedded-Composer-Component-Controls).

Complete examples of JavaScript code that initializes and authorizes the Composer`EmbedManager` class are provided in [Embedded JavaScript Examples](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070926989-Embedded-JavaScript-Examples).

Follow these steps:

* [Step 1. Verify the Prerequisites Have Been Met](#Prereq)
* [Step 2. Make the Embed Manager Available to Your Application](#Step2)
* [Step 3. Initialize and Authorize the Embed Manager](#Step3)
* [Step 4. Create and Render a Composer Component in Your Application](#Step4)

## Step 1. Verify the Prerequisites Have Been Met

Verify that the embedded dashboard prerequisites have been met. See [Embedded Component Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117720077-Embedded-Component-Prerequisites).

## Step 2. Make the Embed Manager Available to Your Application

To make the Composer's embed manager available to your application, include this script in your HTML:

<script data-name="composer-embed-manager" src="https://<sampleurl>/embed/embed.js"></script>

where `<samplecomposerurl>` is the URL of your Composer instance.

After this script is run, the `initComposerEmbedManager` function is available globally in `window`.

## Step 3. Initialize and Authorize the Embed Manager

Use the `window.initComposerEmbedManager` function to initialize and authorize the embed manager. This can be done using the following configuration properties. Note that the token you supply must be obtained beforehand using the [Trusted Access API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701148717453-Trusted-Access-API-Endpoints), usually in backend code that supports your HTML.

The `getToken` property is a method that returns a token from [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access) prior to token expiration. Here is an example:

const getEmbedManagerPromise =   
window.initComposerEmbedManager({  
 getToken: function () {  
 // transform for the embed syntax  
 return getToken().then((result) => { // getToken function uses the Trusted Access API  
 return {  
 access\_token: result.token,  
 expires\_in: result.expiresIn,  
 };  
 });  
 },  
});

After the `initComposerEmbedManager` function is called, it returns a promise that resolves an instance of the `EmbedManager` class. The objects, methods, properties, and embedded events provided with the Composer`EmbedManager` class can be used in your HTML.

## Step 4. Create and Render a Composer Component in Your Application

After the Composer`EmbedManager` class has been initialized and authorized, you can use its methods to embed a Composer component in your application and set various properties for that component. In addition, you can use Composer embedded events to control component behavior when specific events occur.

Other `EmbedManager` methods can be used to modify, refresh, and remove Composer components in your application.

Complete descriptions of the supported `EmbedManager` methods and properties are provided in [EmbedManager Methods](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117892237-EmbedManager-Methods), [Embedded Dashboard Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects), and [Embedded Visual Authoring Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070653325-Embedded-Visual-Authoring-Properties-and-Objects). Supported Composer embedded events are described in [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events).

The following simple example creates and renders an embedded dashboard:

getEmbedManagerPromise.then((embedManager) => {  
 embedManager.createComponent('dashboard',  
 {  
 dashboardId: <id>, // dashboard id  
 <property>,... // set of properties  
 }  
 ).then(dashboard => dashboard.render(  
 htmlElement, // htmlElement  
 {width: '100%', height: '100%'}  
 ))  
});  
  
// Example with async await  
async function createComponent() {  
 const embedManager = await getEmbedManagerPromise;  
 const newDashboard = await embedManager.createComponent('dashboard',  
 {  
 dashboardId: <id>, // dashboard id  
 <property>,... // set of properties  
 });  
 newDashboard.render(  
 htmlElement, // htmlElement or selector  
 {width: '100%', height: '100%'}  
 ));  
}

The following simple example creates and renders an embedded lite dashboard:

embedManager.createComponent('lite-dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"lite-dashboard",
"application":{
"banner":false,
"logo":true
},
"interactivityProfileName":"lite",
"theme":"modern",
"editor":{
"placement": "docRight"
},
"header": {
"title": "My Lite Dashboard"
"showActions": false,
"showTitle": false,
"visible": false
},
"availableVisTypes" : [`HISTOGRAM`,`BOX\_PLOT`,`HEATMAP`]
}
);

Optionally, return dashboards to your users that match a filter string you've defined (partial example):

// Fetch filtered dashboard list
const response = await fetch(
`${composerUrl}/api/dashboards?filter=tags NOT IN ["internal"]`,
{headers}
);

Supported operators include `IN`, `NOT`, `!=`, `<>`, `AND`, and `OR`.
