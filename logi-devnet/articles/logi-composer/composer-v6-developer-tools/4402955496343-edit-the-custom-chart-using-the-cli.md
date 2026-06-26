---
title: "Edit the Custom Chart Using the CLI"
id: 4402955496343
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955496343-Edit-the-Custom-Chart-Using-the-CLI
updated_at: 2021-08-07T17:30:11Z
---

# Edit the Custom Chart Using the CLI

# Edit the Custom Chart Using the CLI

To edit a custom chart using the custom chart CLI:

Make sure you are in the visual’s folder and run the following edit command:

```
$ zd-chart edit
```

Alternatively, you can specify the path to the visual in the edit command. For example:

```
$ zd-chart edit -d <path-to-visual>
```

After running the edit command, follow the prompts to update the visual's controls, name, variables, or visibility.

When all edits are finished, be sure to rebuild the visual before pushing it to the server. See [*Install Dependencies and Build the Custom Chart Using the CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4402955495063-Install-Dependencies-and-Build-the-Custom-Chart-Using-the-CLI).

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
