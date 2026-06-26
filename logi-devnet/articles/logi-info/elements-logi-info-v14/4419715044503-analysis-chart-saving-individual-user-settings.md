---
title: "Analysis Chart - Saving Individual User Settings"
id: 4419715044503
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715044503-Analysis-Chart-Saving-Individual-User-Settings
updated_at: 2022-07-17T02:02:28Z
---

# Analysis Chart - Saving Individual User Settings

# Analysis Chart - Saving Individual User Settings

The Analysis Chart will automatically **save** a user's runtime configuration changes during their session, if the **Save File** attribute is set. The file specified will be created if it does not exist but its containing folder is not automatically created. You must ensure that the account used by the web server to run the application has "Write" permission to the folder.

Save files can also be stored in a database, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks).

You can also save separate configurations for each user that survive their session. If Logi Security is being used, include the @Function.UserName~ token as part of the Save File name. If not, use @Function.GUID~ to generate a unique file name for the user and save the file name as a cookie in the user's browser.

Users' settings can be cleared by calling the Analysis Chart report with the **rdAcReset** parameter set to *True*. To get fresh data from the datasource while maintaining the user's settings, call the report with the **rdAcRefreshData** parameter set to *True*.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699534615/workac_08.png)

In the example above, a Label has been added to an Analysis Report as a link that clears the user's settings. The Target.Report element is set to *Current Report* and the Link Parameters element is used to pass the rdAcReset parameter.
