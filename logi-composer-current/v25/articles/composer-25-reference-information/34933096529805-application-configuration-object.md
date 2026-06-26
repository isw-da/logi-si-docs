---
title: "Application Configuration Object"
id: 34933096529805
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933096529805-Application-Configuration-Object
updated_at: 2026-05-26T22:07:57Z
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
