---
title: "Analysis Filter - Saving Individual User Settings"
id: 4419715047575
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715047575-Analysis-Filter-Saving-Individual-User-Settings
updated_at: 2022-07-17T02:02:20Z
---

# Analysis Filter - Saving Individual User Settings

# Analysis Filter - Saving Individual User Settings

The Analysis Filter will automatically save a user's runtime filter changes during their session, if the **Save File** attribute is set. The file specified will be created if it does not exist but its containing folder is not automatically created. You must ensure that the account used by the web server to run the application has "Write" permission to the folder (usually, creating the folder under the application's root folder will handle this).

You can also save separate configurations for each user that survive their sessions. If Logi Security is being used, include the @Function.UserName~ token as part of the Save File name. If not, you can use @Function.GUID~ to generate a unique file name for the user and then save the file name as a cookie in the user's browser.
