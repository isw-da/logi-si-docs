---
title: "Implement OAuth 2.0 with Composer"
id: 4402955667735
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955667735-Implement-OAuth-2-0-with-Composer
updated_at: 2021-08-07T17:32:00Z
---

# Implement OAuth 2.0 with Composer

# Implement OAuth 2.0 with Composer

Composer supports the OAuth 2.0 protocol's implicit workflow for user authentication and authorization. Here is some terminology that is used.

| Term | Definition |
| --- | --- |
| access token | A token created by a resource server and returned to an authorized client, identifying that client in future requested transactions. |
| client | A third-party application that attempts to access the user's account. The client must obtain permission from the resource owner before it can do so. |
| resource owner | The owner, typically a human, of an account. The resource owners can give access to some portion of their account. |
| resource server | The Composer server used to access the user's information. |
| transaction | An attempt by a client to create, read, update, or delete Composer resources or to use Composer functionality in a third-party application. |

In Composer's implementation, only a Composer server's supervisor can create a client to access that particular server. After a Composer server's supervisor has created one or more clients, developers can use those clients to request access tokens from the Composer server. At this point, the Composer server will request the user grant access to the application. When the user grants access, the server supplies an access token to the client application. After those access tokens are granted, the client application can use those access tokens to request Composer transactions, getting data and using functionality, in their own applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952813847/oauth_308x295.png)

The following high-level steps will guide you in this workflow.

1. [*Enable Trusted Access and OAuth 2.0*](https://devnet.logianalytics.com/hc/en-us/articles/4402963049367-Enable-Trusted-Access-and-OAuth-2-0).
2. [*Register an OAuth Client*](https://devnet.logianalytics.com/hc/en-us/articles/4402955666199-Register-an-OAuth-Client).
3. [*Request an Access Token*](https://devnet.logianalytics.com/hc/en-us/articles/4402955665559-Request-an-Access-Token).
4. [*Request a Transaction with OAuth 2.0*](https://devnet.logianalytics.com/hc/en-us/articles/4402955666967-Request-a-Transaction-with-OAuth-2-0).

Using these high-level steps, developers can add the ability to use Composer data and functionality to their own applications, restricting authorization to the level and permissions of the user logged in.
