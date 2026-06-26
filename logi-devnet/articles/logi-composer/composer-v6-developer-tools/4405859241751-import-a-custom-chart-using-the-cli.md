---
title: "Import a Custom Chart Using the CLI"
id: 4405859241751
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859241751-Import-a-Custom-Chart-Using-the-CLI
updated_at: 2021-09-21T01:27:33Z
---

# Import a Custom Chart Using the CLI

# Import a Custom Chart Using the CLI

To import a custom chart using the custom chart CLI:

Run the `zd-chart import` command, specifying the path to the library. You can import visual zip files that were downloaded from the Manage Custom Charts page or a custom chart created with an older version of the CLI.

```
$ zd-chart import [options] <visualname> <path-to-visual>
```

where `<path-to-visual>` is the relative path to the zip file containing the visual you want to import.

The following options are available:

* -a, -app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -u, -user [user:password] Specify the user name and password to use for server authentication.
* -h, -help output usage information

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

A custom chart is bundled before it is pushed to the Composer server. This creates a `/dist` directory containing the necessary files required to send the visual to the Composer server. This `/dist` custom chart zip file is not compatible with the `zd-chart import` command and cannot be imported using the Manage Custom Charts page in the UI. To import the `/dist` custom chart zip file, use the `zd-chart push` command instead.
