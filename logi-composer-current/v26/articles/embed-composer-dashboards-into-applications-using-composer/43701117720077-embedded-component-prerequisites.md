---
title: "Embedded Component Prerequisites"
id: 43701117720077
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117720077-Embedded-Component-Prerequisites
updated_at: 2026-05-29T14:08:31Z
---

# Embedded Component Prerequisites

# Embedded Component Prerequisites

To embed a Composer component into your own application, the following prerequisites must be met:

* You must have created a host application into which you want to embed the component.
* [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access), enabled by default, must be enabled and configured to authenticate users of your embedded components. See [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access). Be sure that your application is registered as a Composer client and that you have met the [prerequisites of Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access#Prerequi).

  **Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access) for all embed-related workflows.
* Cross-origin sharing (CORS) must be enabled for your Composer instance. See [Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054098061-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS).
* You need to be a Composer administrator or a user assigned to a group with the **Generate Embed Code** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) so you can generate [library](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081719053-Generate-an-Embeddable-Dashboard-HTML-Snippet), [visual gallery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701086397581-Generate-a-Visual-Gallery-HTML-Snippet), or [sources inventory](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117598861-Generate-a-Sources-Inventory-HTML-Snippet) snippets used for embedding.
