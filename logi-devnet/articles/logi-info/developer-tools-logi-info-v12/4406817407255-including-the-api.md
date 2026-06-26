---
title: "Including the API"
id: 4406817407255
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817407255-Including-the-API
updated_at: 2022-04-06T06:05:56Z
---

# Including the API

# Including the API

The Embedded ReportsAPI, which is a JavaScript file, is:

*<yourLogiApp>*/rdTemplate/rdEmbedApi/rdEmbed.js

To use it, include a link to it at the **end** of your custom HTML page, just above the </body> tag:

```
1. <body>
2. ...
3. <script src="https://<yourLogiApp>/rdTemplate/rdEmbedApi/rdEmbed.js" type="text/Javascript">
4. </script>
5. </body>
```

Next, create a div element to contain the embedded Logi report, and give it a unique idattribute.

```
1. <div id="div1" />
```

Then decide which of the two following embedding approaches, described in the following sections, you want to use: **Markup** or **JavaScript**.
Note: The Embedded Reports API works well with all modern browsers, but some features (such as auto-sizing and accessing embedded reports) will not work with older browser, such as IE7.
