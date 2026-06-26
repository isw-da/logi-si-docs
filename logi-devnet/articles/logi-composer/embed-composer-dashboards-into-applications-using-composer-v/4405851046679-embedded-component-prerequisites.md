---
title: "Embedded Component Prerequisites"
id: 4405851046679
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851046679-Embedded-Component-Prerequisites
updated_at: 2021-09-21T01:28:28Z
---

# Embedded Component Prerequisites

# Embedded Component Prerequisites

To embed a Composer component into your own application, the following prerequisites must be met:

* You must have created a host application into which you want to embed the Composer component.
* [OAuth](https://devnet.logianalytics.com/hc/en-us/articles/4405859465111-Enable-Trusted-Access-and-OAuth-2-0) authentication or [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) must be enabled.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

  If Trusted Access will be used to authenticate users of your embedded components, be sure it is enabled and configured. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access). Be sure that your application is registered as a Composer client and that you have met the [prerequisites of Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access#Prerequi).
* Cross-origin sharing (CORS) must be enabled for your Composer instance. See [*Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)*](https://devnet.logianalytics.com/hc/en-us/articles/4405850901783-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS-).
* You will need to be a Composer administrator or a user assigned to a group with the **Can Generate Embed Code**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) so you can generate any dashboard snippets used for embedding.
