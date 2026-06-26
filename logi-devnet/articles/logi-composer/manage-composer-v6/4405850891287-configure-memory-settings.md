---
title: "Configure Memory Settings"
id: 4405850891287
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850891287-Configure-Memory-Settings
updated_at: 2022-05-11T14:53:26Z
---

# Configure Memory Settings

# Configure Memory Settings

To change memory allocation settings for Composer microservices:

1. From your terminal, SSH to your Composer server.
2. To modify the memory settings for Composer microservices, you need to edit or create the corresponding
   `.jvm` files in `/etc/zoomdata/`. Perform the following steps:

   ```
   vi/etc/zoomdata/<component_name>.jvm
   ```

   For complete information on editing configuration files, see [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).
3. Add or update the following line(s) in the corresponding `.jvm` files.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743928087/criticalicon_26x26.gif) Do not allocate more than 85% of your total system memory to all microservices.

   The following example configures the Composer server to use 20 GB of RAM in the `zoomdata.jvm` configuration file. You can adjust the number to fit your system's needs. Replace the
   **20** with the necessary memory allocation for your operating environment.

   ```
   -Xms20g  
   -Xmx20g
   ```
4. Save and exit the `.jvm` file.
5. Restart the microservice for which you have modified the settings:

   For CentOS 7 or 8 or Ubuntu 16 or 18:

   ```
   sudo systemctl restart <service-name>
   ```

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back into Composer.
