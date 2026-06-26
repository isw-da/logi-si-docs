---
title: "Configure Composer"
id: 43700989620365
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700989620365-Configure-Composer
updated_at: 2026-05-29T14:07:20Z
---

# Configure Composer

# Configure Composer

The Composer server uses multiple configuration files to ensure successful deployment of Composer in your operating environment. Each component has configuration files including a `<component_name>.properties` file and a `<component_name>.jvm` file.

Use the configuration files to make changes to the Composer server and how it functions. The configuration files need to be created after the Composer server has been installed to override Composer's default configuration. To modify the settings in these files, edit them in the `/etc/zoomdata` directory, as described in [Edit a Configuration File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053803917-Edit-a-Configuration-File).

A full list of the configuration file names can be found in [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).

Every `<component_name>.jvm` file should include an `Xmx` JVM option to control the maximum heap memory limit for the application. See [Configure Memory Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings).
