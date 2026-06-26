---
title: "Optional Embedded Visual Authoring Breadcrumb Properties"
id: 34932936970765
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936970765-Optional-Embedded-Visual-Authoring-Breadcrumb-Properties
updated_at: 2026-05-26T22:07:16Z
---

# Optional Embedded Visual Authoring Breadcrumb Properties

# Optional Embedded Visual Authoring Breadcrumb Properties

Optionally, you can pass breadcrumb properties as parameters to the [`createComponent` method](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932928903565-EmbedManager-Methods) when embedding Composer visual authoring components.

Here is a sample:

"breadcrumbs": {
"[title](#title)": "<title>",
"[onClick](#onClick)": () => {console.log('clicked')},
"[href](#href)": "<uri-or-fqdn>",
"[target](#target)": "\_blank"
}

The following table describes the optional breadcrumb properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"title":"<title>"` | none | The first item breadcrumbs title. A valid title should be specified in quotes (`"<title>"`).  Type: string |
| `"onClick"` | none | The click action handler for the breadcrumb title.  Type: function |
| `"href":"<uri-or-fqdn>"` | none | The link address of the breadcrumb title.  A valid link address, such as a URI or Fully Qualified Domain Name should be specified in quotes (`"<uri-or-fqdn>"`).  Type: string |
| `"target":"_blank"` | none | The link target parameter. Use `"_blank"` to open in a new tab.  A valid link target should be specified in quotes (`"<uri-or-fqdn>"`).  Type: string |
