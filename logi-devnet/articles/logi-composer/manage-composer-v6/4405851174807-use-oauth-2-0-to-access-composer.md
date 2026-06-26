---
title: "Use OAuth 2.0 to Access Composer"
id: 4405851174807
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851174807-Use-OAuth-2-0-to-Access-Composer
updated_at: 2021-09-21T01:29:34Z
---

# Use OAuth 2.0 to Access Composer

# Use OAuth 2.0 to Access Composer

Composer supports the OAuth 2.0 protocol for authentication and authorization as well as the OAuth 2.0 Implicit Workflow.
See also [*Implement OAuth 2.0 with Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851172503-Implement-OAuth-2-0-with-Composer).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

To configure OAuth 2.0 Implicit Workflow, you need to create a client identifier (Client ID) for your application in Composer. When working with Composer, your application requests an access token from Composer. This access token is used to obtain access to Composer resources.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747400343/oauth-authorization_348x333.png)

## Manage Client ID in Composer

You can create, read, update, or delete the Client ID using Composer's Public REST API.

### Create Client ID

Before you begin, you must register your application in Composer using the Public REST API.

If you need assistance to set up the Client ID in Composer, contact Composer [Technical
Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

### Access Token Request

After your application is set up in Composer, the user can send a request containing (1) the client ID, (2) a callback URL and other service parameters to Composer. Composer checks whether there are active sessions for that user. If not, the user must log in with appropriate credentials. After the user is identified in Composer (either via standard login or from an existing session), user consent is requested. By confirming your consent, you allow the client application to use Composer resources on behalf of your Composer account. Then, Composer creates an access token for your client app with the same access rights for the corresponding user.

The OAuth 2.0 configuration property `oauth.token.always-create-new` ensures that a valid access token is present all the time for Composer iFrameless embedding. When this property is set to `true` (the default), a new valid OAuth access token is generated each time a `POST /api/oauth2/token` or `GET /api/oath/authorize` endpoint request is issued, and any previously generated tokens are not invalidated. They will expire naturally. If this property is set to `false` and a `POST /api/oauth2/token` or `GET /api/oath/authorize` endpoint request is issued, a new valid OAuth access token is generated for the user if one is not already available or the existing valid user access token is returned.

The Composer service redirects the user to the specified callback URL in client app. The access token is provided as a request parameter.

See also [*Handle OAuth 2.0 Invalid or Expired Access Tokens*](https://devnet.logianalytics.com/hc/en-us/articles/4405851173527-Handle-OAuth-2-0-Invalid-or-Expired-Access-Tokens).

### Working with Composer Using Obtained Access Token

Each time when the client app requests resources from the Composer server, an access token is sent and corresponding resources are returned to the app.
