---
title: "Security Configuration Object"
id: 4405851148695
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851148695-Security-Configuration-Object
updated_at: 2021-09-21T01:29:25Z
---

# Security Configuration Object

# Security Configuration Object

The security configuration object contains the key or token that your client requires to access Composer.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

* When you generate a security key for a data source, users of the data source are automatically granted Read permission for all existing visuals using the data source, but not for any new visuals created after the security key was generated. Instead, a new security key must be generated for new visuals.
* When you generate a security key for a dashboard, users of the dashboard are automatically granted Read permission for all existing visuals on the dashboard for which they have Read permissions. However, if a new visual is created on the dashboard after the security key is generated, dashboard users will not automatically be granted Read permission for the new visual. Instead, a new security key must be generated for newer visuals on the dashboard. )

## Example

```
   var credentialsConfig = {     
   key: '1234567890abcdef'     
   };
```

The security configuration object should have
**only one** of the following options.

* **key**
  : valid Composer security key; for steps to generate a security key, see
  [*Generate a Security Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851169431-Generate-a-Security-Key)
  . The client created will have credentials matching those used to create the security key.
* **access\_token**: OAuth token for accessing the Composer server; for steps to generate an OAuth token, see [*Request an Access Token*](https://devnet.logianalytics.com/hc/en-us/articles/4405859463575-Request-an-Access-Token). The client created will have credentials matching those used to create the OAuth token.
