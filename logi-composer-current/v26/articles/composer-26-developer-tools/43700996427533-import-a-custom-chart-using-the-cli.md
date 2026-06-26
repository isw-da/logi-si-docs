---
title: "Import a Custom Chart Using the CLI"
id: 43700996427533
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996427533-Import-a-Custom-Chart-Using-the-CLI
updated_at: 2026-05-29T14:07:58Z
---

# Import a Custom Chart Using the CLI

# Import a Custom Chart Using the CLI

**Import a custom chart using the custom chart CLI**

Run the `cmp-chart import` command, specifying the path to the library. You can import visual zip files that were downloaded from the Manage Custom Charts page or a custom chart created with an older version of the CLI.

$ cmp-chart import [options] <visualname> <path-to-visual>

where `<path-to-visual>` is the relative path to the zip file containing the visual you want to import.

The following options are available:

* `-a, -app [URL]` Specify the Composer application server URL (e.g. https://myserver/composer)
* `-u, -user [user:password]` Specify the user name and password to use for server authentication.
* `-h, -help` Output usage information

**Note:** Composer v24 Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

A custom chart is bundled before it is pushed to the Composer server. This creates a `/dist` directory containing the necessary files required to send the visual to the Composer server. This `/dist` custom chart zip file is not compatible with the `cmp-chart import` command and cannot be imported using the Manage Custom Charts page in the UI. To import the `/dist` custom chart zip file, use the `cmp-chart push` command instead.
