---
title: "Configuring Scheduler and SMTP Services"
id: 4406817197335
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817197335-Configuring-Scheduler-and-SMTP-Services
updated_at: 2022-04-06T06:10:45Z
---

# Configuring Scheduler and SMTP Services

# Configuring Scheduler and SMTP Services

As an optional feature, InfoGo allows you to schedule report production and delivery via email.

![](https://devnet.logianalytics.com/hc/article_attachments/5263096722455/criticalicon.png) The scheduling feature is dependent on the **Logi Scheduler**, a service that must be installed with Logi Info. If the Scheduler is *not* installed, you can re-run the Logi Info installer at any time and install it.

Use the following steps to configure these features:

![](https://devnet.logianalytics.com/hc/article_attachments/5263068973079/cfginfogo125_05.png)

1. Configure the Scheduler: In the InfoGo application's \_Settings definition, uncomment the "goScheduler" element, as shown above. Its default attributes will work in most scenarios. For more detailed information about other configurations, see [Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406818028311-Using-Logi-Scheduler).  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/5263060301335/cfginfogo125_06.png)
2. Enable the Scheduler icons: In the \_Settings definition, set the "goSchedulerEnabled" constant to *True*, as shown above. This controls the appearance of the Scheduler icons for items in the Home page.

# 

3. Uncomment the "goMail" element and provide an email server name, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5263090352407/cfginfogo125_08.png)

Once scheduling has been configured and enabled, a scheduling icon will appear for each **Report** item in the Home page resource list, as shown above. Users can click this icon at runtime to schedule report production and delivery.
