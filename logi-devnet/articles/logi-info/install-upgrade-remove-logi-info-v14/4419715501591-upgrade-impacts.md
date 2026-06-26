---
title: "Upgrade Impacts"
id: 4419715501591
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715501591-Upgrade-Impacts
updated_at: 2022-07-17T02:06:08Z
---

# Upgrade Impacts

# Upgrade Impacts

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Logi v12 products include several changes you should know about *before* upgrading:

* Logi v12 products include stylistic and appearance improvements in charts, super elements, themes, etc. which are noticeably different. You may care to do a test upgrade before committing to a comprehensive upgrade.
* The built-in Themes shipped with Logi v12.1+ have been changed internally to allow customization with the Theme Editor tool. Custom Themes you may have created based on earlier versions of the built-in Themes *will continue to work* correctly in v12.1+ but may not be editable in the Theme Editor. To make them so, you will have to recreate your customizations starting with one of the new built-in Themes.
* You *must* use Application Pools that use .NET 4.x. If such an application pool doesn't exist, Studio will generate a warning when you upgrade an existing Logi application. When you create a new application, Studio will create a new application pool, named "Logi Info .Net v4.x", and will assign the application to it.
* Logi Info includes a free, 15-day trial license but, when it expires, you will need to purchase a regular license. If you're a customer in good standing, Logi Customer Service will assign that license to you in advance, but you will need to go to DevNet and download the license file.
