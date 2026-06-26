---
title: "Edit a  Configuration File"
id: 43701053803917
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053803917-Edit-a-Configuration-File
updated_at: 2026-05-29T14:07:19Z
---

# Edit a  Configuration File

# Edit a Configuration File

You can edit the properties for your Composer configuration in the configuration files. For a complete list of configuration files, see [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).

**Note:** insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded.

Quickly determine what changes you've made to a properties file using `diff` in Linux. For example:

diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties

or

diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties

For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

**Edit a** Composer **configuration file in Linux:**

1. From your terminal, SSH to your Composer server.
2. Stop the appropriate Composer microservice (Composer, Screenshot, or the specific connector server).

   For the appropriate Linux command, see  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop).
3. Use the following command to access and open the configuration file:

   vi /etc/zoomdata/<config-file-name>

   For example:

   vi /etc/zoomdata/zoomdata.properties

   Names of valid configuration files are listed in [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).

   If the configuration file does not exist, this command creates it.

   **Note:** 
   If you are not logged in as a root user, then you need to enter
   `sudo vi /etc/zoomdata/zoomdata.properties` to create the desired file.

   Make sure the file is readable by the `zoomdata` microservice account.
4. Add the new variable or property into the file on a new line or edit an existing one, as needed. See:

   * [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties)
   * [zoomdata.jvm Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990181901-zoomdata-jvm-Options)
   * [Query Engine Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041000973-Query-Engine-Properties)
   * [screenshot-service.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054295053-screenshot-service-properties-Properties)
   * [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files)
5. Save and exit the configuration file.
6. Restart Composer microservices.

   For the appropriate Linux command line, see
    [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

**Edit a** Composer **configuration file in Windows:**

1. Open the configuration file using a text editor that can edit Windows property files.

   Names of valid configuration files are listed in [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).
2. Stop the appropriate Composer microservice (Composer, Screenshot, or the specific connector server).

   For the appropriate Windows commands, see
   [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference).
3. Add the new variable or property into the file on a new line or edit an existing one, as needed. See:

   * [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties)
   * [zoomdata.jvm Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990181901-zoomdata-jvm-Options)
   * [Query Engine Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041000973-Query-Engine-Properties)
   * [screenshot-service.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054295053-screenshot-service-properties-Properties)
   * [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files)
4. Save and exit the configuration file.
5. Restart Composer microservices.

   For the appropriate Windows commands, see
   [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference).

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back into Composer. Confirm that your changes have taken effect.
