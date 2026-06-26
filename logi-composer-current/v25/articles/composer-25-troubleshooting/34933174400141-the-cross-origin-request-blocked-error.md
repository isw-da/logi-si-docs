---
title: "The Cross-Origin Request Blocked Error"
id: 34933174400141
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933174400141-The-Cross-Origin-Request-Blocked-Error
updated_at: 2026-05-26T22:08:08Z
---

# The Cross-Origin Request Blocked Error

# The Cross-Origin Request Blocked Error

Cross-origin resource sharing (CORS) is a new standard introduced in HTML 5 that allows web applications to use HTTP headers to specify which origins are permitted to request resources on the server. Modern web browsers will consult the Access-Control-Allow-Origin header on how to relax the same origin policy for a given page.

By default, this setting was disabled starting version 1.5.0SR1 due to security vulnerability concerns. However, CORS can be enabled for certain or all domains through the zoomdata.conf (
`/etc/zoomdata`
) file. Please add the following parameter:

access.control.allow.origin=\*

The `*` will open CORS for all domains. If you want to specify specific domains, replace the `*` with the appropriate domain name. Refer to your Tomcat documentation to verify the appropriate syntax to use.

Please restart Composer server after making this change and also make sure to clear your browser cache.
