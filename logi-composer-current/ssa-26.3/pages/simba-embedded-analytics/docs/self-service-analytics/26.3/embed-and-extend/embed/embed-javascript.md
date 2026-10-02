> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed Components Using JavaScript and Trusted Access

You can embed a Self-Service Analytics component using JavaScript.

The following components can be embedded:

* dashboards, lite dashboards
* visual authoring experience
* source editor

When components are embedded, the way in which users can interact with them is determined by settings established in their user account. See [Embedded Self-Service Analytics Component Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed-controls).

Complete examples of JavaScript code that initializes and authorizes the `EmbedManager` class are provided in [Embedded JavaScript Examples](#embedded-javascript-examples).

Follow these steps:

* [Step 1. Verify the Prerequisites Have Been Met](#step-1-verify-the-prerequisites-have-been-met)
* [Step 2. Make the Embed Manager Available to Your Application](#step-2-make-the-embed-manager-available-to-your-application)
* [Step 3. Initialize and Authorize the Embed Manager](#step-3-initialize-and-authorize-the-embed-manager)
* [Step 4. Create and Render a Component in Your Application](#step-4-create-and-render-a-component-in-your-application)

<h2 id="step-1-verify-the-prerequisites-have-been-met">
  Step 1. Verify the Prerequisites Have Been Met
</h2>

Verify that the embedded dashboard prerequisites have been met. See [Embedded Component Prerequisites](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed#embedded-component-prerequisites).

<h2 id="step-2-make-the-embed-manager-available-to-your-application">
  Step 2. Make the Embed Manager Available to Your Application
</h2>

To make the Self-Service Analytics's embed manager available to your application, include this script in your HTML:

```xml theme={null}
<script data-name="composer-embed-manager" src="https://<sampleurl>/embed/embed.js"></script>
```

where `<samplecomposerurl>` is the URL of your Self-Service Analytics instance.

After this script is run, the `initComposerEmbedManager` function is available globally in `window`.

<h2 id="step-3-initialize-and-authorize-the-embed-manager">
  Step 3. Initialize and Authorize the Embed Manager
</h2>

Use the `window.initComposerEmbedManager` function to initialize and authorize the embed manager. This can be done using the following configuration properties. Note that the token you supply must be obtained beforehand using the [Trusted Access API](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov#trusted-access-api-endpoints), usually in backend code that supports your HTML.

The `getToken` property is a method that returns a token from [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) prior to token expiration. Here is an example:

```javascript theme={null}
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

After the `initComposerEmbedManager` function is called, it returns a promise that resolves an instance of the `EmbedManager` class. The objects, methods, properties, and embedded events provided with the `EmbedManager` class can be used in your HTML.

<h2 id="step-4-create-and-render-a-component-in-your-application">
  Step 4. Create and Render a Component in Your Application
</h2>

After the `EmbedManager` class has been initialized and authorized, you can use its methods to embed a Self-Service Analytics component in your application and set various properties for that component. In addition, you can use embedded events to control component behavior when specific events occur.

Other `EmbedManager` methods can be used to modify, refresh, and remove components in your application.

Complete descriptions of the supported `EmbedManager` methods and properties are provided in [EmbedManager Methods](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods), [Embedded Dashboard Properties and Objects](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects), and [Embedded Visual Authoring Properties and Objects](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-visual-authoring-properties-and-objects). Supported embedded events are described in [Embedded Events](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-eventlisteners).

The following simple example creates and renders an embedded dashboard:

```javascript theme={null}
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

The following simple example creates and renders an embedded lite dashboard:

```javascript theme={null}
embedManager.createComponent('lite-dashboard', const componentConfig = { "dashboardId": "<dashboard-ID>", "componentInstanceId":"<component-instance-ID>", "type":"lite-dashboard", "application":{ "banner":false, "logo":true }, "interactivityProfileName":"lite", "theme":"modern", "editor":{ "placement": "docRight" }, "header": { "title": "My Lite Dashboard" "showActions": false, "showTitle": false, "visible": false }, "availableVisTypes" : [`HISTOGRAM`,`BOX_PLOT`,`HEATMAP`] } );
```

Optionally, return dashboards to your users that match a filter string you have defined (partial example):

```javascript theme={null}
// Fetch filtered dashboard list
const response = await fetch(
  `${composerUrl}/api/dashboards?filter=tags NOT IN ["internal"]`,
  {headers}
);
```

Supported operators include `IN`, `NOT`, `!=`, `<>`, `AND`, and `OR`.

<h2 id="embedded-javascript-examples">
  Embedded JavaScript Examples
</h2>

This section provides JavaScript examples that use methods, properties, and embedded events of the `EmbedManager` class to embed, refresh, reauthenticate, or remove Self-Service Analytics components from your application.

### Embedded Dashboard JavaScript Example

The following JavaScript example uses methods, properties, and embedded events of the `EmbedManager` class to embed, refresh, reauthenticate, and remove a dashboard.

* The `createOrGetEmbedManager` asynchronous function provides an initial access token using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov).
* The `addDashboard` asynchronous function embeds a dashboard in the application. It uses the dashboard ID as input so it knows which dashboard to embed. It also specifies some properties for the dashboard.
* The `clearDashboard` asynchronous function removes a dashboard from the application. It uses the dashboard ID as input so it knows which dashboard to remove.
* The `refreshDashboard` asynchronous function refreshes the authorization token for the embedded dashboard using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov).
* The `application` asynchronous function at the end combines the use of all the previous functions and uses embedded events to trigger some of them.

<Note>
  The Self-Service Analytics `EmbedManager` class must be made available to your HTML application prior to using this sample in your application. See Embed Components Using JavaScript and Trusted Access.
</Note>

<Note>
  Self-Service Analytics provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.
</Note>

```javascript theme={null}
async function createOrGetEmbedManager(<token>) {
   return window.initComposerEmbedManager({ //embed manager is a singleton and will be created only on the first call
      getToken: function () {
          // transform for the embed syntax
          return getToken().then((result) => {
              return {
                  "access_token": "result.token",
                  "expires_in": "result.expiresIn",
              };
          });
      }
   });
}

async function addDashboard(<id>) { // id of the composer dashboard
   const embedManager = await createOrGetEmbedManager();

   const dashboard = await embedManager.createComponent('dashboard', {
      "dashboardId": "<id>", // required
      "theme": "composer",
      "interactivityProfileName": "interactive",
      interactivityOverrides {
        "settings":{
           "CHANGE_LAYOUT": true,
        },
        "visualSettings":{
           "FILTER": false,
        },
     },
     "editor": {
         "placement": "dockRight" // use eve sidepanel
      },
      "header": {
         "visible": true,
         "showTitle": true,
         "showActions": false, // will hide actions bar
         "title": "Static custom title"
      }
   });

   dashboard.render(document.querySelector('#dashboard'), { width: '800px', height: '400px' });
   return dashboard;
}

async function clearDashboard(<id>) {
   const embedManager = await createOrGetEmbedManager();
   embedManager.removeComponent(<id>);
}

async function refreshDashboard(<newToken>) {
   const embedManager = await createOrGetEmbedManager();
   embedManager.updateToken(<newToken>).then(() => {
      embedManager.refresh();
   });
}

(async function application() {
   const token = await getComposerToken(); // some function of the 3rd party app that calls application API and return composer token retrieved via TA
   const dashboards = await getUserDashboard(); // some function of the 3rd party app that retrieved dashboards for the user
   createOrGetEmbedManager(token);

   // if token is expired composer will raise next event
   document.addEventListener('composer-unauthorized', async () => {
      const token = await getComposerToken();
      const embedManager = createOrGetEmbedManager();
      refreshDashboard(token);
   })
   // render first dashboard in the list
   const embeddedDashboard = addDashboard(dashboards[0].id);

   // embedded component supports an ability to subscribe on the component specific events
   embeddedDashboard.addEventListener('composer-dashboard-ready', () => {
      // triggered when all charts are rendered. put custom logic here.
   })
   document.querySelector('#clear-button').addEventListener('click', () => {
      clearDashboard(embeddedDashboard.componentInstanceId); // clears embedded dashboard when clicked on some button in the application
   })

})()
```

### Embedded Visual Authoring JavaScript Example

The following JavaScript example uses methods, properties, and embedded events of the `EmbedManager` class to embed a visual authoring instance.

<Note>
  The Self-Service Analytics `EmbedManager` class must be made available to your HTML application prior to using this sample in your application. See Embed Components Using JavaScript and Trusted Access.
</Note>

<Note>
  Self-Service Analytics provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.
</Note>

```javascript theme={null}
// NOTE: This example assumes that the EmbedManager has already been initialized
const visualBuilder = await embedManager.createComponent('visual-builder', {
    visualId: <id>, // ID of existing visual
    source: {
        "visualId": "<id>", // ID of visual template, used for creating a new visual, do not pass it with visualId
    },
// If neither visualId is passed (visualId or source.visualId) an empty visual builder will be opened)
    "theme": "composer",
    "header": {
        "visible": true,
        "showTitle": true,
        "showActions": false, // hides the visual actions bar
        "title": "Static custom title"
    },
    "breadcrumbs": { // optional configuration of the breadcrumbs
        "title": "Visuals",
        "onClick": () => {console.log('clicked')},
        "href": "http://www.google.com",
        "target": "_blank"
    },
    interactivityOverrides: { // optional overrides for visual interactivity
        "visualSettings": {
            "FILTER": false,
            "GROUPING": true,
            "METRICS": false, // accept both boolean and string values
            "SETTINGS": false,
            "SORT": true,
            "ZOOM_ACTION": false
        }
    }
});

visualBuilder.render(document.querySelector('#builder'), { width: '800px', height: '100px' });
```
