---
title: " Security Configuration Object"
id: 34933128778637
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933128778637--Security-Configuration-Object
updated_at: 2026-05-26T22:07:59Z
---

#  Security Configuration Object

# Security Configuration Object

The security configuration object contains the required access token you generate for your client to access Composer.

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access) for all embed-related workflows.

## Example

var credentialsConfig = {   
 access\_token: TRUSTED\_ACCESS\_TOKEN,  
 };

The security configuration object should contain the required trusted access token you generate.

* **access\_token**: Trusted access token for accessing the Composer server. See  [Generate a User's Access Token](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access#Generate). The client created should have credentials matching those used to create the trusted access token.
