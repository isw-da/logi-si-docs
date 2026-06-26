---
title: "Server-Level Variables"
id: 4405850889495
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850889495-Server-Level-Variables
updated_at: 2021-09-21T01:26:49Z
---

# Server-Level Variables

# Server-Level Variables

Server-level variables can be viewed by Composer supervisors on the Server-Level Variables page.

Use your supervisor credentials to access these variables. Select the **Advanced** menu to access the Server-Level Variables page. Do not add or delete any variables on this page. If you do, you could compromise your Composer environment.

Server-level variables are defined as key-value pairs.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Server-level variables are set by Composer and, with the exception described next, must not be changed. Changing a variable could potentially compromise your Composer environment. If you must change a server-level variable, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

The only server-level variable that you might change is the `dashboard-v1-api` key. Slide this key on (`true`) to use `vnd.composer.dashboards.v1+json` for backward compatibility for the `/api/dashboards` endpoint, including the use of the `bookmarksMap` object (instead of the new `content` object). Be sure to select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747454743/save-blue-supervisor-btn_73x25.png) at the bottom of the page to save your changes. For more information, see the discussion of the `/api/dashboards` endpoint in the Composer 6.9 API Updates in [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The `dashboard-v1-api` key is deprecated and will be removed in a future release.
