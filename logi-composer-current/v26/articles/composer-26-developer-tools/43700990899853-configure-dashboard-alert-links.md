---
title: "Configure Dashboard Alert Links "
id: 43700990899853
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990899853-Configure-Dashboard-Alert-Links
updated_at: 2026-05-29T14:07:11Z
---

# Configure Dashboard Alert Links 

# Configure Dashboard Alert Links

When you create an alert definition and set up email notification for alerts, Logi Composer sends recipients your customized alerts message, which includes a link to the dashboard associated with the alert.

**Note:** 
In all environments, `{Dashboard.id}` is resolved at run time for an alert's email notification.

## Stand Alone Environment

Include the static fully qualified domain name for your Logi Composer environment:

alert.dashboard.link.template=${composer.schema}${zoomdata.base-url}/visualization/#{'$'}{Dashboard.id}

Where `{composer.schema}=#{${server.ssl.enabled}?'https':'http'}://` and `zoomdata.base-url=${server.address:localhost}:${server.port:8080}${server.servlet.context-path}`.
