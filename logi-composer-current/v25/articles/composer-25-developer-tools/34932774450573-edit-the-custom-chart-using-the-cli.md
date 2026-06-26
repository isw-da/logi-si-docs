---
title: "Edit the Custom Chart Using the CLI"
id: 34932774450573
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932774450573-Edit-the-Custom-Chart-Using-the-CLI
updated_at: 2026-05-26T22:06:46Z
---

# Edit the Custom Chart Using the CLI

# Edit the Custom Chart Using the CLI

**Edit a custom chart using the custom chart CLI**

Make sure you are in the visual’s folder and run the following edit command:

$ cmp-chart edit

Alternatively, you can specify the path to the visual in the edit command. For example:

$ cmp-chart edit -d <path-to-visual>

After running the edit command, follow the prompts to update the visual's controls, name, variables, or visibility.

When all edits are finished, be sure to rebuild the visual before pushing it to the server. See [Install Dependencies and Build the Custom Chart Using the CLI](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932774023693-Install-Dependencies-and-Build-the-Custom-Chart-Using-the-CLI).

**Note:** Logi Composer Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.
