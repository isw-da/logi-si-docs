---
title: "Enable Trusted Access and OAuth 2.0"
id: 4402963049367
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963049367-Enable-Trusted-Access-and-OAuth-2-0
updated_at: 2021-08-07T17:31:56Z
---

# Enable Trusted Access and OAuth 2.0

# Enable Trusted Access and OAuth 2.0

You must enable Trusted Access or the OAuth 2.0 protocol before you can create clients and allow Composer to provide access tokens to authorized clients using Trusted Access or OAuth.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4402955672599-Trusted-Access) for all embed-related workflows.

If OAuth security is not enabled by the supervisor in the supervisor UI, then all OAuth client and token-related API endpoints return a 404 response code or a 401 unauthorized response code (when an existing token is used). In addition, the OAuth API endpoints are not visible in the Swagger documentation. The primary OAuth endpoints are:

* `/api/oauth2/client` endpoints
* `/api/oauth2/token` endpoints
* `/api/oauth/token` endpoints
* `/oauth/authorize` endpoint

For information about Trusted Access endpoints, see [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4402955671831-Trusted-Access-API-Endpoints).

**To enable OAuth 2.0:**

1. Log in to Composer using the supervisor account.
2. Select **Security**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952814103/security-services_576x250.png)
3. Switch the **Trusted Access & OAUTH** setting to **ON**.
4. Select **Save**.
5. Restart Composer. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402963006871-Restart-Composer-Microservices).

After you have set OAuth to ON, you can continue to [register an OAuth client](https://devnet.logianalytics.com/hc/en-us/articles/4402955666199-Register-an-OAuth-Client) or
[request an access token](https://devnet.logianalytics.com/hc/en-us/articles/4402955665559-Request-an-Access-Token).
