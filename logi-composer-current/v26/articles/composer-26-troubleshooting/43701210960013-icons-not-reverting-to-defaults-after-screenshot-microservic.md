---
title: "Icons Not Reverting to Defaults After Screenshot Microservice Disabled"
id: 43701210960013
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210960013-Icons-Not-Reverting-to-Defaults-After-Screenshot-Microservice-Disabled
updated_at: 2026-05-29T14:09:37Z
---

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

The screenshot microservice can be enabled in Composer using CentOS and Ubuntu. However, users might notice that even after disabling the screenshot microservice, Composer
continues to use existing screenshot images and does **not** automatically revert back to the original default icons for visuals or dashboards used by Composer after installation. To revert the icons used by Composer for the visuals or dashboards before the screenshot microservice was enabled, you must delete all the screenshots in the metadata directly.

To do this in MongoDB, run the following commands:

use zoom;
db.screenshots.remove({});

Use the `mongo` command to access the mongo shell through the Linux command line.

**Note:** 
Make sure you disable the screenshot microservice as well via the `zoomdata.conf` and `zoomdata.properties` files and restart the Composer microservice for the changes to take effect.
