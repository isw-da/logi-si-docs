---
title: "IIS: ASP.NET Impersonation "
id: 4406822503831
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822503831-IIS-ASP-NET-Impersonation
updated_at: 2022-04-06T06:08:29Z
---

# IIS: ASP.NET Impersonation 

# IIS: ASP.NET Impersonation

This scenario, shown with IIS 7.5, lets you run your Logi application under a different security context. This is a required configuration when using Logi OLAP to connect to Microsoft SQL Server Analysis Services cubes via the MSOLAP provider.

To configure your Logi Application for this type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563098391/logisecsen_03_558x297.png)

1. Using the **IIS Manager** utility, select your Logi application, and then select the **Authentication** feature.
2. Disable the *Anonymous Authentication* option, as shown above.
3. Enable the *ASP.NET Impersonation*  option, as shown above.
4. Right-click the option and select Edit..., then enter credentials for the account you want to impersonate in the resulting dialog box.
5. Enable the *Windows Authentication* option, as shown above.
6. Exit the feature and restart the appropriate Application Pool.

Now, when the URL for your Logi application is browsed, authorized domain users will not see a login dialog box at all; instead they'll proceed directly into the Logi application and the appropriate impersonated credentials will be used for connection to other services.
