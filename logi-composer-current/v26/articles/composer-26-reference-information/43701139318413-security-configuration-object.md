---
title: " Security Configuration Object"
id: 43701139318413
section: "Composer 26 Reference Information"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701139318413--Security-Configuration-Object
updated_at: 2026-05-29T14:09:16Z
---

#  Security Configuration Object

# Security Configuration Object

The security configuration object contains the required access token you generate for your client to access Composer.

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access) for all embed-related workflows.

## Example

var credentialsConfig = {   
 access\_token: TRUSTED\_ACCESS\_TOKEN,  
 };

The security configuration object should contain the required trusted access token you generate.

* **access\_token**: Trusted access token for accessing the Composer server. See  [Generate a User's Access Token](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access#Generate). The client created should have credentials matching those used to create the trusted access token.
