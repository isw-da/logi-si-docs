---
title: "Icons Not Reverting to Defaults After Screenshot Microservice Disabled"
id: 4402955690007
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955690007-Icons-Not-Reverting-to-Defaults-After-Screenshot-Microservice-Disabled
updated_at: 2021-08-07T17:32:11Z
---

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

# Icons Not Reverting to Defaults After Screenshot Microservice Disabled

The Screenshot microservice can be enabled in Composer using CentOS and Ubuntu. However, users might notice that even after disabling the Screenshot microservice, Composer
continues to use existing screenshot images and does **not** automatically revert back to the original default icons for visuals or dashboards used by Composer after installation. To revert the icons used by Composer for the visuals or dashboards before the Screenshot microservice was enabled, you must delete all the screenshots in the metadata directly.

To do this in MongoDB, run the following commands:

```
use zoom;
db.screenshots.remove({});
```

Use the `mongo` command to access the mongo shell through the Linux command line.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Make sure you disable the Screenshot microservice as well via the `zoomdata.conf` and `zoomdata.properties` files and restart the Composer microservice for the changes to take effect.
