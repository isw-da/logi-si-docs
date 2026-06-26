---
title: "List All Custom Charts on the Server Using the CLI"
id: 4402955497111
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955497111-List-All-Custom-Charts-on-the-Server-Using-the-CLI
updated_at: 2021-08-07T17:30:12Z
---

# List All Custom Charts on the Server Using the CLI

# List All Custom Charts on the Server Using the CLI

To list all custom charts stored on the Composer server using the custom chart CLI:

Run the following command:

```
$ zd-chart ls
```

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
