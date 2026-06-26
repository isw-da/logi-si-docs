---
title: "The Cross-Origin Request Blocked Error"
id: 4402955686807
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955686807-The-Cross-Origin-Request-Blocked-Error
updated_at: 2021-08-07T17:32:11Z
---

# The Cross-Origin Request Blocked Error

# The Cross-Origin Request Blocked Error

Cross-origin resource sharing (CORS) is a new standard introduced in HTML 5 that allows web applications to use HTTP headers to specify which origins are permitted to request resources on the server. Modern web browsers will consult the Access-Control-Allow-Origin header on how to relax the same origin policy for a given page.

By default, this setting was disabled starting version 1.5.0SR1 due to security vulnerability concerns. However, CORS can be enabled for certain or all domains through the zoomdata.conf (
`/etc/zoomdata`
) file. Please add the following parameter:

```
access.control.allow.origin=*
```

The \* will open CORS for all domains. If you want to specify specific domains, replace the \* with the appropriate domain name. Refer to your Tomcat documentation to verify the appropriate syntax to use.

Please restart Composer server after making this change and also make sure to clear your browser cache.
