---
title: "Embedded Visual Authoring Properties and Objects"
id: 4405851051543
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851051543-Embedded-Visual-Authoring-Properties-and-Objects
updated_at: 2021-09-21T01:28:29Z
---

# Embedded Visual Authoring Properties and Objects

# Embedded Visual Authoring Properties and Objects

Properties can be passed as parameters to the [`createComponent` method](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods) when embedding Composer visual authoring components.

Here is a sample:

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
     <optional breadcrumb properties>
});
```

The following table describes all of the available properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `<optional breadcrumb properties>` | Optional breadcrumb properties are described in [*Optional Embedded Visual Authoring Breadcrumb Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4409054868887-Optional-Embedded-Visual-Authoring-Breadcrumb-Properties). | |
| `"header.showActions": false` | `true` | Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"header.showTitle": false` | `true` | Indicates whether the visual header title should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"header.title": <text>` | none | Specifies a static title for the visual.  Type: string |
| `"header.visible": false` | `true` | Indicates whether the visual header should be visible for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"interactivityOverrides"` | none | Specifies interactivity override settings for visual authoring. The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals. For a list of visual interactivity settings you can specify, see [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).  Type: object |
| `"source.visualId":"<id>"` | null | The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |
| `"theme":"dark"` | `composer` | The theme for the embedded visual. Valid values are `composer`, `modern`, or `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes) to the application, more options are available in this list and you may have introduced a different default.  Type: string |
| `"visualId":"<id>"` | null | The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |
