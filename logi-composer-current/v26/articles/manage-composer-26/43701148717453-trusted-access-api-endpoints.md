---
title: "Trusted Access API Endpoints"
id: 43701148717453
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701148717453-Trusted-Access-API-Endpoints
updated_at: 2026-05-29T14:09:24Z
---

# Trusted Access API Endpoints

# Trusted Access API Endpoints

The following API endpoints can be used to manage Trusted Access.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/trusted-access/clients` | GET | Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method.  For a description of these, see [Trusted Access Client Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175838349-Trusted-Access-Client-Properties). |
| `/api/trusted-access/clients` | POST | Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique.  When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated. |
| `/api/trusted-access/clients/<id>` | GET | Returns the Trusted Access client information for a specific client.  The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | DELETE | Deletes a specific Trusted Access client.  The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | PATCH | Updates the Trusted Access client information for a specific client.  The request must specify the client ID and the number of seconds for which the access token is valid. |
| `/api/trusted-access/pull/tokens` | POST | Use pull to request a user access token for users that already exist in Composer.  The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer).  You can't update user context such as user attributes or groups using `pull`. |
| `/api/trusted-access/push/tokens` | POST | Use push to request a user access token for new and existing users by sending their context to Composer. Existing users are updated if their context has changed.  Context must contain `username`, and `account`. It can optionally include `email`, `fullname`, `groups` and other individual `attributes`  Several reserved keys are restricted from use in Composer as custom user attributes: `composerUserName` and `accountId`. If you push these reserved keys, a 400 Bad Request error is returned via API. |
