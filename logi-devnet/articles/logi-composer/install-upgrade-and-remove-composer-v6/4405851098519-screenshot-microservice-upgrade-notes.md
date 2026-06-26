---
title: "Screenshot Microservice Upgrade Notes"
id: 4405851098519
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851098519-Screenshot-Microservice-Upgrade-Notes
updated_at: 2021-09-21T01:28:56Z
---

# Screenshot Microservice Upgrade Notes

# Screenshot Microservice Upgrade Notes

After upgrading, the screenshots on the Home page may look different. This occurs if there has been a change in the screenshot aspect ratio. To make the screenshots look correct, make sure that the
`screenshot.daemon.enabled` property in the `zoomdata.properties` file is set to `true`. Remember to restart the Composer server microservice after the change (see [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices)).

After you have updated the properties file, you can update the screenshots in one of the following ways:

* In the `zoomdata.properties` file, modify the `screenshot.daemon.schedule.rate` property and set it to a more frequent refresh rate.
* Execute a cURL call to update a screenshot for a specific dashboard.
* Execute a cURL call to upload a custom image for a specific dashboard. Otherwise, the screenshots will be updated when the refresh screenshot procedure runs according to the configured refresh rate.
