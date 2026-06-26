---
title: "Composer 6.5 Enhancements"
id: 4405851163799
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851163799-Composer-6-5-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.5 Enhancements

# Composer 6.5 Enhancements

This topic describes the significant enhancements in Composer 6.5.

* [*New Trusted Access Authorization Introduced*](#New)
* [*Embedded Dashboard Changes*](#Embedded)
* [*User Interface Changes*](#User)

## New Trusted Access Authorization Introduced

Composer now provides its own security methodology that allows for machine-to-machine authorization of Composer resources when embedded in your application (the “parent” application). This is a form of “delegated” authorization where the parent application can determine, on demand, how and when to authorize any given embedded Composer component to an end-user logged into the parent application. This methodology is called *Trusted Access*.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

On request from the parent application, Trusted Access provides a user access token with defined authorization rules that account for user privileges, object permissions, security filters and any specific user attributes used in interpolation. This user access token can then be used in the parent application to serve any Composer specific embedded components such as dashboards for the respective user. For information on how tokens are initiated and requested in your applications, see [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

New API endpoints have been introduced to support Trusted Access. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

For complete information, see [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access).

## Embedded Dashboard Changes

In this release, some significant changes were made to how dashboards can be embedded in your applications. Primarily, while your existing embedded dashboard HTML snippets will continue to work, this release introduces the ability to embed dashboards using JavaScript code. This is more powerful than the HTML script snippet provided in previous releases because it provides you with more tailoring options for the dashboards in your application. The following changes were made:

* The Advanced options (**Root**, **Embed ID**, **Show Banner**, **Show Header**, **Show Logo**, **Show Title**, **Show Breadcrumbs**, and **Show Actions**) previously available on the Embed Code dialog that produces an embeddable HTML script snippet have been removed. Any existing applications you have that use an embedded dashboard that uses these options will still work. However, new embedded dashboards are encouraged to use JavaScript instead. See [*Generate an Embeddable Dashboard HTML Snippet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).
* A new `EmbedManager` class has been added. Use the methods in this class to manage a dashboard in your application. This endpoint provides multiple functions that can be used to create the dashboard, remove it, reload it, and update it. See [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).
* A new `initComposerEmbedManager` function has been added. Use this `window` method to initialize and authorize the new Composer EmbedManager class in your application. See [*Token-Related Configuration Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859343511-Supported-Token-Related-Configuration-Properties)
* New Composer embedded events have been added that you can use in your JavaScript to better tailor how the dashboard behaves in your application. See [*Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4405851052695-Supported-Composer-v6-Embedded-Events).
* You can embed multiple Composer dashboards on a single page of your application and in a single `<div>` in your application, including embedding one or more empty dashboards. You can also embed the same dashboard multiple times on a page and each embedded instance can use its own property settings (theme, mode, header, title). Finally, the dashboards can be embedded using different methods: you can embed one dashboard using [generated embed code](https://devnet.logianalytics.com/hc/en-us/articles/4405851047703-Embed-a-Dashboard-Using-a-Generated-Snippet-and-OAuth-Access-Tokens) and another dashboard using [JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

  In past releases, you could only embed a single dashboard on an application page.

  See [*Embed Multiple Composer Dashboards On a Single Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405851045783-Embed-Multiple-Composer-Dashboards-On-a-Single-Page).

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

For complete information about embedding dashboards, see [*Embed Composer Components Into Your Application*](https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application). A JavaScript example embedding a dashboard is provided in [*Embedded Dashboard JavaScript Example*](https://devnet.logianalytics.com/hc/en-us/articles/4405851053719-Embedded-Dashboard-JavaScript-Example).

## User Interface Changes

The following changes were made to the user interface in this release:

* The Advanced options (**Root**, **Embed ID**, **Show Banner**, **Show Header**, **Show Logo**, **Show Title**, **Show Breadcrumbs**, and **Show Actions**) previously available on the Embed Code dialog that produces an embeddable HTML script snippet have been removed. Any existing applications you have that use an embedded dashboard that uses these options will still work. However, new embedded dashboards are encouraged to use JavaScript instead. See [*Generate an Embeddable Dashboard HTML Snippet*](https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).
* The **OAUTH** option on the [Security page](https://devnet.logianalytics.com/hc/en-us/articles/4405859465111-Enable-Trusted-Access-and-OAuth-2-0) of the Supervisor UI has been renamed **Trusted Access & OAUTH**.
