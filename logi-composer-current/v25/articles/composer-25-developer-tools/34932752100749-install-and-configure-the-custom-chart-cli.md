---
title: "Install and Configure the Custom Chart CLI"
id: 34932752100749
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932752100749-Install-and-Configure-the-Custom-Chart-CLI
updated_at: 2026-05-26T22:06:52Z
---

# Install and Configure the Custom Chart CLI

# Install and Configure the Custom Chart CLI

**Note:** 
Before installing Composer's custom chart CLI, verify that `Node.js` version 10 or later and `npm` version 5.6 or later are installed on your machine.

**Install and configure the custom chart CLI**:

1. Install the custom chart CLI by running the following:

   $ npm install composer-chart-cli@<x> -g

where `<x>` is `6`, the version of the custom chart CLI you are installing.

2. After installation, you can configure the default environment that is used by the custom chart CLI. This makes creating and pushing custom charts easier, as you do not have to provide the server URL and credentials with every command. Run the following to start the configuration process:

   $ cmp-chart config
3. Follow the prompts to store your default server configuration in an encrypted file. After the server configuration has been saved, the CLI checks for the presence of this file when you omit the server URL and credentials when running commands.
4. After installing, you can create new visuals or make updates to current custom charts.

**Note:** Logi Composer v7.10 and later works with the new version of the Composer CLI tool, version 1 (`composer-chart-cli`). This new version of the CLI tool enables you to manage custom charts in your Composer v7.10 and later environment. Familiar commands and locations have changed: commands that use `zd` now use `cmp`, and that use `zoomdata` now use `composer`.
