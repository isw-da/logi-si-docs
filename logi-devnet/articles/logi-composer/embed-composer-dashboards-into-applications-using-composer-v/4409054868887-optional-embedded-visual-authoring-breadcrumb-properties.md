---
title: "Optional Embedded Visual Authoring Breadcrumb Properties"
id: 4409054868887
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4409054868887-Optional-Embedded-Visual-Authoring-Breadcrumb-Properties
updated_at: 2021-09-21T01:26:23Z
---

# Optional Embedded Visual Authoring Breadcrumb Properties

# Optional Embedded Visual Authoring Breadcrumb Properties

Optionally, you can pass breadcrumb properties as parameters to the [`createComponent` method](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods) when embedding Composer visual authoring components.

Here is a sample:

```
     "breadcrumbs": { // optional configuration of the breadcrumbs
          "title": "Visuals",
          "onClick": () => {console.log('clicked')},
          "href": "http://www.google.com",
          "target": "_blank"
     }
```

The following table describes the optional breadcrumb properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"breadcrumbs.href":"<address>"` | none | The link address of the breadcrumb title. A valid link address should be specified in quotes (`"<address>"`).  Type: string |
| `"breadcrumbs.onClick"` | none | The click action handler for the breadcrumb title.  Type: function |
| `"breadcrumbs.target":"_blank"` | none | The link target parameter. Use `"_blank"` to open in a new tab. A valid link target should be specified in quotes (`"<target>"`).  Type: string |
| `"breadcrumbs.title":"<title>"` | none | The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).  Type: string |
