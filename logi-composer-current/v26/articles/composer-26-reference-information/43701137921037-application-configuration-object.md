---
title: "Application Configuration Object"
id: 43701137921037
section: "Composer 26 Reference Information"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701137921037-Application-Configuration-Object
updated_at: 2026-05-29T14:09:11Z
---

# Application Configuration Object

# Application Configuration Object

The application configuration object contains the parameters that your client needs to identify a Composer server.

## Example

var applicationConfig = {   
secure: true,   
host: 'www.yourcompanysite.com',   
port: 8443,   
path: '/zoomdata'   
};

The values for each key should be as follows:

* **secure**: true to use HTTPS (secure) protocol, otherwise
  `false`
* **host**: the base URL where your Composer server is hosted
* **port**: the port that your Composer uses to communicate; by default, this is
  `8443`
* **path**: the path from your base URL for your Composers server; by default, this is
  `‘/zoomdata’`
