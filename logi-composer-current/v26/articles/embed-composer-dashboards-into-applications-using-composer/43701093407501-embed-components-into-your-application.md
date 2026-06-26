---
title: "Embed  Components Into Your Application"
id: 43701093407501
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093407501-Embed-Components-Into-Your-Application
updated_at: 2026-05-29T14:08:05Z
---

# Embed  Components Into Your Application

# Embed Components Into Your Application

Embed components into your own applications to provide seamless integration for your users.

The following components can be embedded:

* dashboards, lite dashboards
* visual authoring experience
* source editor

When components are embedded, the way in which users can interact with them is determined by settings established in their user account. See [Embedded Composer Component Controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081977869-Embedded-Composer-Component-Controls).

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access) for all embed-related workflows.

The list of options available on an embedded [visual's drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) [**Read Only**](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081719053-Generate-an-Embeddable-Dashboard-HTML-Snippet), no menu is available at all.
* The [visual interactivity settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual) specified in the visual definition.
* The [dashboard interactivity settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076696717-Control-How-Users-Interact-With-a-Dashboard) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) or within the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) itself, depending on the setting of the [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) property.

* If [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) and the resulting sidebar editing panels.

  If [`editor.placement`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects) is set to `modals`, the options appear in the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) itself and the resulting floating dialogs.

**Note:** 
In environments where you use Typescript for your client side code, you can use Embed Manager as an npm package. See <https://www.npmjs.com/package/logi-embed>.

See the following topics for embedding components using JavaScript:

* [Embedded Component Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117720077-Embedded-Component-Prerequisites)
* [Token-Related Configuration Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070712973-Token-Related-Configuration-Properties)
* [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)
* [EmbedManager Methods](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117892237-EmbedManager-Methods)
* [Embedded Dashboard Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects)
* [Embedded Visual Authoring Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070653325-Embedded-Visual-Authoring-Properties-and-Objects)
* [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events)
* [Interactivity Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070270733-Interactivity-Properties)
* [Embedded Composer Component Controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081977869-Embedded-Composer-Component-Controls)

See the following topics for embedding a dashboard using an embeddable dashboard snippet:

* [Embedded Component Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117720077-Embedded-Component-Prerequisites)
* [Generate an Embeddable Dashboard HTML Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081719053-Generate-an-Embeddable-Dashboard-HTML-Snippet)
* [Generate a Visual Gallery HTML Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701086397581-Generate-a-Visual-Gallery-HTML-Snippet)
* [Embed a Dashboard Using a Generated Snippet and Trusted Access Tokens](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098820877-Embed-a-Dashboard-Using-a-Generated-Snippet-and-Trusted-Access-Tokens)
* [Embedded Composer Component Controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081977869-Embedded-Composer-Component-Controls)
* [Embed Multiple Dashboards On a Single Page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070120717-Embed-Multiple-Dashboards-On-a-Single-Page)

See the following topics for embedding the source editor:

* [Embedded Source Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071044493-Embedded-Source-Editor)
* [Embed Source Editor Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070976013-Embed-Source-Editor-Properties)
