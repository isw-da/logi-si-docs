---
title: "Token-Related Configuration Properties"
id: 43701070712973
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070712973-Token-Related-Configuration-Properties
updated_at: 2026-05-29T14:08:31Z
---

# Token-Related Configuration Properties

# Token-Related Configuration Properties

The `initComposerEmbedManager` window function supports the following token-related configuration properties.

| Property | Description |
| --- | --- |
| `getToken` | This method returns a token using [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access). This is the same as the the `window.composerGetToken` method. There is no default.  getToken: () => { return Promise.resolve({ // this is an example function. server side should be called in production "access\_token": "60a26b4f-c5d7-49af-a90b-1da4e6eb12b8", "expires\_in": "6000" }); } |
