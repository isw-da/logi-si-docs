---
title: "Embed Composer Components Into Your Application"
id: 4405859263895
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application
updated_at: 2021-09-21T01:27:44Z
---

# Embed Composer Components Into Your Application

# Embed Composer Components Into Your Application

You can embed Composer components into your own applications.

The following components can be embedded:

* dashboards
* visual authoring experience.

When components are embedded, the way in which users can interact with them is determined by settings established by their Composer user definition. See [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405851048727-Embedded-Composer-Component-Controls).

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

The list of options available on an embedded [visual's drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) [**Read Only**](https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet), no menu is available at all.
* The [visual interactivity settings](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual) specified in the visual definition.
* The [dashboard interactivity settings](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) or within the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) itself, depending on the setting of the [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) property.

* If [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) and the resulting sidebar editing panels.

  If [`editor.placement`](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) is set to `modals`, the options appear in the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) itself and the resulting floating dialogs.

See the following topics for embedding components using JavaScript:

* [*Embedded Component Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851046679-Embedded-Component-Prerequisites)
* [*Token-Related Configuration Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859343511-Supported-Token-Related-Configuration-Properties)
* [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access)
* [*EmbedManager Methods*](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods)
* [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects)
* [*Embedded Visual Authoring Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851051543-Supported-Embedded-Visual-Authoring-Properties-and-Objects)
* [*Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4405851052695-Supported-Composer-v6-Embedded-Events)
* [*Interactivity Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405851049623-Supported-Interactivity-Properties)
* [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405851048727-Embedded-Composer-Component-Controls)

See the following topics for embedding a dashboard using an embeddable dashboard snippet:

* [*Embedded Component Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851046679-Embedded-Component-Prerequisites)
* [*Generate an Embeddable Dashboard HTML Snippet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet)
* [*Embed a Dashboard Using a Generated Snippet and OAuth Access Tokens*](https://devnet.logianalytics.com/hc/en-us/articles/4405851047703-Embed-a-Dashboard-Using-a-Generated-Snippet-and-OAuth-Access-Tokens)
* [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405851048727-Embedded-Composer-Component-Controls)
* [*Embed Multiple Composer Dashboards On a Single Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405851045783-Embed-Multiple-Composer-Dashboards-On-a-Single-Page)
