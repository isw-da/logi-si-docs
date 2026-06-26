---
title: "Embedded Visual Authoring Properties and Objects"
id: 43701070653325
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070653325-Embedded-Visual-Authoring-Properties-and-Objects
updated_at: 2026-05-29T14:08:29Z
---

# Embedded Visual Authoring Properties and Objects

# Embedded Visual Authoring Properties and Objects

The following properties can be passed as parameters to the [`createComponent` method](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117892237-EmbedManager-Methods) when embedding Composer visual authoring components.

Here is a sample.

**Note:** 
This example assumes that the EmbedManager has already been initialized, and the ID of a visual template is passed.

const getToken = async () => {
const response = await fetch('<playground-uri-and-username-token>', {
method: 'GET',
credentials: 'same-origin'
});
return response.json().then((result) => {
return {
access\_token: result.token,
expires\_in: result.expiresIn,
};
});
};
const embedManagerPromise = window.initComposerEmbedManager({ getToken: getToken });
const componentConfig = {
"[theme](#theme "theme details")":"modern",
"[header](#header)": {
"[showTitle](#showTitle)": false,
"[visible](#visible)": false,
"[showActions](#showActions)": false,
"[title](#title)": "<title-text>",
}
}
const createEmbedComponent = (embedManager, config, containerElementId = 'widget-holder') => {
embedManager.createComponent("visual-builder", config).then(component => {
component.render(document.getElementById(containerElementId), { width:"100%", height: "100%" });
})
}
embedManagerPromise.then(embedManager => {
createEmbedComponent(embedManager, componentConfig, 'widget-holder');
});

The following table describes the available properties for `componentConfig`.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"theme":"dark"` | `composer` | The theme for the embedded visual. Valid values are `composer`, `modern`, or `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-UI-Themes) to the application, more options are available in this list and you may have introduced a different default.  Type: string |

The following table describes the available `header` properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"showTitle": true` | `true` | Indicates whether the visual header title should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"visible": false` | `true` | Indicates whether the visual header should be visible for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"showActions": false` | `true` | Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"title": <text>` | none | Specifies a static title for the visual.  Type: string |

The following table describes the available `breadcrumb` properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `<optional breadcrumb properties>` |  | Optional breadcrumb properties are described in [Optional Embedded Visual Authoring Breadcrumb Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701102946701-Optional-Embedded-Visual-Authoring-Breadcrumb-Properties). |
| `"breadcrumbs.onClick"` | none | The click action handler for the breadcrumb title.  Type: function |
| `"breadcrumbs.target":"_blank"` | none | The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).  Type: string |
| `"breadcrumbs.title":"<title>"` | none | The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).  Type: string |

The following table describes the available properties for source visualID.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"source.visualId":"<id>"` | null | The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |
| `"interactivityOverrides"` | none | Specifies interactivity override settings for visual authoring. The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals. For a list of visual interactivity settings you can specify, see [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).  Type: object |
| `"visualId":"<id>"` | null | The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`). If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened. If both are provided, `visualId` is used.  Type: string |

The following table describes all of the available properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `<optional breadcrumb properties>` | Optional breadcrumb properties are described in [Optional Embedded Visual Authoring Breadcrumb Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701102946701-Optional-Embedded-Visual-Authoring-Breadcrumb-Properties). | |
| `"breadcrumbs.onClick"` | none | The click action handler for the breadcrumb title.  Type: function |
| `"breadcrumbs.target":"_blank"` | none | The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).  Type: string |
| `"breadcrumbs.title":"<title>"` | none | The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).  Type: string |
| `"header.showActions": false` | `true` | Indicates whether the visual header actions should be shown for the embedded visual. Valid values are `true` or `false`.  Type: boolean |
| `"header.showTitle": false` | `true` | Indicates whether the visual header title should be shown for the embedded visual.  Valid values are `true` or `false`.  Type: boolean |
| `"header.title": <text>` | none | Specifies a static title for the visual.  Type: string |
| `"header.visible": false` | `true` | Indicates whether the visual header should be visible for the embedded visual.  Valid values are `true` or `false`.  Type: boolean |
| `"interactivityOverrides"` | none | Specifies interactivity override settings for visual authoring.  The interactivity settings specified in this object will override any interactivity settings specified for the individual visuals.  For a list of visual interactivity settings you can specify, see [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).  Type: object |
| `"source.visualId":"<id>"` | null | The source ID of a visual template, used for creating a new visual in visual authoring. This represents a predefined visual template. A valid source ID should be specified in quotes (`"<source-visual-ID>"`).  If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened.  If both are provided, `visualId` is used.  Type: string |
| `"theme":"dark"` | `composer` | The theme for the embedded visual. Valid values are `composer`, `modern`, or `dark`.  The initial default theme, `composer`, is the same as the `modern` theme.  However, if you [add your own themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-UI-Themes) to the application, more options are available in this list and you may have introduced a different default.  Type: string |
| `"visualId":"<id>"` | null | The visual ID for an existing visual for visual authoring. A valid visual ID should be specified in quotes (`"<visual-ID>"`).  If neither `visualId` or `source.visualId` is specified, an empty visual authoring instance will be opened.  If both are provided, `visualId` is used.  Type: string |

**Note:** 
You can include several controls for embedded visuals, allowing users to select and deselect favorite visuals, as well as filter the list of visuals in the embedded Visual Gallery by favorite status. See [Use the Visual Gallery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701180261773-Use-the-Visual-Gallery).
