---
title: "Edit the Custom Chart Using the CLI"
id: 4405859240727
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859240727-Edit-the-Custom-Chart-Using-the-CLI
updated_at: 2021-09-21T01:27:35Z
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

When all edits are finished, be sure to rebuild the visual before pushing it to the server. See [*Install Dependencies and Build the Custom Chart Using the CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405850968599-Install-Dependencies-and-Build-the-Custom-Chart-Using-the-CLI).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.
