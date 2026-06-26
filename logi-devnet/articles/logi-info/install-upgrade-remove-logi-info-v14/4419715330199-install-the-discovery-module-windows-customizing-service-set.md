---
title: "Install the Discovery Module - Windows - Customizing Service Settings"
id: 4419715330199
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715330199-Install-the-Discovery-Module-Windows-Customizing-Service-Settings
updated_at: 2022-07-17T01:47:06Z
---

# Install the Discovery Module - Windows - Customizing Service Settings

# Install the Discovery Module - Windows - Customizing Service Settings

You may wish to customize Logi services settings which, assuming a
default installation location, can be found in the LogiApplicationService and LogiDataService files:

<installationFolder>\platform\settings\logiApplicationService.json  
 <installationFolder>\platform\settings\logiDataService.json

The beginning of the
logiApplicationService.json
file looks like this:

{  
 "disableSchemaValidation": false,  
 "logiApplicationService": {  
 "description": "Platform
logiApplicationService Configuration",  
 "logLevel": "error",  
"corsOriginWhiteList": "\*",  
 "accessTokenGracePeriod": 120,  
 "system": {  
 "pollingIntervalSeconds":
15,  
 "pollingTimeoutMinutes":
-1  
 },

For example, the requiredcorsOriginWhiteList
attribute, highlighted above, specifies which servers the service will
respond to, allowing you to restrict access to the service, if desired.
The default value, "\*", tells the service to respond to
*all* servers; to restrict access enter a single IP address or server
name (as a string) or a JSON array of them, such as:

["http://server1","http://server2","http://192.168.1.1"]

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Changes to some settings may cause applications to fail.
For example,

![](https://devnet.logianalytics.com/hc/article_attachments/4419714813079/installdm31_08a.png)

changing the
platformBaseUrl
setting, shown above, may cause integrations with Logi Info applications
to fail.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) You'll need to stop and restart both services to have any changes to
the settings file take effect.
