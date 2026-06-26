---
title: "Including in Main Applications"
id: 4419722986263
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722986263-Including-in-Main-Applications
updated_at: 2022-07-17T01:45:54Z
---

# Including in Main Applications

## Including in Main Applications

Developers may want to actually include their Logi report as part of their main ASP.NET or Java web application. It *is* possible to do this, however, it introduces dependencies and complications, so it's not a recommended approach.
For example, the web.config file used by a Logi .NET reporting application is slightly different from that used by a traditional .NET application, and when the Logi app is part of the main app, these differences have to be resolved for both to run correctly.
The flexibility and performance provided by running Logi applications as separate applications usually outweighs the convenience of packaging everything together within the main application.
