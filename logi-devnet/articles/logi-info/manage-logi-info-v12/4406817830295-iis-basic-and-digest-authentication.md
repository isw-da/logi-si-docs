---
title: "IIS: Basic and Digest Authentication "
id: 4406817830295
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817830295-IIS-Basic-and-Digest-Authentication
updated_at: 2023-01-30T18:41:27Z
---

# IIS: Basic and Digest Authentication 

# IIS: Basic and Digest Authentication

This scenario simply configures the web server, IIS 7.5, to require valid credentials before allowing any access to the Logi application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) When using **Basic****Authentication**, user login credentials are sent to the web server in plain text, without any encryption. Anyone attempting to compromise your system security could intercept network messages and examine the unencrypted credentials. This security method is *not* recommended for use on public networks. **Digest****Authentication** improves on this
by sending hashed
credentials.

To configure your Logi Application for either type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563098135/logisecsen_01.png)

1. Using the **IIS Manager** utility, select your Logi application, and then select the **Authentication** feature.
2. Disable the *Anonymous Authentication* option, as shown above.
3. Enable the *Basic Authentication* or *Digest Authentication* option, as shown above.
4. Exit the feature and restart the appropriate Application Pool.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575551127/logisecsen_02_416x251.png)

Now, when your Logi application is browsed, users will see the dialog box shown above and will have to provide valid credentials for your network domain before seeing the Logi application.
