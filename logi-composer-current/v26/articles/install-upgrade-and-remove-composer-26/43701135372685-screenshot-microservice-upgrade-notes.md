---
title: "Screenshot Microservice Upgrade Notes"
id: 43701135372685
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135372685-Screenshot-Microservice-Upgrade-Notes
updated_at: 2026-05-29T14:08:49Z
---

# Screenshot Microservice Upgrade Notes

# Screenshot Microservice Upgrade Notes

After upgrading, the screenshots on the Home page may look different. This occurs if there has been a change in the screenshot aspect ratio. To make the screenshots look correct, make sure that the
`screenshot.daemon.enabled` property in the `zoomdata.properties` file is set to `true`. Remember to restart the Composer server microservice after the change (see  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart)).

After you have updated the properties file, you can update the screenshots in one of the following ways:

* In the `zoomdata.properties` file, modify the `screenshot.daemon.schedule.rate` property and set it to a more frequent refresh rate.
* Execute a cURL call to update a screenshot for a specific dashboard.
* Execute a cURL call to upload a custom image for a specific dashboard. Otherwise, the screenshots will be updated when the refresh screenshot procedure runs according to the configured refresh rate.
