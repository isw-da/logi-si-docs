---
title: "Icons Not Reverting to Defaults After Screenshot Microservice Disabled"
id: 34933205076749
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933205076749-Icons-Not-Reverting-to-Defaults-After-Screenshot-Microservice-Disabled
updated_at: 2026-05-26T22:08:27Z
---

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

The Screenshot microservice can be enabled in Composer using CentOS and Ubuntu. However, users might notice that even after disabling the Screenshot microservice, Composer
continues to use existing screenshot images and does **not** automatically revert back to the original default icons for visuals or dashboards used by Composer after installation. To revert the icons used by Composer for the visuals or dashboards before the Screenshot microservice was enabled, you must delete all the screenshots in the metadata directly.

To do this in MongoDB, run the following commands:

use zoom;
db.screenshots.remove({});

Use the `mongo` command to access the mongo shell through the Linux command line.

**Note:** 
Make sure you disable the Screenshot microservice as well via the `zoomdata.conf` and `zoomdata.properties` files and restart the Composer microservice for the changes to take effect.
