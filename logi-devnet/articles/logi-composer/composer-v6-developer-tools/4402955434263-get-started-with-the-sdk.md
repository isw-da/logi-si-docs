---
title: "Get Started with the SDK"
id: 4402955434263
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955434263-Get-Started-with-the-SDK
updated_at: 2021-08-07T17:29:15Z
---

# Get Started with the SDK

# Get Started with the SDK

The Composer Software Development Kit (SDK) is a set of tools to help software developers extend Composer's capabilities and embed them into custom and third-party applications. It is intended for use by software developers.
Be sure to read [*Composer REST API Overview*](https://devnet.logianalytics.com/hc/en-us/articles/4402955436951-Composer-REST-API-Overview) as well as the following topics.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access) for all embed-related workflows.

* [*What Can I Do with the SDK?*](#What)
* [*What's in the Box?*](#What's)
* [*What Do I Need to Get Started?*](#What2)
* [*Where Do I Begin?*](#Where)

## What Can I Do with the SDK?

The Composer SDK allows you to extend and embed Composer's data analytics server to fit your own particular needs. You can:

* Use Composer data in your own web application
* Embed a Composer visual in your own web application
* Create a custom chart to use in Composer or your own web application
* Use Composer administrative controls in your own application
* Use [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access) to secure your application's use of Composer

## What's in the Box?

The Composer SDK is a toolkit for extending Composer's native capabilities and for embedding Composer analytics in your own application. It includes:

* **JavaScript client** (the application framework) - to query data and embed visuals from Composer in a custom web application
* **REST APIs** - to programmatically manage Composer's administrative features, including sources, groups and users, security, and more.
* **Visualization Framework** - to add new visuals to Composer gallery
* **Samples** - working code to help you see the various APIs in action
* **How-to guides** - to provide steps for different common tasks
* **Reference documentation** - for easily looking up various object definitions and methods.

## What Do I Need to Get Started?

The Composer SDK is a toolkit to augment your own skills and tools as you build your own applications and extend Composer itself. To get started, you need:

* access to
  **a Composer server**
* **administrative access** to one or more accounts on the server, or ideally supervisor access to the server itself
* some
  **data**
* **competence with JavaScript** and web development principles, if you want to use Composer's client library or visualization framework
* an
  **understanding of REST APIs** and web asynchronous processes, if you intend to use Composer's REST APIs

## Where Do I Begin?

How you get started with Composer depends upon what you want to do.

| I want to... | Description |
| --- | --- |
| customize the way the Composer app looks: the login screen, the logo, and so on. | You do not need the SDK to make customizations to the Composer application. For information about customizing the look and feel of the Composer app, see [*White Label the Composer Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4402962887703-White-Label-the-Composer-Interface). |
| create dashboards of visuals. | You do not need the SDK to create dashboards of Composer visuals. For information about creating dashboards in the Composer application, see [*Manage Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4402962942615-Manage-Dashboards) . |
| add a new visual to the Composer gallery of visuals. | The Composer SDK includes a JavaScript framework for creating or importing visuals and adding them to those provided by Composer. For more information, see [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4402955500311-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI) . |
| modify an existing Composer visual's functionality. | The Composer SDK includes templates for its visuals. You can create a new visual from one of these templates and modify the template to your own specifications. For more information, see [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4402955500311-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI) . |
| embed a visual in my own custom web application. | The SDK includes a JavaScript client library that allows you to embed a visual in your web app. For more information, see [*Embed a Visual in Your Web Page*](https://devnet.logianalytics.com/hc/en-us/articles/4402955438231-Embed-a-Visual-in-Your-Web-Page) .  Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access) for all embed-related workflows. |
| use data from Composer in my own custom web application. | The SDK includes a JavaScript client library that allows you to use data from Composer in your web app. For more information, see [*Use a Data Query*](https://devnet.logianalytics.com/hc/en-us/articles/4402955437591-Use-a-Data-Query). |
| manage Composer users, accounts, data sources, etc., in my own custom application or script. | The SDK includes a large number of REST methods that allow you administer the metadata of your Composer server in your own application or using cURL or a REST client. For more information, see [*Composer REST API Overview*](https://devnet.logianalytics.com/hc/en-us/articles/4402955436951-Composer-REST-API-Overview) . |
| use [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access) to securely access Composer functionality in my own application. | For more information, see [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access). |
