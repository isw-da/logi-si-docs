---
title: "Including the API"
id: 4419715275287
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715275287-Including-the-API
updated_at: 2023-10-06T11:38:28Z
---

# Including the API

# Including the API

The Embedded Reports API, which is a JavaScript file, is:

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

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) The Embedded Reports API works well with all modern browsers, but some features (such as auto-sizing and accessing embedded reports) will not work with older browser, such as IE7.
