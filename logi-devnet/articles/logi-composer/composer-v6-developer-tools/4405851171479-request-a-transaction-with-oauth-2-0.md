---
title: "Request a Transaction with OAuth 2.0"
id: 4405851171479
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851171479-Request-a-Transaction-with-OAuth-2-0
updated_at: 2021-09-21T01:29:33Z
---

# Request a Transaction with OAuth 2.0

# Request a Transaction with OAuth 2.0

After your application has [requested and received an access token](https://devnet.logianalytics.com/hc/en-us/articles/4405859463575-Request-an-Access-Token), it can use the access token to authenticate itself while requesting transactions. The following points illustrate use-cases that require authentication and give sample code to illustrate using the OAuth access token to provide that authentication.

## Use a Data Query or Embedding a Visual

To [use a data query](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query) or to [embed a Composer visual](https://devnet.logianalytics.com/hc/en-us/articles/4405850883735-Embed-a-Visual-in-Your-Web-Page) in your own web application, you must use Composer's JavaScript client library to create a Composer client. Creating a client requires code like this:

```
   ZoomdataSDK.createClient({
   credentials: credentialConfig,
   application: applicationConfig
   })
```

Composer allows its [security configuration object](https://devnet.logianalytics.com/hc/en-us/articles/4405851148695-Security-Configuration-Object) to contain either a [source-based security key](https://devnet.logianalytics.com/hc/en-us/articles/4405851169431-Generate-a-Security-Key) or an OAuth access token, but not both. In the example above, the security configuration object is associated with the `credentials` key using the variable name
`credentialConfig`. The example below shows a security configuration object that uses an OAuth token rather than a Composer security key.

```
   var credentialsConfig = {
   access_token: '8615a80b-28c0-4521-930f-5ab6f26d3686'
   };
```

## Use cURL

You can naturally use
cURL or the library of your choice to request a transaction using OAuth 2.0. For example:

```
curl -X GET https://<yourserver/composer>/api/<users/123456789>  
-H "Content-Type: application/vnd.composer.v2+json; Authorization: Bearer <ff16372e-38a7-4e29-88c2-1fb92897f558> "
```

in which:

* `<yourserver/zoomdata>` is the DNS and path for your Composer server, using the correct protocol.
* `<users/123456789>` is replaced with the method and parameters that you wish to use
* `Authorization` parameter contains your own access token
