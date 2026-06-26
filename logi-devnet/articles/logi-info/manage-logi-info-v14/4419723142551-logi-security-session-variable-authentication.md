---
title: "Logi Security: Session Variable Authentication "
id: 4419723142551
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723142551-Logi-Security-Session-Variable-Authentication
updated_at: 2022-07-17T02:23:32Z
---

# Logi Security: Session Variable Authentication 

# Logi Security: Session Variable Authentication

In this scenario, which uses your own custom login application or process, on successful authentication you create a Session variable, named "rdUsername", to hold the user login ID value. Logi Security can then use that Session variable to authorize access to features in your Logi application.

To do this, first configure your web server to use whatever authentication method is appropriate for your custom login application or process. Then configure your Logi Application for this type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/7522758012311/logisecsen_07_566x310.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *AuthSession*.
3. Set the **Security Enabled** attribute to *True*.
4. Add additional security-related elements (Roles, Rights, SecurityProcess, etc. - not shown) as necessary.

When you login and run your Logi application, you should be able to access your login ID using @Session.rdUsername~.
