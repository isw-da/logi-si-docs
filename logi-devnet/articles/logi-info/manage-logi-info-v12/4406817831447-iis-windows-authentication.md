---
title: "IIS: Windows Authentication  "
id: 4406817831447
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817831447-IIS-Windows-Authentication
updated_at: 2022-04-06T06:08:30Z
---

# IIS: Windows Authentication  

# IIS: Windows Authentication

In this scenario, shown with IIS 7.5, the name of a user who has already been authenticated by Windows domainor network security is supplied to the Logi application. This is a very secure form of authentication and convenient for users because theydo not have to login twice.

To configure your Logi Application for either type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583744791/logisecsen_04_470x227.png)

1. Using the **IIS Manager** utility, select your Logi application, and then select the **Authentication** feature.
2. Disable the *Anonymous Authentication* option, as shown above.
3. Enable the *Windows Authentication* option, as shown above.
4. Exit the feature and restart the appropriate Application Pool.

Now, when the URL for your Logi application is browsed, authorized domain users will not see a login dialog box at all; instead they'll proceed directly into the Logi application. Users who are not authorized will be redirected to an error page.
