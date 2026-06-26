---
title: "Edit a Composer Configuration File"
id: 4405850887703
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File
updated_at: 2021-09-21T01:26:47Z
---

# Edit a Composer Configuration File

# Edit a Composer Configuration File

You can edit the properties for your Composer configuration in the configuration files. For a complete list of configuration files, see [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Composer discourages changing properties in the `/opt/zoomdata/conf` directory. Instead we recommend that you copy the files you want to change to the `/etc/zoomdata` directory and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded. In addition, you can quickly determine what changes you've made to a properties file using `diff`. For example:

```
diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
```

or

```
diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
```

To edit a Composer configuration file:

1. From your terminal, SSH to your Composer server.
2. Stop the appropriate Composer microservice (Composer, Screenshot, or the specific connector server).

   For the appropriate Linux command, see [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Use the following command to access and open the configuration file:

   ```
   vi /etc/zoomdata/<config-file-name>
   ```

   For example:

   ```
   vi /etc/zoomdata/zoomdata.properties
   ```

   Names of valid configuration files are listed in [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files).

   If the configuration file does not exist, this command creates it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you are not logged in as a root user, then you need to enter
   `sudo vi /etc/zoomdata/zoomdata.properties` to create the desired file.

   Make sure the file is readable by the `zoomdata` microservice account.
4. Add the new variable or property into the file on a new line or edit an existing one, as needed. See:

   * [*zoomdata.properties Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405850907159-zoomdata-properties-Properties)
   * [zoomdata.jvm Options](https://devnet.logianalytics.com/hc/en-us/articles/4405850906263-zoomdata-jvm-Options)
   * [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties)
   * [screenshot-service.properties Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405850904471-screenshot-service-properties-Properties)
   * [Connector Properties and Property Files](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files)
5. Save and exit the configuration file.
6. Restart Composer microservices.

   For the appropriate Linux command line, see
   [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

Wait a few minutes for the microservice to restart completely, then open a new browser window to log back into Composer. Confirm that your changes have taken effect.
