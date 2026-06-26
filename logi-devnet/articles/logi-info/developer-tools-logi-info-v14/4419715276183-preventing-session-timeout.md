---
title: "Preventing Session Timeout"
id: 4419715276183
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715276183-Preventing-Session-Timeout
updated_at: 2022-07-17T02:07:56Z
---

# Preventing Session Timeout

# Preventing Session Timeout

The parent application and its embedded Logi reports may be hosted on
separate web servers and, if so, there will be independent session state
maintained for them on each host. Session expiration on either host may
cause problems. The Embedded Reports API provides functionality for
preventing session timeout for parent and embedded reports.
To use it, create a minimum web page (.htm, .html, .aspx, etc.) that has
no visual elements in the parent application and use the following method
to "ping" it (request the page) at specified intervals.  
**keepSessionsAlive(pingParentPageUrl, interval)**  
 Pings the parent and embedded applications at the defined interval (in
milliseconds). The default interval is 60000 (1 minute).

```
1. function CreateMyEmbeddedApp() {
2. var options = {
3. applicationUrl : "https://myAppServer/myLogiAppToEmbed",
4. report : "Default",
5. autoSizing : "height"
6. };

8. var report = EmbeddedReporting.create("divEmbedDiv", options);

10. EmbeddedReporting.keepSessionsAlive("https://myParentApp/keepAlive.htm", 60000);
11. }
```

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
The .keepSessionsAlive method call must be placed *after* the
.create method call in your code.

The method pings the page in the parent application and also automatically
determines the URL of the embedded Logi application and pings a standard
page that's supplied with the Logi Info product (so you *don't* have
to create a page to ping in the embedded application).

If you have both the parent and the embedded application on the same
server, be sure that you specify the same domain for them. For example, do
not use https://localhost/myApp to embed
the application and then
https://127.0.0.1/myParentApp for the
keepSessionsAlive method.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) This technique only works with a single embedded Logi
application; if you have reports from multiple Logi applications embedded
in the same parent application, this method *will not* ping all the
Logi applications.
