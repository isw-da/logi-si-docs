---
title: "Register an OAuth Client"
id: 4405851170327
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851170327-Register-an-OAuth-Client
updated_at: 2021-09-21T01:29:34Z
---

# Register an OAuth Client

# Register an OAuth Client

Before an application can make a secure request from a Composer server, it must be registered with the server as one of its clients. Typically, each application is registered as a client distinct from other existing clients. To register a client application, you must have access to the supervisor login for the Composer server. If you do not have access to the supervisor login, you can ask your Composer server supervisor to assist you in completing these steps to register your application as a client app of your Composer server.

The following steps will help you register your application as a client of a Composer server.

1. Use [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) or another REST API client application to make the following REST call to the Composer server that will serve your client application.

   ```
   POST <yourserver>/<yourpath>/api/oauth2/client
   ```

   Where:

   * `<yourserver>` is replaced with the DNS or IP address of your Composer instance, with any necessary port number
   * `<yourpath>` is replaced with your Composer server's path, usually *composer* or *zoomdata*

   For example: `POST https://my.composer.com/composer/api/oauth2/client`.

   Be sure to:

   * Use the content type `application/vnd.composer.v2+json`.
   * Use basic auth and provide the supervisor ID and password.
   * Provide the required JSON object in the body of the REST request. Typically, the request body's JSON object looks something like this:

     ```
     {         
     "accessTokenValiditySeconds": 600,       
     "autoApprove": true,         
     "clientName": "<name>",         
     "registeredRedirectUri": [         
     "<uri1>:<port>",         
     "<uri2>:<port>/<specificpath>"         
     ]         
     }
     ```

     Where:

     + `accessTokenValiditySeconds` specifies the number of seconds for which OAuth access token is valid. The recommended value is 600 seconds.
     + `autoApprove` specifies whether OAuth access is automatically approved. The recommended value is `true`.
     + `clientname` specifies a client name of your choice to use for easy reference.
     + the `registeredRedirectUri` key is supplied with an array listing all URIs (including the port numbers) for your applications to which the Composer server may redirect the user's browser after the user has logged in granting permission to the Composer client application. For example: `"http://localhost:3000/signin"`

   The response body of the REST call is a JSON object that provides keys similar to those in the request body. Here is a sample:

   ```
   {
      "id": "5f170a43b3cb1f0001a20b3f",
      "clientId": "<very-long-client-ID-appears-here>",
      "clientSecret": "ODBlZjZkZjYtNTEzNS00ODMzLWI0NDgtZTI2ZGUyYzA1MWIz",
      "grantTypes": [
         "implicit"
      ],
      "registeredRedirectUri": [
         "http://localhost:3000/signIn"
      ],
      "clientName": " ComposerEmbed ",
      "accessTokenValiditySeconds": 600,
      "autoApprove": true
   }
   ```

   The value of each key verifies the correct implementation of the requested value. Additionally, the HATEOAS link objects are added into the response body. The most important difference is that the
   `clientId` key is supplied with a value by the Composer server. A typical `clientId` looks something like:

   ```
   balDbGllbrROYW1lMFQ2MzAwNTI0mDE0NTk2LUmNmMtaxekNC1htdTlkOTM4N2ZlOGZlOA==
   ```

   This `clientId` is used in the following steps.
2. Embed the client ID in your application so that it can be used to request access tokens for secure transactions. In most cases, doing so means assigning the `clientId` string to a variable or to a member of a JSON object.

After you have registered your application as an OAuth client, your application can [request an access token](https://devnet.logianalytics.com/hc/en-us/articles/4405859463575-Request-an-Access-Token).
