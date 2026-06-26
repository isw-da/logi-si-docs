---
title: "Configure Memory Settings"
id: 34932637063437
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings
updated_at: 2026-05-26T22:06:15Z
---

# Configure Memory Settings

# Configure Memory Settings

Unified service memory configuration recommendations can help you avoid out of memory issues, unpredictable service stability, and memory allocation. We strongly recommend you use the new default for Java: Xms=Xmx. These updated default memory allocations are designed configure your services more effectively for a production load after installation or upgrade.

**Note:** Composerv23.2  requires slightly higher memory expectations than previous releases. Upgrading will not overwrite your memory configuration if you have already overwritten the default configuration settings.

If you’re upgrading your environment:

* Review your data source connector usage; stop unused connectors.
* Review your memory settings based on the chart below.

|  | 7.x / 23.1 Xms/Xmx | 23.2 and later Xms/Xmx |
| --- | --- | --- |
| Admin Server | 512M/1024M | Deprecated |
| Config Server | 512M/1024M | Deprecated |
| Data Writer | 128M/256M | 512M/512M |
| EDC \* | 128M/512M | 512M/512M |
| EDC hdfs/s3 | 512M/3584M | 1500M/1500M |
| Query Engine | 1G/6G | 4G/4G |
| Screenshot Service | 128M/1G | 750M/750M |
| Zoomdata Web | 1G/2G | 4G/4G |

**Change memory allocation settings for** Composer **microservices**

1. From your terminal, SSH to your Composer server.
2. To modify the memory settings for Composer microservices, you need to edit or create the corresponding
   `.jvm` files in `/etc/zoomdata/`. Perform the following steps:

   vi/etc/zoomdata/<component\_name>.jvm

   For complete information on editing configuration files, see [Edit a Configuration File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932669980557-Edit-a-Configuration-File).
3. Add or update the following line(s) in the corresponding `.jvm` files.

   **Important:** 
   Do not allocate more than 85% of your total system memory to all microservices.

   The following example configures the Composer server to use 20 GB of RAM in the `zoomdata.jvm` configuration file. You can adjust the number to fit your system's needs. Replace the
   **20** with the necessary memory allocation for your operating environment.

   -Xms20g  
   -Xmx**20**g
4. Save and exit the `.jvm` file.
5. Restart the microservice for which you have modified the settings:

   For CentOS and Ubuntu:

   sudo systemctl restart <service-name>

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back into Composer.
