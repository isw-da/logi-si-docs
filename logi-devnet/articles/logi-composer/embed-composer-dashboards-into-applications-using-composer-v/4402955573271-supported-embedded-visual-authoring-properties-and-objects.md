---
title: "Supported Embedded Visual Authoring Properties and Objects"
id: 4402955573271
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955573271-Supported-Embedded-Visual-Authoring-Properties-and-Objects
updated_at: 2021-08-07T17:31:03Z
---

# Supported Embedded Visual Authoring Properties and Objects

# Supported Embedded Visual Authoring Properties and Objects

The following properties can be passed as parameters to the [`createComponent` method](https://devnet.logianalytics.com/hc/en-us/articles/4402955571991-Supported-EmbedManager-Methods) when embedding Composer visual authoring components.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"breadcrumbs.href":"<address>"` | none | The link address of the breadcrumb title. A valid link address should be specified in quotes (`"<address>"`).  Type: string |
| `"breadcrumbs.onClick"` | none | The click action handler for the breadcrumb title.  Type: function |
| `"breadcrumbs.target":"_blank"` | none | The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).  Type: string |
| `"breadcrumbs.title":"<title>"` | none | The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).  Type: string |
| `"header.showActions": false` | `true` | Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"header.showTitle": false` | `true` | Indicates whether the visual header title should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"header.visible": false` | `true` | Indicates whether the visual header should be visible for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"interactivityOverrides"` | none | Specifies interactivity override settings for visual authoring. The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals. For a list of visual interactivity settings you can specify, see [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402955732247-Control-How-Users-Interact-With-a-Visual).  Type: object |
| `"source.visualId":"<id>"` | null | The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |
| `"visualId":"<id>"` | null | The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |
