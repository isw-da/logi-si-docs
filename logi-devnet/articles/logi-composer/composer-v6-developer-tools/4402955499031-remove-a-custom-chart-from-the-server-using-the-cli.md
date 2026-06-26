---
title: "Remove a Custom Chart from the Server Using the CLI"
id: 4402955499031
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955499031-Remove-a-Custom-Chart-from-the-Server-Using-the-CLI
updated_at: 2021-08-07T17:30:14Z
---

# Remove a Custom Chart from the Server Using the CLI

# Remove a Custom Chart from the Server Using the CLI

To remove a custom chart from the server using the custom chart CLI:

Run the following command:

```
$ zd-chart rm
```

After running the command you will be prompted to select the visual name and confirm its deletion.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
