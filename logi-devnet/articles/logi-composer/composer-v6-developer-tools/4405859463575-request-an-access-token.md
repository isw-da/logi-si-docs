---
title: "Request an Access Token"
id: 4405859463575
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859463575-Request-an-Access-Token
updated_at: 2021-09-21T01:29:33Z
---

# Request an Access Token

# Request an Access Token

After you have [registered an application as an OAuth client](https://devnet.logianalytics.com/hc/en-us/articles/4405851170327-Register-an-OAuth-Client) with a particular Composer server and provided the client ID to the client, the client application can request permission from the Composer server to access a user's resources by requesting an access token. Before the Composer server will serve the request, the user must specifically authorize it to do so using Composer's login screen. When the user has authorized the server to serve resources to the client, the server will grant the client an access token. Your client can request an access token using the following steps.

The OAuth 2.0 configuration property `oauth.token.always-create-new` ensures that a valid access token is present all the time for Composer iFrameless embedding. When this property is set to `true` (the default), a new valid OAuth access token is generated each time a `POST /api/oauth2/token` or `GET /oauth/authorize` endpoint request is issued, and any previously generated tokens are not invalidated. They will expire naturally. If this property is set to `false` and a `POST /api/oauth2/token` or `GET /oauth/authorize` endpoint request is issued, a new valid OAuth access token is generated for the user if one is not already available or the existing valid user access token is returned.

**To request an access token from a Composer server:**

1. Use a JavaScript library that supports HTTP calls, such as jQuery, to program your client to make an HTTP GET request to the following URL.

   ```
   <yourserver>/composer/oauth/authorize?client_id=<yourid>&redirect_uri=<https://www.yourapp.com>&response_type=token&scope=read
   ```

   where:

   * `<yourserver>` is replaced with your server's DNS or IP address, together with any necessary port number
   * `<yourid>` is replaced with your application's registered clientId
   * `<https://www.yourapp.com>` is replaced with the URI (with the correct protocol) to which Composer should redirect the browser upon successful login and authorization by the user.

     As part of the OAuth 2.0 protocol, Composer will only redirect the user's browser to a URI included in the
     `registeredRedirectUri` list provided to Composer when the client is registered.

   When your user successfully completes the login and authorization request, the Composer server redirects the user's browser to the
   `redirect_uri` that you specified in the GET call above. The full URI to which the user's browser is redirected includes a parameter called
   `access_token`. For example:

   ```
   www.yourapp.com/#access_token=2ea7e479-0e4f-4720-9f74-e4465be9933b&token_type=bearer&expires_in=600
   ```
2. In your application on the page receiving the redirect, extract the `access_token` parameter from the URI that loaded the page. Popular sites like Stack Overflow can provide guidance on how to extract parameters from the URI used to query a page. For example, see
   [Get URL parameter... in js](https://stackoverflow.com/questions/19491336/how-to-get-url-parameter-using-jquery-or-plain-javascript).

After you have extracted the access token, your application can use it to [request a transaction](https://devnet.logianalytics.com/hc/en-us/articles/4405851171479-Request-a-Transaction-with-OAuth-2-0).
