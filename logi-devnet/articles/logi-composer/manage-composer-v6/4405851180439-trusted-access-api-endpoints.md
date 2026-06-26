---
title: "Trusted Access API Endpoints"
id: 4405851180439
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints
updated_at: 2022-05-16T08:49:49Z
---

# Trusted Access API Endpoints

# Trusted Access API Endpoints

The following API endpoints can be used to manage Trusted Access.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/trusted-access/clients` | GET | Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method. For a description of these, see [*Trusted Access Client Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859468951-Trusted-Access-Client-Properties). |
| `/api/trusted-access/clients` | POST | Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique. When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated. |
| `/api/trusted-access/clients/<id>` | GET | Returns the Trusted Access client information for a specific client. The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | DELETE | Deletes a specific Trusted Access client. The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | PATCH | Updates the Trusted Access client information for a specific client. The request must specify the client ID and the number of seconds for which the access token is valid. |
| `/api/trusted-access/token` | POST | Generates a new access token for a user. The request must specify the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer). |
