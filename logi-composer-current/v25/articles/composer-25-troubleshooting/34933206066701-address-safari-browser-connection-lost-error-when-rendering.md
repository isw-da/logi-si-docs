---
title: "Address Safari Browser Connection Lost Error When Rendering a Visual"
id: 34933206066701
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933206066701-Address-Safari-Browser-Connection-Lost-Error-When-Rendering-a-Visual
updated_at: 2026-05-26T22:08:26Z
---

# Address Safari Browser Connection Lost Error When Rendering a Visual

# Address Safari Browser Connection Lost Error When Rendering a Visual

## Symptom

When trying to render a visual using one of your data sources (including Composer's Real Time Sales demo source), you may observe an issue where the visual never finishes rendering and you receive a 'connection lost' error as a red bar across the top of the browser. Specifically, this issue seems to only occur when using Safari but not in other browsers such as Chrome.

## Possible Cause and Resolution

You may be encountering this issue because you are trying to use a self-signed certificate in Safari. By default, Composer will initially use a self-signed certificate for SSL unless otherwise configured. Because of how Safari's security settings are configured, the web-socket requests are likely getting denied causing the "connection lost" error and the visual to never render properly. You can address this issue by one of two methods:

1. Disable SSL in your Composer Server
   and make sure to use the 'http' connection when connecting to Composer via Safari
2. Configure your Composer server to use a new, valid SSL certificate instead of using the default, self-signed certificate. This can be done by
   adding an SSL certificate to your Composers server
