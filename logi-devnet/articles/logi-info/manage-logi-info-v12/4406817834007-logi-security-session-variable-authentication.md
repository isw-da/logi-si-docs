---
title: "Logi Security: Session Variable Authentication "
id: 4406817834007
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817834007-Logi-Security-Session-Variable-Authentication
updated_at: 2022-04-06T06:08:30Z
---

# Logi Security: Session Variable Authentication 

# Logi Security: Session Variable Authentication

In this scenario, which uses your own custom logon application or process, on successful authentication you create a Session variable, named "rdUsername", to hold the user login ID value. Logi Security can then use that Session variable it to authorize access to features in your Logi application.

To do this, first configure your web server to use whatever authentication method is appropriate for your custom logon application or process. Then configure your Logi Application for this type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583744279/logisecsen_07_566x310.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *AuthSession*.
3. Set the **Security Enabled** attribute to *True*.
4. Add additional security-related elements (Roles, Rights, etc. - not shown) as necessary.

When you login and run your Logi application, you should be able to access your login ID using @Session.rdUsername~.
