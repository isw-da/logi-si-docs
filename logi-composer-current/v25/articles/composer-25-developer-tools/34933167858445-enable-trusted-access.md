---
title: "Enable Trusted Access"
id: 34933167858445
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933167858445-Enable-Trusted-Access
updated_at: 2026-05-26T22:09:28Z
---

# Enable Trusted Access

# Enable Trusted Access

Trusted Access is enabled by default in Composer. This enables you to create clients, and Composer to provide access tokens to authorized clients using Trusted Access. It can be disabled by a system administrator or member of the supervisors group, and another authentication method used.

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access) for all embed-related workflows.

If Trusted Access is not enabled, all Trusted Access client and token-related API endpoints return a 404 response code or a 401 unauthorized response code (when an existing token is used). In addition, the Trusted Access API endpoints are not visible in the Swagger documentation. For information about Trusted Access endpoints, see [Trusted Access API Endpoints](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933140345869-Trusted-Access-API-Endpoints).

**Enable or disable Trusted Access:**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Security** from the menu.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167059889293)
3. Switch the **Trusted Access**  setting to **OFF** to disable, or **ON** to enable.
4. Select **Save**.
5. Restart Composer. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

When Trusted Access is ON, you can [register a client](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access#Register) or
[generate an access token](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access#Generate).
