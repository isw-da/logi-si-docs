---
title: "Application Configuration Object"
id: 4405851137943
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851137943-Application-Configuration-Object
updated_at: 2021-09-21T01:29:20Z
---

# Application Configuration Object

# Application Configuration Object

The application configuration object contains the parameters that your client needs to identify a Composer server.

## Example

```
var applicationConfig = {     
secure: true,     
host: 'www.yourcompanysite.com',     
port: 8443,     
path: '/zoomdata'     
};
```

The values for each key should be as follows:

* **secure**: true to use HTTPS (secure) protocol, otherwise
  `false`
* **host**: the base URL where your Composer server is hosted
* **port**: the port that your Composer uses to communicate; by default, this is
  `8443`
* **path**: the path from your base URL for your Composer server; by default, this is
  `‘/zoomdata’`
