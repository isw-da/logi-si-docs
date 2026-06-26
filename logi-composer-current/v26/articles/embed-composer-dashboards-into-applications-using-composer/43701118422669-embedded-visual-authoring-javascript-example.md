---
title: "Embedded  Visual Authoring JavaScript Example"
id: 43701118422669
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118422669-Embedded-Visual-Authoring-JavaScript-Example
updated_at: 2026-05-29T14:08:35Z
---

# Embedded  Visual Authoring JavaScript Example

# Embedded Visual Authoring JavaScript Example

The following JavaScript example uses methods, properties, and embedded events of the `EmbedManager` class to embed a visual authoring instance.

**Note:** 
The Composer`EmbedManager` class must be made available to your HTML application prior to using this sample in your application. See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

**Note:** Composer provides a `componentInstanceId` provides a as part of event details for dashboard, source, and visual events.

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
"target": "\_blank"
},
interactivityOverrides: { // optional overrides for visual interactivity
"visualSettings": {
"FILTER": false,
"GROUPING": true,
"METRICS": false, // accept both boolean and string values
"SETTINGS": false,
"SORT": true,
"ZOOM\_ACTION": false
}
}
});
visualBuilder.render(document.querySelector('#builder'), { width: '800px', height: '100px' });
