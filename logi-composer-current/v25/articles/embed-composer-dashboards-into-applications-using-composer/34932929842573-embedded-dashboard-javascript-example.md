---
title: "Embedded  Dashboard JavaScript Example"
id: 34932929842573
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932929842573-Embedded-Dashboard-JavaScript-Example
updated_at: 2026-05-26T22:07:17Z
---

# Embedded  Dashboard JavaScript Example

# Embedded Dashboard JavaScript Example

The following JavaScript example uses methods, properties, and embedded events of the `EmbedManager` class to embed, refresh, reauthenticate, and remove a dashboard.

* The `createOrGetEmbedManager` asynchronous function provides an initial access token using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access).
* The `addDashboard` asynchronous function embeds a dashboard in the application. It uses the dashboard ID as input so it knows which dashboard to embed. It also specifies some properties for the dashboard.
* The `clearDashboard` asynchronous function removes a dashboard from the application. It uses the dashboard ID as input so it knows which dashboard to remove.
* The `refreshDashboard` asynchronous function refreshes the authorization token for the embedded dashboard using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access).
* The `application` asynchronous function at the end combines the use of all the previous functions and uses embedded events to trigger some of them.

**Note:** 
The Composer`EmbedManager` class must be made available to your HTML application prior to using this sample in your application. See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930219405-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

**Note:** Composer provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.

async function createOrGetEmbedManager(<token>) {
return window.initComposerEmbedManager({ //embed manager is a singleton and will be created only on the first call
getToken: function () {
// transform for the embed syntax
return getToken().then((result) => {
return {
"access\_token": "result.token",
"expires\_in": "result.expiresIn",
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
"CHANGE\_LAYOUT": true,
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
document.addEventListener('composer-unathorized', async () => {
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
