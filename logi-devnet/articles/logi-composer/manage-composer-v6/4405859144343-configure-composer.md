---
title: "Configure Composer"
id: 4405859144343
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859144343-Configure-Composer
updated_at: 2024-03-25T13:28:29Z
---

# Configure Composer

# Configure Composer

The Composer server uses multiple configuration files to ensure successful deployment of Composer in your operating environment. Each Composer component has configuration files including a `<component_name>.properties` file and a `<component_name>.jvm` file.

Use the Composer configuration files to make changes to the Composer server and how it functions. The configuration files need to be created after the Composer server has been installed to override Composer's default configuration. To modify the settings in these files, edit them in the `/etc/zoomdata` directory, as described in [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).

A full list of the configuration file names can be found in [Configuration Property Files](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files).

Every `<component_name>.jvm` file should include an `Xmx` JVM option to control the maximum heap memory limit for the application. See [*Configure Memory Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405850891287-Configure-Memory-Settings).
