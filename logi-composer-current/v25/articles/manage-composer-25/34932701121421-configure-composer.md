---
title: "Configure Composer"
id: 34932701121421
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932701121421-Configure-Composer
updated_at: 2026-05-26T22:06:14Z
---

# Configure Composer

# Configure Composer

The Composer server uses multiple configuration files to ensure successful deployment of Composer in your operating environment. Each Composer component has configuration files including a `<component_name>.properties` file and a `<component_name>.jvm` file.

Use the Composer configuration files to make changes to the Composer server and how it functions. The configuration files need to be created after the Composer server has been installed to override Composer's default configuration. To modify the settings in these files, edit them in the `/etc/zoomdata` directory, as described in [Edit a Configuration File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932669980557-Edit-a-Configuration-File).

A full list of the configuration file names can be found in [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).

Every `<component_name>.jvm` file should include an `Xmx` JVM option to control the maximum heap memory limit for the application. See [Configure Memory Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings).
