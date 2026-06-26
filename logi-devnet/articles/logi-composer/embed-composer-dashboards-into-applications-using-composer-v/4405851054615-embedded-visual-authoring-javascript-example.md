---
title: "Embedded  Visual Authoring JavaScript Example"
id: 4405851054615
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851054615-Embedded-Visual-Authoring-JavaScript-Example
updated_at: 2021-09-21T01:28:30Z
---

# Embedded  Visual Authoring JavaScript Example

# Embedded Visual Authoring JavaScript Example

The following JavaScript example uses methods, properties, and embedded events of the `EmbedManager` class to embed a visual authoring instance.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The Composer `EmbedManager` class must be made available to your HTML application prior to using this sample in your application. See [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

```
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
