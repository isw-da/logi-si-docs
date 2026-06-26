---
title: "Embed  Components Into Your Application"
id: 34932763726605
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763726605-Embed-Components-Into-Your-Application
updated_at: 2026-05-26T22:06:55Z
---

# Embed  Components Into Your Application

# Embed Components Into Your Application

You can embed Composer components into your own applications.

The following components can be embedded:

* dashboards, lite dashboards
* visual authoring experience
* source editor

When components are embedded, the way in which users can interact with them is determined by settings established in their Composer user account. See [Embedded Composer Component Controls](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932935896589-Embedded-Composer-Component-Controls).

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access) for all embed-related workflows.

The list of options available on an embedded [visual's drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects) [**Read Only**](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919505677-Generate-an-Embeddable-Dashboard-HTML-Snippet), no menu is available at all.
* The [visual interactivity settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933282294029-Control-How-Users-Interact-With-a-Visual) specified in the visual definition.
* The [dashboard interactivity settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814650893-Control-How-Users-Interact-With-a-Dashboard) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) or within the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) itself, depending on the setting of the [`editor.placement`](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects) property.

* If [`editor.placement`](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) and the resulting sidebar editing panels.

  If [`editor.placement`](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects) is set to `modals`, the options appear in the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) itself and the resulting floating dialogs.

**Note:** 
In environments where you use Typescript for your client side code, you can use Embed Manager as an npm package. See <https://www.npmjs.com/package/logi-embed>.

See the following topics for embedding components using JavaScript:

* [Embedded Component Prerequisites](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932946576909-Embedded-Component-Prerequisites)
* [Token-Related Configuration Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932950694029-Token-Related-Configuration-Properties)
* [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930219405-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)
* [EmbedManager Methods](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932928903565-EmbedManager-Methods)
* [Embedded Dashboard Properties and Objects](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects)
* [Embedded Visual Authoring Properties and Objects](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932921551501-Embedded-Visual-Authoring-Properties-and-Objects)
* [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events)
* [Interactivity Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932920874253-Interactivity-Properties)
* [Embedded Composer Component Controls](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932935896589-Embedded-Composer-Component-Controls)

See the following topics for embedding a dashboard using an embeddable dashboard snippet:

* [Embedded Component Prerequisites](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932946576909-Embedded-Component-Prerequisites)
* [Generate an Embeddable Dashboard HTML Snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919505677-Generate-an-Embeddable-Dashboard-HTML-Snippet)
* [Generate a Visual Gallery HTML Snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915110285-Generate-a-Visual-Gallery-HTML-Snippet)
* [Embed a Dashboard Using a Generated Snippet and Trusted Access Tokens](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932920270221-Embed-a-Dashboard-Using-a-Generated-Snippet-and-Trusted-Access-Tokens)
* [Embedded Composer Component Controls](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932935896589-Embedded-Composer-Component-Controls)
* [Embed Multiple Composer Dashboards On a Single Page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932919997069-Embed-Multiple-Composer-Dashboards-On-a-Single-Page)

See the following topics for embedding the source editor:

* [Embedded Source Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932951431309-Embedded-Source-Editor)
* [Embed Source Editor Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982468749-Embed-Source-Editor-Properties)
