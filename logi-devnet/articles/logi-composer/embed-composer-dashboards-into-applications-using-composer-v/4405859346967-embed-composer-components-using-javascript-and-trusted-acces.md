---
title: "Embed Composer Components Using JavaScript and Trusted Access"
id: 4405859346967
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access
updated_at: 2022-05-20T10:53:13Z
---

# Embed Composer Components Using JavaScript and Trusted Access

# Embed Composer Components Using JavaScript and Trusted Access

You can embed a Composer component using JavaScript.

The following components can be embedded:

* dashboards
* visual authoring experience.

When components are embedded, the way in which users can interact with them is determined by settings established by their Composer user definition. See [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405851048727-Embedded-Composer-Component-Controls).

Complete examples of JavaScript code that initializes and authorizes the Composer `EmbedManager` class are provided in [*Embedded JavaScript Examples*](https://devnet.logianalytics.com/hc/en-us/articles/4405859345943-Embedded-JavaScript-Examples).

Follow these steps:

* [*Step 1. Verify the Prerequisites Have Been Met*](#Prereq)
* [*Step 2. Make the Embed Manager Available to Your Application*](#Step2)
* [*Step 3. Initialize and Authorize the Embed Manager*](#Step3)
* [*Step 4. Create and Render a Composer Component in Your Application*](#Step4)

## Step 1. Verify the Prerequisites Have Been Met

Verify that the embedded dashboard prerequisites have been met. See [*Embedded Component Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851046679-Embedded-Component-Prerequisites).

## Step 2. Make the Embed Manager Available to Your Application

To make the Composer's embed manager available to your application, include this script in your HTML:

```
<script data-name="composer-embed-manager" src="https://<samplecomposerurl>/embed/embed.js"></script>
```

where `<samplecomposerurl>` is the URL of your Composer instance.

After this script is run, the `initComposerEmbedManager` function is available globally in `window`.

## Step 3. Initialize and Authorize the Embed Manager

Use the `window.initComposerEmbedManager` function to initialize and authorize the embed manager. This can be done using either of the following configuration properties. Note that the token you supply must be obtained beforehand using the [Trusted Access API](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints), usually in backend code that supports your HTML.

* The `initialToken` property provides a string representing a [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) or OAuth token. When the token expires, the embedded dashboard must be manually refreshed (using the [`updateToken` method](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods)). Here is an example:

  ```
  const getEmbedManagerPromise =   
  window.initComposerEmbedManager({
        initialToken: <tokenValue> // tokenValue is provided by the Trusted Access API  
  });
  ```
* The `getToken` property is a method that returns a token from [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) or OAuth prior to token expiration. Here is an example:

  ```
  const getEmbedManagerPromise =   
  window.initComposerEmbedManager({  
         getToken: function () {  
             // transform for the embed syntax  
             return getToken().then((result) => { // getToken function uses the Trusted Access API  
                 return {  
                     access_token: result.token,  
                     expires_in: result.expiresIn,  
                 };  
              });  
          },  
  });
  ```

  After the `initComposerEmbedManager` function is called, it returns a promise that resolves an instance of the `EmbedManager` class. The objects, methods, properties, and embedded events provided with the Composer`EmbedManager` class can be used in your HTML.

## Step 4. Create and Render a Composer Component in Your Application

After the Composer `EmbedManager` class has been initialized and authorized, you can use its methods to embed a Composer component in your application and set various properties for that component. In addition, you can use Composer embedded events to control component behavior when specific events occur.

Other `EmbedManager` methods can be used to modify, refresh, and remove Composer components in your application.

Complete descriptions of the supported `EmbedManager` methods and properties are provided in [*EmbedManager Methods*](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods), [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects), and [*Embedded Visual Authoring Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851051543-Supported-Embedded-Visual-Authoring-Properties-and-Objects). Supported Composer embedded events are described in [*Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4405851052695-Supported-Composer-v6-Embedded-Events).

The following simple example creates and renders an embedded dashboard:

```
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
```
