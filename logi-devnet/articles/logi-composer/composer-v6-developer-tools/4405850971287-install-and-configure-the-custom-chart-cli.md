---
title: "Install and Configure the Custom Chart CLI"
id: 4405850971287
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850971287-Install-and-Configure-the-Custom-Chart-CLI
updated_at: 2021-09-21T01:27:35Z
---

# Install and Configure the Custom Chart CLI

# Install and Configure the Custom Chart CLI

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Before installing Composer's custom chart CLI, verify that `Node.js` version 10 or later and `npm` version 5.6 or later are installed on your machine.

To install and configure the custom chart CLI:

1. Install the custom chart CLI by running the following:

   ```
   $ npm install zoomdata-chart-cli@<x> -g
   ```

where `<x>` is either `4` or `5`, depending on the version of the custom chart CLI you are installing.

2. After installation, you can configure the default environment that is used by the custom chart CLI. This makes creating and pushing custom charts easier, as you do not have to provide the server URL and credentials with every command. Run the following to start the configuration process:

   ```
   $ zd-chart config
   ```
3. Follow the prompts to store your default server configuration in an encrypted file. After the server configuration has been saved, the CLI checks for the presence of this file when you omit the server URL and credentials when running commands.
4. After installing, you can create new visuals or make updates to current custom charts.
