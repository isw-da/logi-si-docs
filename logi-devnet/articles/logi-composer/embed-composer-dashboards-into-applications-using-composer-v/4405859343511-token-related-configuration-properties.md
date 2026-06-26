---
title: "Token-Related Configuration Properties"
id: 4405859343511
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859343511-Token-Related-Configuration-Properties
updated_at: 2021-09-21T01:28:30Z
---

# Token-Related Configuration Properties

# Token-Related Configuration Properties

The `initComposerEmbedManager` window function supports the following token-related configuration properties.

| Property | Description | Description |
| --- | --- | --- |
| `initialToken` | Provides a string representing a token from [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access). There is no default.  It is ignored when `getToken` is also passed in `initComposerEmbedManager`. |  |
| `getToken` | This method returns a token using Trusted Access. This is the same as the the window.composerGetToken method. There is no default.  ``` getToken: () => {       return Promise.resolve({ // this is an example function. server side should be called in production          "access_token": "60a26b4f-c5d7-49af-a90b-1da4e6eb12b8",         "expires_in": "6000"       });     } ``` | This method returns a token using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access). This is the same as the the `window.composerGetToken` method. There is no default. |
