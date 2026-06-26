---
title: "Handle OAuth 2.0 Invalid or Expired Access Tokens"
id: 4405851173527
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851173527-Handle-OAuth-2-0-Invalid-or-Expired-Access-Tokens
updated_at: 2021-09-21T01:29:35Z
---

# Handle OAuth 2.0 Invalid or Expired Access Tokens

# Handle OAuth 2.0 Invalid or Expired Access Tokens

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

If an endpoint starts with `<host>:<port>/composer/api/` and you request it using an invalid or expired OAuth 2.0 access token, Composer produces one of the following responses:

```
HTTP/1.1 401 Unauthorized  
WWW-Authenticate: Bearer realm="oauth", error="invalid_token", error_description="Access token expired: <token>"  
  "error": "invalid_token",  
  "error_description": "Access token expired: <token>"  
}
```

**or**

```
HTTP/1.1 401 Unauthorized  
WWW-Authenticate: Bearer realm="oauth", error="invalid_token", error_description="Invalid access token: <token>"  
{  
  "error": "invalid_token",  
  "error_description": "Invalid access token: <token>"  
}
```

If you request a public link to a dashboard with an invalid or expired access token, you will be redirected to Composer's login page.

This behavior impacts all API endpoints if you are using the API.
